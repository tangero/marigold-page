/**
 * Firebase Cloud Functions for FCM Topic Subscription
 * Deploy with: firebase deploy --only functions
 */

const functions = require('firebase-functions');
const admin = require('firebase-admin');

admin.initializeApp();

/**
 * Subscribe a device token to a topic
 * Called from frontend when user opts in to notifications
 */
exports.subscribeToTopic = functions
  .region('europe-west1')
  .https.onRequest(async (req, res) => {
    // CORS headers
    res.set('Access-Control-Allow-Origin', '*');
    res.set('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.set('Access-Control-Allow-Headers', 'Content-Type');

    // Handle preflight
    if (req.method === 'OPTIONS') {
      res.status(204).send('');
      return;
    }

    if (req.method !== 'POST') {
      res.status(405).json({ error: 'Method not allowed' });
      return;
    }

    try {
      const { token, topic } = req.body;

      if (!token || !topic) {
        res.status(400).json({ error: 'Missing token or topic' });
        return;
      }

      // Validate topic name (only allow our topics)
      const allowedTopics = ['marigold-news', 'vibecoding-news'];
      if (!allowedTopics.includes(topic)) {
        res.status(400).json({ error: 'Invalid topic' });
        return;
      }

      // Subscribe token to topic
      const response = await admin.messaging().subscribeToTopic(token, topic);

      console.log(`Subscribed to ${topic}:`, response);

      res.status(200).json({
        success: true,
        topic: topic,
        successCount: response.successCount,
        failureCount: response.failureCount
      });

    } catch (error) {
      console.error('Subscription error:', error);
      res.status(500).json({ error: error.message });
    }
  });

/**
 * Unsubscribe a device token from a topic
 */
exports.unsubscribeFromTopic = functions
  .region('europe-west1')
  .https.onRequest(async (req, res) => {
    res.set('Access-Control-Allow-Origin', '*');
    res.set('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.set('Access-Control-Allow-Headers', 'Content-Type');

    if (req.method === 'OPTIONS') {
      res.status(204).send('');
      return;
    }

    if (req.method !== 'POST') {
      res.status(405).json({ error: 'Method not allowed' });
      return;
    }

    try {
      const { token, topic } = req.body;

      if (!token || !topic) {
        res.status(400).json({ error: 'Missing token or topic' });
        return;
      }

      const response = await admin.messaging().unsubscribeFromTopic(token, topic);

      res.status(200).json({
        success: true,
        topic: topic,
        successCount: response.successCount,
        failureCount: response.failureCount
      });

    } catch (error) {
      console.error('Unsubscription error:', error);
      res.status(500).json({ error: error.message });
    }
  });
