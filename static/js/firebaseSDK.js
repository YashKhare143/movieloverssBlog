const firebaseConfig = {
    apiKey: "AIzaSyA2RkujpNLpwOu1rat_RO5sI4xVk05kNbc",
    authDomain: "mlblog-cb778.firebaseapp.com",
    databaseURL: "https://mlblog-cb778-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "mlblog-cb778",
    storageBucket: "mlblog-cb778.appspot.com",
    messagingSenderId: "393804279142",
    appId: "1:393804279142:web:5dbbcc4a9a039a65646ca7",
    measurementId: "G-NMPGWXK2QG"
};

firebase.initializeApp(firebaseConfig);
const messaging = firebase.messaging();

function subscribeUs() {
    messaging
        .requestPermission()
        .then(function () {
            messaging.getToken({ vapidKey: 'BFVKqrJtM0eSg5zcsqc1YAZqxiTSlreCSiLQQkc0ueBPmyktzVbMbina4s9evSK9H9BUot0nmUf4Z_d6NHInWJ8' }).then((currentToken) => {
                if (currentToken) {
                    // Send the token to your server and update the UI if necessary
                    $("#token").val(currentToken);
                    // v = $("#token").val();
                    $("#T_F").submit();

                    
                } else {
                    // Show permission request UI
                   
                }
            }).catch((err) => {
                
                // ...
            });
        })
        .catch(function (err) {
           
        });
}


// Get registration token. Initially this makes a network call, once retrieved
// subsequent calls to getToken will return from cache.



messaging.onMessage((payload) => {
    // console.log('Message received. ', payload);

});

