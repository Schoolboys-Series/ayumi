# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00000A74 (CP2 作哉散歩)

label block_00000A75:
    # Node: 00000A75 (開始)

    if judge_lm_condition([]):
        jump block_00000A78

    return

label block_00000A78:
    # Node: 00000A78 (Misaki)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "sakuya_tsubasachan"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_00000A79

    return

label block_00000A79:
    # Node: 00000A79 (Misaki XCTA)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", False, True, talk_label="block_00000A76", target_label="block_00000A77") from _call_scb_global_map_112
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲学園\"" }]):
        jump block_00000A7C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"住宅街\"" }]):
        jump block_00000A7A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" }]):
        jump block_00003A7E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" }]):
        jump block_00000A7D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲駅\"" }]):
        jump block_00000AB2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"昼休み不可\"" }]):
        jump block_00000A79
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00000A76
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00000A77
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00003A74
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001F9E

    return

label block_00000A7C:
    # Node: 00000A7C (Misaki school)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("校门"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000A7B

    return

label block_00000A7B:
    # Node: 00000A7B (Misaki school)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_427
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A7F

    return

label block_00003A7F:
    # Node: 00003A7F (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00003A7C

    return

label block_00003A7C:
    # Node: 00003A7C (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00000A78

    return

label block_00000A7A:
    # Node: 00000A7A (Residential street)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("住宅街"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000A7E

    return

label block_00000A7E:
    # Node: 00000A7E (Residential street 四朗 point)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (216, 290),"image": "images/Chapter 2/Menu/Shiro point.png","hover": "images/Chapter 2/Menu/Shiro hover.png","name": "四朗"}, {"pos": (552, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (696, 360),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_428
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A7F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000A94
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00000A9C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"四朗\"" }]):
        jump block_00000A89

    return

label block_00000A94:
    # Node: 00000A94 (Residential street truning)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("住宅街路口"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A4E74E94E7C549809795CEBC732E6326 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000A95

    return

label block_00000A95:
    # Node: 00000A95 (Residential street truning)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (120, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "花乃湯"}, {"pos": (512, 320),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "神社"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_429
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"花乃湯\"" }]):
        jump block_00000AA2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"神社\"" }]):
        jump block_00000AA0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A7A

    return

label block_00000AA2:
    # Node: 00000AA2 (Hanano)
    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("花乃汤"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BB828FFB3AED43E6BB07C3169278015F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000AA3
    if judge_lm_condition([]):
        jump block_00000AAE

    return

label block_00000AA3:
    # Node: 00000AA3 (Hanano)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "ポスター"}, {"pos": (232, 272),"image": "images/Menu/Shougintoki.png","hover": "images/Menu/Shougintoki hover.png","name": "翔銀時"}, {"pos": (80, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_430
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A94
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000AAE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"翔銀時\"" }]):
        jump block_00000AAB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ポスター\"" }]):
        jump block_00001F79

    return

label block_00000AAE:
    # Node: 00000AAE (River)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("河边"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_788AB1D278244B129D0C9F9230156AD7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000AAF

    return

label block_00000AAF:
    # Node: 00000AAF (River)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_431
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000AA2

    return

label block_00000AAB:
    # Node: 00000AAB (翔銀時)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_4E1328DF58984CDDB873E6CA9A162506 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "你好。今天天气真不错。\n晴朗温暖，稍不注意就会睡过去。"

    show rs_image_1DB126B964544691AE7B64404BF2995F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "从学校来的路上，\nY字路口右转有一间神社。"

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "那里祭祀的是很灵验的梦境之神，\n似乎能让人{color=#808000}做想做的梦{/color}。"

    show rs_image_CA5DCF09EC6F43D3BF094A232BE224FB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "正好也很久没去了，\n你要不要也陪我去看看呢。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000AA3

    return

label block_00001F79:
    # Node: 00001F79 (Poster)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_048FEDA101B44195A010E4D967CEAF07 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    show rs_image_7448A3B2C6EF4B219EA7F33064B8CE76 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000AA3

    return

label block_00000AA0:
    # Node: 00000AA0 (Jinja)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("神社"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_65FB514C0D3B40558703DF2D35F42E17 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000AA1

    return

label block_00000AA1:
    # Node: 00000AA1 (Jinja)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_432
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A94

    return

label block_00000A9C:
    # Node: 00000A9C (Square)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ reverse_volume("music", 1)

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("广场"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3B5A1C5EC3AA4BC08F04842878E1A1F0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000A9D

    return

label block_00000A9D:
    # Node: 00000A9D (Square)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (624, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "泉の公園"}, {"pos": (120, 328),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "？？？"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_433
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉の公園\"" }]):
        jump block_00000AA9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A7A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"？？？\"" }]):
        jump block_00000A9E

    return

