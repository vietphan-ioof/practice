/*
	p2p voice call application

	approaches:
		p2p:
			- avast.com/c-p2p-vpn-server#
		-- webRTC 
		-- p2p-sip 
		   - https://en.wikipedia.org/wiki/Peer-to-peer_SIP
		   - https://github.com/theintencity/sip-js
*/



const http = require('http');
const express = require('express');
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
















