import json
import os
from image_processor import ImageProcessor

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)

    processor = ImageProcessor(config)

    image_path = input("Введите путь к изображению: ").strip()
    if not os.path.exists(image_path):
        print("Файл не найден.")
        return

    qr_data = input("Введите данные для QR-кода: ").strip()

    print("Доступные сценарии:", list(config['scenarios'].keys()))
    scenario_name = input("Выберите сценарий: ").strip()
    if scenario_name not in config['scenarios']:
        print("Некорректный сценарий.")
        return

    result_image = processor.find_place_and_place_qr(image_path, qr_data, scenario_name)

    output_path = "output_" + os.path.basename(image_path)
    result_image.save(output_path)
    print(f"Изображение сохранено как {output_path}")

if __name__ == "__main__":
    main()
