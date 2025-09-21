// This file lives in static/js/ and handles all the client-side logic for authentication.

// Main responsibilities of auth.js:
// 	•	Capture login/register form submissions (from index.html).
// 	•	Send the data to Flask backend routes (/login, /register) using fetch() or axios.
// 	•	Handle Flask’s response (success → redirect to /dashboard, failure → show error).
// 	•	Manage logout button click (clear local/session storage, redirect to /).
// 	•	Optionally: remember user with localStorage (remember me checkbox).

// ⸻

// 🔗 What it links to
// 	•	index.html → includes auth.js with:
// <script src="{{ url_for('static', filename='js/auth.js') }}"></script> 
// •	app.py + routes/auth.py → Flask endpoints that process login and register.
// @app.route('/login', methods=['POST'])
// def login():
//     # validate user credentials
//     # return success or error



document.addEventListener('DOMContentLoaded', function() {
    // Handle login form submission
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const rememberMe = document.getElementById('rememberMe').checked;
            
                // Send login data to Flask backend
                fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ username, password, rememberMe })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        window.location.href = '/dashboard';
                    } else {
                        alert(data.error || 'Login failed');
                    }
                })
                .catch(error => {
                    console.error('Login error:', error);
                    alert('An unexpected error occurred.');
                });
            });
        }
    });