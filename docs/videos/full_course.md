# Flet Beginner Course for Game Development

## [Flet 1.0 Python for Beginners Course Overview (Learn Python by Building Games) 1](https://youtu.be/F2f98GhkKUA)

Start of tutorial series on Flet Python games. Covers getting free sprite graphics for games, using 4 degrees of movement.

This video introduces a beginner-friendly Python tutorial series where the primary goal is to learn Python fundamentals, using Flet 1.0 to make the learning process more visual and engaging.

Instead of starting with abstract examples, we build a very simple, game-like application entirely in Python. We use character graphics inspired by the Pepper & Carrot comic (sourced from OpenGameArt with proper attribution) to make the experience more fun and concrete—especially for learners who benefit from visual feedback.

This first video is a preview and orientation. It shows how assets are prepared, how sprites are positioned on screen, and how Python code controls movement and animation. The actual step-by-step coding begins in the next videos.

What this series focuses on:

Learning core Python concepts through hands-on practice
Using Flet 1.0 as a lightweight UI framework (no Dart or Flutter required)
Working with images, coordinates, and simple animations

Practicing modern Python features such as:

- dataclasses
- state stored in objects
- observable / reactive updates
- Understanding how UI state changes trigger screen updates

What this series is not:

- It is not a full game development course
- It is not an advanced Flutter or Flet deep dive
- It is not optimized for production games

Instead, this series is designed as a low-friction way to practice Python while seeing immediate, visual results. Flet makes it possible to run the same Python code on Windows, macOS, Linux, web, and mobile, but portability is a bonus—not the main objective.

If you are new to Python, or you want a more engaging way to practice Python fundamentals, this series is a good place to start.

### Credits

Pepper & Carrot thumbnail graphic from David Revoy, released user [CC4](https://creativecommons.org/licenses/by/4.0/).

[Pepper & Carrot](https://www.peppercarrot.com/)

[Pepper & Carrot sprite sheet](https://opengameart.org/content/24x32-peppercarrot-characters)

From [diamonddmgirl](https://opengameart.org/users/diamonddmgirl)

---

## [Flet 1.0 Reactive State Management in Python - 2](https://youtu.be/e0krw8TrGII)

Python tutorial series explaining reactive state management and UI development using Flet. The project is inspired by the Pepper & Carrot comic and uses a simple sprite-based character (Pepper) to demonstrate how observables, reactive programming, and MVC-style separation work in a Python UI application.
We look at how a character can move left, right, up, and down using basic animation frames, while the UI automatically re-renders in response to state changes—without manually calling page.update(). The key idea is learning observables: instead of directly mutating UI elements, we update application state and let listeners react to those changes.
Topics covered in this overview:

- Reactive programming and data binding concepts
- Managing UI state with Flet observables (Flet 1.0 beta)
- Declarative UI patterns in Python
- MVC-style separation of model, view, and control
- Sprite animation using multiple image frames
- Dictionary unpacking and immutable-style state updates
- Using Python decorators to create reactive behavior

This tutorial series is not meant to be a game development course. For serious game development, tools like Pygame (Python) or Flame with Flutter are better choices. Instead, this project is designed as a fun and approachable way to practice state management and reactive UI patterns in pure Python.
If you're coming from Flutter, this tutorial can also serve as a conceptual bridge. After completing it, you could rebuild the same example using Riverpod, Bloc, or Provider to reinforce your understanding of state management across ecosystems.
In the next video, we'll start from a blank screen and build everything step by step.
If you're interested in learning how reactive UIs work—while staying entirely in Python—this series is for you.

---

## [Start Flet 1.0 Game With Background Graphics - 3](https://youtu.be/hdQhcMid5D4)

Start a new Flet 1.0 Python project and begin coding your game world.

- Initialize new project with uv and Python 3.13
- Add Flet 0.80 with uv
- Organize project using Model View Control (MVC)
- Added the "world" background image in the view folder
- Import your view into main
- @ft.component
- Declarative UI for reactive state
- page.render()
- Adjust flet window width
- Flet Stack for layers and pixel positioning

## [4 Python + Flet 1.0 Game Dev: Layered Backgrounds, Sprites, and Observable Game State](https://youtu.be/AyS3HWiEalE)

Building a simple 2D game with Python and Flet 1.0 by placing a character sprite on top of a background using layered rendering.

Flet concepts covered:

- GameState class using Python dataclasses
- ft.observable
- ft.use_state
- page.run_task()
- ft.use_effect()

Introduce the core idea of layers by drawing the background first and then rendering the character on top using a canvas-style approach. The character sprite is wrapped in a Container, which gives us precise control over positioning and prepares us for movement and animation in later videos.

- Using images as layers (background vs. foreground sprite)
- Wrapping a sprite in a Container to control left and top positioning
- Starting with a single-frame character image (PNG) before animation
- Structuring a scalable game state using Python @dataclass
- Making game state reactive with ft.observable
- Connecting state changes to UI updates without set_state
- Moving a character using async loops, use_effect, and run_task

By the end of the video, Pepper is moving smoothly across the screen based on changes to a shared game state—laying the foundation for multi-directional movement, input handling, and sprite animations.

In the next video, we'll slow down and explain the architecture in more detail using slides, including how observables, async tasks, and state management work together in Flet.

This series is beginner-friendly and focuses on learning Python through practical, visual game development concepts.

## [Python + Flet State Management Explained: useState, Observable Classes, and Game Animation - 5](https://youtu.be/RyUpdMONqN0)

## [Python + Flet 1.0 Game Animation: Sprite Frames, Direction State, and Walking Animations - 6](https://youtu.be/dKS-Nhf6OoY)

## [Python + Flet 1.0: Add Direction Buttons (Up/Down/Left/Right) with State-Driven Re-Renders - 7](https://youtu.be/Vi7LwQJiZG8)
