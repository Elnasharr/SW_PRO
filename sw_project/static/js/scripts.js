document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    const profileInfo = document.getElementById('profileInfo');
    const logoutBtn = document.getElementById('logoutBtn');

    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            localStorage.setItem('user', JSON.stringify({ email }));
            window.location.href = 'index.html'; 
        });
    }

    if (signupForm) {
        signupForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            localStorage.setItem('user', JSON.stringify({ name, email }));
            window.location.href = 'index.html'; 
        });
    }

    if (profileInfo) {
        const user = JSON.parse(localStorage.getItem('user'));
        if (user) {
            profileInfo.innerHTML = `<p>Name: ${user.name || 'N/A'}</p><p>Email: ${user.email}</p>`;
        } else {
            window.location.href = 'login.html';
        }
    }

    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            localStorage.removeItem('user');
            window.location.href = 'index.html';
        });
    }


    const loginNavItem = document.getElementById('loginNavItem');
    const profileNavItem = document.getElementById('profileNavItem');
    const user = JSON.parse(localStorage.getItem('user'));
    if (user) {
        loginNavItem.classList.add('d-none');
        profileNavItem.classList.remove('d-none');
    } else {
        loginNavItem.classList.remove('d-none');
        profileNavItem.classList.add('d-none');
    }
});