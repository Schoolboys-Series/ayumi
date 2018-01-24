label scb_global_map(time, character, place, allow_change_time, allow_break, allow_talk=True, allow_target=True, talk_label="", target_label="", break_confirm=True, break_confirm_title=(_("你确实要终止任务吗?"),_("说的是，以后再做吧"),_("不不不，手滑了"))):
    if time == 'daytime':
        $ time = 'lunchtime'
    # Background
    show expression "global_map_" + place + "_" + time as global_map_place_background
    # Show weather
    if time == 'lunchtime':
        show expression "images/Moving/Weather/Daytime.png" at global_map_weather_lunchtime as global_map_weather
    elif time == 'twilight':
        show expression "images/Moving/Weather/Twilight.png" at global_map_weather_twilight as global_map_weather
    elif time == 'night':
        show expression "images/Moving/Weather/Night.png" at global_map_weather_night as global_map_weather
    # Show title and place string
    if Chapter == 1:
        show global_map_title_1 (_("CHAPTER 1 第一章")) at global_map_fade as global_map_title
        if place == 'school_inside':
            show global_map_place_1 (_("御咲学园内")) at global_map_fade as global_map_place
        elif place == 'school_outside':
            show global_map_place_1 (_("御咲学园外")) at global_map_fade as global_map_place
        elif place == 'misaki':
            show global_map_place_1 (_("御咲市")) at global_map_fade as global_map_place
    elif Chapter == 2:
        show global_map_title_2 (_("CHAPTER 2 第二章")) at global_map_fade as global_map_title
        if place == 'school_inside':
            show global_map_place_2 (_("御咲学园内")) at global_map_fade as global_map_place
        elif place == 'school_outside':
            show global_map_place_2 (_("御咲学园外")) at global_map_fade as global_map_place
        elif place == 'misaki':
            show global_map_place_2 (_("御咲市")) at global_map_fade as global_map_place
        elif place == 'hotel':
            show global_map_place_2 (_("酒店")) at global_map_fade as global_map_place
    elif Chapter == 3:
        show global_map_title_3 (_("CHAPTER 3 第三章")) at global_map_fade as global_map_title
        if place == 'school_inside':
            show global_map_place_3 (_("御咲学园内")) at global_map_fade as global_map_place
        elif place == 'school_outside':
            show global_map_place_3 (_("御咲学园外")) at global_map_fade as global_map_place
        elif place == 'misaki':
            show global_map_place_3 (_("御咲市")) at global_map_fade as global_map_place
    elif Chapter == 4:
        show global_map_title_4 (_("END OF SEMESTER 学期末")) at global_map_fade as global_map_title
        if place == 'school_inside':
            show global_map_place_4 (_("御咲学园内")) at global_map_fade as global_map_place
        elif place == 'school_outside':
            show global_map_place_4 (_("御咲学园外")) at global_map_fade as global_map_place
        elif place == 'misaki':
            show global_map_place_4 (_("御咲市")) at global_map_fade as global_map_place
        elif place == 'dream':
            show global_map_place_4 (_("梦之温泉")) at global_map_fade as global_map_place
    # Show character image
    show expression "global_map_character_moving_" + time + "_" + character + "_" + str(Chapter) as global_map_character:
        xpos -400
        pause 1.6
        easein_back 0.4 xpos 0
    pause 1.6
    # Show selection screen
    label scb_global_map_jump_tag:
    call screen scb_global_map_screen(time, character, place, allow_change_time, allow_break, allow_talk, allow_target)
    if (_return == "talk"):
        $ renpy.call(talk_label)
        jump scb_global_map_jump_tag
    elif (_return == "target"):
        $ renpy.call(target_label)
        jump scb_global_map_jump_tag
    elif (_return == "break"):
        if break_confirm:
            call scb_selector(break_confirm_title[0], [
               { "name": "yes", "content": break_confirm_title[1] },
               { "name": "no", "content": break_confirm_title[2] }
            ], False) from _call_scb_selector_35
        else:
            $ _lm_selected_value = "yes"
        if _lm_selected_value != "yes":
            jump scb_global_map_jump_tag
        else:
            hide global_map_place_background
            hide global_map_title
            hide global_map_place
            hide global_map_character
            hide global_map_weather
            hide global_map_hint
            with Dissolve(0.2)

            $ _lm_selected_value = "目標破棄"
            return "目標破棄"
    else:
        hide global_map_place_background
        hide global_map_title
        hide global_map_place
        hide global_map_character
        hide global_map_weather
        hide global_map_hint
        with Dissolve(0.2)
        
        $ _lm_selected_value = _return
        return _return

