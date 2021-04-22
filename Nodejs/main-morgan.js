const express = require("express");
const app = express();
const download = require(__dirname + "/download.js");
const logger = require('morgan');

app.use(logger('dev'));

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
