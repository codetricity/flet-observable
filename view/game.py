import flet as ft
import asyncio
from model.game_state import GameState
from control.movement import update_sprite

@ft.component
def GameView():
    state, _ = ft.use_state(GameState())
    
    # Animation loop using use_effect
    def start_animation():
        async def tick():
            while True:
                await asyncio.sleep(0.2)
                update_sprite(state)
        
        return ft.context.page.run_task(tick)
    
    ft.use_effect(start_animation, [])
    
    # Button handlers
    def on_left_click(e):
        state.set_direction("left")
    
    def on_right_click(e):
        state.set_direction("right")
    
    def on_down_click(e):
        state.set_direction("down")
    
    # Get current frame based on state
    frames = {
        "right": ["assets/right_1.png", "assets/right_2.png", "assets/right_3.png"],
        "left": ["assets/left_1.png", "assets/left_2.png", "assets/left_3.png"],
        "down": ["assets/down_1.png", "assets/down_2.png", "assets/down_3.png"],

    }
    current_frame_idx = state.current_frame[state.direction]
    current_frame_path = frames[state.direction][current_frame_idx]
    
    # Build UI based on state
    sprite = ft.Container(
        content=ft.Image(
            src=current_frame_path,
            width=80,
            height=120
        ),
        left=state.sprite_x,
        top=state.sprite_y,
    )
    
    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Button("left", on_click=on_left_click),
                    ft.Button("right", on_click=on_right_click),
                    ft.Button("down", on_click=on_down_click)
                ]
            ),
            ft.Stack(
                controls=[ft.Image(src="background.jpg"), sprite],
                width=800,
                height=600,
            ),
        ]
    )
