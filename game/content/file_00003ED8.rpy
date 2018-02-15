# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003ED8 (End of semester Night Misaki)

label block_00003ED9:
    # Node: 00003ED9 (開始)

    if judge_lm_condition([{ "scope": 0, "content": "VarExists(\"E_StudyRedirect\") == True" }]):
        jump block_00003F10
    if judge_lm_condition([]):
        jump block_00003EDC

    return

label block_00003F10:
    # Node: 00003F10 (Redirect)

    if judge_lm_condition([{ "scope": 0, "content": "E_StudyRedirect == True" }]):
        jump block_00003F11
    if judge_lm_condition([]):
        jump block_00003EDC

    return

label block_00003F11:
    # Node: 00003F11 (Cancel: Redirect)
    $ del E_StudyRedirect

    if judge_lm_condition([]):
        jump block_00003F2B

    return

label block_00003F2B:
    # Node: 00003F2B (Home)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Out.png","hover": "images/MOVING/ACTIONS/Out hover.png","name": "移動"}, {"pos": (408, 192),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "写真"}, {"pos": (176, 312),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "休む"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_713
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003F2A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"休む\"" }]):
        jump block_00003F2C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"写真\"" }]):
        jump block_00003F02

    return

label block_00003F2A:
    # Node: 00003F2A (Out)
    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51


    if judge_lm_condition([]):
        jump block_00003EF2

    return

label block_00003EF2:
    # Node: 00003EF2 (宝咲 inside)
    if sys_music_current_file != "sound/BGM/Night.ogg":
        play music "sound/BGM/Night.ogg" loop
        $ sys_music_current_file = "sound/BGM/Night.ogg"

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

    $ set_place_title(_("宝咲上学路"))
    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B43989DF0DC847C09F17E6BC37E5C232 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EF3

    return

label block_00003EF3:
    # Node: 00003EF3 (宝咲 inside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (384, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_714
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003EF0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003F28

    return

label block_00003EF0:
    # Node: 00003EF0 (宝咲)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("宝咲"))
    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E3E8ED1CA4664F89AC2C2CB6432FC3BA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C3SG1 == True" }]):
        jump block_00003EF1
    if judge_lm_condition([]):
        jump block_00003F0F

    return

label block_00003EF1:
    # Node: 00003EF1 (宝咲)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (352, 264),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_715
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003F25
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003EF2

    return

label block_00003F25:
    # Node: 00003F25 (Station)
    $ zorder_tag_D71B998959E446A69B3BAF1EFCCB35F6 = 400

    if judge_lm_condition([]):
        jump block_00003F26

    return

label block_00003F26:
    # Node: 00003F26 (選擇)
    call scb_bus_selector(show_misaki=True, show_takarasaki=False, show_umesaki=False) from _call_scb_bus_selector_16

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"乗らない\"" }]):
        jump block_00003F27
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲\"" }]):
        jump block_00003EE9

    return

label block_00003F27:
    # Node: 00003F27 (Return)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003EF1

    return

label block_00003EE9:
    # Node: 00003EE9 (御咲)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Train 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Train 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Train 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.4


    if judge_lm_condition([]):
        jump block_00003EF7

    return

label block_00003EF7:
    # Node: 00003EF7 (御咲站)
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
    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3DCDD617B76F49E5BFF51D15DBF7C139 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EF8

    return

label block_00003EF8:
    # Node: 00003EF8 (御咲站)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (336, 352),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (200, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "路線図"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_716
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003F13
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003F22
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"路線図\"" }]):
        jump block_00003EFE

    return

label block_00003F13:
    # Node: 00003F13 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00003F12

    return

label block_00003F12:
    # Node: 00003F12 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00003EDC

    return

label block_00003EDC:
    # Node: 00003EDC (Misaki)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Night.ogg":
        play music "sound/BGM/Night.ogg" loop
        $ sys_music_current_file = "sound/BGM/Night.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "tomo"
    $ sys_ayumi_global_map_time = "night"

    if judge_lm_condition([]):
        jump block_00003F00

    return

label block_00003F00:
    # Node: 00003F00 (Misaki LCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", True, False, talk_label="block_00003EDA", target_label="block_00003EDB") from _call_scb_global_map_170
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲学園\"" }]):
        jump block_00003EE0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"住宅街\"" }]):
        jump block_00003EDE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" }]):
        jump block_00003EE4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲駅\"" }]):
        jump block_00003EF7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"昼休み\"" }]):
        jump block_00003F20
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00003EDA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00003EDB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00003F00
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00003EFF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" }]):
        jump block_00003EE1

    return

