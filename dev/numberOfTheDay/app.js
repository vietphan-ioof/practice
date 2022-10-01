//use ctrl+C to cancell and end the server
/*
 * A process that is blocked is one that is waiting for some event, 
 * such as a resource becoming available or the completion of an I/O operation.[1]
*/

/*
 * guess a number.
 * It tells how close your are compared to your peers in ranking
 * at the end of the day it shows the previous number and stores it in the database
 * it also stores the high scores for one day.
*/

// a self fullfilling leaderboard that shows at what time your best result was and if your headed in a better or worse direction 
// compared to your top result.

const http = require('http');
const fs = require('fs');
const uc = require('upper-case');
const querystring = require('querystring');

const hostname = '127.0.0.1';
const port = 3000;

const winner = "YOU WON YOU CHEEKY BASTARD!";
const closeThanTopAnswer = "YOU ARE GETTING CLOSER MY FRIEND";
const worseThanTopAnswer = " YOU ARE GETTING FARTHER LOSER";

var numOfDay = 0;
var topScore = true;

/*
//creating mongodb database
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017//mydb";

MongoClient.connect(url, function(err, db){
	if(err) throw err;
	console.log("Databasae created BOI!");
	var dbo = db.db("mydb");
	var scoreX = { name: "", highScore: 5};
	dbo.collection("leaderboard").insertOne(scoreX, function(err, res){
		if(err) throw err;
		console.log("1 document inserted");
		db.close();
	});
});

*/


//storing topScore as a cookie 


function parseCookies (request) {
    const list = {};
    const cookieHeader = request.headers?.cookie;
    if (!cookieHeader) return list;

    cookieHeader.split(`;`).forEach(function(cookie) {
        let [ name, ...rest] = cookie.split(`=`);
        name = name?.trim();
        if (!name) return;
        const value = rest.join(`=`).trim();
        if (!value) return;
        list[name] = decodeURIComponent(value);
    });

    return list;
}

function setCookie(cname, cvalue, response){
	response.writeHead(200, {'Set-Cookie':'sesh=wakadoo; expires='+ new Date(new Date().getTime()+86409000).toUTCString()});
}


//generates the large random number that will cycle every 24 hours for the user to guess
// adding grhahms number notation function
function genLargeNum(){
	return Math.floor(Math.random()*(1000000000000-1) + 1).toString();
}

function testNumberGenerator(){
	return Math.floor(Math.random()*(10-1) + 1).toString();
}

function init(){
	numOfDay = testNumberGenerator();
	topScore = true;
	console.log("NUMER OF THE DAYYYYYYY" + " " + numOfDay);
}

//set this to update every 86400 seconds or 24 hours
//setInterval(function(){init()}, 10000);
init();

let cookie = require('http.cookie');

const server = http.createServer((req, res) => {
		
	console.log(cookies);

	res.writeHead(200, {
		"Set-Cookie": `mycookie=test`,
		"Content-Type": `text/plain`
	});

	var RESULT = " ";

	//store variable and update it in database.
	if(req.method == "POST"){
		var body = '';
		
		var cookies = parseCookies(req);

		req.on('data', function(data){
			body+=data;

			if(body.length > 1e6)
				req.connection.destroy();
		});

		req.on('end', function() {
			var post = querystring.parse(body);
			console.log(post['guess']);
			answer = post['guess'];

			if(topScore === true){
				setCookie("topGuess", answer, res);
				topScore = false;
			}

			if(numOfDay.toString() === answer){
				RESULT = winner;
			}else if(Math.abs(answer-numOfDay.toString()) <= Math.abs(parseCookies("topGuess")-numOfDay.toString())){
				RESULT = closeThanTopAnswer;
				setCookie("topGuess", answer, 1);
			}else if(Math.abs(answer-numOfDay.toString()) > Math.abs(parseCookies("topGuess")-numOfDay.toString())){
				RESULT = worseThanTopAnswer;
			}
		});
	}

	fs.readFile('index.html', ((err, data) => {
		res.writeHead(200, {'Content-type': 'text/html'});
		res.write(data);
		res.write(genLargeNum());
		res.write('<br/>');
		res.write(RESULT);
		res.write('<br/>');
		res.write(parseCookies("topGuess").toString());
		return res.end();
	}));
});

server.listen(port, hostname, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});








































