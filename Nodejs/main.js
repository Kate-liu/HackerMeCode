const express = require("express");
const app = express();
const download = require(__dirname + "/download.js");

app.use('/download', download);

app.get('/', (req, res) => {
    res.send("Hello you and me!");
})

app.get('/news', (req, res) => {
    res.send("news page");
})

app.listen(80, () => {
    console.log('listening on 80 port!');
})