image global_map_title_1 = ParameterizedText(
    size=16,
    color="#FFFFFF",
    font="font/source-hans-sans-heavy.ttc",
    pos=(131, 5),
    outlines=[
        (absolute(3), "#64DF6600", absolute(0), absolute(0)),
        (absolute(2), "#64DF6688", absolute(0), absolute(0)),
        (absolute(1), "#64DF66FF", absolute(0), absolute(0))
    ]
)
image global_map_place_1 = ParameterizedText(
    size=16,
    color="#FFFFFF",
    font="font/source-hans-sans-heavy.ttc",
    xanchor=1.0,
    pos=(750, 5),
    outlines=[
        (absolute(3), "#64DF6600", absolute(0), absolute(0)),
        (absolute(2), "#64DF6688", absolute(0), absolute(0)),
        (absolute(1), "#64DF66FF", absolute(0), absolute(0))
    ]
)
image global_map_title_2 = ParameterizedText(
    size=16,
    color="#FFFFFF",
    font="font/source-hans-sans-heavy.ttc",
    pos=(131, 5),
    outlines=[
        (absolute(3), "#56589800", absolute(0), absolute(0)),
        (absolute(2), "#56589888", absolute(0), absolute(0)),
        (absolute(1), "#565898FF", absolute(0), absolute(0))
    ]
)
image global_map_place_2 = ParameterizedText(
    size=16,
    color="#FFFFFF",
    font="font/source-hans-sans-heavy.ttc",
    xanchor=1.0,
    pos=(750, 5),
    outlines=[
        (absolute(3), "#56589800", absolute(0), absolute(0)),
        (absolute(2), "#56589888", absolute(0), absolute(0)),
        (absolute(1), "#565898FF", absolute(0), absolute(0))
    ]
)
image global_map_title_3 = ParameterizedText(
    size=16,
    color="#FFFFFF",
    font="font/source-hans-sans-heavy.ttc",
    pos=(131, 5),
    outlines=[
        (absolute(3), "#DE5A8700", absolute(0), absolute(0)),
        (absolute(2), "#DE5A8788", absolute(0), absolute(0)),
        (absolute(1), "#DE5A87FF", absolute(0), absolute(0))
    ]
)
image global_map_place_3 = ParameterizedText(
    size=16,
    color="#FFFFFF",
    font="font/source-hans-sans-heavy.ttc",
    xanchor=1.0,
    pos=(750, 5),
    outlines=[
        (absolute(3), "#DE5A8700", absolute(0), absolute(0)),
        (absolute(2), "#DE5A8788", absolute(0), absolute(0)),
        (absolute(1), "#DE5A87FF", absolute(0), absolute(0))
    ]
)
image global_map_title_4 = ParameterizedText(
    size=16,
    color="#FFFFFF",
    font="font/source-hans-sans-heavy.ttc",
    pos=(131, 5),
    outlines=[
        (absolute(3), "#5193C800", absolute(0), absolute(0)),
        (absolute(2), "#5193C888", absolute(0), absolute(0)),
        (absolute(1), "#5193C8FF", absolute(0), absolute(0))
    ]
)
image global_map_place_4 = ParameterizedText(
    size=16,
    color="#FFFFFF",
    font="font/source-hans-sans-heavy.ttc",
    pos=(675, 5),
    outlines=[
        (absolute(3), "#5193C800", absolute(0), absolute(0)),
        (absolute(2), "#5193C888", absolute(0), absolute(0)),
        (absolute(1), "#5193C8FF", absolute(0), absolute(0))
    ]
)

