const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json({ message: '📄 Documents API is working!' });
});

module.exports = router;