label block_00003EE0:
    # Node: 00003EE0 (Misaki school)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ reverse_volume("music", 1)

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("校门"))
    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5333E0D1BE9A4EB995FB5238B3E3566A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EDF

    return

label block_00003EDF:
    # Node: 00003EDF (Misaki school)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (96, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "屋外トイレへ"}, {"pos": (456, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "学校看板"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_717
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003F13
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外トイレへ\"" }]):
        jump block_00003F07
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学校看板\"" }]):
        jump block_00003F05

    return

label block_00003F07:
    # Node: 00003F07 (Outside toilet)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("室外厕所"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_53694044B4E04C70B4E4443B16015802 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003F06

    return

label block_00003F06:
    # Node: 00003F06 (Outside toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_718
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003EE0

    return

label block_00003F05:
    # Node: 00003F05 (Board)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_3BE9AC227F0142FBAABEEB7605D6A3F9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003EDF

    return

label block_00003EDE:
    # Node: 00003EDE (Residential street)
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
    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C6E646A376EB4D6687DFAAD949959131 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EE2

    return

label block_00003EE2:
    # Node: 00003EE2 (Residential street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (552, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (696, 360),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_719
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003F13
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003EE6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00003EEA

    return

label block_00003EE6:
    # Node: 00003EE6 (Residential street turning)
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
    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_449F8C5E2EEC417FAE1BD172ABAAC1C1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EE7

    return

label block_00003EE7:
    # Node: 00003EE7 (Residential street turning)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (120, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "花乃湯", "condition":[{"scope":0,"content":"0 == 1"}]}, {"pos": (512, 320),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "神社"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_720
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"神社\"" }]):
        jump block_00003EEE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003EDE

    return

label block_00003EEE:
    # Node: 00003EEE (Jinja)
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
    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3A154174F212493AAD3E3E9CB36251C7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "IsCaveMemoAvailable == False" }]):
        jump block_00003F09
    if judge_lm_condition([]):
        jump block_00003EEF

    return

label block_00003F09:
    # Node: 00003F09 (Jinja hidden)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (529, 330),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "手紙"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_721
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"手紙\"" }]):
        jump block_00003F0A
    if judge_lm_condition([]):
        jump block_00003EE6

    return

label block_00003F0A:
    # Node: 00003F0A (Memo)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    pause 0.5

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？好像有什么东西。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3E0CBD2C9B6745D4BABE60C027B35BD1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.7

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这是什么？\n竟然往神社赛钱箱乱放，真该遭报应——！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好！作为好孩子就由我处理了！"

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈，会不会被神明夸奖呐。\n"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "能发生什么好事就好了呐——♪"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("神社"))
    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"


    if judge_lm_condition([]):
        jump block_00003F0D

    return

label block_00003F0D:
    # Node: 00003F0D (EnableCaveMemo)
    $ IsCaveMemoAvailable = True

    if judge_lm_condition([]):
        jump block_00003EEF

    return

label block_00003EEF:
    # Node: 00003EEF (Jinja)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_722
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003EE6

    return

label block_00003EEA:
    # Node: 00003EEA (Square)
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
    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B963C3D0E0E24FB59197E3C91C7EFFBD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EEB

    return

label block_00003EEB:
    # Node: 00003EEB (Square)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (624, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "泉の公園"}, {"pos": (120, 328),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "？？？"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_723
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉の公園\"" }]):
        jump block_00003EF4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003EDE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"？？？\"" }]):
        jump block_00003EEC

    return

label block_00003EF4:
    # Node: 00003EF4 (Spring water park)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2222EF2E666049F8B64636B5EA692C8F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5


    if judge_lm_condition([{ "scope": 0, "content": "C3QNori == False" }]):
        jump block_00003EF5
    if judge_lm_condition([]):
        jump block_00003F04

    return

label block_00003EF5:
    # Node: 00003EF5 (Spring water park 朔 quest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (368, 168),"image": "images/End of semester/Menu/Nori quest.png","hover": "images/MENU/Nori hover.png","name": "朔"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.5, 0.2) from _call_lm_menu_724
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"朔\"" }]):
        jump block_00003EF6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003EEA

    return

