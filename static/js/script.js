// ===========================
// Initialize Flatpickr Inputs
// ===========================
document.addEventListener("DOMContentLoaded", function() {
    // Initialize Flatpickr for birth date in profile
    flatpickr("input[name='birth_date']", {
        dateFormat: "Y-m-d"
    });

    // Initialize Flatpickr for the booking date input (All days enabled)
    flatpickr("input[name='booking_date']", {
        dateFormat: "Y-m-d",
        minDate: "today"
    });
});