screen scb_global_map_screen(time, character, place, allow_change_time, allow_break, allow_talk=True, allow_target=True):
    frame at global_map_action_movein:
        style "global_menu_frame"
        add "images/Moving/Actions/Base.png" xpos 0 ypos 80 at global_map_fade
        if allow_change_time:
            if time == "twilight":
                imagebutton:
                    xpos 8
                    ypos 121
                    idle "images/Moving/Actions/Lunchbreak.png"
                    hover "images/Moving/Actions/Lunchbreak hover.png"
                    hovered Play("menu_effect", "sound/Effect Sound/System - choose.ogg")
                    action [Play("menu_effect", "sound/Effect Sound/System - click.ogg"), Return("昼休み")]
            else:
                imagebutton:
                    xpos 8
                    ypos 121
                    idle "images/Moving/Actions/Afterschool.png"
                    hover "images/Moving/Actions/Afterschool hover.png"
                    hovered Play("menu_effect", "sound/Effect Sound/System - choose.ogg")
                    action [Play("menu_effect", "sound/Effect Sound/System - click.ogg"), Return("放課後")]
        else:
            if time == "twilight":
                imagebutton:
                    xpos 8
                    ypos 121
                    idle "images/Moving/Actions/Lunchbreak disabled.png"
            else:
                imagebutton:
                    xpos 8
                    ypos 121
                    idle "images/Moving/Actions/Afterschool disabled.png"
        if allow_talk:
            imagebutton:
                xpos 66
                ypos 121
                idle "images/Moving/Actions/Talk.png"
                hover "images/Moving/Actions/Talk hover.png"
                hovered Play("menu_effect", "sound/Effect Sound/System - choose.ogg")
                action [Play("menu_effect", "sound/Effect Sound/System - click.ogg"), Return("talk")]
        else:
            imagebutton:
                xpos 66
                ypos 121
                idle "images/Moving/Actions/Talk disabled.png"
        if allow_target:
            imagebutton:
                xpos 124
                ypos 121
                idle "images/Moving/Actions/Target.png"
                hover "images/Moving/Actions/Target hover.png"
                hovered Play("menu_effect", "sound/Effect Sound/System - choose.ogg")
                action [Play("menu_effect", "sound/Effect Sound/System - click.ogg"), Pause(0.4), Return("target")]
        else:
            imagebutton:
                xpos 124
                ypos 121
                idle "images/Moving/Actions/Target disabled.png"
        if allow_break:
            imagebutton:
                xpos 182
                ypos 121
                idle "images/Moving/Actions/Giveup.png"
                hover "images/Moving/Actions/Giveup hover.png"
                hovered Play("menu_effect", "sound/Effect Sound/System - choose.ogg")
                action [Play("menu_effect", "sound/Effect Sound/System - click.ogg"), Return("break")]
        else:
            imagebutton:
                xpos 182
                ypos 121
                idle "images/Moving/Actions/Giveup disabled.png"
                hover "images/Moving/Actions/Giveup disabled hover.png"
    
    
    if character != "empty":
        frame at global_map_character_movein:
            style "global_menu_frame"
            imagebutton:
                xpos 16
                ypos 264
                idle "images/Moving/Actions/Character.png"
                hover "images/Moving/Actions/Character hover.png"
                hovered Play("menu_effect", "sound/Effect Sound/System - choose.ogg")
                action Show("scb_global_map_character_info", transition=Dissolve(0.3), character=character)

    $ place_list = []
    if place == 'school_inside':
        $ place_list = global_map_places_school_inside
    elif place == 'school_outside':
        $ place_list = global_map_places_school_outside
        if "C0SShinobuState" in globals():
            $ place_list = place_list[0:-1]
    elif place == 'misaki':
        $ place_list = global_map_places_misaki
    elif place == 'hotel':
        $ place_list = global_map_place_hotel
    elif place == 'dream':
        $ place_list = global_map_place_dream
    
    frame at global_map_place_movein:
        style "global_menu_frame"
        $ y_position = 29
        for i, place in enumerate(place_list):
            imagebutton:
                ypos y_position
                idle place["image"]
                hover place["image"][0:-4] + " hover" + place["image"][-4:]
                hovered Play("menu_effect", "sound/Effect Sound/System - choose.ogg")
                action [Play("menu_effect", "sound/Effect Sound/System - click.ogg"), Pause(0.4), Return(place["name"])]
            text place["title"]:
                style "scb_global_map_place_title"
                ypos y_position + 10
            $ y_position += 88
        $ del y_position
    $ del place_list
    if place == "dream":
        add "global_map_hint_dream"
    else:
        add "global_map_hint_" + time at global_map_hint_fade
    add "images/Help/Moving/Background.png" at global_map_help
    for i in range(8):
        add "global_map_hint_content_" + str(i + 1) at global_map_hint_content_transform(i * 5.0)

