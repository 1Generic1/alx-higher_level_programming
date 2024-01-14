document.addEventListener('DOMContentLoaded', function() {
  let headerElement = document.querySelector('header');
  if (headerElement) {
    headerElement.style.color = '#FF0000';
  } else {
    console.error('Unable to find the <header> element.');
  }
});
