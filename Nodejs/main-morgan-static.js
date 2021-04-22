const express = require("express");
const app = express();
const download = require(__dirname + "/download.js");
const logger = require('morgan');

app.use(logger('dev'));

app.use(express.static('public'));  // http://127.0.0.1/js/selfjs.js
// app.use('/media', express.static('public'));  // http://127.0.0.1/media/js/selfjs.js

app.listen(80, () => {
    console.log('listening on 80 port!');
})

app.use('/download', download);

app.get('/', (req, res) => {
    res.send("Hello you and me!");
})

app.get('/news', (req, res) => {
    res.send("news page");
})
