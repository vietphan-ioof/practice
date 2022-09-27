

//use ctrl+C to cancell and end the server

/*
 *
 * A process that is blocked is one that is waiting for some event, 
 * such as a resource becoming available or the completion of an I/O operation.[1]
*/

//to include a module use require()
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
	console.log(req);
	res.writeHead(200, {'Content-Type': 'text/html'});
	res.write('Hello World');
	res.end();
});

server.listen(port, hostname, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});











































