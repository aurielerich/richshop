function showToast(title, message, type = 'normal', duration = 5000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');

    if (!toastComponent) return;
    toastTitle.textContent = title;
    toastMessage.textContent = message;
    toastComponent.classList.remove(
        'bg-green-50', 'border-green-500', 'text-green-700', // Success
        'bg-red-50', 'border-red-500', 'text-red-700',     // Error
        'bg-blue-50', 'border-blue-500', 'text-blue-700',   // Info (Baru)
        'bg-white', 'border-gray-300', 'text-gray-800'     // Normal
    );

    if (type === 'success') {
        toastComponent.classList.add('bg-green-50', 'border-green-500', 'text-green-700');
    } 
    else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-700');
    } 
    else if (type === 'info') {
        toastComponent.classList.add('bg-blue-50', 'border-blue-500', 'text-blue-700');
    } 
    else {
        toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-800');
    }
    toastComponent.classList.remove('hidden');
    toastComponent.offsetHeight; 
    
    toastComponent.classList.remove('opacity-0', '-translate-y-full');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', '-translate-y-full');

        setTimeout(() => {
            toastComponent.classList.add('hidden');
        }, 500);

    }, duration);
}