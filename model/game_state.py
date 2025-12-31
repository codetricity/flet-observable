from dataclasses import dataclass
import flet as ft

@dataclass
@ft.observable
class GameState:
    direction: str = "right"
    sprite_x: int = 5
    sprite_y: int = 300
    current_frame: dict[str, int] = None

    # from dataclass.  runs after initialization
    def __post_init__(self):
        if self.current_frame is None:
            self.current_frame = {
                "right": 0,
                "left": 0,
                "up": 0,
                "down": 0,
            }
    
    def set_direction(self, direction: str):
        self.direction = direction