style scb_global_map_place_title:
    xpos 410
    size 40
    color "#FFFFFF"
    font "font/source-hans-sans-heavy.ttc"
    xanchor 0.5
    outlines [(absolute(2), "#04949AFF", absolute(0), absolute(0)),
              (absolute(4), "#04949A88", absolute(0), absolute(0)),
              (absolute(6), "#04949A44", absolute(0), absolute(0)),
              (absolute(8), "#04949A00", absolute(0), absolute(0))]

screen scb_global_map_character_info(character):
    imagebutton:
        idle "global_map_character_info_" + character
        action Hide("scb_global_map_character_info", transition=Dissolve(0.3))
    text "当前人员" text_align 0.5 xalign 0.5 ypos 5 color "#FFFFFF" outlines[(absolute(2), "#000000", absolute(0), absolute(0))]

define global_map_places_school_inside = [
    { "name": "廊下", "title": _("二楼走廊"), "image": "images/Moving/Places/Aisle 2.png" },
    { "name": "屋上", "title": _("屋顶"), "image": "images/Moving/Places/Roof.png" },
    { "name": "音楽室", "title": _("音乐室"), "image": "images/Moving/Places/Music room.png" },
    { "name": "図書室", "title": _("图书馆"), "image": "images/Moving/Places/Library.png" },
    { "name": "トイレ", "title": _("厕所"), "image": "images/Moving/Places/Toilet.png" },
    { "name": "学園外", "title": _("学园外"), "image": "images/Moving/Places/School outside.png" }
]
define global_map_places_school_outside = [
    { "name": "下駄箱", "title": _("鞋箱"), "image": "images/Moving/Places/Shoe cupboard.png" },
    { "name": "中庭", "title": _("中庭"), "image": "images/Moving/Places/Atrium.png" },
    { "name": "体育館前", "title": _("体育馆前"), "image": "images/Moving/Places/Gym outside.png" },
    { "name": "校舎裏", "title": _("校舍内"), "image": "images/Moving/Places/Schoolhouse.png" },
    { "name": "校門", "title": _("校门"), "image": "images/Moving/Places/School door.png" },
    { "name": "学園内", "title": _("学园内"), "image": "images/Moving/Places/School inside.png" }
]
define global_map_places_misaki = [
    { "name": "御咲学園", "title": _("御咲学园"), "image": "images/Moving/Places/Misaki school.png" },
    { "name": "住宅街", "title": _("住宅街"), "image": "images/Moving/Places/Residential street.png" },
    { "name": "商店街", "title": _("商店街"), "image": "images/Moving/Places/Shopping street.png" },
    { "name": "公園", "title": _("公园"), "image": "images/Moving/Places/Park.png" },
    { "name": "御咲駅", "title": _("御咲站"), "image": "images/Moving/Places/Misaki station.png" }
]
define global_map_place_hotel = [
    { "name": "ロビー", "title": _("大厅"), "image": "images/Chapter 2/Moving/Places/Lobby.png" }
]
define global_map_place_dream = [
    { "name": "室内ゾーン１", "title": _("室内（一）"), "image": "images/Dream/Moving/Places/Inside 1.png" },
    { "name": "室内ゾーン２", "title": _("室内（二）"), "image": "images/Dream/Moving/Places/Inside 2.png" },
    { "name": "屋外ゾーン１", "title": _("室外（一）"), "image": "images/Dream/Moving/Places/Outside 1.png" },
    { "name": "屋外ゾーン２", "title": _("室外（二）"), "image": "images/Dream/Moving/Places/Outside 2.png" },
    { "name": "花乃湯ゾーン", "title": _("花乃汤"), "image": "images/Dream/Moving/Places/Hanano.png" },
    { "name": "プールゾーン", "title": _("泳池"), "image": "images/Dream/Moving/Places/Swimming pool.png" }
]

