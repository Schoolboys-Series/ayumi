label scb_bus_selector(show_misaki=True, show_takarasaki=True, show_umesaki=True):
    call screen scb_bus_selector(show_misaki, show_takarasaki, show_umesaki)
    if _return == 0:
        $ _lm_selected_value = "梅咲"
    elif _return == 6:
        $ _lm_selected_value = "宝咲"
    elif _return == 7:
        $ _lm_selected_value = "御咲"
    else:
        $ _lm_selected_value = "乗らない"

    return

screen scb_bus_selector(show_misaki=True, show_takarasaki=True, show_umesaki=True):
    frame at scb_selector_item:
        style "scb_bus_selector_frame"
        text _("选择目标地点") style "scb_bus_selector_title"
        add "images/Selection/Route/Map.png" xpos 0 ypos 0
        for i, place in enumerate([_("梅咲站"),_("尼咲站"),_("伊丹咲站"),_("川西池口站"),_("中山菩萨站"),_("清稳神站"),_("宝咲站"),_("御咲市站"),_("武咲尾站"),_("四田站")]):
            if (i == 0 and show_umesaki) or (i == 6 and show_takarasaki) or (i == 7 and show_misaki):
                imagebutton:
                    xpos 160 + i * 49
                    ypos 219
                    idle "images/Selection/Route/Button.png"
                    hover "images/Selection/Route/Button hover.png"
                    action Return(i)
            text place style "scb_bus_selector_place_name":
                xpos 166 + i * 49
        textbutton _("返回"):
            xalign 0.5
            ypos 472
            text_style "scb_bus_selector_backbutton"
            action Return(-1)
            
style scb_bus_selector_frame is empty
style scb_bus_selector_title:
    size 60
    ypos 87
    xalign 0.5
    color "#FFFFFF"
    font "font/source-hans-sans-heavy.ttc"
    outlines [(absolute(12), "#FF2EC6", absolute(0), absolute(0))]
style scb_bus_selector_place_name:
    size 20
    ypos 275
    color "#000000"
    vertical True
    font "font/source-hans-sans-medium.ttc"
    outlines [(absolute(2), "#FFFFFF", absolute(0), absolute(0))]
style scb_bus_selector_backbutton:
    size 30
    color "#FFFFFF"
    font "font/source-hans-sans-heavy.ttc"
    outlines [(absolute(4), "#FF2EC6", absolute(0), absolute(0))]
    hover_color "FF2EC6"
    hover_outlines [(absolute(4), "#FFFFFF", absolute(0), absolute(0))]
