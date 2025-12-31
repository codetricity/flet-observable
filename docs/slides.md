---
marp: true
theme: default
paginate: true
---

# Python and Flet Concepts for Beginners

## Pepper Tutorial

- UI development patterns
- Reactive programming concepts
- Flet's declarative UI approach
- MVC architecture

---

# Observables: Reactive State Management

## What are Observables?

- **Observables** are objects that notify listeners when their values change
- When an observable property changes, the UI automatically updates
- This is called **reactive programming** or **data binding**

---

## Observable in Flet with `ft.observable`

```python
from dataclasses import dataclass
import flet as ft

@dataclass
@ft.observable
class GameState:
    direction: str = "right"
    sprite_x: int = 5
    sprite_y: int = 300
```

- The `@ft.observable` decorator makes the class reactive
- When you change `state.direction`, the UI automatically re-renders
- No manual UI updates such as `page.update()` needded

---

# Observables: Comparison with Flutter

## Flutter's Approach

Flutter doesn't have built-in observables. Developers use state management libraries:

**Riverpod Example:**

```dart
@riverpod
class GameState extends _$GameState {
  @override
  String build() => "right";
  
  void setDirection(String dir) {
    state = dir; // Automatic notification
  }
}
```

**BLoC Example:**

```dart
class GameBloc extends Bloc<GameEvent, GameState> {
  GameBloc() : super(GameState(direction: "right"));
  
  void setDirection(String dir) {
    emit(state.copyWith(direction: dir)); // Manual emit
  }
}
```

---

## Flet Difference with Flutter

**Key Differences:**

- Flutter requires **third-party libraries** (Riverpod, BLoC, Provider) for state management
- Flet has **built-in observables** with `@ft.observable` decorator
- Flutter's libraries often require manual state updates or event emissions
- Flet automatically detects changes to observable properties
- Flet's approach is simpler and requires less boilerplate

---

## Flet Observable (mutable) vs Riverpod (immutable) 

**Flet (Mutable):**

- Direct property mutation: `state.sprite_x += 10`
- Same object instance, properties change
- Simpler, less boilerplate
- Built into Flet framework

**Riverpod (Immutable):**

- Create new state objects: `state.copyWith(...)`
- Each update creates a new instance
- More explicit, better for testing
- Requires third-party package

---

## Flutter Signals (Mutable-like)

- Direct signal updates: `spriteX.value += 10`
- Signals are reactive primitives
- Simpler than Riverpod, similar to Flet
- Third-party package (inspired by SolidJS)

---

# Flet Observable vs Riverpod: When to Use

## Flet Observable

**Best for:**

- Simple to medium complexity apps
- Direct property mutations
- Rapid prototyping
- Teaching basic games concepts (single sprite example)
- Less boilerplate needed

**Note:** For Flutter game development, developers typically use **Flame** (a game engine built on Flutter) rather than raw Riverpod for sprite animations and game loops.

---

## Flet Observable vs Riverpod vs Flutter Signals: Comparison

**All provide reactive state management, but with different patterns:**

**Flet Observable:**

```python
@ft.observable
class GameState:
    sprite_x: int = 5

state.sprite_x += 10  # Direct mutation, auto-updates UI
```

**Flutter Signals:**

```dart
final spriteX = signal(5);

spriteX.value += 10;  // Direct mutation, auto-updates UI
```

---

**Riverpod:**

```dart
state = state.copyWith(spriteX: state.spriteX + 10);  // Immutable update
```

**Key Differences:**

- **Flet**: Mutable objects, direct property access, built-in
- **Flutter Signals**: Mutable signals, direct value access, third-party (closest to Flet!)
- **Riverpod**: Immutable state, provider pattern, third-party
- **Flame** (Flutter games): Game engine with built-in sprite/animation systems

---

**For sprite motion app:**

- **Flet's observable** is simpler and more direct (built-in)
- **Flutter Signals** would be the closest equivalent - direct mutation like Flet
  - great practice opportunity
- **Riverpod** would require more setup (state classes, providers, copyWith)
  - you need to learn Riverpod or BLoC anyway with Flutter, so good practice
- **Flame** would handle sprites differently (component-based game objects)

**Note:** Flutter Signals is the most similar to Flet's observable pattern - both allow direct mutation with automatic UI updates!

---

# Observables: Comparison with React

## React's Approach

```jsx
const [direction, setDirection] = useState("right");

// Changing state triggers re-render
setDirection("left");
```

**Key Difference:**

- React uses hooks (`useState`) for component-level state
- Flet observables work at the class level, similar to state management libraries like Redux or MobX
- Flet observables can be shared across multiple components

---

# `ft.use_state`: Managing Component State

## What is `use_state`?

- `use_state` is a **hook** that manages state in Flet components
- It returns the current state and a setter function
- Similar to React's `useState` hook

