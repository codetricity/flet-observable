from model.game_state import GameState

right_frames = ["assets/right_1.png", "assets/right_2.png", "assets/right_3.png"]
left_frames = ["assets/left_1.png", "assets/left_2.png", "assets/left_3.png"]

def update_sprite(state: GameState) -> None:
    """Update sprite position and frame based on direction."""
    match state.direction:
        case "right":
            current = state.current_frame["right"]
            # Update frame index - this will trigger observable update
            state.current_frame = {**state.current_frame, "right": (current + 1) % len(right_frames)}
            if state.sprite_x < 800 - 80:
                state.sprite_x += 10
        case "left":
            current = state.current_frame["left"]
            # Update frame index - this will trigger observable update
            state.current_frame = {**state.current_frame, "left": (current + 1) % len(left_frames)}
            if state.sprite_x > 0:
                state.sprite_x -= 10
        case _:
            pass
