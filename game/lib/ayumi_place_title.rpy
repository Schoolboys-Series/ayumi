init python:
    sys_current_place_title = None
    def set_place_title(place=False):
        if place == globals()["sys_current_place_title"]:
            return
        globals()["sys_current_place_title"] = place
        renpy.hide_screen("scb_place_title")
        renpy.with_statement(Dissolve(0.2))
        if place == "" or place == None:
            renpy.show_screen("scb_place_title_button_only", _layer="screens", _tag="scb_place_title")
            renpy.with_statement(Dissolve(0.2))
        elif place == False:
            pass
        else:
            renpy.show_screen("scb_place_title", _layer="screens", _tag="scb_place_title", place=place)
            renpy.with_statement(Dissolve(0.2))

screen scb_place_title(place):
    add "gui/place_title_background.png" at right_top
    imagebutton:
        xpos 756
        ypos 12
        idle "gui/menu_button.png"
        hover "gui/menu_button hover.png"
        action ShowMenu("save")
    text place:
        xpos 675
        ypos 30
        size 18
        color "#60300C"
        xanchor 0.5
        yanchor 0.5
        text_align 0.5
        font "font/zcool-happy-ayumi-extended.ttf"

screen scb_place_title_button_only():
    add "gui/place_title_background.png" at scb_place_image_button_only
    imagebutton:
        xpos 756
        ypos 12
        idle "gui/menu_button.png"
        hover "gui/menu_button hover.png"
        action ShowMenu("save")

transform scb_place_image_button_only:
    yalign 0.0
    xanchor 0.0
    xpos 725