label block_00003EF6:
    # Node: 00003EF6 (朔 quest)
    $ set_window("イベントモード")
    stop music fadeout 1.5
    $ sys_music_current_file = ""

    stop effect2 fadeout 1.5
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1.5

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2222EF2E666049F8B64636B5EA692C8F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.9

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 200
    show rs_image_9327E92116934E66A96F4E0381646B64 as tag_E99970E1386B453DAF81C3AE2C72BE8E at right_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_62324AD297554FE987C680452CEE232E "哦呀，居然会在这种时间遇到。\n"
    show rs_image_9AD45D644515456B9DF8ED034B70000C as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "晚上好，森海友同学。"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔——那个……你是……"

    show rs_image_EC4DA012C01145D0B337D26F85D2756C as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "哈哈，不要装了。前些日子的旅行，虽说是偶然，我们也见过面。"

    show rs_image_9327E92116934E66A96F4E0381646B64 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "那段时间对我们双方应该都很有意义。"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦，朔君！{w=0.5}\n{nw}"
    show rs_image_285E40B50F3F466F9AE41CD837D82E42 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "对不对不起，和那时候形象差距太大，一时没能认出来。"

    show rs_image_76BFBAD96CEB4046A3782EFCCAAFAF80 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "这样。{w=0.5}算了，{color=#FF8000}那家伙{/color}也没能认出来，这不怪你。"

    show rs_image_76EBFB69D3934625A3E97B836F99E8BC as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    stop music2 fadeout 1.5
    $ sys_music2_current_file = ""

    rs_character_62324AD297554FE987C680452CEE232E "……{w=0.5}{nw}"
    if sys_music_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1DB550D0E6EB48529705057DFE7E198C as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.3

    extend "这么说很突然，但森海同学，我有件事需要你帮忙。"

    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，现在？唔，不过——已经这么晚，我还要回去做饭……"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对不起——下次可以吗？"

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_F33F4D4959B947DB9755DD0A59FB7942 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_62324AD297554FE987C680452CEE232E "……我明白了。既然你这么说，那就不勉强了。"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！{w=0.4}{nw}"
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那么下次见——！拜拜！"

    window hide

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 1.3

    if sys_music_current_file != "sound/BGM/Night.ogg":
        play music "sound/BGM/Night.ogg" loop
        $ sys_music_current_file = "sound/BGM/Night.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ set_place_title(_("广场"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B963C3D0E0E24FB59197E3C91C7EFFBD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.8

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.5

    window show

    rs_character_62324AD297554FE987C680452CEE232E "你想去什么地方？“不勉强”是用强硬手段也要达到目标的意思。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶？"
    if sys_effect2_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=32}……！？！？！？{/size}"

    window hide

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 2.5

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B97A3992A1D24282B85B44E0C876F034 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222BBB56F7BA4025B3E942F40786CBC9

    pause 0.5

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FFFF80}那之后的事情记不清了。{/color}{w}{color=#FFFF80}不过，应该发生了很多事。{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 200
    show rs_image_D244929D2FE04BEBB96CD94BCD6EB0BA as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_195F518B89564C98A557F130D2E603F0

    extend "{color=#FFFF80}被带到不知名的地方，被坏人洗脑操纵。{/color}"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 200
    show rs_image_68589D1EC3074BE4A9E98B90660B88D3 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at Transform(xpos=270, yalign=0.0) zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_195F518B89564C98A557F130D2E603F0

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FFFF80}后来和正义的伙伴爆发了激烈的冲突。{/color}"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_195F518B89564C98A557F130D2E603F0

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FFFF80}最后是和朋友感动的重逢。{/color}"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_195F518B89564C98A557F130D2E603F0

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FFFF80}我不知道那究竟是梦境还是现实。{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FFFF80}不过，有件事是可以确定的。那就是，{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    extend "{color=#FFFF80}我……{/color}{w}{w=0.5}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Look! 1.ogg"

    show rs_image_CB15A79501FD4DA1B7BFB3859176C1BA as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_7D201433F8374283B302D701D825C874

    extend "{color=#FFFF80}得到了寄宿着不可思议力量的{/color}{color=#FF0000}“超人套装”{/color}{color=#FFFF80}！{/color}"

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1


    if judge_lm_condition([]):
        jump block_00003F08

    return

label block_00003F08:
    # Node: 00003F08 (QUEST FINISH)
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

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003F0B

    return

label block_00003F0B:
    # Node: 00003F0B (C3Q朔)
    $ C3QNori = True

    if judge_lm_condition([]):
        jump block_00003F14

    return

label block_00003F14:
    # Node: 00003F14 (終了)

    return

label block_00003F04:
    # Node: 00003F04 (Spring water park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_725
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003EEA

    return

label block_00003EEC:
    # Node: 00003EEC (Forest)
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

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_464C61F258484AD3A9B3DD56248E993A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C3QNori == True" }]):
        jump block_00003F15
    if judge_lm_condition([]):
        jump block_00003EED

    return

label block_00003F15:
    # Node: 00003F15 (Forest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (400, 360),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "洞窟へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_726
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "E_IsCaveFirstArrive == True" }]):
        jump block_00003F18
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003EEA
    if judge_lm_condition([]):
        jump block_00003F16

    return

