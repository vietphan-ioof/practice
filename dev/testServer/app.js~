const express = require('express');
const app = express()
const port = 8000


const cookieParser = require('cookie-parser');

app.use(cookieParser());


app.get('/', (req, res) => {

	console.log(req.cookies);

	let options = {
		maxAge: 1000 * 60 * 5, 
		httpOnly: true,
	}
	console.log("error here");
	res.cookie('cookieName', 'cookieValue', {maxAge: 900000, httpOnly: true});
	res.end();
});

app.listen(port, () => {
	console.log('bruh cookies better work on this piece of shit ${port}');
});





















































