# flet animation demo with observable

## observable

ft.observable is a Flet decorator that makes a class reactive, so UI components automatically re-render when its properties change.

### How it works

When you mark a class with @ft.observable, Flet tracks changes to its properties. When a property changes, any component using that observable automatically re-renders.

```python
@ft.component
def GameView():
    state, _ = ft.use_state(GameState())  # state is observable
    
    # When state.sprite_x or state.direction changes,
    # this component automatically re-renders!
    sprite = ft.Container(
        left=state.sprite_x,  # Reads from observable
        ...
    )
```

## post_init

`__post_init__` is a special method in Python dataclasses that runs automatically after the dataclass-generated `__init__` completes.

### How it works

When you use @dataclass, Python generates an `__init__` that sets all the fields. `__post_init__` runs right after that, so you can add initialization logic.
In your code:


## Art

* [Pepper&Carrot](https://opengameart.org/content/24x32-peppercarrot-characters)
  * [Pepper & Carrot site](https://www.peppercarrot.com/en/)
  * other [24x32 sets](https://opengameart.org/art-search-advanced?field_art_tags_tid=24x32)
