const express = require("express");
const app = express();
const download = require(__dirname + "/download.js");
const logger = require('morgan');

app.use(logger('dev'));

const mid_function = (req, res, next) => {
    console.log("mid function!")
    next();
}

app.use(mid_function);

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
