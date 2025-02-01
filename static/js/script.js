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

// ===========================
// Handle AJAX Form Submissions
// ===========================
document.addEventListener("DOMContentLoaded", function () {
    function handleFormSubmission(formId) {
        const form = document.getElementById(formId);
        if (!form) return;

        const errorDiv = document.getElementById("form-errors");
        if (!errorDiv) return;

        form.addEventListener("submit", function (event) {
            event.preventDefault();
            errorDiv.innerHTML = "";
            errorDiv.style.display = "none";
            
            const formData = new FormData(form);

            fetch(form.action, {
                method: "POST",
                body: formData
            })
            .then(response => {
                if (!response.ok) throw new Error("Network response was not ok");
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    window.location.href = data.redirect_url;
                } else if (data.errors && Array.isArray(data.errors)) {
                    errorDiv.innerHTML = data.errors.join("<br>");
                    errorDiv.style.display = "block";
                } else {
                    errorDiv.innerHTML = "An unexpected error occurred. Please try again.";
                    errorDiv.style.display = "block";
                }
            })
            .catch(error => {
                console.error("Error:", error);
                errorDiv.innerHTML = "A network error occurred. Please check your connection and try again.";
                errorDiv.style.display = "block";
            });
        });
    }

    handleFormSubmission("reservation-form");
    handleFormSubmission("reservation-edit-form");
});