function openModal() {
    const modal = document.getElementById('pet-modal');
    if (modal) {
        modal.classList.remove('hidden');
    }
}

// close modal
const closeBtn = document.getElementById('close-modal-btn');
if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
        e.preventDefault();
        document.getElementById('pet-modal').classList.add('hidden');
    });
}


/**
 * @param {string} name
 * @param {string} photo
 */

function selectPet(name, photo) {
    document.getElementById('selected-pet-name').value = name;

    const display = document.querySelector('.selected-pet-details');
    
    const fullStaticPath = `/static/${photo.replace('../', '')}`;
    
    display.innerHTML = `
        <img src="${fullStaticPath}" 
             alt="${name}" 
             onerror="this.src='/static/images/default.png';">
        <b>${name}</b>`;
    document.getElementById('pet-modal').classList.add('hidden');
}