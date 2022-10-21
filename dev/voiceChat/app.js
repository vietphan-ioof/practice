
const express = require('express');
const http = require('http');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static("public"));

app.get('/', (req, res) => {
	res.render(path.join(__dirname, '/public/index.html'));
});


app.listen(port, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
}

























