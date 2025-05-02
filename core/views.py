import os
import unicodedata
from django.conf import settings
from django.shortcuts import render

def home(request):
    video_files_data = []
    # Шлях до папки з відео в статиці core
    if settings.STATICFILES_DIRS:
        # Використовуємо перший шлях з STATICFILES_DIRS
        video_dir = os.path.join(settings.STATICFILES_DIRS[0], 'core', 'media')
    else:
        # Fallback, якщо STATICFILES_DIRS не задано
        video_dir = os.path.join(settings.BASE_DIR, 'core', 'static', 'core', 'media')

    allowed_extensions = ('.mp4', '.mov', '.avi', '.mkv', '.webm')

    # Словник українських НАЗВ для відео (ключ - англ. base_name)
    video_titles_ukr = {
        "left-under-the-snow-on-hoverla": "Залишились під снігом на Говерлі",
        "spent-the-night-in-a-tree-above-bukovel": "Заночував на дереві над Буковелем",
        "moment": "Моментик",
        "be-careful-very-beautiful": "Обережно! Дуже красиво",
        "the-night-begins-in-the-carpathians": "Починається ніч у Карпатах",
        "dawn-from-a-tree-over-bukovel": "Світанок з дерева над Буковелем",
        "dawn-the-mountains-are-changing-color": "Світанок. Гори міняють колір",
        "skiing-down-from-hoverla": "Спуск аж з Говерли на лижах",
        "this-is-the-top-trailer": "Це ж самий топовий трейлер"
    }

    # Словник українських ОПИСІВ для відео (ключ - англ. base_name)
    video_descriptions_ukr = {
        "left-under-the-snow-on-hoverla": "Шторм, сніг і справжня боротьба з природою — та ще пригода!",
        "spent-the-night-in-a-tree-above-bukovel": "Підвісна хатина, вітер у кронах і ніч на висоті — досвід, що запам'ятається.",
        "moment": "Короткий, але теплий кадр...",
        "be-careful-very-beautiful": "Класика Карпат. Летиш над хмарами — і здається, світ зупиняється.",
        "the-night-begins-in-the-carpathians": "Небо, вкрите зірками, і тиша, яка говорить гучніше за слова.",
        "dawn-from-a-tree-over-bukovel": "Перші промені пробиваються крізь хмари. Тиша. Світ прокидається.",
        "dawn-the-mountains-are-changing-color": "Палаючі вершини. Неймовірна гра світла на висоті.",
        "skiing-down-from-hoverla": "Фрістайл із даху України. Вітер в обличчя, свобода під ногами.",
        "this-is-the-top-trailer": "Команда, енергія, пік. Це — відео, яке хочеться передивитись."
    }

    # Кастомний порядок відео (АКТУАЛЬНІ англійські імена)
    custom_order = [
        "this-is-the-top-trailer",
        "spent-the-night-in-a-tree-above-bukovel",
        "skiing-down-from-hoverla"
    ]

    if os.path.exists(video_dir) and os.path.isdir(video_dir):
        try:
            # Тепер os.listdir() поверне нові англійські імена файлів
            for filename in os.listdir(video_dir):
                if os.path.isfile(os.path.join(video_dir, filename)) and filename.lower().endswith(allowed_extensions):
                    if not filename.startswith('.'):
                        # Отримуємо актуальне англійське ім'я файлу без розширення
                        # Перетворюємо на lowercase для уніфікації ключа
                        base_name = os.path.splitext(filename)[0].lower()
                        
                        # Отримуємо українську назву та опис
                        title_ukr = video_titles_ukr.get(base_name, base_name.replace('-', ' ').capitalize()) # Fallback: англ. назва
                        description_ukr = video_descriptions_ukr.get(base_name, "") # Fallback: порожній опис
                        
                        video_files_data.append({
                            'filename': filename,          # Актуальне ім'я файлу (англ.)
                            'title_ukr': title_ukr,        # Українська назва для відображення
                            'description': description_ukr, # Український опис
                            'base_name': base_name          # Англ. base_name (lowercase) для сортування
                        })

            # Функція для кастомного сортування (працює з англ. іменами)
            def get_sort_key(video_data):
                base_name = video_data['base_name']
                if base_name in custom_order:
                    return (custom_order.index(base_name), base_name)
                else:
                    return (float('inf'), base_name)

            video_files_data.sort(key=get_sort_key)

        except OSError as e:
            # Можна додати логування помилки тут: print(f"Error accessing video directory: {e}")
            pass

    context = {
        'video_files': video_files_data, # Тепер містить і filename, і title_ukr, і description
    }
    return render(request, 'core/home.html', context)