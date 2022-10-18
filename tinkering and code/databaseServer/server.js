/*
 * problem statement
	Before your interview, write a program that runs a server that is accessible on 
	http://localhost:4000/. When your server receives a request on 	
	http://localhost:4000/set?somekey=somevalue it should store the passed key and value 
	in memory. When it receives a request on http://localhost:4000/get?key=somekey it should 
	return the value stored at somekey  
*/

const express = require('express');
const app = express();
const port = 4000;
var pair = [];

app.get('/', (req, res) => {
	res.write("hello world");
	res.end();
});

app.get('/set', (req, res) => {
	console.log(req.query);
    pair.push(req.query);

	var result = JSON.stringify(pair);
	var result2 = JSON.parse(result);

	res.send("variables set");

});

app.get('/get', (req, res) => {
	var key = req.query.key;
	console.log(pair);
	res.send("value:" + " " + pair[0][key]);
});

app.listen(port, () => {
	console.log(`server running on port ${port}`);
});




























