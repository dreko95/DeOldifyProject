import os
from pathlib import Path
from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import get_artistic_image_colorizer
import torch
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Your dataset is empty.")

device.set(device=DeviceId.GPU0 if torch.cuda.is_available() else DeviceId.CPU)

ROOT_PATH = Path(__file__).parent
INPUT_PATH = ROOT_PATH / "input"
OUTPUT_PATH = ROOT_PATH / "output"
MODEL_PATH = ROOT_PATH / "DeOldify" 

# Ініціалізація колоризатора
colorizer = get_artistic_image_colorizer(
    root_folder=MODEL_PATH,
    render_factor=35,
    weights_name="combined_256x256",
)

# Колоризація всіх зображень з папки input
image_extensions = ('.jpg', '.jpeg', '.png')
input_images = [p for p in INPUT_PATH.iterdir() if p.suffix.lower() in image_extensions]

if not input_images:
    print("У папці input немає зображень для колоризації.")
else:
    for input_image in input_images:
        print(f"Колоризація: {input_image.name}")
        result_path = colorizer.plot_transformed_image(
            path=input_image,
            render_factor=35,
            compare=True,  
            results_dir=OUTPUT_PATH
        )
        print(f"Результат збережено у: {result_path}")