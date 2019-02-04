const modalImage = document.querySelector('#modal-photo');
const modalTitle = document.querySelector('#modal-title');

document.querySelectorAll('.additional-photo').forEach(img => {
    img.addEventListener('click', e => {
        modalImage.src = e.target.src;
        modalTitle.textContent = `Photo ${e.target.dataset.index}`;
    });
});