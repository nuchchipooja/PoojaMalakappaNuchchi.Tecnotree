const transferForm = document.querySelector('form[action="/transfer"]');
const withdrawForm = document.querySelector('form[action="/withdraw"]');
const updateInfoForm = document.querySelector('form[action="/update-info"]');

transferForm.addEventListener('submit', (event) => {
  event.preventDefault(); // prevent default form submission behavior
  const recipientAccount = document.getElementById('recipient-account').value;
  const transferAmount = document.getElementById('transfer-amount').value;
  const verificationCode = document.getElementById('verification-code').value;
  
  // do something with form data, e.g. send request to server
});

withdrawForm.addEventListener('submit', (event) => {
  event.preventDefault(); // prevent default form submission behavior
  const transferAmount = document.getElementById('transfer-amount').value;
  const verificationCode = document.getElementById('verification-code').value;
  
  // do something with form data, e.g. send request to server
});

updateInfoForm.addEventListener('submit', (event) => {
  event.preventDefault(); // prevent default form submission behavior
  const name = document.getElementById('name').value;
  const address = document.getElementById('address').value;
  const phone = document.getElementById('phone').value;
  
  // do something with form data, e.g. send request to server
});
