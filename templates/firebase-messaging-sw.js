importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-messaging.js');
firebase.initializeApp({
    apiKey: "AIzaSyA2RkujpNLpwOu1rat_RO5sI4xVk05kNbc",
    authDomain: "mlblog-cb778.firebaseapp.com",
    databaseURL: "https://mlblog-cb778-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "mlblog-cb778",
    storageBucket: "mlblog-cb778.appspot.com",
    messagingSenderId: "393804279142",
    appId: "1:393804279142:web:5dbbcc4a9a039a65646ca7",
    measurementId: "G-NMPGWXK2QG"
  });

  const messaging = firebase.messaging();

self.addEventListener('notificationclick', (event) => {
  // console.log("notification open")
  var action_click = event.notification.data.click_action;
  event.notification.close();
  // This looks to see if the current is already open and
  // focuses if it is
  window.open(action_click, '_blank');
  // event.waitUntil(clients.openWindow(action_click)
  
});