// Add JavaScript code here
// For example, you can add code to validate the form fields before submission
// or add code to dynamically load images or content when the user scrolls down

// Example form validation code
const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const name = form.name.value.trim();
  const email = form.email.value.trim();
  const message = form.message.value.trim();
  
  if (name === '') {
    alert('Please enter your name');
    return;
  }
  
  if (email === '') {
    alert('Please enter your email');
    return;
  }
  
  if (message === '') {
    alert('Please enter a message');
    return;
  }
  
  // Submit form data to server using AJAX or fetch API
  // and display a success message to the user
  
  const formData = new FormData();
  formData.append('name', name);
  formData.append('email', email);
  formData.append('message', message);
  
  fetch('https://port-back.echendu.repl.co/contact', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log('API response:', data);
  })
  .catch(error => {
    console.error('API error:', error);
  });
  

  alert('Form submitted successfully!');
  form.reset();
});