image global_map_character_moving_lunchtime_sakuya_tsubasachan_1 = "images/Chapter 1/Moving/Sakuya+Tsubasa-chan/Daytime.png"
image global_map_character_moving_lunchtime_shiro_tsubasachan_1 = "images/Chapter 1/Moving/Shiro+Tsubasa-chan/Daytime.png"
image global_map_character_moving_lunchtime_shiro_yukio_1 = "images/Chapter 1/Moving/Shiro+Yukio/Daytime.png"
image global_map_character_moving_lunchtime_tomo_1 = "images/Chapter 1/Moving/Tomo/Daytime.png"
image global_map_character_moving_twilight_tomo_1 = "images/Chapter 1/Moving/Tomo/Twilight.png"
image global_map_character_moving_lunchtime_tomo_shinobu_1 = "images/Chapter 1/Moving/Tomo+Shinobu/Daytime.png"
image global_map_character_moving_twilight_tomo_shinobu_1 = "images/Chapter 1/Moving/Tomo+Shinobu/Daytime.png"
image global_map_character_moving_lunchtime_tomo_shintaro_1 = "images/Chapter 1/Moving/Tomo+Shintaro/Daytime.png"
image global_map_character_moving_lunchtime_tomo_tsubasa_1 = "images/Chapter 1/Moving/Tomo+Tsubasa/Daytime.png"
image global_map_character_moving_lunchtime_tsubasa_1 = "images/Chapter 1/Moving/Tsubasa/Daytime.png"
image global_map_character_moving_lunchtime_itou_2 = "images/Chapter 2/Moving/Itou/Daytime.png"
image global_map_character_moving_lunchtime_nori_2 = "images/Chapter 2/Moving/Nori/Daytime.png"
image global_map_character_moving_lunchtime_saburo_2 = "images/Chapter 2/Moving/Saburo/Daytime.png"
image global_map_character_moving_lunchtime_sakuya_tsubasachan_2 = "images/Chapter 2/Moving/Sakuya+Tsubasa-chan/Daytime.png"
image global_map_character_moving_lunchtime_shintaro_2 = "images/Chapter 2/Moving/Shintaro/Daytime.png"
image global_map_character_moving_lunchtime_sora_2 = "images/Chapter 2/Moving/Sora/Daytime.png"
image global_map_character_moving_lunchtime_tomo_2 = "images/Chapter 2/Moving/Tomo/Daytime.png"
image global_map_character_moving_twilight_tomo_2 = "images/Chapter 2/Moving/Tomo/Twilight.png"
image global_map_character_moving_night_tomo_2 = "images/Chapter 2/Moving/Tomo/Night.png"
image global_map_character_moving_twilight_tomo_shinobu_2 = "images/Chapter 2/Moving/Tomo+Shinobu/Twilight.png"
image global_map_character_moving_twilight_tomo_yuuhi_2 = "images/Chapter 2/Moving/Tomo+Yuuhi/Twilight.png"
image global_map_character_moving_night_tsubasa_2 = "images/Chapter 2/Moving/Tsubasa/Night.png"
image global_map_character_moving_lunchtime_tsuki_2 = "images/Chapter 2/Moving/Tsuki/Daytime.png"
image global_map_character_moving_twilight_tsuki_sora_2 = "images/Chapter 2/Moving/Tsuki+Sora/Twilight.png"
image global_map_character_moving_lunchtime_yukio_2 = "images/Chapter 2/Moving/Yukio/Daytime.png"
image global_map_character_moving_lunchtime_yuuhi_2 = "images/Chapter 2/Moving/Yuuhi/Daytime.png"
image global_map_character_moving_twilight_sakuya_3 = "images/Chapter 3/Moving/Sakuya/Twilight.png"
image global_map_character_moving_lunchtime_sakuya_tsubasachan_3 = "images/Chapter 3/Moving/Sakuya+Tsubasa-chan/Daytime.png"
image global_map_character_moving_lunchtime_shinobu_3 = "images/Chapter 3/Moving/Shinobu/Daytime.png"
image global_map_character_moving_twilight_shinobu_3 = "images/Chapter 3/Moving/Shinobu/Twilight.png"
image global_map_character_moving_twilight_shinobu_school_3 = "images/Chapter 3/Moving/Shinobu+School/Twilight.png"
image global_map_character_moving_twilight_shinobu_nori_3 = "images/Chapter 3/Moving/Shinobu+Nori/Twilight.png"
image global_map_character_moving_lunchtime_shinobu_tsubasa_shintaro_3 = "images/Chapter 3/Moving/Shinobu+Tsubasa+Shintaro/Daytime.png"
image global_map_character_moving_lunchtime_tomo_3 = "images/Chapter 3/Moving/Tomo/Daytime.png"
image global_map_character_moving_lunchtime_tomo_4 = "images/Chapter 3/Moving/Tomo/Daytime.png"
image global_map_character_moving_twilight_tomo_3 = "images/Chapter 3/Moving/Tomo/Twilight.png"
image global_map_character_moving_twilight_tomo_4 = "images/Chapter 3/Moving/Tomo/Twilight.png"
image global_map_character_moving_twilight_tomo_school_3 = "images/Chapter 3/Moving/Tomo+School/Twilight.png"
image global_map_character_moving_night_tomo_3 = "images/Chapter 3/Moving/Tomo/Night.png"
image global_map_character_moving_night_tomo_4 = "images/Chapter 3/Moving/Tomo/Night.png"
image global_map_character_moving_lunchtime_tomo_shinobu_3 = "images/Chapter 3/Moving/Tomo+Shinobu/Daytime.png"
image global_map_character_moving_lunchtime_tsuki_sora_shintaro_3 = "images/Chapter 3/Moving/Tsuki+Sora+Shintaro/Celemony.png"
image global_map_character_moving_twilight_tsuki_sora_tomo_school_3 = "images/Chapter 3/Moving/Tsuki+Sora+Tomo+School/Twilight.png"
image global_map_character_moving_lunchtime_empty_4 = "images/Dream/Moving/Empty/Daytime.png"