---

# `ft.use_state`: Example

```python
@ft.component
def GameView():
    state, _ = ft.use_state(GameState())
    
    def on_left_click(e):
        state.set_direction("left")
        # UI automatically updates!
    
    return ft.Button("Left", on_click=on_left_click)
```

**How it works:**

1. `use_state` creates an instance of `GameState`
2. When `state.direction` changes, the component re-renders
3. The UI reflects the new state automatically

---

# `ft.use_state`: Key Points

## Important Concepts

- **State persists** between re-renders
- **Only the component** using `use_state` re-renders when state changes
- The second return value (setter) is optional if you modify the state object directly
- State is **local to the component** unless you pass it as props

---

# Python Dataclasses: Clean Data Structures

## What are Dataclasses?

- Dataclasses are a Python feature for creating classes that mainly store data
- They automatically generate common methods like `__init__`, `__repr__`, and `__eq__`
- Less boilerplate code!

---

# Python Dataclasses: Basic Example

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# Automatically generated:
# - __init__(self, name: str, age: int)
# - __repr__(self)
# - __eq__(self, other)
```

---

**Before dataclasses:**

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    # ... more boilerplate
```

---

## Python Dataclasses: Default Values and Post-Initialization

```python
@dataclass
@ft.observable
class GameState:
    direction: str = "right"  # Default value
    sprite_x: int = 5
    sprite_y: int = 300
    current_frame: dict[str, int] = None
    
    def __post_init__(self):
        # Runs after initialization
        if self.current_frame is None:
            self.current_frame = {
                "right": 0,
                "left": 0,
                "up": 0,
                "down": 0,
            }
```

---

# Flet's New Declarative UI

## What is Declarative UI?

- **Declarative**: Describe *what* the UI should look like
- **Imperative**: Write code that tells *how* to build the UI step-by-step

---

# Flet's New Declarative UI: The Old Way

## Imperative Approach (Old Flet)

```python
def main(page: ft.Page):
    button = ft.Button("Click me")
    
    def on_click(e):
        button.text = "Clicked!"  # Manual update
        page.update()  # Manual refresh
    
    button.on_click = on_click
    page.add(button)
```

---

**Problems:**

- Manual UI updates
- Easy to forget `page.update()`
- State and UI can get out of sync

---

# Flet's New Declarative UI: The New Way

## Declarative Approach (New Flet)

```python
@ft.component
def GameView():
    state, _ = ft.use_state(GameState())
    
    def on_click(e):
        state.direction = "left"
        # UI updates automatically!
    
    return ft.Button("Left", on_click=on_click)
```

---

**Benefits:**

- UI automatically reflects state
- No manual `page.update()` calls
- State and UI always in sync
- More like React/Flutter

---

# Flet's New Declarative UI: Component Pattern

## How Declarative Components Work

```python
@ft.component
def GameView():
    state, _ = ft.use_state(GameState())
    
    # This function runs every time state changes
    # It returns the UI structure
    return ft.Column(
        controls=[
            ft.Button("Left", on_click=lambda e: state.set_direction("left")),
            ft.Image(src=frames[state.direction][state.current_frame[state.direction]])
        ]
    )
```

---

**Key Points:**

- Component is a function that returns UI
- Re-renders automatically when state changes
- UI is a function of state: `UI = f(state)`

---

# `ft.use_effect`: Side Effects and Lifecycle

## What is `use_effect`?

- `use_effect` runs code when a component mounts or when dependencies change
- Perfect for:

  - Starting animations
  - Fetching data
  - Setting up subscriptions
  - Cleaning up resources

---

# `ft.use_effect`: Basic Example

```python
@ft.component
def GameView():
    state, _ = ft.use_state(GameState())
    
    def start_animation():
        async def tick():
            while True:
                await asyncio.sleep(0.2)
                update_sprite(state)  # Update state
        
        return ft.context.page.run_task(tick)
    
    ft.use_effect(start_effect, [])  # Run once on mount
    
    return ft.Column(...)
```

---

**How it works:**

- The function passed to `use_effect` runs when the component mounts
- Empty dependency list `[]` means "run only once"
- Return a cleanup function to stop the animation

---

# `ft.use_effect`: Dependencies

## Dependency Array

```python
# Run once on mount
ft.use_effect(setup, [])

# Run every time 'count' changes
ft.use_effect(update, [count])

# Run every render (usually avoid this)
ft.use_effect(update, None)
```

---

**Best Practice:**

- Always include dependencies that the effect uses
- Empty array `[]` for one-time setup
- Return cleanup function for resources

---

# MVC Architecture: Model-View-Controller

**MVC** separates your application into three parts:

- **Model**: Data and business logic
- **View**: User interface
- **Controller**: Handles user input and coordinates Model and View

