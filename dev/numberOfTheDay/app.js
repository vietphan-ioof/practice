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
const express = require('express');
const path = require("path");
const app = express();

const fs = require('fs');
const uc = require('upper-case');
const bodyParser = require('body-parser');
const querystring = require('querystring');
var cookieParser = require('cookie-parser');
var Cookies = require('cookies');

app.use(express.static("public"));

app.use(cookieParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded());
app.use(bodyParser.urlencoded({extended: true}));

const hostname = '127.0.0.1';
const port = 3000;

const winner = "YOU WON YOU CHEEKY BASTARD!";
const closeThanTopAnswer = "YOU ARE GETTING CLOSER MY FRIEND";
const worseThanTopAnswer = " YOU ARE GETTING FARTHER LOSER";

var numOfDay = 0;
var firstTime = true;

//storing topscore as a cookie 
function parseCookies (request) {
    const list = {};
    const cookieHeader = request.headers?.cookie;
	console.log(request.headers);
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
	response.writeHead(200, {
		"Set-Cookie": `${cname}=${cvalue}`,
		"Content-Type": `text/plain`,
	});
}

//generates the large random number that will cycle every 24 hours for the user to guess
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


app.get('/' , (req, res) => {
	
	var RESULT = " ";
	var answer = 0;

	res.sendFile(path.join(__dirname, '/public/index.html'));


	if(numOfDay.toString() === answer){
		RESULT = winner;
	}else if(Math.abs(answer-numOfDay.toString()) <= Math.abs(parseCookies("topGuess")-numOfDay.toString())){
		RESULT = closeThanTopAnswer;
		setCookie("topGuess", answer, res);
	}else if(Math.abs(answer-numOfDay.toString()) > Math.abs(parseCookies("topGuess")-numOfDay.toString())){
		RESULT = worseThanTopAnswer;
	}

	if(req.method == "POST"){
		console.log("POST REQUEST POST REQUEST BABY");
		var body = '';
		
		req.on('data', function(data){
			body+=data;

			if(body.length > 1e6)
				req.connection.destroy();
		});

		req.on('end', function() {
			var post = querystring.parse(body);
			console.log(post['guess']);
			answer = post['guess'];
		});

	}
	

});

app.post('/', function(req, res){
	console.log(req.body);
	res.sendFile(path.join(__dirname, '/public/index.html'));
});


app.listen(port, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});









































