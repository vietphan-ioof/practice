//use ctrl+C to cancell and end the server

/*
 *
 * A process that is blocked is one that is waiting for some event, 
 * such as a resource becoming available or the completion of an I/O operation.[1]
*/

/*
 * guess a number.
 * It tells how close your are compared to your peers in ranking
 * at the end of the day it shows the previous number and stores it in the database
 * it also stores the high scores for one day.
 *
*/

const http = require('http');
const fs = require('fs');
const uc = require('upper-case');
const querystring = require('querystring');

const hostname = '127.0.0.1';
const port = 3000;
var numOfDay = 0;


function genLargeNum(){
	return Math.floor(Math.random()*(1000000000000-0) + 0).toString();
}

function testNumberGenerator(){
	return Math.floor(Math.random()*(3-0) + 0).toString();
}

function init(){
	numOfDay = testNumberGenerator();
	console.log("NUMER OF THE DAYYYYYYY" + " " + numOfDay);
}

setInterval(function(){init()}, 5000);


const server = http.createServer((req, res) => {
	var RESULT = false;
	
	if(req.method == "POST"){
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

			if(numOfDay.toString() === answer){
				RESULT = true;
			}
		});
	}


	fs.readFile('index.html', ((err, data) => {
		res.writeHead(200, {'Content-type': 'text/html'});
		res.write(data);
		res.write(genLargeNum());
		res.write(RESULT.toString());
		return res.end();
	}));
});

server.listen(port, hostname, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});











































