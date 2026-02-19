document.addEventListener('DOMContentLoaded', () => {
  const firstNameInput = document.getElementById('first_name');
  const lastNameInput = document.getElementById('last_name');
  const usernameInput = document.getElementById('username');

  function generateUsername() {
    const firstName = firstNameInput.value.trim();
    const lastName = lastNameInput.value.trim();

    if (firstName || lastName) {
      // Convert to lowercase
      // Replace spaces or multiple spaces with underscore
      const username = `${firstName} ${lastName}`
        .toLowerCase()
        .normalize('NFD') // decompose accents
        .replace(/[\u0300-\u036f]/g, '') // remove diacritics
        .replace(/\s+/g, '_'); // replace spaces with underscores

      usernameInput.value = username;
    } else {
      usernameInput.value = '';
    }
  }

  // Listen to both inputs
  firstNameInput.addEventListener('input', generateUsername);
  lastNameInput.addEventListener('input', generateUsername);
});
