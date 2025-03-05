const express = require('express');
const router = express.Router();

// Dummy user data for testing
router.get('/me', (req, res) => {
    res.json({ message: "✅ User route is working!" });
});

module.exports = router;
