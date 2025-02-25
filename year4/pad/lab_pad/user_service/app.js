const express = require('express');
const app = express();

app.use(express.json());

let users = [{ id: '1', name: 'User One' }];

app.post('/sendNotification', (req, res) => {
    const { user_id, message } = req.body;
    if (!user_id || !message) {
        console.log('Missing user_id or message');
        return res.status(400).json({ error: 'Missing user_id or message' });
    }
    console.log(`Notification sent to user ${user_id}: ${message}`);
    res.status(200).json({ status: 'Notification sent successfully' });
});

app.get('/status', (req, res) => {
    res.json({ status: "User Service is running" });
});

app.listen(50052, () => {
    console.log('UserService started on port 50052');
});
