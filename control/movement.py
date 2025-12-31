from model.game_state import GameState

right_frames = ["assets/right_1.png", "assets/right_2.png", "assets/right_3.png"]
left_frames = ["assets/left_1.png", "assets/left_2.png", "assets/left_3.png"]
down_frames = ["assets/down_1.png", "assets/down_2.png", "assets/down_3.png"]
up_frames = ["assets/up_1.png", "assets/up_2.png", "assets/up_3.png"]

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
        case "down":
            current = state.current_frame["down"]
            # Update frame index - this will trigger observable update
            state.current_frame = {**state.current_frame, "down": (current + 1) % len(right_frames)}
            if state.sprite_y < 600 - 120:
                state.sprite_y += 10
        case "up":
            current = state.current_frame["up"]
            # Update frame index - this will trigger observable update
            state.current_frame = {**state.current_frame, "up": (current + 1) % len(up_frames)}
            if state.sprite_y > 0:
                state.sprite_y -= 10                
        case _:
            pass
