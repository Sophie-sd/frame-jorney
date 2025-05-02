document.addEventListener('DOMContentLoaded', () => {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', () => {
            navbarToggler.classList.toggle('active');
            navbarCollapse.classList.toggle('active');
        });

        const navLinks = navbarCollapse.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navbarCollapse.classList.contains('active')) {
                    navbarToggler.classList.remove('active');
                    navbarCollapse.classList.remove('active');
                }
            });
        });
    }

    const reviewsSlider = document.querySelector('.reviews-list.tns-slider');
    if (reviewsSlider) {
        const slider = tns({
            container: reviewsSlider,
            items: 1,
            slideBy: 1,
            autoplay: false,
            loop: false,
            controlsContainer: ".reviews-controls",
            prevButton: ".reviews-controls .prev",
            nextButton: ".reviews-controls .next",
            nav: false,
            mouseDrag: true,
            gutter: 20,
            responsive: {
                600: { items: 2 },
                992: { items: 3 }
            }
        });
    }

    AOS.init({
        duration: 800,
        once: true,
        offset: 50
    });

    const openModalBtn = document.getElementById('open-contact-modal');
    const closeModalBtn = document.getElementById('close-contact-modal');
    const contactModal = document.getElementById('contact-modal');
    const modalOverlay = document.getElementById('modal-overlay');

    const openModal = () => {
        if (contactModal) contactModal.classList.add('active');
    };

    const closeModal = () => {
        if (contactModal) contactModal.classList.remove('active');
    };

    if (openModalBtn) {
        openModalBtn.addEventListener('click', openModal);
    }

    if (closeModalBtn) {
        closeModalBtn.addEventListener('click', closeModal);
    }

    if (modalOverlay) {
        modalOverlay.addEventListener('click', closeModal);
    }
    
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && contactModal && contactModal.classList.contains('active')) {
            closeModal();
        }
    });

    const lightbox = GLightbox({
        selector: '.glightbox',
    });
    if (lightbox) {
        lightbox.reload();
    }

    const showMoreBtn = document.getElementById('show-more-portfolio');
    if (showMoreBtn) {
        showMoreBtn.addEventListener('click', () => {
            const hiddenItems = document.querySelectorAll('.portfolio-item-hidden');
            hiddenItems.forEach(item => {
                item.classList.remove('portfolio-item-hidden');
                item.style.animation = 'fadeIn 0.5s ease-out forwards';
            });
            
            showMoreBtn.style.display = 'none';

            if (typeof lightbox !== 'undefined' && lightbox) {
                lightbox.reload();
            }
        });
    }

}); 