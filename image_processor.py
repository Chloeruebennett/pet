import qrcode
from PIL import Image
from pattern_strategy import PlacementStrategy
from factory import StrategyFactory
import random

class ImageProcessor:
    def __init__(self, config):
        self.config = config

    def generate_qr_code(self, data: str, size=150):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')
        img = img.resize((size, size), Image.ANTIALIAS)
        return img

    def find_place_and_place_qr(self, base_image_path, qr_data, scenario_name):
        base_image = Image.open(base_image_path).convert('RGBA')
        scenario_conf = self.config['scenarios'].get(scenario_name)
        if not scenario_conf:
            raise ValueError(f"Scenario {scenario_name} not found in config.")

        pattern_name = scenario_conf['pattern']
        margin = scenario_conf.get('margin', 10)

        qr_img = self.generate_qr_code(qr_data)
        qr_size = qr_img.size

        # Создаем стратегию размещения
        strategy = StrategyFactory.create_strategy(pattern_name, base_image, qr_size, margin)
        position = strategy.get_position()

        # Определяем слой для смешивания
        combined = base_image.copy()
        combined.paste(qr_img, position, qr_img)

        return combined
