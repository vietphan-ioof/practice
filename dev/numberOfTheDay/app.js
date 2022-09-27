

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
	return Math.random().toString();
}

const server = http.createServer((req, res) => {
	fs.readFile('index.html', ((err, data) => {
		res.writeHead(200, {'Content-type': 'text/html'});
		res.write(data);
		res.write(uc.upperCase("uppercase is a module for lazy turds"));
		res.write("<br/>");
		res.write("<br/>");
		res.write(genLargeNum());
		return res.end();
	}));
});

server.listen(port, hostname, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});










































