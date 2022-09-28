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

function genLargeNum(){
	return Math.floor(Math.random()*(1000000000000-0) + 0).toString();
}

function parsePost(request, response, callback){
	var queryData = "";
	if(typeof callback !== 'function') return null;

	if(request.method == 'POST'){
		request.on('data', function(data) {
			queryData+=data;
			if(queryData.length > 1e6){
				queryData = "";
				response.writeHead(413, {'Content-Type': 'text/plain'}).end();
				request.connection.destroy();
			}
		});
		
		request.on('end', function() {
			request.post = querystring.parse(queryData);
			callback();
		});
	}else {
		response.writeHead(405, {'Content-Type': 'text/plain'});
		response.end();
	}
}


const server = http.createServer((req, res) => {
	if(req.method == 'POST'){
		parsePost(req, res, function(){
			console.log("THE RESULTS");
			console.log(req.post);
		});
	}
	fs.readFile('index.html', ((err, data) => {
		res.writeHead(200, {'Content-type': 'text/html'});
		res.write(data);
		res.write(genLargeNum());
		return res.end();
	}));
});

server.listen(port, hostname, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});











































