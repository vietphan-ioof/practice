/*
	TF2 Tracker
	
	https://www.npmjs.com/package/steamapi
	https://wiki.teamfortress.com/wiki/WebAPI

*/

const http = require('http');
const express = require('express');
const steamAPI = require('steamapi');
const path = require('path');

const app = express();

const hostname = '127.0.0.1';
const port = 3000;

app.use(express.static("public"));

app.get('/', function(req, res){
	res.render(path.join(__dirname, '/public/index.html'));
});

app.listen(port, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});














