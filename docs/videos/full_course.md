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

---

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

---

## [Python + Flet State Management Explained: useState, Observable Classes, and Game Animation - 5](https://youtu.be/RyUpdMONqN0)

Lecture on state in the Flet game we're building with Python.

How ft.use_state works in Flet, how it compares to React's useState, and why observable Python classes are often the better choice for complex, mutable game state such as character movement and animation.

Topics covered in this lesson include:

- What ft.use_state returns (state + optional setter)
- Why the setter can be ignored when using observable objects
- Managing game state with a Python @dataclass
- How ft.observable enables direct mutation with automatic re-rendering
- When to use setters vs. observable classes
- Immutable vs. mutable state in Flet
- Preventing unnecessary re-renders and infinite render loops
- Structuring state for performance and scalability
- Using use_effect for animations and one-time setup
- Dependency arrays and when effects re-run

Explain game-related data such as sprite position, direction, and animation frame belong in a single observable state object, and how changing any of those values automatically updates only the affected UI component—not the entire screen.

This video is conceptual and architectural, helping you build an understanding of how Flet's reactive model works. In the next lesson, we apply these ideas directly by adding animation and continuing to move Pepper across the screen.

This tutorial is part of a beginner-friendly Python + Flet series, with a focus on clean architecture, performance, and learning transferable UI state management concepts.

## [Python + Flet 1.0 Game Animation: Sprite Frames, Direction State, and Walking Animations - 6](https://youtu.be/dKS-Nhf6OoY)

Add character animation to our Python + Flet game by introducing directional sprite frames and cycling through them over time.

Up to this point, our character could move across the screen in a single direction using position updates. Now, we extend the game state to support animation by tracking both direction and current animation frame, and we wire everything together so the sprite visually "walks" as it moves.

What you'll learn in this lesson:

- Extending the game state with direction and current_frame
- Using a Python @dataclass with **post_init** to initialize animation state

- Representing animation frames as lists of image paths
- Tracking animation state with a dictionary keyed by direction
- Cycling frames using the Python modulo operator
- Updating sprite frames on a timed loop
- Separating logic using a simple MVC-style structure
- Model: game state (GameState)
- View: Flet UI and sprite rendering
- Control: movement and animation logic
- Using dictionary unpacking to update frame state cleanly
- Swapping image sources dynamically inside a Flet Image component

Build the animation system so it scales naturally to all four directions (left, right, up, down), even though this video focuses on moving to the right. Each direction uses the same looping logic—only the frame list changes.

By the end of the video, Pepper walks smoothly across the screen using a three-frame animation loop, and the infrastructure is in place to add directional input next.

In the next lesson, we'll introduce Flet buttons to control movement direction and connect user input directly to game state updates.

This tutorial is part of a beginner-friendly Python + Flet game development series, with a strong emphasis on clean architecture, state-driven UI updates, and reusable animation logic.

---

## [7 Python + Flet 1.0: Add Direction Buttons (Up/Down/Left/Right) with State-Driven Re-Renders](https://youtu.be/Vi7LwQJiZG8)

In this tutorial, we take our Flet 1.0 game from a sprite that only moves in one direction to a fully controllable character with four-direction movement using Flet buttons.

We start with Pepper walking to the right, then add a simple button UI (Left, Right, Up, Down). Each button click updates the game state, which triggers a reactive screen re-render—so the sprite changes direction and animation frames immediately based on state changes.

What you'll build and learn:

- Create Flet buttons and wire them to click handlers
- Replace a single Stack return with a Column layout (UI + game view)
- Add a button row and align controls cleanly in the UI
- Extend animation support from "right only" to all four directions
- Add frame lists for left/up/down and switch frame sets based on direction
- Update sprite X/Y bounds correctly for each direction (screen limits)
- Demonstrate how changing state drives re-rendering in a declarative UI

Architecture focus (MVC):

- Model: GameState stores direction, sprite position, and current animation frame
- View: the Flet UI (buttons + sprite + background) displays state
- Controller: movement logic updates the model based on user input

By the end of the video, you'll have a working directional controller where button clicks flow through the controller, update the model, and automatically re-render the view—setting you up to add more game mechanics, more characters, and more complex interactions.
