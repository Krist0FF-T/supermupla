
# 2024-07-19
- created the repo, started development
- impl a View system
    - views are stored in App.views
    - Game is a special View, that is stored separately
        - this way it's unpoppable and accessible from other views
    - if App.views isn't empty, the last element is the App.current_element, but App.game otherwise
    - only App.current_view is drawn and updated
    - example usage:
```python
# App._handle_global_events (called before current_view.handle_events)
if ev.key == pg.K_ESCAPE:
    if self.views:
        self.pop_view()
    else:
        self.push_view(PauseView(self))

# PauseView.handle_events
if ev.key == pg.K_s:
    self.app.push_view(SettingsView(self.app))
```
- wrote an setup script, and installation steps in the README.md (for Linux only)

# 2024-07-20
- translated README.md to hungarian (README-HU.md)
- impl a Camera system
    - different modes:
        - lerp: linearly interpolates towards target every frame by 5%
        - instant: sets instantly to target
    - zooming
    - can translate from world to screen co-ordiates (both point and rect)



