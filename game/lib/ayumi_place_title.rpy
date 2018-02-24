init python:
    sys_current_place_title = None
    def set_place_title(place=False):
        if place == globals()["sys_current_place_title"]:
            return
        globals()["sys_current_place_title"] = place
        renpy.hide_screen("scb_place_title")
        renpy.with_statement(Dissolve(0.2))
        if place == False:
            renpy.hide_screen("scb_quick_menu")
            renpy.with_statement(Dissolve(0.2))
            pass
        else:
            renpy.show_screen("scb_place_title", _layer="screens", _tag="scb_place_title", place=place)
            renpy.with_statement(Dissolve(0.2))
            hotfix_2()

screen scb_place_title(place):
    if place == "" or place == None:
        pass
    else:
        text place style "scb_place_title_text"

screen scb_quick_menu():
    default expanded = False
    showif expanded == True:
        frame at sck_quick_menu_action_container:
            style "default"
            add "gui/quick_menu.png" zoom 0.25 yalign 0.005 xalign 0.995
            imagebutton:
                xpos 730
                ypos 90
                idle "gui/menu_close.png"
                hover "gui/menu_close hover.png"
                action SetScreenVariable("expanded", False)
            imagebutton:
                xpos 680
                ypos 100
                idle "gui/menu_load.png"
                hover "gui/menu_load hover.png"
                action [SetScreenVariable("expanded", False), ShowMenu("load")]
            imagebutton:
                xpos 670
                ypos 45
                idle "gui/menu_screenshot.png"
                hover "gui/menu_screenshot hover.png"
                action [SetScreenVariable("expanded", False), Screenshot()]
            imagebutton:
                xpos 720
                ypos 40
                idle "gui/menu_button.png"
                hover "gui/menu_button hover.png"
                action [SetScreenVariable("expanded", False), ShowMenu("save")]
    else:
        imagebutton at scb_quick_menu_image_small:
            yalign 0.005
            xalign 0.995
            idle "gui/quick_menu cover.png"
            action SetScreenVariable("expanded", True)

style scb_place_title_text:
    xpos 160
    ypos 25
    size 18
    color "#60300C"
    xanchor 0.5
    yanchor 0.5
    text_align 0.5
    outlines [(absolute(2), "#FFFFFFFF", absolute(0), absolute(0)),
              (absolute(4), "#FFFFFF88", absolute(0), absolute(0)),
              (absolute(6), "#FFFFFF44", absolute(0), absolute(0)),
              (absolute(8), "#FFFFFF00", absolute(0), absolute(0))]
    font "font/zcool-happy-ayumi-extended.ttf"

transform scb_quick_menu_image_banner:
    yalign 0.005
    xalign 0.995
    zoom 0.1
    on show:
        easein 0.2 zoom 0.25
    on hide:
        easein 0.2 zoom 0.1
transform sck_quick_menu_action_container:
    yalign 0.0
    xalign 1.0
    zoom 0.45
    on show:
        easein 0.2 zoom 1
    on hide:
        easein 0.2 zoom 0.45
transform scb_quick_menu_image_small:
    yalign 0.005
    xalign 0.995
    zoom 0.5
    on show:
        alpha 0.0
        pause 0.2
        alpha 1.0
    on hide:
        alpha 0.0
