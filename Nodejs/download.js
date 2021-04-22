const express = require("express");
const router = express.Router();

router.get('/', (req, res) => {
    res.send('download page');
})

router.get('/docs', (req, res) => {
    res.send('download page docs');
})

module.exports = router;

