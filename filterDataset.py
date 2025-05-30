from PIL import Image
from pathlib import Path
import os

ROOT_PATH = Path(__file__).parent.absolute()
INPUT_PATH = ROOT_PATH / "Datasets" / "images"

# Шляхи для виводу
OUT_128_COLOR = ROOT_PATH / "Datasets" / "combined_128x128" / "color"
OUT_128_BW = ROOT_PATH / "Datasets" / "combined_128x128" / "bw"
OUT_256_COLOR = ROOT_PATH / "Datasets" / "combined_256x256" / "color"
OUT_256_BW = ROOT_PATH / "Datasets" / "combined_256x256" / "bw"

# Створюємо вихідні папки, якщо їх немає
os.makedirs(OUT_128_COLOR, exist_ok=True)
os.makedirs(OUT_128_BW, exist_ok=True)
os.makedirs(OUT_256_COLOR, exist_ok=True)
os.makedirs(OUT_256_BW, exist_ok=True)

image_extensions = ['.jpg', '.jpeg', '.png']
all_images = []
for ext in image_extensions:
    all_images.extend(list(INPUT_PATH.glob(f"*{ext}")))

if not all_images:
    print(f"У папці {INPUT_PATH} не знайдено зображень.")
    exit(1)

count = 0
for img_path in all_images:
    try:
        with Image.open(img_path) as img:
            width, height = img.size
            # Перевіряємо, що зображення квадратне та більше 256 пікселів
            if width == height and width > 256:
                img_128 = img.resize((128, 128), Image.LANCZOS)
                img_256 = img.resize((256, 256), Image.LANCZOS)

                out_color_128 = OUT_128_COLOR / img_path.name
                out_color_256 = OUT_256_COLOR / img_path.name
                img_128.save(out_color_128)
                img_256.save(out_color_256)

                # Створюємо чорно-білу версію
                bw_128 = img_128.convert("L").convert("RGB")
                bw_256 = img_256.convert("L").convert("RGB")

                out_bw_128 = OUT_128_BW / img_path.name
                out_bw_256 = OUT_256_BW / img_path.name
                bw_128.save(out_bw_128)
                bw_256.save(out_bw_256)

                count += 1
                print(f"Оброблено {count} зображень: {img_path.name}")
            else:
                print(f"Пропущено {img_path.name}: не квадратне або розмір <= 256 (ширина: {width}, висота: {height})")
    except Exception as e:
        print(f"Помилка при обробці {img_path.name}: {e}")

if count == 0:
    print("Не знайдено жодного квадратного зображення зі стороною > 256.")
else:
    print(f"Обробка завершена. Усього успішно відсортовано {count} зображень.")