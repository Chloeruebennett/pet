from abc import ABC, abstractmethod
from PIL import Image

class PlacementStrategy(ABC):
    def __init__(self, base_image: Image.Image, qr_size: tuple, margin: int):
        self.base_image = base_image
        self.qr_size = qr_size
        self.margin = margin

    @abstractmethod
    def get_position(self):
        pass

class BottomRightStrategy(PlacementStrategy):
    def get_position(self):
        width, height = self.base_image.size
        qr_width, qr_height = self.qr_size
        x = width - qr_width - self.margin
        y = height - qr_height - self.margin
        return (x, y)

class CenterStrategy(PlacementStrategy):
    def get_position(self):
        width, height = self.base_image.size
        qr_width, qr_height = self.qr_size
        x = (width - qr_width) // 2
        y = (height - qr_height) // 2
        return (x, y)

class TopLeftStrategy(PlacementStrategy):
    def get_position(self):
        return (self.margin, self.margin)