label block_00003F18:
    # Node: 00003F18 (Cancel: First)
    $ E_IsCaveFirstArrive = False

    if judge_lm_condition([]):
        jump block_00003F17

    return

label block_00003F17:
    # Node: 00003F17 (First arrive)
    window show

    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『这前面非常危险。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『不过，以前得到过一件寄宿着\n不可思议力量的{/color}{color=#FF0000}超人服装{/color}{color=#0080FF}。{/color}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_CB15A79501FD4DA1B7BFB3859176C1BA as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "{color=#0080FF}穿上后就可以顺利前进了。』{/color}"

    window hide

    $ set_place_title(_("迷之地点"))
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003F16

    return

label block_00003F16:
    # Node: 00003F16 (朔洞窟)
    call block_00002B81 from _call_block_00002B81_1

    if judge_lm_condition([]):
        jump block_00003F19

    return

label block_00003F19:
    # Node: 00003F19 (RESET)
    if sys_music_current_file != "sound/BGM/Night.ogg":
        play music "sound/BGM/Night.ogg" loop
        $ sys_music_current_file = "sound/BGM/Night.ogg"

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

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_464C61F258484AD3A9B3DD56248E993A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003F15

    return

label block_00003EED:
    # Node: 00003EED (Forest empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_727
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003EEA

    return

label block_00003EE4:
    # Node: 00003EE4 (Shopping street)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A06541B8404D4065AD2E26F7B0FBD5B4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EE5

    return

label block_00003EE5:
    # Node: 00003EE5 (Shopping street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_728
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003F13

    return

label block_00003F20:
    # Node: 00003F20 (Daytime)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    stop music fadeout 1
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 0.8

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003F21

    return

label block_00003F21:
    # Node: 00003F21 (終了)

    return

label block_00003EDA:
    # Node: 00003EDA (Conversation)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "已经这么晚，必须赶快回家了。"

    window hide

    $ set_window("(標準)")

    return

label block_00003EDB:
    # Node: 00003EDB (Target)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『尽快回家为好。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003EFF:
    # Node: 00003EFF (Chatacter)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E12C07C263114A53A918CA2B2E9A063D = 500
    show rs_image_4E1A5FBD35C1444A97E790B9906A7732 as tag_E12C07C263114A53A918CA2B2E9A063D at center_bottom zorder zorder_tag_E12C07C263114A53A918CA2B2E9A063D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_ED234D4517E14A4EB0C635E1C4B85E12 = 500
    show rs_image_EC0A4B149A8A4350BF4B66268E95D844 as tag_ED234D4517E14A4EB0C635E1C4B85E12 at center_bottom zorder zorder_tag_ED234D4517E14A4EB0C635E1C4B85E12 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause

    hide tag_ED234D4517E14A4EB0C635E1C4B85E12
    hide tag_E12C07C263114A53A918CA2B2E9A063D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 200
    $ zorder_tag_88D3209FDD1D4A2E8369A5A61DF50852 = 400

    if judge_lm_condition([]):
        jump block_00003F00

    return

label block_00003EE1:
    # Node: 00003EE1 (Park)
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
    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F080DC78D9E041C8851F42F8A37F4FC3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EE3

    return

label block_00003EE3:
    # Node: 00003EE3 (Park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_729
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003F13

    return

label block_00003F22:
    # Node: 00003F22 (Station)
    $ zorder_tag_D71B998959E446A69B3BAF1EFCCB35F6 = 400

    if judge_lm_condition([]):
        jump block_00003F24

    return

label block_00003F24:
    # Node: 00003F24 (選擇)
    call scb_bus_selector(show_misaki=False, show_takarasaki=True, show_umesaki=False) from _call_scb_bus_selector_17

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"乗らない\"" }]):
        jump block_00003F23
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"宝咲\"" }]):
        jump block_00003EE8

    return

