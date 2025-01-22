// Initialize Flatpickr for date inputs on accounts/profile/edit
document.addEventListener("DOMContentLoaded", function() {
    flatpickr("input[name='birth_date']", {
        dateFormat: "Y-m-d" 
    });
});