label block_00000AA9:
    # Node: 00000AA9 (Spring water park)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("泉水公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Wave 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wave 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4C85C2BFFE134BFDADEC528506A90841 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000AAA

    return

label block_00000AAA:
    # Node: 00000AAA (Spring water park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_434
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A9C

    return

label block_00000A9E:
    # Node: 00000A9E (Forest)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("迷之地点"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7D781D05099A4C93AF6B1D005359F3E9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000A9F

    return

label block_00000A9F:
    # Node: 00000A9F (Forest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_435
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A9C

    return

label block_00000A89:
    # Node: 00000A89 (四朗)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_3262D60C74654385A3E1B28F01BB2B2E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_bottom zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_F69A7F8603174D3296CF7683C5C0D06C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，小翼！\n"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_D5EC6359084E4C79A1257082BC289D09 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "过来，让我抱抱♪"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_83E2064E232640149A12D7598C5FE5C3 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_bottom zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪～♪"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "四朗，你不应该是对狗不拿手的么？"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_33259AF0E1B94B0293947AFB69BDD5F9 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_bottom zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "现在害怕还是害怕，但不知为何小翼没关系。"

    show rs_image_F69A7F8603174D3296CF7683C5C0D06C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "也许是被激发母性了？\n抱也抱过了，也被带去个各种地方……"

    show rs_image_D5EC6359084E4C79A1257082BC289D09 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊！对了，我有想带你们去的地方哦。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "如果有时间的话可以跟我来吗？"

    window hide

    pause 0.5

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2.4

    $ set_window("イベントモード")
    if sys_effect2_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Grass 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A924E6FB7A0740108CE21D8D0C0FC8D2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_5ECF4017CE3E48E0B749AA1981DD40C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_356ECD8406BB49698A4D9CAD3C494C73 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.3

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg"

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "小翼好厉害，这种山路也能走在前面。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "这根本不算什么，对不对，小翼。"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！"

    window hide

    pause 0.6

    if sys_effect2_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Grass 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Grass 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7639E4BE73E34BBD9D978953E896CF0C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.9

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_6AB5AA5EB92C42B0B217FDBBA0887900 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_F31BFD9162C64D929725A6AF4C2C2823 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哇，不错……还有这种地方啊。"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_6AB5AA5EB92C42B0B217FDBBA0887900 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_2878DCD08C8E473AAB40E72467C7EB0E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "看，第一次来很兴奋对不对？可以随便玩哦，小翼。"

    show rs_image_1C82CB9D173841FFB02A50833A57F72E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪——{w=0.45}{nw}"
    show rs_image_6AB5AA5EB92C42B0B217FDBBA0887900 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "汪汪。"

    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "意外得很冷静……难道以前来过？"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸——！好不容易觉得能吓小翼一跳的——"

    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我不记得带它来过啊……唔。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪！"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "回来！很危险的！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哇！小翼等等！！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_C2EBA78177DC4C19BB09CDE7382841A8 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "安……安全……。"

    show rs_image_378656EE14E64F23B3B990BE2E8D8E2E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呜——"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_81749C79DF1A40F3BF020F0ACBD64CA8 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小翼居然会向湖里跳……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "胆子太大了。哈～幸亏赶上。差点吓死我。"

    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "谢了，四朗，帮大忙了。看来还是不能掉以轻心。"

    show rs_image_E0D2132CD8F74B5CB3274596C13F9EA2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "毕竟它看到湖的时候眼神就变了……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "就那么想游泳？不过，没有毛巾所以不行。"

    show rs_image_9138D3EAFC66405AA95FD2DC03C7E56E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小翼，今天就先算了。我会去学如何保证你安全游泳的。"

    show rs_image_4CBCF132AF8F49E38C726D5800545B50 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呜……"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_1C82CB9D173841FFB02A50833A57F72E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "汪汪！{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    extend ""

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "等等！？"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "这次又怎么了～？"

    window hide

    pause 0.7

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.4

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6AB5AA5EB92C42B0B217FDBBA0887900 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_A924E6FB7A0740108CE21D8D0C0FC8D2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.6

    window show

    show rs_image_1C82CB9D173841FFB02A50833A57F72E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哈哈……汪汪！"

    pause 0.3

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，{color=#00FFFF}这棵树{/color}是！"

    window hide

    pause 0.5

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 5-3.png
    $ zorder_rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B = -100
    show rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B as rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B zorder zorder_rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B onlayer master
    hide rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222BBB56F7BA4025B3E942F40786CBC9

    pause 0.5

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我以前爬上过这里。从上面看下来的景色非常好……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……小翼也想看吗？不过再怎么说也爬不上去吧。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！汪！"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_4CBCF132AF8F49E38C726D5800545B50 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_9ACAEF851EAF4CECBC5BA7CA6AAF6C36 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_D264D770FEE64C5F8D0ED7B023B96089 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_195F518B89564C98A557F130D2E603F0

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不行！太危险了！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔——……"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_81749C79DF1A40F3BF020F0ACBD64CA8 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "啊！\n那干脆把小翼放在书包里……？"

    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不行。"

    show rs_image_D264D770FEE64C5F8D0ED7B023B96089 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊……真遗憾，小翼。"

    show rs_image_378656EE14E64F23B3B990BE2E8D8E2E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……"

    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……{w=0.5}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_8062453DA5634CCDA38E1C0EDC7F13EC = 200
    $ zorder_tag_8CFE356306CD4C6584632E2A447DEEF2 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_8062453DA5634CCDA38E1C0EDC7F13EC at right_top zorder zorder_tag_8062453DA5634CCDA38E1C0EDC7F13EC onlayer master
    show rs_image_C2EBA78177DC4C19BB09CDE7382841A8 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8CFE356306CD4C6584632E2A447DEEF2 at left_top zorder zorder_tag_8CFE356306CD4C6584632E2A447DEEF2 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "～～～唔。{w=0.35}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8CFE356306CD4C6584632E2A447DEEF2
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_70576159A31C474CAECF9B7AFDBBF16F as tag_8062453DA5634CCDA38E1C0EDC7F13EC zorder zorder_tag_8062453DA5634CCDA38E1C0EDC7F13EC onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "四朗！你在干什么！下来！！" # 四朗！危ないから降りろ！コラ！！ 按中文习惯“你在干什么”会更贴切一些

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_905E9C679FD7435E8DF16A4ECBCB85EA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    rs_character_3B4C660F421B4BE392BB540B580F0339 "没、没关系的。我很擅长爬树，也会注意安全的！"

    window hide

    pause 0.8

    hide tag_8062453DA5634CCDA38E1C0EDC7F13EC
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.8

    if sys_music2_current_file != "sound/Effect Sound/Swallow 1.ogg":
        play music2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    # Gallery unlock: images/CG/Shiro+Tsubasa-chan.png
    $ zorder_rs_image_6C20080978734302A13DBD9F5C977D8A = -100
    show rs_image_6C20080978734302A13DBD9F5C977D8A as rs_image_6C20080978734302A13DBD9F5C977D8A zorder zorder_rs_image_6C20080978734302A13DBD9F5C977D8A onlayer master
    hide rs_image_6C20080978734302A13DBD9F5C977D8A

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_6C20080978734302A13DBD9F5C977D8A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "看，小翼，到了！景色很棒？要好好记住哦。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊——等下肯定要被前辈骂了……到时候要帮我说话哦，小翼。"

    window hide

    pause 0.7

    show rs_image_905E9C679FD7435E8DF16A4ECBCB85EA as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 1.3

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show center_title (_("{size=29}谢谢！最——喜欢四朗了！{/size}")) as center_title zorder 1000
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    pause 2.0

    hide center_title
    with rs_effect_FC474B930CE449DD8BE5D4980A132631

    $ set_window("イベントモード")
    pause 0.6

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "很痒啊小翼，不要这样……真是爱撒娇呐……{w}乖乖。"

    window hide

    pause 0.5

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_A924E6FB7A0740108CE21D8D0C0FC8D2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 0.4

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    window hide

    pause 1

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.8

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_4CBCF132AF8F49E38C726D5800545B50 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_D264D770FEE64C5F8D0ED7B023B96089 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_A924E6FB7A0740108CE21D8D0C0FC8D2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 0.5

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "对、对不起……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呜——"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……{w=0.4}{nw}"
    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……算了。{w=0.4}{nw}"
    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "下次也拜托你了。"

    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "诶？"

    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我毕竟上不去树，下次也拜托你带小翼上去了。"

    show rs_image_9138D3EAFC66405AA95FD2DC03C7E56E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不过！下次必须要买安全的容器。书包太小太危险，不行。"

    show rs_image_356ECD8406BB49698A4D9CAD3C494C73 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "前辈……！"

    show rs_image_1C82CB9D173841FFB02A50833A57F72E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_59434F19656445578114DA38D9F0C893 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不愧是我的穗海前辈！太帅了♪"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪～♪"

    window hide

    pause 1

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 1.7


    if judge_lm_condition([]):
        jump block_000025D0

    return

label block_000025D0:
    # Node: 000025D0 (QUEST FINISH)
    $ set_window("(標準)")
    if sys_effect2_current_file != "sound/BGM/Quest Finished.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_effect2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 1.5

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_00002F25

    return

label block_00002F25:
    # Node: 00002F25 (C2Q作哉)
    $ C2QSakuya = True

    if judge_lm_condition([]):
        jump block_00003A80

    return

label block_00003A80:
    # Node: 00003A80 ()

    return

label block_00003A7E:
    # Node: 00003A7E (Shopping street)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5F022B91486841699EAC5FE3BDC0F5CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003A7D

    return

label block_00003A7D:
    # Node: 00003A7D (Shopping street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (104, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_436
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A7F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003A7B

    return

label block_00003A7B:
    # Node: 00003A7B (Inside)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "STAY，小翼。{w}前面人太多，太危险了。"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F1AE8B76A99E4FC297AF2F180FA7033F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00003A7D

    return

label block_00000A7D:
    # Node: 00000A7D (Park)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AC1A95BA21694004A67885C809E98CFF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000A81

    return

label block_00000A81:
    # Node: 00000A81 (Park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (160, 184),"image": "images/Menu/Kobayashi.png","hover": "images/Menu/Kobayashi hover.png","name": "小林"}, {"pos": (320, 184),"image": "images/Menu/Minami.png","hover": "images/Menu/Minami hover.png","name": "南"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_437
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A7F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" }]):
        jump block_00000A88
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" }]):
        jump block_00000AC0

    return

label block_00000A88:
    # Node: 00000A88 (小林)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_F3C56AC05CFF4764BCEAA3638847A04F as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000025CE

    return

label block_000025CE:
    # Node: 000025CE (小林+南)
    window show

    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_1CDB21F0CE5D4659A6BA9E03A4285F77 as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_EA79386263E543A88D4DC03B8BD44485 "啊，是作哉哥！\n"
    show rs_image_0DD616D8E2914FC2859CDB40FCB50F1A as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哈哈哈——♪小翼真的好小哦——！"

    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_7AB112E4EED34DAFBB2FA71D1F060DBF as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "小林酱，这很好笑嘛——？"

    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_E714266E48C34071B1AFC8E511D39DD5 as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "小翼本来就很小，\n但从远处看作哉哥散步的样子，\n觉得更小了。"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈哈，小翼——一，\n对方在看不起你哦。说点什么。"

    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0117E4BD45BE4974A1BFEF7415F2DDEE as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪、汪汪！"

    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_7AB112E4EED34DAFBB2FA71D1F060DBF as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "它说了什么？"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "{color=#FF8000}『我按人类的年龄可是\n比你们还要大哦！比你们大哦！』{/color}\n{w=0.6}这样说的。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "按照人类的年龄大概和我一样。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6DE28515804147EF8461CDC6769400E8 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "这样——小翼变成人类\n会是什么样子呐！我想看！"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈哈，我也想。\n不知道会不会做小翼变成人类的梦呐。"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000A81

    return

label block_00000AC0:
    # Node: 00000AC0 (南)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_BEF9DE93926B41AEA207953580E58EC3 as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000025CE

    return

label block_00000AB2:
    # Node: 00000AB2 (御咲站)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("御咲站"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_07BACEE3C1C64F1DAD61CD240DF0C2E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000AB6

    return

label block_00000AB6:
    # Node: 00000AB6 (御咲站)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (336, 352),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (200, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "路線図"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_438
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A7F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000ABF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"路線図\"" }]):
        jump block_00001F64

    return

