label scb_selector(title, items, auto_indent=True):
    call screen scb_selector_screen(title, items, auto_indent)
    $ _lm_selected_value = _return["name"]
    $ _lm_selected_index = _return["index"]

screen scb_selector_screen(title, items, auto_indent):
    if title != None and title != "":
        frame:
            if auto_indent:
                style "scb_selector_frame_indent"
                add "gui/input_caption.png" pos (85, 464)
            else:
                style "scb_selector_frame"
                add "gui/input_caption.png" pos (135, 464)
            text title xalign 0.5 yanchor 0.5 ypos 507 font "font/zcool-happy-ayumi-extended.ttf"
    $ y_position = 100
    for i, item in enumerate(items):
        frame at scb_selector_item:
            if auto_indent:
                style "scb_selector_content_frame_indent"
            else:
                style "scb_selector_content_frame"
            imagebutton:
                xalign 0.5
                ypos y_position
                idle "gui/selector.png"
                hover "gui/selector hover.png"
                hovered Play("menu_effect", "sound/Effect Sound/System - choose.ogg")
                action [Play("menu_effect", "sound/Effect Sound/System - click.ogg"), Pause(0.2), Return({"name":item["name"],"index":i})]
            text item["content"]:
                style "scb_selector_item_text"
                ypos y_position + 10
        $ y_position += 80
    $ del y_position

screen scb_selector_preview(x, y, target):
    add target pos (x, y)

transform scb_selector_item:
    on show:
        alpha 0.0
        linear 0.2 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.2 alpha 0.0

style scb_selector_frame is default:
    area (0, 0, 800, 600)
    background Solid("#FFFFFF44")
style scb_selector_frame_indent is scb_selector_frame:
    left_padding 100
style scb_selector_content_frame is default
style scb_selector_content_frame_indent is scb_selector_content_frame:
    left_padding 100
style scb_selector_item_text is default:
    color "#FFFFFF"
    outlines [(absolute(1), "#214297", absolute(0), absolute(0))]
    size 22
    xalign 0.5
    text_align 0.5
    font "font/zcool-happy-ayumi-extended.ttf"
