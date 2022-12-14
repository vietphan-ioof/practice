/*
	p2p anonymous voice call application game where you have to keep saying 

	approaches:
		p2p:
			- avast.com/c-p2p-vpn-server#
		-- webRTC 
			- https://www.tutorialspoint.com/webrtc/webrtc_architecture.htm
		-- p2p-sip 
		   - https://en.wikipedia.org/wiki/Peer-to-peer_SIP
		   - https://github.com/theintencity/sip-js
		   - https://developer.mozilla.org/en-US/docs/Web/Guide/API/WebRTC/Peer-to-peer_communications_with_WebRTC
*/



const http = require('http');
const express = require('express');
const app = express();

import * as Y from 'yjs';
import {WebrtcProvider} from 'y-webrtc';

const ydoc = new Y.Doc();

const hostname = '127.0.0.1';
const port = 3000;

app.use(express.static("public"));

app.get('/', function(req, res){
	res.render(path.join(__dirname, '/public/index.html'));
});

app.listen(port, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});
















