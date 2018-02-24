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
