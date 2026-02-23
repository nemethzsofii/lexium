document.querySelectorAll('.number-format').forEach((input) => {
  function formatNumber(value) {
    if (!value) return '';
    const numeric = value.replace(/\D/g, '');
    return numeric.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
  }

  input.addEventListener('input', function () {
    const cursorPosition = this.selectionStart;
    const formatted = formatNumber(this.value);
    this.value = formatted;
    this.setSelectionRange(cursorPosition, cursorPosition);
  });
});
