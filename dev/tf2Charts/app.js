/*
	TF2 Tracker
	
	https://www.npmjs.com/package/steamapi
	https://wiki.teamfortress.com/wiki/WebAPI
	F191259D56059F8FEE6A458710180A24

*/

const http = require('http');
const express = require('express');
const steamAPI = require('steamapi');
const path = require('path');

//starting the steam api
const SteamAPI = require('steamapi');
const steam = new SteamAPI('F191259D56059F8FEE6A458710180A24');

const app = express();

const hostname = '127.0.0.1';
const port = 3000;

app.use(express.static("public"));

steam.resolve('https://steamcommunity.com/id/DimGG').then(id => {
	console.log("hi");
	console.log(id);

	steam.getUserSummary(id).then(summary => {
		console.log(summary);
	});

	steam.getUserStats(id, 80924).then(stats => {
		console.log(stats);
	});
});


app.get('/', function(req, res){

	res.render(path.join(__dirname, '/public/index.html'));
	
});

app.listen(port, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});














