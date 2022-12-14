/*
	TF2 Tracker

	: write blog post : 
	
	https://www.npmjs.com/package/steamapi
	https://wiki.teamfortress.com/wiki/WebAPI
	F191259D56059F8FEE6A458710180A24


	make the UI not shit
*/

const http = require('http');
const https = require('https');
const express = require('express');
const steamAPI = require('steamapi');
const path = require('path');
const bodyParser = require('body-parser');
const fs = require('fs');

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
const port = 8080;

/*
	set custom steam url
	set acheivemnts to public
		 - send exception if not satisfied
*/

let USERNAME ='';
let url = 'https://steamcommunity.com/id/';
let CLASS = "";
invalid = "    ";

app.get('/', function(req, res){
	USERNAME = "dragonsofdra";
	let string = 'https://steamcommunity.com/profiles/76561198253369292';
	let string2 = 'https://steamcommunity.com/id/Dragonsofdra';
	let string3 = 'https://steamcommunity.com/id/DimGG';
	let string4 = 'https://steamcommunity.com/id/zkae';

	var homePageCSS = {
		style : fs.readFileSync('./public/homePage/css/homePageStyles.css', 'utf8'),
	};

	res.render(path.join(__dirname, './public/homePage/homePage.html'), {RESULT: invalid, myCSS : homePageCSS});
});

app.post('/', function(req, res){
	//impliment error handler.
	console.log(req.body['guess']);
	USERNAME = req.body['guess'];

	steam.resolve(url+USERNAME).then(id => {
		res.redirect('/classChooser');
	}).catch(function(e){
		console.log("WRONG USERNAME");
		invalid = "INVALID USERNAME. PLEASE ENTER VALID STEAM ID. FOLLOW INSTRUCTIONS BELOW IF YOU NEED HELP";
		res.redirect('/');
	});
});

app.get('/classChooser', function(req, res){

	var classSelectCSS = {
		style : fs.readFileSync('./public/classSelect/css/classSelectStyles.css', 'utf8'),
	};

	res.render(path.join(__dirname, './public/classSelect/classSelect.html'), {myCSS: classSelectCSS});
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
	}else if(req.body['sniper'] == "Sniper"){
		CLASS = "sniper";
	}else if(req.body['engineer'] == "Engineer"){
		CLASS = "engineer";
	}else if(req.body['pyro'] == "Pyro"){
		CLASS = "pyro";
	}else if(req.body['ach'] == "Find Your General Achievements" ){
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
			let statNames = [];
			let temp = stats.stats;
			let keys = Object.keys(temp);
			let result = stats.stats[keys[0]]
//			console.log(result);
			bruh = stats.stats[keys[0]];
		

			console.log("+++++++++++++++++++++++++++++++++++++");
			for(let x in stats.stats){
				if(x.toLowerCase().includes(CLASS)){
					if(x.toLowerCase().includes(".")){
					   statNames.push(x.replaceAll(".", " "));									
					}else if(x.toLowerCase().includes("_")){
						statNames.push(x.replaceAll("_" , " "));
					}
					classStats.push(stats.stats[x]);
//					statNames.push(x);
				}
			}
			console.log(classStats);
			res.render(path.join(__dirname, './public/classPage.html'), {stats :classStats, names : statNames});
			console.log("+++++++++++++++++++++++++++++++++++++");
			});
		});
});

app.get('/ach', function(req, res){
	var fetchId = steam.resolve(url+USERNAME).then(function(id) {
		console.log(id);
		let names = [];
		let descriptions = [];
		let achieved = [];

		result = steam.getUserAchievements(id, 440).then(a => {
				console.log(a);
				let achStats = [];
				console.log("+++++++++++++++++++++++++++++++++++++");
				for(let x in a.achievements){
					achStats.push(a.achievements[x]);
					names.push(a.achievements[x].name);
					descriptions.push(a.achievements[x].description);
					if(a.achievements[x].achieved === true){
						achieved.push("achieved.");
					}else if(a.achievements[x].achieved === false){
						achieved.push("not achieved yet.");
					}
				}
				console.log(achStats);
				res.render(path.join(__dirname, './public/achievementsPage.html'), {name : names, description : descriptions, achieve : achieved});
				console.log("+++++++++++++++++++++++++++++++++++++");
			});
		});
});

app.listen(port, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});














