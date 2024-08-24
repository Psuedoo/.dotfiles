from libqtile import layout
from libqtile.config import Match

# from .widgets import colors

layouts = [
    layout.Columns(
        margin=8, border_focus="#1F1D2E", border_normal="#1F1D2E", border_width=0
    ),
    layout.Max(
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
        margin=8,
        border_width=0,
    ),
    # layout.Floating(
    #     border_focus="#1F1D2E",
    #     border_normal="#1F1D2E",
    #     margin=8,
    #     border_width=0,
    # ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
