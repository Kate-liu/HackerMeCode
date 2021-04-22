const express = require("express");
const app = express();
const path = require('path');

app.listen(80, () => {
    console.log('listening on 80 port!');
})

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.get('/', function (req, res) {
    res.render('index', {
        title: 'Hello',
        message: 'hello world pug engine!'
    });
});