image global_map_character_info_itou = "images/Moving/Character/Itou.png"
image global_map_character_info_nori = "images/Moving/Character/Nori.png"
image global_map_character_info_saburo = "images/Moving/Character/Saburo.png"
image global_map_character_info_sakuya = "images/Moving/Character/Sakuya.png"
image global_map_character_info_sakuya_tsubasachan = "images/Moving/Character/Sakuya+Tsubasa-chan.png"
image global_map_character_info_shinobu = "images/Moving/Character/Shinobu.png"
image global_map_character_info_shinobu_nori = "images/Moving/Character/Shinobu+Nori.png"
image global_map_character_info_shintaro = "images/Moving/Character/Shintaro.png"
image global_map_character_info_shiro = "images/Moving/Character/Shiro.png"
image global_map_character_info_shiro_tsubasachan = "images/Moving/Character/Shiro+Tsubasa-chan.png"
image global_map_character_info_sora = "images/Moving/Character/Sora.png"
image global_map_character_info_tomo = "images/Moving/Character/Tomo.png"
image global_map_character_info_tomo_shinobu = "images/Moving/Character/Tomo+Shinobu.png"
image global_map_character_info_tomo_shintaro = "images/Moving/Character/Tomo+Shintaro.png"
image global_map_character_info_tomo_tsubasa = "images/Moving/Character/Tomo+Tsubasa.png"
image global_map_character_info_tsuki_sora_tomo_school = "images/Moving/Character/Tomo+Tsuki+Sora.png"
image global_map_character_info_tomo_yuuhi = "images/Moving/Character/Tomo+Yuuhi.png"
image global_map_character_info_tsubasa = "images/Moving/Character/Tsubasa.png"
image global_map_character_info_shinobu_tsubasa_shintaro = "images/Moving/Character/Tsubasa+Shinobu+Shintaro.png"
image global_map_character_info_tsuki = "images/Moving/Character/Tsuki.png"
image global_map_character_info_tsuki_sora = "images/Moving/Character/Tsuki+Sora.png"
image global_map_character_info_tsuki_sora_shintaro = "images/Moving/Character/Tsuki+Sora+Shintaro.png"
image global_map_character_info_yukio = "images/Moving/Character/Yukio.png"
image global_map_character_info_shiro_yukio = "images/Moving/Character/Yukio+Shiro.png"
image global_map_character_info_yuuhi = "images/Moving/Character/Yuuhi.png"

style global_menu_frame is default
transform global_map_fade:
    alpha 0
    linear 0.4 alpha 1.0

transform global_map_character_movein:
    on show:
        xpos -240
        easein_back 0.4 xpos 0
    on hide:
        xpos 0
        linear 0.4 xpos -240

transform global_map_place_movein:
    on show:
        xpos 800
        easein 0.4 xpos 256
    on hide:
        xpos 256
        easein 0.4 xpos 800

transform global_map_action_movein:
    on show:
        xpos -245
        easein 0.6 xpos 0
    on hide:
        xpos 0
        easein 0.4 xpos -245

