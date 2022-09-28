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
const querystring = ('querystring');

const hostname = '127.0.0.1';
const port = 3000;
var numOfDay = 0;

function genLargeNum(){
	return Math.floor(Math.random()*(1000000000000-0) + 0).toString();
}

function handler(req, res){
	var POST = {};
	if(req.method == 'POST'){
		req.on('data', function(data){
			data = data.toString();
			data = data.split('&');

			for(x=0; x<data.length; x++){
				var _data = data[x].split("=");
				console.log(_data[1]);
				POST[_data[0]] = _data[1];
			}
			console.log("input: ");
			console.log(_data[1]);

			console.log(_data[1] + " " + numOfDay.toString());
			if(_data[1] === numOfDay.toString()){
				return(true);
			}

			return(false);
		});
	}
}

const server = http.createServer((req, res) => {
	fs.readFile('index.html', ((err, data) => {
		res.writeHead(200, {'Content-type': 'text/html'});
		res.write(data);
		res.write(genLargeNum());
		var result = handler(req, res).then(function(result){
			return(result);
		});
		console.log(result);
		if(result === true){
			console.log("YOU DID IT MOTHAFUCKA");
		}
		return res.end();
	}));
});

server.listen(port, hostname, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});











































