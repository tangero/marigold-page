// Firebase Cloud Messaging Service Worker
// Handles background push notifications for marigold.cz and vibecoding.cz

importScripts('https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.7.0/firebase-messaging-compat.js');

// Firebase configuration
firebase.initializeApp({
  apiKey: "AIzaSyDb03VE1UNGcOeukc2yn1wGRnaOrL-i5uo",
  authDomain: "marigold-web.firebaseapp.com",
  projectId: "marigold-web",
  storageBucket: "marigold-web.firebasestorage.app",
  messagingSenderId: "776408181252",
  appId: "1:776408181252:web:912de8993063dfdae5e351"
});

const messaging = firebase.messaging();

// Handle background messages
messaging.onBackgroundMessage((payload) => {
  console.log('[FCM SW] Background message received:', payload);

  // Extract notification data
  const data = payload.data || {};
  const notification = payload.notification || {};

  const title = data.title || notification.title || 'Nový článek';
  const body = data.body || notification.body || 'Podívejte se na nový obsah';
  const icon = data.icon || '/assets/images/logo-192.png';
  const url = data.url || '/';

  const notificationOptions = {
    body: body,
    icon: icon,
    badge: '/assets/images/badge-72.png',
    tag: 'fcm-notification',
    renotify: true,
    data: { url: url }
  };

  self.registration.showNotification(title, notificationOptions);
});

// Handle notification click
self.addEventListener('notificationclick', (event) => {
  console.log('[FCM SW] Notification clicked:', event);

  event.notification.close();

  const url = event.notification.data?.url || '/';

  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true })
      .then((windowClients) => {
        // Check if there's already a window open
        for (const client of windowClients) {
          if (client.url.includes(self.location.origin) && 'focus' in client) {
            client.navigate(url);
            return client.focus();
          }
        }
        // Open new window if none found
        if (clients.openWindow) {
          return clients.openWindow(url);
        }
      })
  );
});

// Service worker install event
self.addEventListener('install', (event) => {
  console.log('[FCM SW] Installing...');
  self.skipWaiting();
});

// Service worker activate event
self.addEventListener('activate', (event) => {
  console.log('[FCM SW] Activated');
  event.waitUntil(clients.claim());
});