label block_00003F23:
    # Node: 00003F23 (Return)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003EF8

    return

label block_00003EE8:
    # Node: 00003EE8 (宝咲)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Train 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Train 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Train 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.4


    if judge_lm_condition([]):
        jump block_00003EF0

    return

label block_00003EFE:
    # Node: 00003EFE (Map)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_507B7F77C4F74464A02D5387DFA7FE2C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    show rs_image_64016442C6754AFBA84D936DA56D33FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003EF8

    return

label block_00003F0F:
    # Node: 00003F0F (宝咲 守)
    $ sys_lm_menu_item = [{"pos": (591, 235),"image": "images/Menu/Mamoru.png","hover": "images/Menu/Mamoru hover.png","name": "マモル"}, {"pos": (312, 264),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_730
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"マモル\"" }]):
        jump block_00003F0E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003EF2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003F25

    return

label block_00003F0E:
    # Node: 00003F0E (守)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_6F2794FD69324483908276C4A713FB7B as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at center_bottom zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_57471360F48A413AB843A4E46D8C5541 "哈……累死了。今天的任务也算结束了。"

    show rs_image_9060496A498A44A9A87B73DE0A9196C6 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "分时段交替巡逻是不错，\n但这样对方在夜班时会不会很辛苦呐。\n毕竟生活节奏每天都会变来变去。"

    show rs_image_B6A6A4DD42794007AD1A9306464D5651 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "要是比现在出席率再降低就麻烦了。\n下次必须和他好好谈谈。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（好长的独白——）"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("宝咲"))
    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"


    if judge_lm_condition([]):
        jump block_00003F0F

    return

label block_00003F28:
    # Node: 00003F28 (Home)

    if judge_lm_condition([]):
        jump block_00003F29

    return

label block_00003F29:
    # Node: 00003F29 (選擇)
    call scb_selector(_("回家？"), [{"name":"はい", "content":_("没问题")}, {"name":"いいえ", "content":_("还有其他事情没做完")}]) from _call_scb_selector_81

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003F01
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00003EF3

    return

label block_00003F01:
    # Node: 00003F01 (Home)
    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    $ set_place_title(_("友的房间"))
    pause 0.6

    if sys_music2_current_file != "sound/BGM/Tomo's room.ogg":
        play music2 "sound/BGM/Tomo's room.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Tomo's room.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_59308A2352314B1E8ABB34860FDB9423 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003F2B

    return

label block_00003F2C:
    # Node: 00003F2C (Rest)

    if judge_lm_condition([]):
        jump block_00003F2D

    return

label block_00003F2D:
    # Node: 00003F2D (選擇)
    call scb_selector(_("今天没有其他安排了？"), [{"name":"はい", "content":_("休息")}, {"name":"いいえ", "content":_("时间还早")}]) from _call_scb_selector_82

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003F2E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00003F2B

    return

label block_00003F2E:
    # Node: 00003F2E (Next day)
    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect2_current_file != "sound/BGM/Finally.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/BGM/Finally.ogg" noloop
        $ sys_effect2_current_file = "sound/BGM/Finally.ogg"

    $ set_place_title(False)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_070289614C9E4592B7E9A0F0E985B92A

    pause 3.5

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5

    if sys_music_current_file != "sound/BGM/Chapter 3.ogg":
        play music "sound/BGM/Chapter 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 3.ogg"


    if judge_lm_condition([]):
        jump block_00003F2F

    return

label block_00003F2F:
    # Node: 00003F2F (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_24

    if judge_lm_condition([]):
        jump block_00003F31

    return

label block_00003F31:
    # Node: 00003F31 (終了)
    $ reverse_volume("music", 1)

    return

label block_00003F02:
    # Node: 00003F02 (Photo)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_9C7CF5F1B0FA4AD9B3C445C4FFD0CE32 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003F2B

    return