---

# MVC Architecture:  Our Project Structure

```text
sprite-motion/
├── model/
│   └── game_state.py    # Model: GameState class
├── view/
│   └── game.py          # View: GameView component
├── control/
│   └── movement.py      # Controller: update_sprite function
└── main.py
```

**Separation of Concerns:**

- Model knows nothing about UI
- View knows nothing about business logic
- Controller coordinates between them

---

# MVC Architecture: Model Layer

## Model (game_state.py)

```python
@dataclass
@ft.observable
class GameState:
    direction: str = "right"
    sprite_x: int = 5
    sprite_y: int = 300
    current_frame: dict[str, int] = None
    
    def set_direction(self, direction: str):
        self.direction = direction
```

---


**Model Responsibility:**

- Stores application data
- Defines data structure
- Contains business logic methods
- No UI code!

---

# MVC Architecture: View Layer

## View (game.py)

```python
@ft.component
def GameView():
    state, _ = ft.use_state(GameState())
    
    # Build UI based on state
    return ft.Column(
        controls=[
            ft.Button("Left", on_click=on_left_click),
            ft.Stack(controls=[sprite])
        ]
    )
```

---

**View Responsibility:**

- Displays data from Model
- Handles user interactions (clicks, input)
- Sends user actions to Controller
- No business logic!

---

# MVC Architecture: Controller Layer

## Controller (movement.py)

```python
def update_sprite(state: GameState) -> None:
    """Update sprite position and frame based on direction."""
    match state.direction:
        case "right":
            state.sprite_x += 10
            # Update animation frame
        case "left":
            state.sprite_x -= 10
```

---


**Controller Responsibility:**

- Processes user actions
- Updates Model based on business rules
- Coordinates between Model and View
- No direct UI manipulation!

---

# MVC Architecture: Data Flow

## How MVC Works Together

```text
User clicks "Left" button
    ↓
View: on_left_click handler
    ↓
Controller: update_sprite(state)
    ↓
Model: state.direction = "left"
    ↓
Observable: Notifies listeners
    ↓
View: Automatically re-renders
```

---

### MVC Data Flow Benefits

- Clear separation of concerns
- Easy to test each layer independently
- Easy to modify one layer without affecting others

---

# Alternative Architectures: MVVM

## Model-View-ViewModel

**Similar to MVC, but:**

- **ViewModel** acts as a bridge between Model and View
- ViewModel exposes data in a View-friendly format
- Common in frameworks like WPF, Vue.js

---

**MVVM Example:**

```python
class GameViewModel:
    def __init__(self, model: GameState):
        self.model = model
    
    @property
    def display_direction(self):
        return self.model.direction.upper()
```

---

# Alternative Architectures: MVP

## Model-View-Presenter

**Similar to MVC, but:**

- **Presenter** contains all UI logic
- View is "dumb" - just displays what Presenter tells it
- View never directly accesses Model

**Key Difference:**

- In MVC, View can read Model directly
- In MVP, View only talks to Presenter

---

# Alternative Architectures: Component-Based

## React/Flutter Style

**No strict separation:**

- Components contain their own state and logic
- State management libraries (Redux, Provider) handle shared state
- More flexible, but can become messy

---

**Component-Based Example:**

```python
@ft.component
def GameView():
    state, _ = ft.use_state(GameState())
    # State and logic in same component
    return ft.Column(...)
```

---

# Architecture Comparison

## When to Use Each?

| Architecture | Best For | Complexity |
| ------------ | -------- | ---------- |
| **MVC** | Traditional apps, clear separation | Medium |
| **MVVM** | Data binding, reactive UIs | Medium |
| **MVP** | Testability, strict separation | Medium |
| **Component-Based** | Small apps, rapid prototyping | Low |

**For beginners:** Start with MVC or Component-Based, then explore others as you grow!

---

# Your Sprite Motion App

1. **Model** (`GameState`): Stores sprite position, direction, frames
2. **View** (`GameView`): Displays buttons and sprite image
3. **Controller** (`update_sprite`): Updates position based on direction
4. **Observables**: Automatically update UI when state changes
5. **Hooks**: `use_state` manages state, `use_effect` runs animation loop

**Result:** Clean, maintainable, reactive application!

---

# Tutorial Concepts

1. **Observables**: Automatic UI updates when data changes
2. **use_state**: Manage component-level state
3. **Dataclasses**: Clean, simple data structures
4. **Declarative UI**: Describe what, not how
5. **use_effect**: Handle side effects and lifecycle
6. **MVC**: Separate concerns for maintainable code

---

# Feedback

- This is a hobby for me
- Try modifying the sprite animation speed
- Add more directions (up, diagonal)
- Experiment with different architectures
- Build your own reactive components

**Have fun!**
