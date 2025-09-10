from pattern_strategy import BottomRightStrategy, CenterStrategy, TopLeftStrategy

class StrategyFactory:
    strategies = {
        "bottom_right": BottomRightStrategy,
        "center": CenterStrategy,
        "top_left": TopLeftStrategy
    }

    @staticmethod
    def create_strategy(pattern_name, base_image, qr_size, margin):
        strategy_cls = StrategyFactory.strategies.get(pattern_name)
        if not strategy_cls:
            raise ValueError(f"Unknown pattern: {pattern_name}")
        return strategy_cls(base_image, qr_size, margin)
