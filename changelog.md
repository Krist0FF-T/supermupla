
# 2024-08-14
- rename the term "addon" to "plugin"
    - also thought about "mod", but it's short for "MODification", but in my case
      they'll be more like building blocks that result in a final game
    - probably will change it a few times in the future XD
- change changelog to new at top

# between these two
- add most blocks and enemies from SuperMuki as tiles (not functional, only to see
  the addon manager in action)
- optimize tile rendering by:
    - skipping empty chunks
    - switching from "blit" at every chunk draw to "blits", so it's more efficient

# 2024-07-20
- translated README.md to hungarian (README-HU.md)
- impl a Camera system
    - different modes:
        - lerp: linearly interpolates towards target every frame by 5%
        - instant: sets instantly to target
    - zooming
    - can translate from world to screen co-ordiates (both point and rect)

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

- wrote a setup script, and installation steps in the README.md (for Linux only)

