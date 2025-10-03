// Blog JS
document.addEventListener("DOMContentLoaded", function () {
  console.log("Django Blog JS Loaded ✅");

  // Example: Show a confirm dialog before logout
  const logoutBtn = document.querySelector(".btn-danger");
  if (logoutBtn) {
      logoutBtn.addEventListener("click", function (e) {
          if (!confirm("Are you sure you want to log out?")) {
              e.preventDefault();
          }
      });
  }

  // Example: Auto-hide alerts after 5 seconds
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach(alert => {
      setTimeout(() => {
          alert.style.display = "none";
      }, 5000);
  });
});
