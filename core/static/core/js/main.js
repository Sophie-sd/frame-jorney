document.addEventListener('DOMContentLoaded', () => {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', () => {
            // Перемикаємо клас active на кнопці
            navbarToggler.classList.toggle('active');
            // Перемикаємо клас active на меню
            navbarCollapse.classList.toggle('active');

            // Опціонально: блокування скролу сторінки при відкритому меню
            // document.body.classList.toggle('no-scroll'); 
            // Потрібно додати в CSS: body.no-scroll { overflow: hidden; }
        });

        // Закриття меню при кліку на посилання (для лендінгу)
        const navLinks = navbarCollapse.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navbarCollapse.classList.contains('active')) {
                    navbarToggler.classList.remove('active');
                    navbarCollapse.classList.remove('active');
                    // document.body.classList.remove('no-scroll');
                }
            });
        });
    }

    // --- Слайдер Відгуків (Tiny Slider) --- 
    const reviewsSlider = document.querySelector('.reviews-list.tns-slider');
    if (reviewsSlider) {
        const slider = tns({
            container: reviewsSlider,
            items: 1, // Скільки слайдів видно на мобільних
            slideBy: 1,
            autoplay: false,
            controlsContainer: ".reviews-controls", // Контейнер для кнопок
            prevButton: ".reviews-controls .prev",
            nextButton: ".reviews-controls .next",
            nav: false, // Вимикаємо точки навігації
            mouseDrag: true, // Дозволяємо перетягування мишкою
            gutter: 20, // Відстань між слайдами
            responsive: {
                600: { // від 600px ширини екрану
                    items: 2 // Показуємо 2 слайди
                },
                992: { // від 992px ширини екрану
                    items: 3 // Показуємо 3 слайди
                }
            }
        });
    }

    // --- Ініціалізація AOS (Animate On Scroll) ---
    AOS.init({
        duration: 800, // Тривалість анімації
        once: true, // Анімація спрацьовує тільки один раз
        offset: 50 // Відступ від низу екрану для спрацювання
    });

    // --- Модальне вікно контакту ---
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
        // Закриваємо по кліку на фон
        modalOverlay.addEventListener('click', closeModal);
    }
    
    // Закриваємо по натисканню Esc
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && contactModal && contactModal.classList.contains('active')) {
            closeModal();
        }
    });
}); 