label block_00000ABF:
    # Node: 00000ABF (Inside)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "STAY，小翼。{w}\n狗不能进入车站，前面不能走了。"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F1AE8B76A99E4FC297AF2F180FA7033F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪？"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不过，像是导盲犬那种受过训练的可以进去的样子。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小翼也想去考一个试试？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_83E2064E232640149A12D7598C5FE5C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嗯嗯，不错的回答呐。\n小翼这么聪明，说不定能考上呢♪"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("御咲站"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000AB6

    return

label block_00001F64:
    # Node: 00001F64 (Map)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_507B7F77C4F74464A02D5387DFA7FE2C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    show rs_image_BE48A05A53B3438C89C8FA4DF06E1A0D as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000AB6

    return

label block_00000A76:
    # Node: 00000A76 (Conversation)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "今天也要好好散步\n把该处理的都处理了呐♪"

    window hide

    $ set_window("(標準)")

    return

label block_00000A77:
    # Node: 00000A77 (Target)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『带小翼在学校周围散步。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003A74:
    # Node: 00003A74 (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_00003A77

    return

label block_00003A77:
    # Node: 00003A77 (終了)

    return

label block_00001F9E:
    # Node: 00001F9E (Character)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_ED234D4517E14A4EB0C635E1C4B85E12
    hide tag_E12C07C263114A53A918CA2B2E9A063D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    return

