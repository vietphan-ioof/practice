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

app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.set('views', __dirname);

const hostname = '127.0.0.1';
const port = 3000;

//app.use(express.static("public"));

let x = {};

let v = 0;

async function fetchUserData(req, res){
	var result = {};
	steam.resolve('https://steamcommunity.com/id/DimGG').then(id => {
		console.log("hi");
		console.log(id);

		steam.getUserSummary(id).then(summary => {
//			console.log(summary);
		});
		result = steam.getUserStats(id, 440).then(stats => {
			return stats;		
			//console.log(stats);
//			console.log(stats.stats.TF_SOLDIER_PARACHUTE_DISTANCE_STAT);
//			res.render(path.join(__dirname, './public/index.html'), {RESULT: stats});
			});
		});
}

/*
	set custom steam url
	set acheivemnts to public
		 - send exception if not satisfied
*/

app.get('/', function(req, res){
	let string = 'https://steamcommunity.com/profiles/76561198253369292';
	let string2 = 'https://steamcommunity.com/id/Dragonsofdra';
	let string3 = 'https://steamcommunity.com/id/DimGG';
	let string4 = 'https://steamcommunity.com/id/zkae';

	var fetchId = steam.resolve(string2).then(function(id) {
		console.log(id);
		result = steam.getUserStats(id, 440).then(stats => {
		console.log(stats);
			let temp = stats.stats;
			let keys = Object.keys(temp);
			let result = stats.stats[keys[0]]
			console.log(result);
			res.render(path.join(__dirname, './public/index.html'), {RESULT:stats.stats[keys[0]]});
			});
		});
});

app.listen(port, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});














