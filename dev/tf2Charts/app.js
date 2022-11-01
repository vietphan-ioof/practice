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
const bodyParser = require('body-parser');

//starting the steam api
const SteamAPI = require('steamapi');
const steam = new SteamAPI('F191259D56059F8FEE6A458710180A24');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded());
app.use(bodyParser.urlencoded({extended: true}));


app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.set('views', __dirname);

const hostname = '127.0.0.1';
const port = 3000;

//app.use(express.static("public"));

/*
	set custom steam url
	set acheivemnts to public
		 - send exception if not satisfied
*/

//rendering multiple items.
//https://stackoverflow.com/questions/15968776/send-multiple-variables-through-render-with-express

let USERNAME ='';
let url = 'https://steamcommunity.com/profiles/';

app.get('/', function(req, res){
	USERNAME = "dragonsofdra";
	let string = 'https://steamcommunity.com/profiles/76561198253369292';
	let string2 = 'https://steamcommunity.com/id/Dragonsofdra';
	let string3 = 'https://steamcommunity.com/id/DimGG';
	let string4 = 'https://steamcommunity.com/id/zkae';

	//ask for user input for steam id
	res.render(path.join(__dirname, './public/index.html'), {RESULT: url+USERNAME});
	/*

	var fetchId = steam.resolve(string2).then(function(id) {
		console.log(id);
		result = steam.getUserStats(id, 440).then(stats => {
		console.log(stats);
			let temp = stats.stats;
			let keys = Object.keys(temp);
			let result = stats.stats[keys[0]]
			console.log(result);
			res.render(path.join(__dirname, './public/index.html'), {RESULT:stats.stats[keys[0]]});
			bruh = stats.stats[keys[0]];
			});

			result2 = steam.getUserAchievements(id, 440).then(a => {
				console.log(a);
			});
		});
		*/
});

app.post('/', function(req, res){
	console.log(req.body['guess']);
	USERNAME = "BOO BOO";
	res.redirect('/statChooser');
});

app.get('/statChooser', function(req, res){
	res.render(path.join(__dirname, './public/index.html'), {RESULT: url+USERNAME});
});

app.listen(port, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});














