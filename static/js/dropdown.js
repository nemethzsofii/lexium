/**
 * @typedef {Object} CaseItem
 * @property {number} id - Case identifier
 * @property {string} name - Case name
 */

/**
 * @typedef {Object} User
 * @property {number} id - User identifier
 * @property {string} first_name - User first name
 * @property {string} last_name - User last name
 */

document.addEventListener('DOMContentLoaded', () => {
  /** @type {string|undefined} */
  var caseResult = populateCaseDropdown();
  if (!caseResult) {
    console.log('No case select element found.');
  } else {
    console.log(caseResult);
  }
});

/**
 * Populate the case select dropdown by fetching case list from server.
 * @returns {string|undefined} Returns a status string, or `undefined` if the select element is not found.
 */
function populateCaseDropdown() {
  /** @type {HTMLSelectElement | null} */
  const caseSelect = /** @type {HTMLSelectElement | null} */ (
    document.getElementById('case-select')
  );
  if (!caseSelect) return;
  fetch('/get-cases')
    .then((response) => {
      /** @type {Response} */
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      /** @type {CaseItem[]} */
      console.log('Esetek betöltve:', data);
      data.forEach((caseItem) => {
        /** @type {HTMLOptionElement} */
        const option = document.createElement('option');
        option.value = String(caseItem.id);
        option.textContent = caseItem.id + ' - ' + caseItem.name;
        caseSelect.appendChild(option);
      });
      return 'Case dropdown populated successfully.';
    })
    .catch((error) => console.error('Error while loading case list:', error));
  return 'Case dropdown population failed.';
}

/**
 * Populate the user select dropdown by fetching users from server.
 * @returns {string|undefined} Returns a status string, or `undefined` if the select element is not found.
 */
function populateUserDropdown() {
  /** @type {HTMLSelectElement | null} */
  const userSelect = /** @type {HTMLSelectElement | null} */ (
    document.getElementById('user-select')
  );
  if (!userSelect) return;

  /** @type {Promise<Response>} */
  const request = fetch('/get-users');
  request
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      /** @type {Promise<User[]>} */
      const user = response.json();
      return user;
    })
    .then((data) => {
      data.forEach((user) => {
        /** @type {HTMLOptionElement} */
        const option = document.createElement('option');
        option.value = String(user.id);
        option.textContent = user.first_name + ' ' + user.last_name;
        userSelect.appendChild(option);
      });
      return 'User dropdown populated successfully.';
    })
    .catch((error) => console.error('Error while loading user list:', error));
  return 'User dropdown population failed.';
}
