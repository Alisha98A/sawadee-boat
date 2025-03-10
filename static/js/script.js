/* global flatpickr */

// ===========================
// Initialize Flatpickr Inputs
// ===========================
document.addEventListener("DOMContentLoaded", function() {
    if (typeof flatpickr !== "undefined") {
        // Initialize Flatpickr for birth date in profile
        flatpickr("input[name='birth_date']", {
            dateFormat: "Y-m-d"
        });

        // Initialize Flatpickr for the booking date input (All days enabled)
        flatpickr("input[name='booking_date']", {
            dateFormat: "Y-m-d",
            minDate: "today"
        });
    } else {
        console.error("Flatpickr is not loaded. Check script inclusion.");
    }
});

// ===========================
// Handle AJAX Form Submissions
// ===========================
document.addEventListener("DOMContentLoaded", function () {
    async function handleFormSubmission(forms) {
        forms.forEach(formId => {
            const form = document.getElementById(formId);
            if (!form) return;

            const errorDiv = document.getElementById("form-errors");
            if (!errorDiv) return;

            form.addEventListener("submit", async function (event) {
                event.preventDefault();
                errorDiv.innerHTML = "";
                errorDiv.style.display = "none";
                
                const formData = new FormData(form);

                try {
                    const response = await fetch(form.action, {
                        method: "POST",
                        body: formData,
                        headers: { "X-Requested-With": "XMLHttpRequest" }
                    });

                    if (!response.ok) throw new Error("Network response was not ok");

                    const data = await response.json();

                    if (data.success) {
                        window.location.href = data.redirect_url;
                    } else {
                        errorDiv.innerHTML = (data.errors && Array.isArray(data.errors))
                            ? data.errors.join("<br>")
                            : "An unexpected error occurred. Please try again.";
                        errorDiv.style.display = "block";
                    }
                } catch (error) {
                    console.error("Error:", error);
                    errorDiv.innerHTML = "A network error occurred. Please check your connection and try again.";
                    errorDiv.style.display = "block";
                }
            });
        });
    }

    handleFormSubmission(["reservation-form", "reservation-edit-form"]);
});

// ===========================
// Navbar Scroll Effect
// ===========================
document.addEventListener("DOMContentLoaded", function () {
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector("#navbarNav");

    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener("click", function () {
            navbarCollapse.classList.toggle("show"); 
        });

        // Close the navbar when a link is clicked
        const navLinks = navbarCollapse.querySelectorAll(".nav-link");
        navLinks.forEach(link => {
            link.addEventListener("click", function () {
                navbarCollapse.classList.remove("show");
            });
        });
    }
});