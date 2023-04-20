const form = document.querySelector('form');




form.addEventListener('submit', function(e) {
 e.preventDefault();
 alert("login Successfull!!!")




// Form validation code here




// Redirect to index.html if form is valid

 window.location.assign('userdashboard.html');

});