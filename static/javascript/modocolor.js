const toggleButton = document.getElementById('toggleTheme');
const body = document.body;

toggleButton.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
});

document.querySelectorAll('.clickable-image').forEach(img => {
    img.addEventListener('click', () => {
        const modal = new bootstrap.Modal(document.getElementById('imgModal'));
        document.getElementById('modalImg').src = img.src;
        modal.show();
    });
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        const modalEl = document.getElementById('imgModal');
        const modal = bootstrap.Modal.getInstance(modalEl);
        if (modal) modal.hide();
    }
});

document.getElementById('modalImg').addEventListener('click', () => {
    const modalEl = document.getElementById('imgModal');
    const modal = bootstrap.Modal.getInstance(modalEl);
    if (modal) modal.hide();
});