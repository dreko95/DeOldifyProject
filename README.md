# DeOldifyProject

Цей проєкт використовує бібліотеку [DeOldify](https://github.com/jantic/DeOldify) та `fastai` для колоризації чорно-білих зображень.

## Встановлення
1. Клонуйте репозиторій.
2. Створіть та активуйте віртуальне середовище, наприклад:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Встановіть залежності:
   ```powershell
   pip install .
   ```

## Структура папок
- `colorize.py` — скрипт для колоризації зображень із папки `input`.  
- `trainModel.py` — тренує модель на датасеті в папці `Datasets/combined_256x256`.  
- `filterPhotos.py` — фільтрує та змінює розмір квадратних зображень, зберігає їх у ч/б та кольоровому форматах.  
- `input/` — вхідні зображення для колоризації.  
- `output/` — збережені кольорові зображення.  
- `Datasets/` — файли для тренування, розділені на ч/б і кольорові.

## Використання
1. Запуск колоризації:
   ```powershell
   python colorize.py
   ```
   Результат буде у папці `output/`.
2. Тренування моделі:
   ```powershell
   python trainModel.py
   ```
   Використовує дані з `Datasets/combined_256x256/bw` та `Datasets/combined_256x256/color`.

## Ліцензія
Проєкт ліцензовано за ліцензією [MIT](LICENSE).