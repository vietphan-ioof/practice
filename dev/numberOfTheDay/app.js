

//use ctrl+C to cancell and end the server

/*
 *
 * A process that is blocked is one that is waiting for some event, 
 * such as a resource becoming available or the completion of an I/O operation.[1]
*/

//to include a module use require()
const http = require('http');
const fs = require('fs');
const uc = require('upper-case');

const hostname = '127.0.0.1';
const port = 3000;

function genLargeNum(){
	return Math.floor(Math.random()*(1000000000000-0) + 0).toString();
}



/*
 * guess a number.
 * It tells how close your are compared to your peers in ranking
 * at the end of the day it shows the previous number and stores it in the database
 * it also stores the high scores for one day.
 *
*/

const server = http.createServer((req, res) => {
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











