transform global_map_weather_lunchtime:
    xpos 130
    ypos 470
    xanchor 0.5
    yanchor 0.5
    alpha 0.0
    pause 1.4
    linear 0.4 alpha 1.0
    parallel:
        rotate 0
        linear 5.0 rotate 360
        repeat

transform global_map_weather_twilight:
    xpos 130
    ypos 470
    xanchor 0.5
    yanchor 0.5
    alpha 0.0
    pause 1.4
    linear 0.4 alpha 1.0
    parallel:
        rotate 0
        linear 30.0 rotate 360
        repeat

transform global_map_weather_night:
    xpos 130
    ypos 470
    xanchor 0.5
    yanchor 0.5
    alpha 0.0
    pause 1.4
    linear 0.4 alpha 1.0
    parallel:
        rotate 0
        linear 5.0 rotate 90
        linear 5.0 rotate 0
        repeat
transform global_map_hint_fade:
    on show:
        alpha 0.0
        pause 0.4
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

transform global_map_help:
    on show:
        alpha 0.0
        xalign 1.0
        yalign 1.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

image global_map_school_outside_lunchtime:
    Solid("#000000")
    pause 0.6
    "images/Background/School outside/School 2.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/School outside.png" with Dissolve(0.4)

image global_map_school_outside_twilight:
    Solid("#000000")
    pause 0.6
    "images/Background/School outside/School 2 twilight.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/School outside twilight.png" with Dissolve(0.4)

image global_map_school_outside_night:
    Solid("#000000")
    pause 0.6
    "images/Background/School outside/School 2 night.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/School outside night.png" with Dissolve(0.4)

image global_map_school_inside_lunchtime:
    Solid("#000000")
    pause 0.6
    "images/Background/School inside/Classroom low angle.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/School inside.png" with Dissolve(0.4)

image global_map_school_inside_twilight:
    Solid("#000000")
    pause 0.6
    "images/Background/School inside/Classroom low angle twilight.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/School inside twilight.png" with Dissolve(0.4)

image global_map_school_inside_night:
    Solid("#000000")
    pause 0.6
    "images/Background/School inside/Classroom low angle night.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/School inside night.png" with Dissolve(0.4)

image global_map_misaki_lunchtime:
    Solid("#000000")
    pause 0.6
    "images/Background/Takarasaki/Takarasaki back road.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/Town.png" with Dissolve(0.4)

image global_map_misaki_twilight:
    Solid("#000000")
    pause 0.6
    "images/Background/Takarasaki/Takarasaki back road twilight.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/Town twilight.png" with Dissolve(0.4)

image global_map_misaki_night:
    Solid("#000000")
    pause 0.6
    "images/Background/Takarasaki/Takarasaki back road night.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/Town night.png" with Dissolve(0.4)
image global_map_dream_lunchtime:
    Solid("#000000")
    pause 0.6
    "images/Background/Outside bath 3.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/Dream.png" with Dissolve(0.4)
image global_map_hotel_lunchtime:
    Solid("#000000")
    pause 0.6
    "images/Background/Hotel/Moving.png" with Dissolve(0.2)
    pause 0.8
    "images/Background/Moving background/Hotel.png" with Dissolve(0.4)

image global_map_hint_lunchtime = "images/Moving/Hint/Daytime.png"
image global_map_hint_twilight = "images/Moving/Hint/Twilight.png"
image global_map_hint_night = "images/Moving/Hint/Night.png"
image global_map_hint_dream = "images/Moving/Hint/Dream.png"
image global_map_hint_content_1 = "images/Help/Moving/1.png"
image global_map_hint_content_2 = "images/Help/Moving/2.png"
image global_map_hint_content_3 = "images/Help/Moving/3.png"
image global_map_hint_content_4 = "images/Help/Moving/4.png"
image global_map_hint_content_5 = "images/Help/Moving/5.png"
image global_map_hint_content_6 = "images/Help/Moving/6.png"
image global_map_hint_content_7 = "images/Help/Moving/7.png"
image global_map_hint_content_8 = "images/Help/Moving/8.png"

transform global_map_hint_content_transform(delay_time):
    yalign 1.0
    xpos 800
    pause delay_time
    easein 0.5 xpos 0
    pause 4.0
    easein 0.5 xpos 800
    pause 35.0 - delay_time
    repeat
