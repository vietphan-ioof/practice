const express = require('express');
const cookieParser = require('cookie-parser');
const app = express()
const port = 8000

app.use(cookieParser('my-secret'));


app.get('/', (req, res) => {
	res.send('Hello World!');
		
	console.log(req.cookies);

	let options = {
		maxAge: 1000 * 60 * 2,
		httpOnly: true,
		signed: true
	};

	res.cookie('topGuess', '20', options);
	res.send();
});

app.use(express.static(__dirname + '/public'));

app.listen(port, () => {
	console.log('bruh cookies better work on this piece of shit ${port}');
});





















































