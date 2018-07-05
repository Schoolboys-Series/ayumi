init python:
    sys_current_place_title = None
    def set_place_title(place=False):
        if place == globals()["sys_current_place_title"]:
            return
        globals()["sys_current_place_title"] = place
        renpy.hide_screen("scb_place_title")
        renpy.with_statement(Dissolve(0.2))
        if place != False:
            renpy.show_screen("scb_place_title", _layer="screens", _tag="scb_place_title", place=place)
            renpy.with_statement(Dissolve(0.2))

screen scb_place_title(place):
    if place == "" or place == None:
        pass
    else:
        text place style "scb_place_title_text"

style scb_place_title_text:
    xpos 790
    ypos 25
    size 18
    color "#60300C"
    xanchor 1.0
    yanchor 0.5
    text_align 0.5
    outlines [(absolute(2), "#FFFFFFFF", absolute(0), absolute(0)),
              (absolute(4), "#FFFFFF88", absolute(0), absolute(0)),
              (absolute(6), "#FFFFFF44", absolute(0), absolute(0)),
              (absolute(8), "#FFFFFF00", absolute(0), absolute(0))]
    font "font/zcool-happy-ayumi-extended.ttf"
