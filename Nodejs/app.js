const express = require("express");
const app = express();

app.get('/hello', (req, res) => {
    res.send("Hello friends!");
})

app.listen(80, () => {
    console.log('listening on 80 port!')
})
