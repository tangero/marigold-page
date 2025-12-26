/**
 * Firebase Cloud Functions for FCM Topic Subscription
 * Deploy with: firebase deploy --only functions
 */

const {onRequest} = require("firebase-functions/v2/https");
const {initializeApp} = require("firebase-admin/app");
const {getMessaging} = require("firebase-admin/messaging");

initializeApp();

/**
 * Subscribe a device token to a topic
 * Called from frontend when user opts in to notifications
 */
exports.subscribeToTopic = onRequest({
  region: "europe-west1",
  cors: true,
}, async (req, res) => {
  if (req.method !== "POST") {
    res.status(405).json({error: "Method not allowed"});
    return;
  }

  try {
    const {token, topic} = req.body;

    if (!token || !topic) {
      res.status(400).json({error: "Missing token or topic"});
      return;
    }

    // Validate topic name (only allow our topics)
    const allowedTopics = ["marigold-news", "vibecoding-news"];
    if (!allowedTopics.includes(topic)) {
      res.status(400).json({error: "Invalid topic"});
      return;
    }

    // Subscribe token to topic
    const response = await getMessaging().subscribeToTopic(token, topic);

    console.log(`Subscribed to ${topic}:`, response);

    res.status(200).json({
      success: true,
      topic: topic,
      successCount: response.successCount,
      failureCount: response.failureCount,
    });
  } catch (error) {
    console.error("Subscription error:", error);
    res.status(500).json({error: error.message});
  }
});

/**
 * Unsubscribe a device token from a topic
 */
exports.unsubscribeFromTopic = onRequest({
  region: "europe-west1",
  cors: true,
}, async (req, res) => {
  if (req.method !== "POST") {
    res.status(405).json({error: "Method not allowed"});
    return;
  }

  try {
    const {token, topic} = req.body;

    if (!token || !topic) {
      res.status(400).json({error: "Missing token or topic"});
      return;
    }

    const response = await getMessaging().unsubscribeFromTopic(token, topic);

    res.status(200).json({
      success: true,
      topic: topic,
      successCount: response.successCount,
      failureCount: response.failureCount,
    });
  } catch (error) {
    console.error("Unsubscription error:", error);
    res.status(500).json({error: error.message});
  }
});
