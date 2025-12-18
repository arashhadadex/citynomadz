document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Check for saved theme preference, default to light
    const currentTheme = localStorage.getItem('theme') || 'light';
    body.classList.add(currentTheme + '-mode');
    updateToggleButton(currentTheme);

    themeToggle.addEventListener('click', () => {
        let newTheme;
        if (body.classList.contains('light-mode')) {
            body.classList.replace('light-mode', 'dark-mode');
            newTheme = 'dark';
        } else {
            body.classList.replace('dark-mode', 'light-mode');
            newTheme = 'light';
        }
        localStorage.setItem('theme', newTheme);
        updateToggleButton(newTheme);
    });

    function updateToggleButton(theme) {
        if (theme === 'dark') {
            themeToggle.querySelector('.icon-light').style.display = 'none';
            themeToggle.querySelector('.icon-dark').style.display = 'inline';
        } else {
            themeToggle.querySelector('.icon-light').style.display = 'inline';
            themeToggle.querySelector('.icon-dark').style.display = 'none';
        }
    }
});