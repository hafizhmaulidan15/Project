// dokum.js
document.addEventListener('DOMContentLoaded', () => {
    // Get the lightbox elements
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const close = document.querySelector('.close');

    // Get the flowchart images
    const flowchartImages = document.querySelectorAll('.image-gallery.flowcharts img');
    
    // Add click event to flowchart images
    flowchartImages.forEach(img => {
        img.addEventListener('click', () => {
            lightbox.style.display = 'block';
            lightboxImg.src = img.src;
        });
    });

    // Add click event to close button
    close.addEventListener('click', () => {
        lightbox.style.display = 'none';
        panzoom.reset(); // Reset zoom on close
    });

    // Add click event to lightbox to close when clicking outside the image
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            lightbox.style.display = 'none';
            panzoom.reset(); // Reset zoom on close
        }
    });

    // Initialize Panzoom
    const panzoom = Panzoom(lightboxImg, {
        maxScale: 4, // Maximum scale factor
        contain: 'outside' // Contain within the viewport
    });

    // Enable mouse wheel zoom
    lightboxImg.parentElement.addEventListener('wheel', panzoom.zoomWithWheel);
});
