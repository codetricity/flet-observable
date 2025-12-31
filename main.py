import flet as ft
from view.game import GameView

def main(page: ft.Page):
    page.window.width=820
    page.render(GameView)

if __name__ == "__main__":
    ft.run(main)
