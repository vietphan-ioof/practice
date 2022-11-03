/*
	TF2 Tracker

	: write blog post : 
	
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

//starting express
const app = express();

//initialization
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
let url = 'https://steamcommunity.com/id/';
let CLASS = "";

app.get('/', function(req, res){
	USERNAME = "dragonsofdra";
	let string = 'https://steamcommunity.com/profiles/76561198253369292';
	let string2 = 'https://steamcommunity.com/id/Dragonsofdra';
	let string3 = 'https://steamcommunity.com/id/DimGG';
	let string4 = 'https://steamcommunity.com/id/zkae';

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
	USERNAME = req.body['guess'];
	res.redirect('/classChooser');
});

app.get('/classChooser', function(req, res){
	res.render(path.join(__dirname, './public/classSelect.html'), {RESULT: url+USERNAME});
});

app.post('/classChooser', function(req, res){
	if(req.body['scout'] == "Scout"){
		CLASS = "scout";
	}else if(req.body['demoman'] == "Demoman"){
		CLASS = "demoman";
	}else if(req.body['heavy'] == "Heavy"){
		CLASS = "heavy";
	}else if(req.body['spy'] == "Spy"){
		CLASS = "spy";
	}else if(req.body['soldier'] == "Soldier"){
		CLASS = "soldier";
	}else if(req.body['medic'] == "Medic"){
		CLASS = "medic";
	}else if(req.body['ach'] == "Achievments" ){
		console.log("IT WOKRED!");
		return res.redirect('/ach');
	}
	res.redirect('/fetchStats');
});

app.get('/fetchStats', function(req, res){
	var fetchId = steam.resolve(url+USERNAME).then(function(id) {
		console.log(id);
		result = steam.getUserStats(id, 440).then(stats => {
		console.log(stats);
			let classStats = [];
			let temp = stats.stats;
			let keys = Object.keys(temp);
			let result = stats.stats[keys[0]]
//			console.log(result);
			res.render(path.join(__dirname, './public/index.html'), {RESULT:stats.stats[keys[0]]});
			bruh = stats.stats[keys[0]];
		

			console.log("+++++++++++++++++++++++++++++++++++++");
			for(let x in stats.stats){
				if(x.toLowerCase().includes(CLASS)){
					classStats.push(stats.stats[x]);
				}
			}
			console.log(classStats);
			console.log("+++++++++++++++++++++++++++++++++++++");
			});

			result2 = steam.getUserAchievements(id, 440).then(a => {
//				console.log(a);
			});
		});
});

app.get('/ach', function(req, res){
	var fetchId = steam.resolve(url+USERNAME).then(function(id) {
		console.log(id);
		result = steam.getUserAchievements(id, 440).then(a => {
				console.log(a);

				let achStats = [];
				console.log("+++++++++++++++++++++++++++++++++++++");
				for(let x in a.achievements){
					achStats.push(a.achievements[x].api);
				}
				console.log(achStats);
				console.log("+++++++++++++++++++++++++++++++++++++");
			});
		});
});

app.listen(port, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});














