# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000001B0 (CP1 Daytime)

label block_000001B1:
    # Node: 000001B1 (開始)
    $ QNewsclubRandom = 0
    $ QSabushinToiletSingle = False
    $ PianoRandom = 0

    if judge_lm_condition([]):
        jump block_000001B4

    return

label block_000001B4:
    # Node: 000001B4 (School outside)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([{ "scope": 0, "content": "C1QTsubasaPhase == 1" }]):
        jump block_00000229
    if judge_lm_condition([{ "scope": 0, "content": "C1QSabushinPhase == 1" }]):
        jump block_0000022A
    if judge_lm_condition([]):
        jump block_000018C1

    return

label block_00000229:
    # Node: 00000229 (友+翼)
    $ sys_ayumi_global_map_character = "tomo_tsubasa"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_00000224

    return

label block_00000224:
    # Node: 00000224 (School outside XCTA)
    if judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_00001FD4", target_label="block_00000D33") from _call_scb_global_map_26
    elif judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_00001FD4", target_label="block_000002B3") from _call_scb_global_map_27
    elif judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_00001FD4", target_label="block_000023CF") from _call_scb_global_map_28
    elif judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_00001FD4", target_label="block_000023D2") from _call_scb_global_map_29
    elif judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000002B2", target_label="block_00000D33") from _call_scb_global_map_30
    elif judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000002B2", target_label="block_000002B3") from _call_scb_global_map_31
    elif judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000002B2", target_label="block_000023CF") from _call_scb_global_map_32
    elif judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000002B2", target_label="block_000023D2") from _call_scb_global_map_33
    elif judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000023D0", target_label="block_00000D33") from _call_scb_global_map_34
    elif judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000023D0", target_label="block_000002B3") from _call_scb_global_map_35
    elif judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000023D0", target_label="block_000023CF") from _call_scb_global_map_36
    elif judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000023D0", target_label="block_000023D2") from _call_scb_global_map_37
    elif judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000023D1", target_label="block_00000D33") from _call_scb_global_map_38
    elif judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000023D1", target_label="block_000002B3") from _call_scb_global_map_39
    elif judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000023D1", target_label="block_000023CF") from _call_scb_global_map_40
    elif judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000023D1", target_label="block_000023D2") from _call_scb_global_map_41
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000002B0", target_label="block_00000D33") from _call_scb_global_map_42
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000002B0", target_label="block_000002B3") from _call_scb_global_map_43
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000002B0", target_label="block_000023CF") from _call_scb_global_map_44
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_000002B0", target_label="block_000023D2") from _call_scb_global_map_45
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00003665
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_0000365E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00003667
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00003649
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00003648
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00003785
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00000224
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1S1Phase == 1" }]):
        jump block_00001FD4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1S1Phase == 1" }]):
        jump block_00000D33
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00000242
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" },{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        jump block_00001FE0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        jump block_000002B2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        jump block_000002B3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" },{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        jump block_00001FE2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        jump block_000023D0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FDE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        jump block_000023D1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000002B0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        jump block_000023CF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        jump block_000023D2

    return

label block_00003665:
    # Node: 00003665 (TO: Shoe cupboard)

    if judge_lm_condition([]):
        jump block_00003663

    return

label block_00003663:
    # Node: 00003663 (TO: Shoe cupboard)

    if judge_lm_condition([]):
        jump block_000001BC

    return

label block_000001BC:
    # Node: 000001BC (Shoe cupboard)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("鞋箱"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "SYSReviewMode == True" }]):
        jump block_000031B2
    if judge_lm_condition([{ "scope": 0, "content": "C1SG1 == True" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_00001F26
    if judge_lm_condition([]):
        jump block_000001C6

    return

label block_000031B2:
    # Node: 000031B2 (Shoe cupboard 觸手A)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}, {"pos": (216, 184),"image": "images/Menu/Tentacle-earthworm.png","hover": "images/Menu/Tentacle-earthworm hover.png","name": "触手A"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_232
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_000001CB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003664
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手A\"" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000031B3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手A\"" }]):
        jump block_00003287

    return

label block_000001CB:
    # Node: 000001CB (Playground)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("校庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1S1Phase == 1" }]):
        jump block_000001F9
    if judge_lm_condition([]):
        jump block_000023B2

    return

label block_000001F9:
    # Node: 000001F9 (Playground 加藤 flag)
    $ sys_lm_menu_item = [{"pos": (328, 140),"image": "images/Chapter 1/Menu/Katou flag.png","hover": "images/Chapter 1/Menu/Katou hover.png","name": "加藤"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (632, 208),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "体育倉庫"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_233
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" }]):
        jump block_000001D6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003662
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" }]):
        jump block_000001E1

    return

label block_000001D6:
    # Node: 000001D6 (加藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_B2CDDF8BF15246E0AB406A3EFE53FF25 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_5B1F7D4B11A347398EE809B70CE694E3 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_81D16F74A3C44B8982DB528D7D934850 "那个啊，班长。\n占用点时间可以不……？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？什么什么？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_39C8643C0E274BB68657C2C746A012BC as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    show rs_image_39C8643C0E274BB68657C2C746A012BC as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_D55CD7D70774471A837BA78DDBD4046F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_81D16F74A3C44B8982DB528D7D934850 "……。"

    if sys_effect2_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哦！？\n加藤酱怎么了？怎么突然开始脱衣服了！？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "难、难道是对我……！？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A92F79586A974C46846E6EC3AD10BB6A as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_81D16F74A3C44B8982DB528D7D934850 "……你觉得{w}我的体格怎么样？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect3_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？欸欸！？突然怎么了。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_88303B9793584A67B06BD58840DA0EB1 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "别问那么多了。……总之请回答。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那、那个……\n毕竟也是在棒球部锻炼出来的我觉得很不错啊……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D55CD7D70774471A837BA78DDBD4046F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_81D16F74A3C44B8982DB528D7D934850 "……这样。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_39C8643C0E274BB68657C2C746A012BC as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_81D16F74A3C44B8982DB528D7D934850 "对，我就算空有一身肌肉，体重也不足。\n不可能成为全市第一。{w}\n所以，我决定采用别的方法。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "请、请问～\n刚才开始我就跟不上谈话了……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_27B13CA425DA4BF4963F3D9AA239AB72 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "抱歉抱歉。\n是呐，赶快进入正题比较好。{w}其实……"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window hide

    $ set_place_title(_("校庭"))
    pause 0.9

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4


    if judge_lm_condition([]):
        jump block_0000370E

    return

label block_0000370E:
    # Node: 0000370E (FLAG: 大家來相撲)
    call block_00003704 from _call_block_00003704

    if judge_lm_condition([]):
        jump block_00002A6C

    return

label block_00002A6C:
    # Node: 00002A6C (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#AA0055}“大家来相扑”{/color}{color=#0080FF}成功结束。』{/color}"

    window hide

    pause 4

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003664

    return

label block_00003664:
    # Node: 00003664 (TO: School outside)

    if judge_lm_condition([]):
        jump block_0000365D

    return

label block_0000365D:
    # Node: 0000365D (TO: School outside)

    if judge_lm_condition([]):
        jump block_0000368D

    return

label block_0000368D:
    # Node: 0000368D (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003651

    return

label block_00003651:
    # Node: 00003651 (TO: School outside)

    if judge_lm_condition([]):
        jump block_000001B4

    return

label block_00003662:
    # Node: 00003662 (TO: Shoe cupboard)

    if judge_lm_condition([]):
        jump block_00003663

    return

label block_000001E1:
    # Node: 000001E1 (PE warehouse)
    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("体育仓库"))
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F36816057C4848709177D4C457D25726 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1SSabuShin == True" }]):
        jump block_000024E3
    if judge_lm_condition([{ "scope": 0, "content": "C1QSabushinPhase == 1" }]):
        jump block_0000020D
    if judge_lm_condition([]):
        jump block_000001E2

    return

label block_000024E3:
    # Node: 000024E3 (PE warehouse 三朗)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (200, 168),"image": "images/Chapter 1/Menu/Saburo PE warehouse.png","hover": "images/Chapter 1/Menu/Saburo PE warehouse hover.png","name": "三朗"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_234
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_00000307
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000001CB

    return

label block_00000307:
    # Node: 00000307 (三朗)
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_F5BAF97AB91D4DFEACDC49C6844D1D26 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这次可要好好睡一觉了。别来烦我了——。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育仓库"))

    if judge_lm_condition([]):
        jump block_000024E3

    return

label block_0000020D:
    # Node: 0000020D (QUEST 三慎)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    pause 0.3

    pause 0.6

    window show

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3D12230112CC4ABBBDFBD0F285452ECF as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……嗯……？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_EAAD2B6A3763430786077CA6C12B7E2A as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "欸！？！？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我来了☆"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_66C3B0B9F05A45B9875CC7A1852E82E8 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "奥、奥村啊……\n你到底是怎么找到这儿的……？"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我啊，只要是三酱在地方就算是宇宙的尽头也会追过去的哦☆"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7A4915F82113486D8F17F9D510285F73 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……是、是么……"

    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈～嗯。好热啊。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "到底是气温太高，\n还是我自己按捺不住呢……"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EAAD2B6A3763430786077CA6C12B7E2A as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱，我呐，只要看到三酱，\n就会抑制不住地心跳不已紧张不止呐～"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……{w=0.3}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    extend "到底是为什么？"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_66C3B0B9F05A45B9875CC7A1852E82E8 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那、那～个，那肯定是身体有恙吧……？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_104E19984CF747D19D3CC74E9452E4A0 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "所以比起我这里请务必去保健室……"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不要不要～\n我不要被三酱以外的任何人摸～"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……这幅身体是只属于三酱的东西哦？"

    if sys_effect3_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EC9153795F8647F2B786CFC11BF340E5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "噫！？别说那么渗人的话！！"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……所以啊……。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{color=#FF00FF}抱我嘛抱我嘛密室独处哦♪♪{/color}"

    if sys_effect2_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A465618EE34C429AB8E4349BD1A608E4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "噫——！！！\n{color=#FF00FF}都说不干了完全没传达到啊！！！{/color}"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.5

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_B97A3992A1D24282B85B44E0C876F034 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.25

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cat 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cat 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cat 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Gun 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Gun 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Gun 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.25

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……猫君，对不起，请安息……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育仓库"))
    pause 0.2


    if judge_lm_condition([]):
        jump block_00002B1F

    return

label block_00002B1F:
    # Node: 00002B1F (C1Q三慎)
    $ C1QSabuShin = True
    $ QSabushinCheck1 = False
    $ C1QSabushinPhase = 0
    $ QSabushinToiletSingle = False

    if judge_lm_condition([]):
        jump block_0000020F

    return

label block_0000020F:
    # Node: 0000020F (QUEST FINISH)
    if sys_effect2_current_file != "sound/BGM/Quest Finished.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_effect2_current_file = "sound/BGM/Quest Finished.ogg"

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.8


    if judge_lm_condition([]):
        jump block_000001CB

    return

label block_000001E2:
    # Node: 000001E2 (PE warehouse)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_235
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000001CB

    return

label block_000023B2:
    # Node: 000023B2 (Playground)
    $ sys_lm_menu_item = [{"pos": (328, 140),"image": "images/Chapter 1/Menu/Katou.png","hover": "images/Chapter 1/Menu/Katou hover.png","name": "加藤"}, {"pos": (632, 208),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "体育倉庫"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_236
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" },{ "scope": 1, "content": "C1S1 == True" }]):
        jump block_000002FB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" },{ "scope": 1, "content": "C1QSabuShin == True" },{ "scope": 2, "content": "C1S5 == False" }]):
        jump block_000024B5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" }]):
        jump block_000023B3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" }]):
        jump block_000001E1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003662

    return

label block_000002FB:
    # Node: 000002FB (加藤 F1后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_B12DC311D86A491398AB2D191F6D3C8E as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_81D16F74A3C44B8982DB528D7D934850 "啊——奖金换到的烤肉\n那种味道至今无法忘记……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "滑子老师在这之上也给予了大力支持，\n吃到了更棒的套餐呐♪"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊——好开心！能在这个班真好♪\n这样的事大家以后也要一起哦！\n创造更多的回忆哦♪"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0C2639EC1DA542BE896A468C179F908B as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "啊哈哈♪是啊！"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000023B2

    return

label block_000024B5:
    # Node: 000024B5 (倉庫 Q三慎后至F5結束前)
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "现在好像很忙的样子，等下再来……"

    window hide

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000023B2

    return

label block_000023B3:
    # Node: 000023B3 (加藤１)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_5B1F7D4B11A347398EE809B70CE694E3 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_81D16F74A3C44B8982DB528D7D934850 "唔……"

    show rs_image_2F87B907B2044D52BCEC5F9AC7715FA4 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "唔————嗯……"

    stop effect2 fadeout 0.8
    $ sys_effect2_current_file = ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（好像在思考什么的样子……现在就先不打扰了）"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "TalkKatou == 0" }]):
        jump block_00002B28
    if judge_lm_condition([]):
        jump block_000023B2

    return

label block_00002B28:
    # Node: 00002B28 (T ++)
    $ TalkKatou = TalkKatou + 1

    if judge_lm_condition([]):
        jump block_000023B2

    return

label block_000031B3:
    # Node: 000031B3 (触手A)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 200
    show rs_image_5171C4277664485482367CFD06553623 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_FB87619C890441AEA41E279A1B588CAC "你想要从梦中醒来，回到现实吗？"

    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))

    if judge_lm_condition([]):
        jump block_000031B4

    return

label block_000031B4:
    # Node: 000031B4 (選擇)
    call scb_selector("", [{"name":"はい", "content":_("嗯，我要回去")}, {"name":"いいえ", "content":_("再等一会")}]) from _call_scb_selector_22

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_000031B2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003713

    return

label block_00003713:
    # Node: 00003713 ()
    $ del QNewsclubRandom
    $ del QSabushinToiletSingle
    $ del PianoRandom

    return

label block_00003287:
    # Node: 00003287 (触手A 劇情中)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 200
    show rs_image_5171C4277664485482367CFD06553623 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_FB87619C890441AEA41E279A1B588CAC "你想要从梦中醒来，回到现实吗？"

    show rs_image_A7C4CBC5126342CD8A04FA3A8072EE5F as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_FB87619C890441AEA41E279A1B588CAC "哦？稍等。\n现在你正进行着{color=#008080}事件{/color}或{color=#FF8000}委托{/color}。"

    show rs_image_466219A035C44D62AD2743E9F494A2F2 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_FB87619C890441AEA41E279A1B588CAC "要醒来的话，就请先{color=#0080FF}完成{/color}或{color=#0080FF}放弃{/color}它们。"

    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))

    if judge_lm_condition([]):
        jump block_000031B2

    return

label block_00001F26:
    # Node: 00001F26 (Shoe cupboard point)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}, {"pos": (160, 96),"image": "images/Menu/Nameko point.png","hover": "images/Menu/Nameko hover.png","name": "滑子"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_237
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_000001CB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003664
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" }]):
        jump block_000029AF

    return

label block_000029AF:
    # Node: 000029AF (Confirm)
    window show

    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『即将进入{/color}{color=#FF0080}下一个章节{/color}{color=#0080FF}。{/color}{w}\n{color=#0080FF}通关前回不来了，确定要继续？』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_000029AD

    return

label block_000029AD:
    # Node: 000029AD (選擇)
    call scb_selector("", [{"name":"はい", "content":_("没问题")}, {"name":"いいえ", "content":_("还有其他事情没做完")}]) from _call_scb_selector_23

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003991
    if judge_lm_condition([]):
        jump block_00001F26

    return

label block_00003991:
    # Node: 00003991 ()
    $ del QNewsclubRandom
    $ del QSabushinToiletSingle
    $ del PianoRandom

    return

label block_000001C6:
    # Node: 000001C6 (Shoe cupboard)
    $ sys_lm_menu_item = [{"pos": (160, 96),"image": "images/Menu/Nameko.png","hover": "images/Menu/Nameko hover.png","name": "滑子"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_238
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003664
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_000001CB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" }]):
        jump block_00001F25

    return

label block_00001F25:
    # Node: 00001F25 (滑子)
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 200
    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "有空记得来我这边。有话和你说。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))

    if judge_lm_condition([]):
        jump block_000001C6

    return

label block_0000365E:
    # Node: 0000365E (TO: Atrium)

    if judge_lm_condition([]):
        jump block_00003659

    return

label block_00003659:
    # Node: 00003659 (TO: Atrium)

    if judge_lm_condition([]):
        jump block_000001BE

    return

label block_000001BE:
    # Node: 000001BE (Atrium)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

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

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1S2 == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "TalkTsubasa > 0" }]):
        jump block_000002B7
    if judge_lm_condition([{ "scope": 0, "content": "C1S2Phase == 1" }]):
        jump block_000002B9
    if judge_lm_condition([{ "scope": 0, "content": "QTsubasaCheck1 == True" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 0, "content": "C1QTsubasaPhase == 1" }]):
        jump block_0000020A
    if judge_lm_condition([]):
        jump block_000001C8

    return

label block_000002B7:
    # Node: 000002B7 (Atrium 翼 flag)
    $ sys_lm_menu_item = [{"pos": (216, 160),"image": "images/Chapter 1/Menu/Tsubasa flag.png","hover": "images/Chapter 1/Menu/Tsubasa hover.png","name": "つばさ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (488, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "食堂へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_239
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_000001E9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"食堂へ\"" }]):
        jump block_00003650
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000365D

    return

label block_000001E9:
    # Node: 000001E9 (F2: 翼)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_28D96DBE93084DC9AD60894E8FC483ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_A6DDCE105645457E8367570AA224AC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……本来很期待的……情侣装……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦，对了！翼君，今天放学后有空吗？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_FC1EB697877A47FE9D35ED5FD247302D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸。"
    show rs_image_F5C2E50E1E4840E8BC325EAA4E4AEC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "难、难道说……\n{w=0.4}{nw}"
    show rs_image_212D585BC6E244759D9630EB4060376C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "要一起去买连帽衫……？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不，不是那么回事啦～{w=0.3}{nw}"
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A6DDCE105645457E8367570AA224AC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "既然翼君放学后有空，{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "今天就继续{color=#FF0080}小钢琴部{/color}的活动好了！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……{w=0.6}{nw}"
    show rs_image_0DCBE3E54DA04EED9BEEBD9CDC472CCA as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "啊，{w=0.4}{nw}"
    show rs_image_C1F34699FB3045D39ED696A2EFA86072 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "嗯！当然。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9E93048B179C4AE4A728558A93AF24A4 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "请像以前那样尽可能多地教我。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))

    if judge_lm_condition([]):
        jump block_00002AEE

    return

label block_00002AEE:
    # Node: 00002AEE (Phase ++)
    $ C1S2Phase = C1S2Phase + 1

    if judge_lm_condition([]):
        jump block_000002BB

    return

label block_000002BB:
    # Node: 000002BB (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#0000FF}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000002B9

    return

label block_000002B9:
    # Node: 000002B9 (Atrium 翼 waiting)
    $ sys_lm_menu_item = [{"pos": (216, 160),"image": "images/Chapter 1/Menu/Tsubasa waiting.png","hover": "","name": "つばさ"}, {"pos": (488, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "食堂へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_240
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_000002BA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"食堂へ\"" }]):
        jump block_00003650
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000365D

    return

label block_000002BA:
    # Node: 000002BA (Waiting: 翼)
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#0000FF}事件{/color}{color=#0080FF}。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_000002B9

    return

label block_00003650:
    # Node: 00003650 (TO: Canteen)

    if judge_lm_condition([]):
        jump block_000001D9

    return

label block_000001D9:
    # Node: 000001D9 (Canteen)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ set_place_title(_("食堂"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D138810390DC4843A14969EAD39A7E06 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1QKimuraConference == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "(QKimuraCheck1 == True) or ((TalkKimura > 0) and (TalkItou > 0))" },{ "scope": 4, "content": "(TalkKatou > 0) or (C1S1 == True)" },{ "scope": 5, "content": "TalkMatsuta > 0" },{ "scope": 5, "content": "C1QMatsuta == True" }]):
        jump block_00002433
    if judge_lm_condition([]):
        jump block_000001DA

    return

label block_00002433:
    # Node: 00002433 (Canteen 木村 Quest)
    $ sys_lm_menu_item = [{"pos": (224, 171),"image": "images/Chapter 1/Menu/Itou.png","hover": "images/Chapter 1/Menu/Itou hover.png","name": "伊藤"}, {"pos": (401, 171),"image": "images/Chapter 1/Menu/Kimura quest.png","hover": "images/Chapter 1/Menu/Kimura hover.png","name": "木村"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_241
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003659
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" },{ "scope": 1, "content": "TalkItou == 1" }]):
        jump block_00000203
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_00002437
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_00000204

    return

label block_00000203:
    # Node: 00000203 (伊藤2)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_DAF577AE15B54B01B826DA420FA601F3 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "伊藤君……{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "是喜欢木村君的对不对？"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8C50A460376E499AA9615F303B3DB388 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……啊？"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_970622185A434FF2976149E41E96C746 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦！什么什么，伊藤酱喜欢我吗？"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_EB587B314B504381BB95D97D5A8F8D13 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……啊！？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "因为，看脸都看出来了。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3BF16D57945F4C8CBB2F523666761C2A as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦，看出来了看出来了！\n各种都出来了呐！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对对！\n肯定想着木村君的事情出来了很多呐♪"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_970622185A434FF2976149E41E96C746 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊哈哈！\n是嘛是嘛想着我出来了啊♪{w}\n……嗯？{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_4DE5F061AA4C4CCEB9BE0190BB384A12 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "出来什么？"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_0BE2302CEC694D7C8D324A696BFCA3DF as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_59AAF132B57B402BB1B9171904F5D5B2

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "闭嘴你们两个下流胚子！！！"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00000236

    return

label block_00000236:
    # Node: 00000236 (T ++)
    $ TalkItou = TalkItou + 1

    if judge_lm_condition([{ "scope": 0, "content": "C1QKimuraConference == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "(QKimuraCheck1 == True) or ((TalkKimura > 0) and (TalkItou > 0))" },{ "scope": 4, "content": "(TalkKatou > 0) or (C1S1 == True)" },{ "scope": 5, "content": "TalkMatsuta > 0" },{ "scope": 5, "content": "C1QMatsuta == True" }]):
        jump block_0000364E
    if judge_lm_condition([]):
        jump block_0000364F

    return

label block_0000364E:
    # Node: 0000364E (BACK: Canteen 木村 [quest])

    if judge_lm_condition([]):
        jump block_00002433

    return

label block_0000364F:
    # Node: 0000364F (BACK: Canteen)

    if judge_lm_condition([]):
        jump block_000001DA

    return

label block_000001DA:
    # Node: 000001DA (Canteen)
    $ sys_lm_menu_item = [{"pos": (224, 171),"image": "images/Chapter 1/Menu/Itou.png","hover": "images/Chapter 1/Menu/Itou hover.png","name": "伊藤"}, {"pos": (401, 171),"image": "images/Chapter 1/Menu/Kimura.png","hover": "images/Chapter 1/Menu/Kimura hover.png","name": "木村"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_242
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003657
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" },{ "scope": 1, "content": "TalkKimuraQKimuraConferenceAfter == True" }]):
        jump block_00002531
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" },{ "scope": 1, "content": "TalkItouKimuraF1After == True" }]):
        jump block_000023C0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" },{ "scope": 1, "content": "TalkItouKimuraF1After == True" }]):
        jump block_000023BF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" },{ "scope": 1, "content": "TalkKimura == 0" }]):
        jump block_000001EA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_000001EB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" },{ "scope": 1, "content": "TalkItou == 0" }]):
        jump block_000001EC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" },{ "scope": 1, "content": "TalkItou == 1" }]):
        jump block_00000203
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_00000204

    return

label block_00003657:
    # Node: 00003657 (TO: Atrium)

    if judge_lm_condition([]):
        jump block_000001BE

    return

label block_00002531:
    # Node: 00002531 (木村 討論會后)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_970622185A434FF2976149E41E96C746 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "下次再发现什么有趣的话题\n我还会来邀请你的，敬请期待♪"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00002B7A

    return

label block_00002B7A:
    # Node: 00002B7A (END: TQAfter)
    $ TalkKimuraQKimuraConferenceAfter = False

    if judge_lm_condition([]):
        jump block_000001DA

    return

label block_000023C0:
    # Node: 000023C0 (木村 F1后)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_4DE5F061AA4C4CCEB9BE0190BB384A12 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000303

    return

label block_00000303:
    # Node: 00000303 (F1后)
    window show

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_970622185A434FF2976149E41E96C746 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呀～！说起来，之前那次相扑真有意思啊。"

    show rs_image_4DE5F061AA4C4CCEB9BE0190BB384A12 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "至今为止一直都没怎么关注过\n没想到会是那么热火朝天的运动呢。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F545EFD7951F4AFBA32D8E45B4637B84 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不知道我们学校有没有相扑部呢。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_98C2C24E953445198A40684A013F0B21 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "唉，三分钟热度来了。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_04998E6592264885AC6A22BDA4356C9C as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "只是关注一下又怎么了？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_67E4971422B24DE799679E73FB92C9E9 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，不过，真要认真练习相扑的话，\n就必须得大量吃饭了啊。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_DAF577AE15B54B01B826DA420FA601F3 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "能说服自己放弃很好很好。\n那这个话题就到此为止了。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect3_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_1DC618E301ED42AE8435A9DEA16D134F as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "不过——体型就算稍微变一变也……"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_8C50A460376E499AA9615F303B3DB388 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "不行！！\n你现在的记录正是因为有那个体型才能保持的！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_6F0457CF971A41C6A1377D79409ED847 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "体型有那么重要么？"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_8C50A460376E499AA9615F303B3DB388 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "当然！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_1D1AEEF7C80944B1B7C5C659B6D536B7 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "什么啊！不要被外表迷惑稍微看看内在啊！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_98C2C24E953445198A40684A013F0B21 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "你除了身体百无一用！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_EA782FC000374B07BEA222220CA187A0 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "果然目标只有身体！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_0BE2302CEC694D7C8D324A696BFCA3DF as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "就是……啊！{w=0.6}{nw}"
    show rs_image_EB587B314B504381BB95D97D5A8F8D13 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……嗯？{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_8F501730CFAF4308B1049AEC8D3A5425 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "才不是啊——！"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00002B79

    return

label block_00002B79:
    # Node: 00002B79 (END: TF1After)
    $ TalkItouKimuraF1After = False
    $ QKimuraCheck1 = True

    if judge_lm_condition([{ "scope": 0, "content": "C1QKimuraConference == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "(QKimuraCheck1 == True) or ((TalkKimura > 0) and (TalkItou > 0))" },{ "scope": 4, "content": "(TalkKatou > 0) or (C1S1 == True)" },{ "scope": 5, "content": "TalkMatsuta > 0" },{ "scope": 5, "content": "C1QMatsuta == True" }]):
        jump block_0000364E
    if judge_lm_condition([]):
        jump block_0000364F

    return

label block_000023BF:
    # Node: 000023BF (伊藤 F1后)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_DAF577AE15B54B01B826DA420FA601F3 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000303

    return

label block_000001EA:
    # Node: 000001EA (木村1)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_4DE5F061AA4C4CCEB9BE0190BB384A12 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_2D674881A534447B9AF06131704236BA as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呜……想吃黄金巧克力面包了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "食堂还有卖剩下的，去买不就好了嘛。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1D1AEEF7C80944B1B7C5C659B6D536B7 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "就是因为不能那么做才麻烦啊。\n我现在被管理着饮食啊。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，为什么？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_67E4971422B24DE799679E73FB92C9E9 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "马上就要到田径大赛了，为了这个，\n社团的经理说必须要控制每天摄入的能量总量。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "要是吃了那个肯定就超了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸、欸……听起来好辛苦呐。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_52F8E79C8A9549B188223DE9EB49A240 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "算是。不过也多亏那家伙在好好管着，\n记录也越来越好了，每天也都不错。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "所以还是要听。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～！好能干的经理哦！\n很了解木村君的样子呐。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_970622185A434FF2976149E41E96C746 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "吼吼，是足以自豪的经理呐。\n不如说，没有他我都活不下去了。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8F501730CFAF4308B1049AEC8D3A5425 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "（呜……！说得太容易让人高兴了啊混蛋……！）"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00000235

    return

label block_00000235:
    # Node: 00000235 (T ++)
    $ TalkKimura = TalkKimura + 1

    if judge_lm_condition([{ "scope": 0, "content": "C1QKimuraConference == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "(QKimuraCheck1 == True) or ((TalkKimura > 0) and (TalkItou > 0))" },{ "scope": 4, "content": "(TalkKatou > 0) or (C1S1 == True)" },{ "scope": 5, "content": "TalkMatsuta > 0" },{ "scope": 5, "content": "C1QMatsuta == True" }]):
        jump block_0000364E
    if judge_lm_condition([]):
        jump block_0000364F

    return

label block_000001EB:
    # Node: 000001EB (木村２)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    window show

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_3BF16D57945F4C8CBB2F523666761C2A as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "知道吗？伊藤按摩超级好的。"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那种“按摩”？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F545EFD7951F4AFBA32D8E45B4637B84 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊？为什么我必须要和伊藤做那种事啊？"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "被反驳了——"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_000001DA

    return

label block_000001EC:
    # Node: 000001EC (伊藤1)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_DAF577AE15B54B01B826DA420FA601F3 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_98C2C24E953445198A40684A013F0B21 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "真是的。木村那家伙又烦又笨……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可是，木村君很有意思呐——{w}\n之前也对{color=#008080}内裤的必要性{/color}进行了一番演说。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_E6C646B587CB46D6B05E2FC1653A8460 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5DDCA804AACB4D00B21AA1E39B724318 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯……那种笨蛋的地方也不能说不好。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "运动神经也很棒呐。\n腿也很长，很帅哦！不愧是田径部！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_95DA5CFF311F453F891E89555974D709 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯……是很长。……唔。是很好……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "而且也很受欢迎呢。\n之前已经听过一些传闻了。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CC2DE2777A2C4FBD87EAF461C8DC516E as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "那当然……因为实际上就是很帅……\n很有魅力……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_0BE2302CEC694D7C8D324A696BFCA3DF as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "可这也太窝火了！！！\n{w=0.2}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "木村可是有那么重要的恋人的！！\n{w=0.2}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "再怎么单相思也根本没有结果啊——！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "伊、伊藤君？？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5DDCA804AACB4D00B21AA1E39B724318 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_710A38AC94C841779DB701B5AC1010FD "…………唉……"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00000236

    return

label block_00000204:
    # Node: 00000204 (伊藤3)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    window show

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_054756984B214AAA9B500BCABA1123A4 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "之前的训练对一年级来说好像太严峻了。\n下次换个计划好了……"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "C1QKimuraConference == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "(QKimuraCheck1 == True) or ((TalkKimura > 0) and (TalkItou > 0))" },{ "scope": 4, "content": "(TalkKatou > 0) or (C1S1 == True)" },{ "scope": 5, "content": "TalkMatsuta > 0" },{ "scope": 5, "content": "C1QMatsuta == True" }]):
        jump block_00002433
    if judge_lm_condition([]):
        jump block_000001DA

    return

label block_00002437:
    # Node: 00002437 (木村討論會)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_3BF16D57945F4C8CBB2F523666761C2A as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦，森海！今天放学后有空吗？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，有空哦。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_98C2C24E953445198A40684A013F0B21 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "这个笨蛋聚集了一堆人想要讨论什么。\n很抱歉不过，能稍微陪陪他嘛？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "讨论？不明觉厉，OK——！"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    pause 1

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_EB8CA9E15D764183BA75236D61684ECB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}{color=#FFFF00}{b}～{/b}{/color}{/size}{size=28}{color=#FFFF00}木村的热血讨论室{/color}{/size}{size=28}{color=#FFFF00}{b}～{/b}{/color}{/size}\n{size=15}{color=#00FFFF}〈{/color}{/size}{color=#00FFFF}主持{/color}{size=15}{color=#00FFFF}〉{/color}{/size}{color=#00FFFF}木村树·伊藤圭 {/color}{size=15}{color=#00FFFF}〈{/color}{/size}{color=#00FFFF}嘉宾{/color}{size=15}{color=#00FFFF}〉{/color}{/size}{color=#00FFFF}森海友・松田健治・加藤准太{/color}{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    extend "今日主题{color=#FF0000}{b}『{/b}{/color}{color=#FF0000}明天世界就要完蛋，你该怎么做？{/color}{color=#FF0000}{b}』{/b}{/color}"

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.8

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_6342DEF8AE284F3280186A636EF8A454 as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_81D16F74A3C44B8982DB528D7D934850 "世界要完蛋啊。{w}\n谁知道……做什么好呢。"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_C7BD395661A249B48A9120BE7F9AC4F9 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_710A38AC94C841779DB701B5AC1010FD "这个极端点说，不考虑顺序\n只要想做的都做不就好了。"

    show rs_image_D225376486A6442D884B00D8B01FDB1E as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "放任欲望的意思？"

    show rs_image_4E4E0F803024464E912750289454A1EB as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "不，那种时候都不知道还\n存不存在能保持理性和矜持的人呢。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_9DC44CEC18594661A7F03686A1C49222 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "肯定没——了！就是那种平时喜欢装帅的人，\n到那时候才会原形毕露。"

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    show rs_image_92C5205651224F16BC4611B909FE784D as tag_724406A84D7141298EFF0D864FAE1534 at left_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "话不能说死。比如，国外的一些死刑犯\n到最后好像会被允许选自己喜欢吃的东西。"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "大快朵颐的人存在，平凡度日的也有，\n将不满埋藏心底的人自然也是有的。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_73489888E4784BB98C0E83EB8D2833A2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸——！多浪费啊——！！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_00E7E377A7304AEDB8426852161513BB as tag_0999797A178545CBA5F244F41BBA50B1 at Transform(xpos=280, yalign=0.0) zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "一般的食物还是有些舍不得呐。{w}\n而且我也觉得并不是一切都能用金钱来衡量。"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_655BD81414F14C09820C0C956BC1B072 as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=80, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "确实吃饭很重要。既然都这样了还是想吃好吃的呢。"

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    show rs_image_8EC686D1582347F8BE3714C4E440B250 as tag_724406A84D7141298EFF0D864FAE1534 at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "对了，这个话题的前置条件是世界要毁灭的话，\n这件事只有我们知道？"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_ED3D215EBC5348549E07BFC8DFA439FA as tag_2C4A74BADF6540698EF3E9A300893D1A at Transform(xpos=460, yalign=0.0) zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊……还没想到那么远。"
    show rs_image_BBA07E7007074DFD973384E84E8918AC as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "要是所有人都知道，\n就会出现为所欲为的罪犯和无法地带了呢。"

    show rs_image_F333E5317DFA468389E2DA087896D09E as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "不如说可能会对世界将要终结感到不安，\n结果最后根本没人敢做也说不定……"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.9

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_30000B766B004F74B2F293CE6ED27616 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……。那个，大家好像讨论地很起兴不过，\n这里更应该正视我们自身的需求。"

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Thunder 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Thunder 1.ogg"

    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_44331B79D1D84C7EAA35F0480004721A

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=28}{color=#FF0080}就是说！！肯定是要获得最棒的快感！！{/color}{/size}"

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_1439FC37B6EB4D19A2C3CA56559E02E4 as tag_724406A84D7141298EFF0D864FAE1534 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    show rs_image_F333E5317DFA468389E2DA087896D09E as tag_0999797A178545CBA5F244F41BBA50B1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_90E48F9CDC734D43AD577A32B4E6F01F as tag_61A891D6A6D047DC93695DA12E13CC75 at center_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.3

    rs_character_8173A72D925D4405AFE69DD1932DD4B5 "……。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_ED3D215EBC5348549E07BFC8DFA439FA as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.55

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_C0C28FE32BFE40499B29AC9C92887630 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_E3F6ADD43DE44A428E1224756613C694 "我明白的——！！我一直在等有人说出这句话啊！"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_376CA53D8BF64CE497CF774B53A38857 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "因为，都已经最后了啊！？"
    show rs_image_A6B4348D830149E99506A5D175DCF690 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "我的话，\n首先要得到最强的电摩，嗡嗡嗡嗡嗡……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_1439FC37B6EB4D19A2C3CA56559E02E4 as tag_724406A84D7141298EFF0D864FAE1534 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    show rs_image_F333E5317DFA468389E2DA087896D09E as tag_0999797A178545CBA5F244F41BBA50B1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_90E48F9CDC734D43AD577A32B4E6F01F as tag_61A891D6A6D047DC93695DA12E13CC75 at center_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_173B284E6DC843AF812C237128860894 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯，我同意班长的意见。……不过电摩就算了。"

    show rs_image_AD0A1253421A4619B2C6792B88C585C3 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "最后还是想和喜欢的……在一起呐。"

    show rs_image_00E7E377A7304AEDB8426852161513BB as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_710A38AC94C841779DB701B5AC1010FD "喜欢的人……嗯，那也很幸福。真的很想这样呢。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_4E4E0F803024464E912750289454A1EB as tag_0999797A178545CBA5F244F41BBA50B1 at Transform(xpos=280, yalign=0.0) zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_29B8A648E5754D2CB7C3C7D85E72E60B as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=80, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_818F9A26E3D54B498441E21C54E5B868 as tag_724406A84D7141298EFF0D864FAE1534 at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    show rs_image_AA33B0FCE2BC4F429904AEEE5D417557 as tag_2C4A74BADF6540698EF3E9A300893D1A at Transform(xpos=460, yalign=0.0) zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_E3F6ADD43DE44A428E1224756613C694 "我不管喜不喜欢都要先干为敬呐——♪啊哈哈♪"

    if sys_effect2_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    show rs_image_70599C5025FC45F69279010EDB3E637D as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "木・村……！"

    show rs_image_B37B38F0EAF54165807FC3B0DED8A099 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "难得要做，能在对方家里偷偷做就好了呢。"

    show rs_image_D809612C8CDB4FB284662AAF7934647E as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "我个人喜欢质量优秀的Love Hotel。床大，洗澡也方便。"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.9

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.4

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "刺激过头了！但真想来一次啊——！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就是就是！光是在网上看看就已经把持不住了！"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "果然最后还是推心置腹地满足性欲最好啊。想要一场浸彻骨髓的H啊。"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "你的话太没品了……只是在按照自己的趣味随便想象而已。"

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_37DF69F2B47C45148B6FB8E9B2E339C5 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_EB8CA9E15D764183BA75236D61684ECB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.3

    rs_character_710A38AC94C841779DB701B5AC1010FD "……不知何时已经完全变成黄段子讨论会了。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=280, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_173B284E6DC843AF812C237128860894 as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=90, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_8EC686D1582347F8BE3714C4E440B250 as tag_724406A84D7141298EFF0D864FAE1534 at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    show rs_image_BBA07E7007074DFD973384E84E8918AC as tag_2C4A74BADF6540698EF3E9A300893D1A at Transform(xpos=450, yalign=0.0) zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_9697147E2D9E441DB1D27E2722186CE4 "……。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_37DA1327FE694B62941F0E61C338883A as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "所以说♪伊藤酱也来……"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_37DF69F2B47C45148B6FB8E9B2E339C5 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔……"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_D474DA018EE64BEABBA0AEC9825003C3 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "好了好了！这次讨论会到此结束！\n谢谢大家参与——！"

    window hide

    pause 0.9

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 2.5

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00002B29

    return

label block_00002B29:
    # Node: 00002B29 (C1Q木村討論)
    $ C1QKimuraConference = True
    $ TalkKimuraQKimuraConferenceAfter = True

    if judge_lm_condition([]):
        jump block_00002438

    return

label block_00002438:
    # Node: 00002438 (QUEST FINISH)
    $ set_window("(標準)")
    if sys_effect2_current_file != "sound/BGM/Quest Finished.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_effect2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 1

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"


    if judge_lm_condition([]):
        jump block_00003652

    return

label block_00003652:
    # Node: 00003652 (TO: School outside)

    if judge_lm_condition([]):
        jump block_0000368D

    return

label block_0000020A:
    # Node: 0000020A (Atrium empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (488, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "食堂へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_243
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000365D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"食堂へ\"" }]):
        jump block_00003650

    return

label block_000001C8:
    # Node: 000001C8 (Atrium)
    $ sys_lm_menu_item = [{"pos": (216, 160),"image": "images/Chapter 1/Menu/Tsubasa.png","hover": "images/Chapter 1/Menu/Tsubasa hover.png","name": "つばさ"}, {"pos": (488, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "食堂へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_244
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003652
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"食堂へ\"" }]):
        jump block_00003650
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "TalkTsubasaQTsubasaAfter == True" }]):
        jump block_00000218
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "TalkTsubasaF1After == True" }]):
        jump block_00002394
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "TalkTsubasaF4After == True" }]):
        jump block_0000243A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "TalkTsubasa == 0" }]):
        jump block_00002B3C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "C1S5 == True" },{ "scope": 2, "content": "FTheater == True" }]):
        jump block_00002B59
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "C1S5 == True" },{ "scope": 2, "content": "FTheater == False" }]):
        jump block_00002B57
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_0000243B

    return

label block_00000218:
    # Node: 00000218 (翼 Q翼后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_28D96DBE93084DC9AD60894E8FC483ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_212D585BC6E244759D9630EB4060376C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君，上次的事情非常感谢。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没什么没什么，不客气！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可是，技安那家伙，\n连道谢都不说，把自己当什么了～{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "真是的！是我们特地去找他的好不好！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F5C2E50E1E4840E8BC325EAA4E4AEC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那个……感谢至少还是说过的……"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是吗？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BE3262D8C1FD4E1984FB548E18E6ACBD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可能被友君的声音盖住了，但好好说过的哦。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……诶，是吗。……嗯，是嘛……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002B33

    return

label block_00002B33:
    # Node: 00002B33 (END: TQAfter)
    $ TalkTsubasaQTsubasaAfter = False

    if judge_lm_condition([]):
        jump block_0000365C

    return

label block_0000365C:
    # Node: 0000365C (BACK: Atrium)

    if judge_lm_condition([]):
        jump block_0000365B

    return

label block_0000365B:
    # Node: 0000365B (BACK: Atrium)

    if judge_lm_condition([]):
        jump block_000001C8

    return

label block_00002394:
    # Node: 00002394 (翼 F1后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_28D96DBE93084DC9AD60894E8FC483ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_0A69793B0E914340A7F1125C52EBD5E3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君，\n上次的相扑大赛『{color=#FF8000}陆田＆杉本{/color}』也来了哦！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你是他们的粉丝？有去要签名吗？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A6DDCE105645457E8367570AA224AC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我没敢去……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈哈！不过，翼君竟然会喜欢他们两个，\n还真是口味特殊……"

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不如说，是变态！！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C28B56D29C43417B9BBE638780F0BBA8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不是的！"

    show rs_image_38AA851595944792BBBFDDE6AAD59E92 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "确实他们下流梗很多，经常挑战播放底线……\n偶尔也有不太和谐的场景，\n但我只是单纯对尼咲出身的艺人有所期待……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "尼咲？我记得翼君住在伊丹咲哦。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3E5246A6872C4ED9A1B378593AEDFD83 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不要在意细节！{w}\n总之，他们很擅长炒热气氛，说话也很有趣。"

    show rs_image_0085117794E34261AF1F405901BFDB33 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "比如之前那个{color=#0080FF}『激烈的场景』{/color}\n他们也给出了比同龄人更成熟的意见！{w}\n友君也请一定要看。"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦、哦……。{w}\n总觉得翼君意外地热衷于他们呐。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002B30

    return

label block_00002B30:
    # Node: 00002B30 (END: TF1After)
    $ TalkTsubasaF1After = False

    if judge_lm_condition([]):
        jump block_0000365C

    return

label block_0000243A:
    # Node: 0000243A (翼 F4后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_28D96DBE93084DC9AD60894E8FC483ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_8093AAE5FCA745689AF6ACB12D446D8D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……友、友君。那个，我有想要商量的事……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么了？\n总觉得又回到刚认识翼君的时候的样子了\n那种阴暗不安的感觉。"

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Bell 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bell 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Bell 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君相信{color=#808000}“二重身”{/color}吗？"

    if sys_music2_current_file != "sound/BGM/Theme/Schoolboys Theme - Fear.ogg":
        play music2 "sound/BGM/Theme/Schoolboys Theme - Fear.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Theme/Schoolboys Theme - Fear.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "“二重身”？记得是会出现和自己一模一样的人，\n如果遇到了就会发生不好的事情的样子？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我觉得幽灵很恐怖也觉得会有，\n但这种都市传说就不怎么相信了——"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_28D96DBE93084DC9AD60894E8FC483ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "最、最近经常听说有人\n在附近看到和我长得一样的别人。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "只是长得像而已？"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0DCBE3E54DA04EED9BEEBD9CDC472CCA as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可、可是，\n和{color=#808000}“那个”{/color}说过话的人告诉我，\n对方也自称为“翼”！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸、欸……其实他们说的就是翼君本人，\n只是你没有发觉而已？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0085117794E34261AF1F405901BFDB33 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不可能！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0C5FA214E7144FE595B8249FC3C15A38 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "再、再说了，我……{w}\n{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_3E5246A6872C4ED9A1B378593AEDFD83 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    extend "我怎么可能会对别人说\n{color=#FF00FF}『汪汪！抱抱！舔舔？』{/color}这种话！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_09DC5387CE03499E9DEA97A2FD00B581 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜——好可怕——！！如何是好友君！！\n如果真的遇到了该如何是好——！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "冷、冷静下来！没关系！\n二重身什么的不存在的！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就算真的有你面前这位\n友超人也会用电摩把对方打倒的！{w}\n所以，嗯！放心。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A6DDCE105645457E8367570AA224AC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……呜……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002B31

    return

label block_00002B31:
    # Node: 00002B31 (END: TF4After)
    $ TalkTsubasaF4After = False

    if judge_lm_condition([]):
        jump block_0000365C

    return

label block_00002B3C:
    # Node: 00002B3C (T ++)
    $ TalkTsubasa = TalkTsubasa + 1

    if judge_lm_condition([]):
        jump block_000001E8

    return

label block_000001E8:
    # Node: 000001E8 (翼 １)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_28D96DBE93084DC9AD60894E8FC483ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀吼——！翼啾！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F5C2E50E1E4840E8BC325EAA4E4AEC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友、友君。早上好。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说起来，夏天买的那件连帽衫\n在学校里居然也穿着呐！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C1F34699FB3045D39ED696A2EFA86072 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸、嗯。\n毕竟是{color=#008080}友君好不容易买来{/color}的。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_5D7907F2DDBC44E9BE62B714F22A194A as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是嘛是嘛！不过啊，制服和连帽衫啊。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "搭配起来好像也很时髦呐。我也想试试。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_212D585BC6E244759D9630EB4060376C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那下次我买来给友君做礼物好了？"

    show rs_image_9E93048B179C4AE4A728558A93AF24A4 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这件衣服绝对是友君穿起来更合适。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我会再去伊丹咲的商店街买回来的。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶！真的！？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "……啊，不过，那就变成情侣装了呐。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_FC1EB697877A47FE9D35ED5FD247302D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸？……啊……！\n{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_2A874B8169574EC78181A7EC6887E271 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "是、是的……唔……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……其实我并……可……"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "很羞耻的样子果然算了～！\n连帽衫角色就交给翼了～"

    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_38AA851595944792BBBFDDE6AAD59E92 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……呜。好、好的……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "明白了……谢谢给我这个特权……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "C1S2 == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "TalkTsubasa > 0" }]):
        jump block_000002B7
    if judge_lm_condition([]):
        jump block_0000365B

    return

label block_00002B59:
    # Node: 00002B59 (翼 Theater前)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3E5246A6872C4ED9A1B378593AEDFD83 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那个！\n{w=0.5}{nw}"
    show rs_image_38AA851595944792BBBFDDE6AAD59E92 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    show rs_image_F5C2E50E1E4840E8BC325EAA4E4AEC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "现、现在伊丹咲的电影院里\n好像有上映怀旧电影的活动……"

    show rs_image_3A2AAC3AE4294D82A6AD4C2DE8D96EDC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "似乎会上映以前流行过的电影……\n所、所以……"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_0085117794E34261AF1F405901BFDB33 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可、可以的话，下次我们可以一起去吗！？"

    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#FF0000}事件回想模式{/color}{color=#0080FF}可以使用了。\n在本章结束前只要和翼说一下话就可以前去观看。』{/color}"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002B5B

    return

label block_00002B5B:
    # Node: 00002B5B (Cancel: First)
    $ FTheater = False
    $ persistent.SystemStoryCache[17] = True

    if judge_lm_condition([]):
        jump block_0000365C

    return

label block_00002B57:
    # Node: 00002B57 (Theater)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_212D585BC6E244759D9630EB4060376C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "要、要一起去看电影吗？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002B5A

    return

label block_00002B5A:
    # Node: 00002B5A (選擇)
    call scb_selector("", [{"name":"はい", "content":_("一起去吧，翼君")}, {"name":"いいえ", "content":_("稍等现在有点事")}]) from _call_scb_selector_24

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002B58
    if judge_lm_condition([]):
        jump block_0000365B

    return

label block_00002B58:
    # Node: 00002B58 (Theater)
    call block_0000213F from _call_block_0000213F_1

    if judge_lm_condition([]):
        jump block_0000365D

    return

label block_0000243B:
    # Node: 0000243B (翼2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_2A874B8169574EC78181A7EC6887E271 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我还想和{color=#008080}上次那样{/color}和友君\n一起去伊丹咲看电影……{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_2DD27A73E9554BD28B842D191657C5BC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！下次也要一起哦！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9E93048B179C4AE4A728558A93AF24A4 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哇——♪"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000001C8

    return

label block_00003667:
    # Node: 00003667 (TO: Gym outside)

    if judge_lm_condition([]):
        jump block_000001BD

    return

label block_000001BD:
    # Node: 000001BD (Gym outside)
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

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1S1 == True" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase == 0" },{ "scope": 3, "content": "C1QMatsuta == False" },{ "scope": 0, "content": "C1QMatsutaPhase == 1" }]):
        jump block_000023B6
    if judge_lm_condition([]):
        jump block_000001C7

    return

label block_000023B6:
    # Node: 000023B6 (Gymoutside +泉)
    $ sys_lm_menu_item = [{"pos": (464, 208),"image": "images/Chapter 1/Menu/Sato.png","hover": "images/Chapter 1/Menu/Sato hover.png","name": "佐藤"}, {"pos": (255, 208),"image": "images/Chapter 1/Menu/Izumi Gym outside.png","hover": "images/Chapter 1/Menu/Izumi Gym outside hover.png","name": "泉"}, {"pos": (91, 263),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "体育館"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_245
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館\"" },{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        jump block_000023BC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"佐藤\"" }]):
        jump block_000023B7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_000023B8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館\"" }]):
        jump block_00002B3D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003666

    return

label block_000023BC:
    # Node: 000023BC (Gym Q松田)
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "必须尽快找到阿月！"

    window hide

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000023B6

    return

label block_000023B7:
    # Node: 000023B7 (佐藤 F1后Q松田前)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 300
    show rs_image_C8A74E1418F4431CAD466A4648F12769 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_bottom zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "我说～你们班那个和你一样的金发同学。"

    rs_character_EA9AA88E88D84B559B925363E2931756 "一股想要干架的气场，\n根本不敢接近。赶快处理掉好吗。"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000023B6

    return

label block_000023B8:
    # Node: 000023B8 (泉 F1后Q松田前)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_E3970153CCFF43E18D64269F143A17AC as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_58FAE766750B4FF09356905A1635623E as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "森、森海君，那个啊。\n松田君好像受到了什么刺激的样子，\n一副十足的侵略姿态。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！那个平时不生气\n一生气就要吓死人的松田大哥！？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "……啊，泉君也是这个类型的呐。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_10019DFD6098404AAC11A841C63592E9 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "是吗？没这回事。\n{w=0.55}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_2F8031BCAB5944949065FE7A21AAC2E3 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不对，重点不是这个！"

    show rs_image_58FAE766750B4FF09356905A1635623E as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "他到底遇到什么了。森海君知道嘛？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不，完全不知道。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    extend "好、好的，作为班长\n不能坐视不管，去看看样子好了！"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000023B6

    return

label block_00002B3D:
    # Node: 00002B3D (Gym)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("体育馆"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_24188CBA120A4166B08F8A3535548A8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000023B9

    return

label block_000023B9:
    # Node: 000023B9 (Gym 松田 quest)
    $ sys_lm_menu_item = [{"pos": (432, 202),"image": "images/Chapter 1/Menu/Matsuta quest.png","hover": "images/Chapter 1/Menu/Matsuta quest hover.png","name": "松田"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_246
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_000023BA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000001BD

    return

label block_000023BA:
    # Node: 000023BA (松田 QUEST)
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A6FC16AAA33445118AFB5AFC737B8AF6 as tag_724406A84D7141298EFF0D864FAE1534 at center_bottom zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "班长，能把赤峰大哥叫来不。{w}\n……他不在的话，身上实在是疼很难受啊。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！？几个意思！？"

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A6FC16AAA33445118AFB5AFC737B8AF6 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "行了快去！！{w}……不然\n{w=0.5}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_EC8B6F3950E8418D8EBA9EF12D2BF7BD as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "就只好先{color=#FF0000}上{/color}班长了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫！……啊，不过像松田亲这样\n有男子气概的类型我说不定可以接受。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E9F1E0F2938347FA9642D7E4902E028B as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "哦——哦。我其实还挺重口的。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shock 1.ogg"

    show rs_image_EC8B6F3950E8418D8EBA9EF12D2BF7BD as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    extend "说不定班长玩着玩着就坏了呐。"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那、那种程度的话……{w}\n开、开玩笑的——！我马上就去找他来——！"

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_00002B24

    return

label block_00002B24:
    # Node: 00002B24 (Phase ++)
    $ C1QMatsutaPhase = C1QMatsutaPhase + 1

    if judge_lm_condition([]):
        jump block_000023BB

    return

label block_000023BB:
    # Node: 000023BB (QUEST START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托已经开始，请达成目标。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_000001BD

    return

label block_00003666:
    # Node: 00003666 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003664

    return

label block_000001C7:
    # Node: 000001C7 (Gym outside)
    $ sys_lm_menu_item = [{"pos": (168, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "体育館へ"}, {"pos": (416, 208),"image": "images/Chapter 1/Menu/Sato.png","hover": "images/Chapter 1/Menu/Sato hover.png","name": "　佐藤"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_247
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003666
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" }]):
        jump block_000001CD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"　佐藤\"" },{ "scope": 1, "content": "TalkSatou == 0" }]):
        jump block_000001ED
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"　佐藤\"" }]):
        jump block_00000200

    return

label block_000001CD:
    # Node: 000001CD (Gym)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("体育馆"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_24188CBA120A4166B08F8A3535548A8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000001CE

    return

label block_000001CE:
    # Node: 000001CE (Gym)
    $ sys_lm_menu_item = [{"pos": (226, 206),"image": "images/Chapter 1/Menu/Izumi.png","hover": "images/Chapter 1/Menu/Izumi hover.png","name": "泉"}, {"pos": (432, 202),"image": "images/Chapter 1/Menu/Matsuta.png","hover": "images/Chapter 1/Menu/Matsuta hover.png","name": "松田"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_248
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000001BD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" },{ "scope": 1, "content": "C1QMatsuta == True" }]):
        jump block_00002B2E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" },{ "scope": 1, "content": "TalkMatsuta == 0" }]):
        jump block_000001D0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_00000202
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" },{ "scope": 1, "content": "TalkIzumi == 0" }]):
        jump block_000001D1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_00000201

    return

label block_00002B2E:
    # Node: 00002B2E (松田 Q松田后)
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    show rs_image_A41E22CFB21F498984105511F0EE3963 as tag_724406A84D7141298EFF0D864FAE1534 at center_bottom zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的啦松田亲！\n刚才为什么要说那么奇怪的话！\n手腕相扑什么的我还是第一次听说——"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E9F1E0F2938347FA9642D7E4902E028B as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "还不是怪你想歪了。{w}\n{nw}"
    show rs_image_468376D97672421A9188EDE9BC95F19B as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过，拜此所赐轻松了。谢了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "手腕相扑啊——好久没试过了呐。\n呐——呐——我们也来一次——"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E9F1E0F2938347FA9642D7E4902E028B as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "我是没问题。\n{w=0.45}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_EC8B6F3950E8418D8EBA9EF12D2BF7BD as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "不过，班长可能就真会玩坏了也说不定。"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 2.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 300
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊呜……松田亲的这种抖S发言\n都快变成日常用语了……"

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_000001CE

    return

label block_000001D0:
    # Node: 000001D0 (松田1)
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_A41E22CFB21F498984105511F0EE3963 as tag_724406A84D7141298EFF0D864FAE1534 at center_bottom zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀吼～松田亲！在做什么呐～？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E9F1E0F2938347FA9642D7E4902E028B as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "陪泉练习排球。被拜托托球给他了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好厉害——！\n松田亲是篮球部的，排球也会呐！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A41E22CFB21F498984105511F0EE3963 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "不不，我只是单纯在向上投球罢了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～！好好哦——好有意思哦～！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2BF6BDCB640D42DD9E7AF5597B9D2073 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "班长要不也来试着打一下？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！可以吗！？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E9F1E0F2938347FA9642D7E4902E028B as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "如何，泉？\n稍微休息一下也没什么问题对不。"

    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_2082061F6BDE4DF0BDF5D7B9C19EA314 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "嗯，可以哦。让我们看看森海君的帅气之处。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    show rs_image_383A8F3374EB4B9180BB664B451D8AF0 as tag_724406A84D7141298EFF0D864FAE1534 at center_bottom zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "好。上了，班长！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    extend "……看好！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好——！给你们看看班长的实力……{w}\n{nw}"
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    if sys_effect_current_file != "sound/Effect Sound/Hit 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊呜！！"

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2F8031BCAB5944949065FE7A21AAC2E3 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "还、还好吗森海君！？"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_11D00458AF904FB288048FBD22D87F55 as tag_724406A84D7141298EFF0D864FAE1534 at center_bottom zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "好、好一记脸面接球……{w}\n{nw}"
    show rs_image_65F293BE15B44EBD948D31F80A79EED3 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……至少也该锻炼锻炼了班长。"

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_0000022F

    return

label block_0000022F:
    # Node: 0000022F (T ++)
    $ TalkMatsuta = TalkMatsuta + 1

    if judge_lm_condition([]):
        jump block_000001CE

    return

label block_00000202:
    # Node: 00000202 (松田2)
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_74683F1B7537443795430EB9D51FB743 as tag_724406A84D7141298EFF0D864FAE1534 at center_bottom zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "下次找绫濑帮忙锻炼一下肌肉好了。\n也不能就这么不管体育祭。"

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_000001CE

    return

label block_000001D1:
    # Node: 000001D1 (泉1)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_E3970153CCFF43E18D64269F143A17AC as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_58FAE766750B4FF09356905A1635623E as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "说起来，我听到了一个可怕的传闻……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可、可怕的传闻……？\n（吞口水）……内、内容是？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1A01B77F792B4D8796C8F3BEBCCD1AE5 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "在御咲学园内，在我们看不到的地方，\n似乎为了某个原因张贴了大量的{color=#808000}符咒{/color}。"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{color=#808000}符{/color}、{color=#808000}符咒{/color}！？{w}\n就是说……我们学校会出来“那个”……？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_58FAE766750B4FF09356905A1635623E as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "……嗯。特别是进校门直走后\n最里面的地方目击情报最多。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔、唔哇～感觉还是别去比较好……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2F8031BCAB5944949065FE7A21AAC2E3 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "……{size=28}啊！{/size}"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫！？什什什什么！？\n别在说这种话题的时候突然喊出来！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_58FAE766750B4FF09356905A1635623E as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "说起来，刚想起来还有个恐怖的传闻……\n就在森海君家的附近，真的没发生过什么？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜？具、具体是什么？"

    show rs_image_1A01B77F792B4D8796C8F3BEBCCD1AE5 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "……就是之前也说过一次的那个。"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "{color=#008A45}每夜每夜都传出嗡嗡嗡的怪声{/color}……{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_7FCA15C0B2C84011B631FEE225910744 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜哇啊啊啊啊啊！！\n快停下！！会睡不着觉的！！"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_00000230

    return

label block_00000230:
    # Node: 00000230 (T ++)
    $ TalkIzumi = TalkIzumi + 1

    if judge_lm_condition([]):
        jump block_000001CE

    return

label block_00000201:
    # Node: 00000201 (泉2)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_10019DFD6098404AAC11A841C63592E9 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "对不起刚才吓到你了。{w}\n友君家附近的怪声肯定是谁听错了。"

    show rs_image_2082061F6BDE4DF0BDF5D7B9C19EA314 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "只是普通的机械的声音而已啦。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_000001CE

    return

label block_000001ED:
    # Node: 000001ED (佐藤1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 300
    show rs_image_B83B13B3FF8B473D901C95E73D036252 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_bottom zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_FB0B40FA12DF419499F7A4CD22541DB0 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_EA9AA88E88D84B559B925363E2931756 "呜～全身都湿透了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么了？佐藤君。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_52DA2DC477DA4AA6B9083C9822781AEE as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "刚才在体育馆里陪泉他们练习排球了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～!\n明明所属文化部，还真能跟上运动部的练习呐。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C8A74E1418F4431CAD466A4648F12769 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "不要小看吹奏乐部啊。\n这边在平时也是会练习肌肉力量的。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——！会练习肌肉啊。\n对哦，吹奏乐器的话必须要用腹肌呢。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_FB0B40FA12DF419499F7A4CD22541DB0 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "因为是需求体力的，所以一开始以为自己能轻松适应{w}\n……结果说是这么说……"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_533EC8AF3B8E46B8B4710A88A3D6D107 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "做不到呢☆哈哈♪"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这什么反应！？"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000233

    return

label block_00000233:
    # Node: 00000233 (T ++)
    $ TalkSatou = TalkSatou + 1

    if judge_lm_condition([]):
        jump block_000001C7

    return

label block_00000200:
    # Node: 00000200 (佐藤2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_B83B13B3FF8B473D901C95E73D036252 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_bottom zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "佐藤君是吹奏乐部的吧？\n和钢琴不同，要让管乐发出声音很麻烦呐。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E357CD4CCB104112BFEBBC268303BA79 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "那当然，不过要领也是有的。"

    if sys_effect2_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A3EBA4BF0CB64E3BA61DEA35EBFF919F as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "慎重的轻覆嘴唇，不要太用力轻轻咬住，\n掌握好力度的话……"
    show rs_image_533EC8AF3B8E46B8B4710A88A3D6D107 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "就可以发出很愉悦的声音了哦♪"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇哦♂听起来好刺激！！\n佐藤君不会是因为这个才～！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_FF952E710E414E64B2C43251843AB9D8 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "你猜。"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000001C7

    return

label block_00003649:
    # Node: 00003649 (TO: Schoolhouse)

    if judge_lm_condition([]):
        jump block_00002B22

    return

label block_00002B22:
    # Node: 00002B22 (Random)
    $ QNewsclubRandom = Random(5)

    if judge_lm_condition([{ "scope": 0, "content": "C1QNewsclubPhase == 1" },{ "scope": 1, "content": "QNewsclubRandom == 0" }]):
        jump block_000024BF
    if judge_lm_condition([]):
        jump block_000001BF

    return

label block_000024BF:
    # Node: 000024BF (新聞部任務)
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

    $ set_place_title(_("校舍内"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    pause 0.5

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    stop music fadeout 3
    $ sys_music_current_file = ""

    pause 0.8

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Grass 1.ogg"

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 200
    show rs_image_466219A035C44D62AD2743E9F494A2F2 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    pause 0.1

    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "发、发现了！！\n新闻部那些人说的{color=#FF0000}巨大蚯蚓{/color}！！"

    window hide

    pause 0.2

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0B29D260FA114D6EB90FB552C6296007 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 200
    show rs_image_FBB2DF0BB74746A29EA713F11F92C1A4 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_15C167A596C24CA5ABBDDF10433FFF71

    pause 0.3

    show rs_image_5171C4277664485482367CFD06553623 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "看来这确实是个不为人知的好地方。\n今天的每日新午餐就是你了。"

    show rs_image_A7C4CBC5126342CD8A04FA3A8072EE5F as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "平日我们总是要定量摄入“精”的，\n如果不能按时的话……！"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哇！？哇啊啊啊啊！！！"

    window hide

    pause 0.4

    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_BAF3BF757577455980E802743F48D2F9

    pause 2.5

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我来汇报了……"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_80DDCB83351245C2B44A943AC22567CC as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "找到巨大蚯蚓了啊！！辛苦了辛苦了！\n那事不宜迟快说说怎么回事！"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜呜！！\n太羞耻了才不要说！\n已经嫁不出去了！呜哇——！！"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_754768FC78144F46AE18D7308D963DB6 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "嗯，和其他目击者一样的反应。\n部长，这件事就到此为止。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_560D536F2A06470C856E0D5C0557DCFB as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "诶？为、为何！？"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_2EA64D401901409BB55B0E9A1C850EB4 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "继续深究部长的安全无法被保证。"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我是小白鼠啊——！！讨厌——！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_90849C45A28049C88275551685CD545A as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "不要激动，森海同学。\n这次非常感谢，{w}来，这是报酬。"

    window hide

    pause 0.2

    if sys_effect2_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Decision 1.ogg"

    # Gallery unlock: images/CG/Newsclub/Newsclub 1.png
    $ zorder_rs_image_267F041B536640EA86097324E1BF5809 = -100
    show rs_image_267F041B536640EA86097324E1BF5809 as rs_image_267F041B536640EA86097324E1BF5809 zorder zorder_rs_image_267F041B536640EA86097324E1BF5809 onlayer master
    hide rs_image_267F041B536640EA86097324E1BF5809

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_CC4336DE74164173AC47C2C317367F10
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_267F041B536640EA86097324E1BF5809 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.4

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『获得了“{/color}{u}{color=#00FFFF}大家一起踢足球{/color}{/u}{color=#00FFFF}”时的照片』{/color}"

    window hide

    pause 0.3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_window("(標準)")
    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_90849C45A28049C88275551685CD545A as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "今后再有什么问题时也请来帮助我们。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_00002B23

    return

label block_00002B23:
    # Node: 00002B23 (C1Q新聞部)
    $ C1QNewsclub = True
    $ C1QNewsclubPhase = 0

    if judge_lm_condition([]):
        jump block_000024C0

    return

label block_000024C0:
    # Node: 000024C0 (QUEST FINISH)
    if sys_effect2_current_file != "sound/BGM/Quest Finished.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_effect2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.8


    if judge_lm_condition([]):
        jump block_000001DC

    return

label block_000001DC:
    # Node: 000001DC (Newsclub)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (112, 160),"image": "images/Chapter 1/Menu/Okajima.png","hover": "images/Chapter 1/Menu/Okajima hover.png","name": "岡島"}, {"pos": (392, 160),"image": "images/Chapter 1/Menu/Kojima.png","hover": "images/Chapter 1/Menu/Kojima hover.png","name": "小島"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_249
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000001B7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" },{ "scope": 1, "content": "TalkOkajima == 0" }]):
        jump block_000001EE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_00000214
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" },{ "scope": 1, "content": "C1QNewsclubPhase == 1" }]):
        jump block_000024BC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_000001EF

    return

label block_000001B7:
    # Node: 000001B7 (Aisle 2)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("二楼走廊"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000001C1

    return

label block_000001C1:
    # Node: 000001C1 (Aisle 2)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (152, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "踊り場へ"}, {"pos": (376, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "新聞部へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_250
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003790
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部へ\"" },{ "scope": 1, "content": "C1QNewsclubPhase == 1" }]):
        jump block_000024BD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部へ\"" },{ "scope": 1, "content": "FNewsclub == True" }]):
        jump block_00002B20
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部へ\"" }]):
        jump block_000001DB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"踊り場へ\"" },{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        jump block_000023BD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"踊り場へ\"" }]):
        jump block_000001DF

    return

label block_00003790:
    # Node: 00003790 (TO: School inside)

    if judge_lm_condition([]):
        jump block_0000378A

    return

label block_0000378A:
    # Node: 0000378A (TO: School inside)

    if judge_lm_condition([]):
        jump block_000001B3

    return

label block_000001B3:
    # Node: 000001B3 (School inside)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([{ "scope": 0, "content": "C1QTsubasaPhase == 1" }]):
        jump block_00000227
    if judge_lm_condition([{ "scope": 0, "content": "C1QSabushinPhase == 1" }]):
        jump block_00000228
    if judge_lm_condition([]):
        jump block_000018C0

    return

label block_00000227:
    # Node: 00000227 (友+翼)
    $ sys_ayumi_global_map_character = "tomo_tsubasa"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_00000223

    return

label block_00000223:
    # Node: 00000223 (School inside XCTA)
    if judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00001FD9", target_label="block_00000D34") from _call_scb_global_map_46
    elif judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00001FD9", target_label="block_00002B14") from _call_scb_global_map_47
    elif judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00001FD9", target_label="block_00002B1B") from _call_scb_global_map_48
    elif judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00001FD9", target_label="block_00002B26") from _call_scb_global_map_49
    elif judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B13", target_label="block_00000D34") from _call_scb_global_map_50
    elif judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B13", target_label="block_00002B14") from _call_scb_global_map_51
    elif judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B13", target_label="block_00002B1B") from _call_scb_global_map_52
    elif judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B13", target_label="block_00002B26") from _call_scb_global_map_53
    elif judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B1C", target_label="block_00000D34") from _call_scb_global_map_54
    elif judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B1C", target_label="block_00002B14") from _call_scb_global_map_55
    elif judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B1C", target_label="block_00002B1B") from _call_scb_global_map_56
    elif judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B1C", target_label="block_00002B26") from _call_scb_global_map_57
    elif judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B25", target_label="block_00000D34") from _call_scb_global_map_58
    elif judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B25", target_label="block_00002B14") from _call_scb_global_map_59
    elif judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B25", target_label="block_00002B1B") from _call_scb_global_map_60
    elif judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00002B25", target_label="block_00002B26") from _call_scb_global_map_61
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1S1Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_000002B1", target_label="block_00000D34") from _call_scb_global_map_62
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_000002B1", target_label="block_00002B14") from _call_scb_global_map_63
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_000002B1", target_label="block_00002B1B") from _call_scb_global_map_64
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_000002B1", target_label="block_00002B26") from _call_scb_global_map_65
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_0000368B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00003680
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_0000368C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00003682
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00003681
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_000038FB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00000223
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1S1Phase == 1" }]):
        jump block_00001FD9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1S1Phase == 1" }]):
        jump block_00000D34
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00000225
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" },{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        jump block_00001FE1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        jump block_00002B13
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        jump block_00002B14
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" },{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        jump block_00001FE3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        jump block_00002B1C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FDF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        jump block_00002B25
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000002B1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        jump block_00002B1B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1QMatsutaPhase == 1" }]):
        jump block_00002B26

    return

label block_0000368B:
    # Node: 0000368B (TO: Aisle 2)

    if judge_lm_condition([]):
        jump block_000001B7

    return

label block_00003680:
    # Node: 00003680 (TO: Roof)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"


    if judge_lm_condition([]):
        jump block_000001B8

    return

label block_000001B8:
    # Node: 000001B8 (Roof)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("屋顶"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "QSabushinCheck1 == True" },{ "scope": 0, "content": "C1QSabushinPhase == 1" },{ "scope": 0, "content": "C1SSabuShin == True" },{ "scope": 0, "content": "C1QSabuShin == True" },{ "scope": 1, "content": "C1S5 == False" }]):
        jump block_000001F3
    if judge_lm_condition([{ "scope": 0, "content": "CXQSabuImechen == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_00002490
    if judge_lm_condition([]):
        jump block_000001C2

    return

label block_000001F3:
    # Node: 000001F3 (Roof empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_251
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003788

    return

label block_00003788:
    # Node: 00003788 (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003789

    return

label block_00003789:
    # Node: 00003789 (TO: School inside)

    if judge_lm_condition([]):
        jump block_0000378C

    return

label block_0000378C:
    # Node: 0000378C (TO: School inside)

    if judge_lm_condition([]):
        jump block_0000378B

    return

label block_0000378B:
    # Node: 0000378B (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003790

    return

label block_00002490:
    # Node: 00002490 (Roof 三朗 quest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (264, 160),"image": "images/Chapter 1/Menu/Saburo quest.png","hover": "images/Chapter 1/Menu/Saburo hover.png","name": "三朗"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_252
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_0000243F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003790

    return

label block_0000243F:
    # Node: 0000243F (三朗美髮店 1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_66CC7FF4E6344DE0A8CBE2F3E7675375 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_E03E986EBB4A47EF85860F9FB78E124A as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那个，白痴呆毛～♪{w}\n有件事想拜托你，能听听不～？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么——什么事——？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_104E19984CF747D19D3CC74E9452E4A0 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "给我弄弄……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呃、呃？"

    if sys_effect2_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shock 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F5BAF97AB91D4DFEACDC49C6844D1D26 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_A465618EE34C429AB8E4349BD1A608E4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=28}把你头发拿来给我弄弄——！！！{/size}"

    window hide

    pause 0.7

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    pause 1.4


    if judge_lm_condition([]):
        jump block_0000248B

    return

label block_0000248B:
    # Node: 0000248B (三朗美髮店)
    call block_00001194 from _call_block_00001194_1

    if judge_lm_condition([]):
        jump block_0000377F

    return

label block_0000377F:
    # Node: 0000377F (RESET)
    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"


    if judge_lm_condition([]):
        jump block_000001B8

    return

label block_000001C2:
    # Node: 000001C2 (Roof)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (264, 160),"image": "images/Chapter 1/Menu/Saburo.png","hover": "images/Chapter 1/Menu/Saburo hover.png","name": "三朗"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_253
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003788
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" },{ "scope": 1, "content": "C1QSabuShin == False" },{ "scope": 2, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 3, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 4, "content": "C1S4 == True" }]):
        jump block_000001F1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" },{ "scope": 1, "content": "C1QSabuShin == True" },{ "scope": 2, "content": "C1S5 == True" }]):
        jump block_00000212
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" },{ "scope": 1, "content": "CXQSabuImechen == True" }]):
        jump block_0000248C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_00002B44

    return

label block_000001F1:
    # Node: 000001F1 (三朗 F4后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_EAAD2B6A3763430786077CA6C12B7E2A as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呜哇！？吓死我了，原来是白痴呆毛……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "猫君反应过头了——发生什么了？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_47DEDE6C50774E7AA3ACCB5ACA319820 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "没什么。{w}还以为是那个\n{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    extend "{size=24}{color=#FF8000}超中学级的変态{/color}{/size}又来了……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说的是慎酱～？怎么了？\n你们关系不是很好么？"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_515C31BD831E4F5BA5F55CD785018663 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "什！？你犯什么病才会看出我们关系好的！！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "因为，慎酱一直都把猫君叫做\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "{color=#FF80FF}“我的老婆”{/color}的说……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "所以……欸？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "你们没在交往？"

    if sys_effect2_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shock 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_A465618EE34C429AB8E4349BD1A608E4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我勒个去！！？\n森海友，恐怖的孩子……！\n这孩子知道自己在说什么不……！？"

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "别胡说了！！怎么可能！！！{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    extend "我、是男人！！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    extend "他，也是男人！！！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——意外地对细节较真呐。\n那种事情根本不用在意——"

    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我们学校同性伴侣也很多了哦？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1A6F637D49AE4DFF8256CCDEC309830C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊——我听不见。什么都听不见。{w}\n……就这样，我走了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶，去做什么？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F5BAF97AB91D4DFEACDC49C6844D1D26 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "上次{color=#008080}在屋顶被袭击{/color}的事件，\n已经把这里变成了危险地带。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_8D6A1C60E37148BBA1537D1AB135E100 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "需要寻找其他没人的好地方了。{w}\n{nw}"
    show rs_image_3D12230112CC4ABBBDFBD0F285452ECF as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哦，对了，校庭的{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#0080C0}那个地方{/color}不错……。"

    show rs_image_E311DFB1888B4C95A25E0CEFD38FB26F as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "再见，白痴呆毛，\n记得务必修好你脑袋里关于情侣定义的故障。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "男女之间没那么多莫名其妙的事。"

    window hide

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.6

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_place_title(_("屋顶"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002B16

    return

label block_00002B16:
    # Node: 00002B16 (Q三慎Check1)
    $ QSabushinCheck1 = True

    if judge_lm_condition([]):
        jump block_000001F3

    return

label block_00000212:
    # Node: 00000212 (三朗 Q三慎F5后)
    $ set_window("イベントモード")
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 1.3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_AE31149E5F7F4DC79066D77A5F625EC2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "白痴呆毛，上次你还真干得出来。\n又导致我的安息之地沦陷了一块。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_AE31149E5F7F4DC79066D77A5F625EC2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_8A80B90628C143D1B3A53C71240BBE2D as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊哈哈，对不起～\n不过，猫君也不是完全不愿意对不对？"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_742789FF7438418190F3D785A3C01259 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "怎么可能！{w}过来受罚，白痴呆毛！\n过来好好让我放松放松！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！！不、不要～！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_91A1C69307F54C4B9424B1859222EE6F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊～轻松了～舒服了～\n简直就和逗猫草一样，欲罢不能啊～"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……呜呜。"
    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    extend "……呼——呼——"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "等、等等！不要这么抓着睡过去啊～！"

    window hide

    pause 0.4

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D6BC962AE17948D893E50BE9B4670973

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_2304A61C05D54DD6B9E15DDB5A3D3949 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-140, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……找～到了。"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_507130D7BD574651B179D6DEF2CE814D = 100
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_507130D7BD574651B179D6DEF2CE814D at center_bottom zorder zorder_tag_507130D7BD574651B179D6DEF2CE814D onlayer master
    show rs_image_093624408E4A49609F348CA15F58D0F1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=320, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    hide tag_507130D7BD574651B179D6DEF2CE814D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫！慎、慎酱！不是的，事情不是你想的那样！！"

    show rs_image_4E534C3CC3ED418EA9C8155C87F1BCBB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……屋顶要上演修罗场了！\n我谁的孩子都没怀～！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D54E703CD633470FAE473BD8F3BE65FA as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "行了行了，不要擅自把剧情导向鲜血的始末！\n那是翼亲那种角色的事。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……不过，也……{w=0.3}{nw}"
    show rs_image_D89F5A4866AB4F38AE527F438BA0139B as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "是呐。"

    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "？？也？"

    window hide

    pause 0.6

    # Gallery unlock: images/CG/The truth of Shintarou 1.png
    $ zorder_rs_image_8A9A9C995593446F8C7F1623E032EB67 = -100
    show rs_image_8A9A9C995593446F8C7F1623E032EB67 as rs_image_8A9A9C995593446F8C7F1623E032EB67 zorder zorder_rs_image_8A9A9C995593446F8C7F1623E032EB67 onlayer master
    hide rs_image_8A9A9C995593446F8C7F1623E032EB67

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_8A9A9C995593446F8C7F1623E032EB67 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.9

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "总觉得，有些难以接受呢。我还是很嫩啊。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……呐呐，慎酱为什么会对猫君这么在意？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯——我自己的情报可是很贵的哦，这位先生。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "通融一下嘛！\n就当是之前带你去猫君那里的谢礼好了！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯……也行。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "一开始，只是觉得在这种环境下仍然没弯的三酱很可爱，\n想要进一步了解，都是好奇心和恶作剧……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "本是这样的，不知何时……{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "也许我是专攻直男的类型～！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "又在插科打诨了！\n慎酱一直都在说别人的事，很少关注自己呐。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "在别人看来，\n慎酱对猫君的态度和热情可是和对其他人完全不同的。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……慎酱对猫君是……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "稍等——！后面的部分说太早了。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "尤其是你这种像是文字冒险游戏主人公\n一样迟钝的更没的说！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？刚才说什么了？"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦，突发性失聪……不愧是主角。{w}\n……算了，我也没有说别人的立场。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说什么奇怪的事情呐——慎酱好怪。\n吃错什么东西了？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼，也许真是。{w}弄醒三酱就不好了，\n我先回去了。再见～"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "保重～拜拜。"

    window hide

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真的走了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "……{w=0.4}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    extend "你。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    # Gallery unlock: images/CG/The truth of Shintarou 2.png
    $ zorder_rs_image_D9FF8323B07F4CB09838C9DC0E934C20 = -100
    show rs_image_D9FF8323B07F4CB09838C9DC0E934C20 as rs_image_D9FF8323B07F4CB09838C9DC0E934C20 zorder zorder_rs_image_D9FF8323B07F4CB09838C9DC0E934C20 onlayer master
    hide rs_image_D9FF8323B07F4CB09838C9DC0E934C20

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_D9FF8323B07F4CB09838C9DC0E934C20 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "！！起、起来了？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "当然。那么大声怎么睡得着。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……一直抓着你的头发抱歉，我要走了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？或许不该我说不过，你完全没睡？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦。早就不想睡了。{w}\n{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_ADA1B960ED91494FBBB6C932EDEE1BAC as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    pause 0.4

    extend "……再见。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_80AC1FBCF08D4C6283030181039745BE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，等等，猫君！"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_1209D298FCAF4E62993FA6F9C54C9FCE as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "咋了？"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "也没那么不情愿对不对？"

    show rs_image_81339CBB1684406EB266897AD5F0330B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    show rs_image_ADA1B960ED91494FBBB6C932EDEE1BAC as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "怎么可能啊笨蛋。"

    window hide

    pause 0.8

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 1.4


    if judge_lm_condition([]):
        jump block_00002B2D

    return

label block_00002B2D:
    # Node: 00002B2D (C1S三慎)
    $ C1SSabuShin = True

    if judge_lm_condition([]):
        jump block_00003788

    return

label block_0000248C:
    # Node: 0000248C (三朗美髮店 2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_66CC7FF4E6344DE0A8CBE2F3E7675375 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "要转换形象么？"

    window hide

    $ set_place_title(_("屋顶"))
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_0000248D

    return

label block_0000248D:
    # Node: 0000248D (選擇)
    call scb_selector("", [{"name":"はい", "content":_("换！换！我要换！")}, {"name":"いいえ", "content":_("容我三思")}]) from _call_scb_selector_25

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_0000248E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_000001C2

    return

label block_0000248E:
    # Node: 0000248E (PREPAR)
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 1


    if judge_lm_condition([]):
        jump block_0000248B

    return

label block_00002B44:
    # Node: 00002B44 (三朗美髮店前)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_E03E986EBB4A47EF85860F9FB78E124A as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那个啊白痴呆毛～♪{w}\n有件事想让你干～……"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "抱歉，现在正忙！下次好了！"

    if sys_effect3_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_26EB8B8FF5BF411DBA453A1E92ADF479 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸——！……算了，等会记得回来啊。"

    window hide

    $ set_place_title(_("屋顶"))
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000001C2

    return

label block_0000368C:
    # Node: 0000368C (TO: Music room)

    if judge_lm_condition([]):
        jump block_000001B9

    return

label block_000001B9:
    # Node: 000001B9 (Music room)
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

    $ set_place_title(_("音乐室"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1S5Phase == 1" }]):
        jump block_000023C8
    if judge_lm_condition([{ "scope": 0, "content": "F5Check1 == True" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000007E9
    if judge_lm_condition([{ "scope": 0, "content": "QTsubasaCheck1 == True" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000001FB
    if judge_lm_condition([]):
        jump block_000001C3

    return

label block_000023C8:
    # Node: 000023C8 (Music room 忍 waiting)
    $ sys_lm_menu_item = [{"pos": (176, 288),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "ピアノ"}, {"pos": (496, 184),"image": "images/Chapter 1/Menu/F5/Shinobu waiting.png","hover": "","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_254
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000023C3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ピアノ\"" }]):
        jump block_000001E4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000038FA

    return

label block_000023C3:
    # Node: 000023C3 (Waiting: 忍)
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#3A00C4}事件{/color}{color=#0080FF}。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_000023C8

    return

label block_000001E4:
    # Node: 000001E4 (選擇)
    call scb_selector("", [{"name":" 演奏しない", "content":_("不想弹")}, {"name":"演奏する", "content":_("弹")}]) from _call_scb_selector_26

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"演奏する\"" },{ "scope": 1, "content": "F5Check1 == False" },{ "scope": 2, "content": "QTsubasaCheck1 == False" },{ "scope": 3, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 4, "content": "C1QTsubasaPhase + C1QSabushinPhase == 0" },{ "scope": 5, "content": "C1SG1 and C1S4 == True" },{ "scope": 6, "content": "C1S5 == False" },{ "scope": 5, "content": "C1QTsubasa == False" }]):
        jump block_00003996
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"演奏する\"" }]):
        jump block_0000023B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \" 演奏しない\"" },{ "scope": 1, "content": "C1S5Phase == 1" }]):
        jump block_000023C8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \" 演奏しない\"" },{ "scope": 1, "content": "F5Check1 == True" },{ "scope": 2, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 3, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 4, "content": "C1SG1 and C1S4 == True" }]):
        jump block_000007E9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \" 演奏しない\"" },{ "scope": 1, "content": "QTsubasaCheck1 == True" },{ "scope": 2, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 3, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000001FB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \" 演奏しない\"" }]):
        jump block_000001C3

    return

label block_00003996:
    # Node: 00003996 (1)
    window hide

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    pause 0.3

    if sys_music2_current_file != "sound/Piano/sti_gymno_01_pi.ogg":
        play music2 "sound/Piano/sti_gymno_01_pi.ogg" noloop
        $ sys_music2_current_file = "sound/Piano/sti_gymno_01_pi.ogg"

    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    show rs_image_94349C8B6C544C10904538FB25DCF572 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2EA8313137C646C685870CF29BCA70C5

    $ zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF = 200
    show rs_image_84F2702404A44AD5A80F28C1E0B77466 as tag_C34E445E70F4457D90AA6C86C64AF3DF at center_bottom zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_D15BB5FFD7EA4F438E7C40A8CB14E35D as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_FDF70B8E22CF4041A27D7412B58243B1 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3

    show rs_image_30D02984B514490284A3FB9E03A86AA3 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3

    show rs_image_8F4EC829E56A41B8BECF49AE2C3BE294 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    show rs_image_E3E21AE1BD2041BCBCDD8137D674DBA2 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_2747F5BE2B9349B3B578D3F290C8626F as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    show rs_image_7BBF189B287443198DF66375A8BA6633 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    hide tag_C34E445E70F4457D90AA6C86C64AF3DF
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    pause 0.4

    show rs_image_94349C8B6C544C10904538FB25DCF572 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2EA8313137C646C685870CF29BCA70C5

    $ reverse_volume("music", 1)

    if judge_lm_condition([]):
        jump block_000001E3

    return

label block_000001E3:
    # Node: 000001E3 (Selector)

    if judge_lm_condition([{ "scope": 0, "content": "C1S5Phase == 1" }]):
        jump block_000023C8
    if judge_lm_condition([{ "scope": 0, "content": "F5Check1 == True" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "C1SG1 and C1S4 == True" }]):
        jump block_000007E9
    if judge_lm_condition([{ "scope": 0, "content": "QTsubasaCheck1 == True" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000001FB
    if judge_lm_condition([{ "scope": 0, "content": "C1S5 == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "C1SG1 and C1S4 == True" }]):
        jump block_000023C7
    if judge_lm_condition([{ "scope": 0, "content": "C1QTsubasa == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000001FC
    if judge_lm_condition([]):
        jump block_000001C3

    return

label block_000007E9:
    # Node: 000007E9 (Music room 忍 flag)
    $ sys_lm_menu_item = [{"pos": (176, 288),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "ピアノ"}, {"pos": (496, 184),"image": "images/Chapter 1/Menu/F5/Shinobu flag.png","hover": "images/Chapter 1/Menu/F5/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_255
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000023C5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ピアノ\"" }]):
        jump block_000001E4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000038FA

    return

label block_000023C5:
    # Node: 000023C5 (F5: 忍)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1BB16A3232D24A24A336EB3F36D6DBE2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_53AE820BA9E64560B2C6D962DEE9DD33 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦，对，说起来今天社团没活动。\n那干脆一起回去好了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦♪第二学期第一次！\n可以哦，当然要一起回去——！{w}\n要不要绕道去玩？"

    show rs_image_5028F6B94B4B4BC883B88492AB07115E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯——没什么必要。{w}\n不过去友的家还是可以的。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00002B0B

    return

label block_00002B0B:
    # Node: 00002B0B (Phase ++)
    $ C1S5Phase = C1S5Phase + 1

    if judge_lm_condition([]):
        jump block_000023C4

    return

label block_000023C4:
    # Node: 000023C4 (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#3A00C4}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_000023C8

    return

label block_000038FA:
    # Node: 000038FA (TO: School inside)

    if judge_lm_condition([]):
        jump block_000038F6

    return

label block_000038F6:
    # Node: 000038F6 (TO: School inside)

    if judge_lm_condition([]):
        jump block_0000378B

    return

label block_000001FB:
    # Node: 000001FB (Music room 翼 quest)
    $ sys_lm_menu_item = [{"pos": (176, 288),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "ピアノ"}, {"pos": (496, 184),"image": "images/Chapter 1/Menu/Tsubasa music room quest.png","hover": "images/Chapter 1/Menu/Tsubasa music room hover.png","name": "つばさクエスト"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_256
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000038FA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさクエスト\"" }]):
        jump block_000001FE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ピアノ\"" }]):
        jump block_000001E4

    return

label block_000001FE:
    # Node: 000001FE (翼 QUEST)
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_28D96DBE93084DC9AD60894E8FC483ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？呐，翼君。\n{w=0.3}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    extend "手上那张纸是什么呐～？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0A69793B0E914340A7F1125C52EBD5E3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸，啊，这个？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这是……老师说要把这个交给体育委员……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊～是不是体育祭的事？\n我们班好像也拿到了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "二班的体育委员是谁？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3A2AAC3AE4294D82A6AD4C2DE8D96EDC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……作、作哉君……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫！？那个坏心眼技安！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_28D96DBE93084DC9AD60894E8FC483ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "等下必须交给他不可……{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_A6DDCE105645457E8367570AA224AC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……呜。可我被他讨厌着……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w=0.3}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "决定了！我和你一起去！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "要是只有翼君一个人肯定会被欺负的。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "就让我作为守护神护卫在旁！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C1F34699FB3045D39ED696A2EFA86072 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哈哈，友君就像神明一样呐。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不过……对我来说……或许真是……{w}\n{nw}"
    show rs_image_BE3262D8C1FD4E1984FB548E18E6ACBD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "谢谢，这下就能安心了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！那么，我们走！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("音乐室"))

    if judge_lm_condition([]):
        jump block_00002B11

    return

label block_00002B11:
    # Node: 00002B11 (Phase ++)
    $ C1QTsubasaPhase = C1QTsubasaPhase + 1

    if judge_lm_condition([]):
        jump block_000001FD

    return

label block_000001FD:
    # Node: 000001FD (QUEST START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托已经开始，请达成目标。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_000001C3

    return

label block_000001C3:
    # Node: 000001C3 (Music room)
    $ sys_lm_menu_item = [{"pos": (176, 288),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "ピアノ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_257
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000038FA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ピアノ\"" }]):
        jump block_000001E5

    return

label block_000001E5:
    # Node: 000001E5 (Piano)
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『要弹钢琴么？』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_000001E4

    return

label block_000023C7:
    # Node: 000023C7 (忍 F5前)
    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_8468BF81A4B147BCB4EA3E30BCD79AD5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "打扰了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欢迎光临，忍——有何贵干？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1BB16A3232D24A24A336EB3F36D6DBE2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，没什么。\n只是偶尔想听听钢琴读读书。{w}\n继续演奏就好。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00002B09

    return

label block_00002B09:
    # Node: 00002B09 (F5Check1)
    $ F5Check1 = True

    if judge_lm_condition([]):
        jump block_000007E9

    return

label block_000001FC:
    # Node: 000001FC (翼 Q翼前)
    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    pause 0.8

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，是翼君——！"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_F5C2E50E1E4840E8BC325EAA4E4AEC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "你、你好。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好呀～今天也来了呐～♪"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C1F34699FB3045D39ED696A2EFA86072 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯、嗯。弹得太出色，被吸引过来了。\n友君真的钢琴弹得好棒呐。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈，多谢多谢～"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("音乐室"))
    pause 0.3


    if judge_lm_condition([]):
        jump block_00000241

    return

label block_00000241:
    # Node: 00000241 (Q翼Check1)
    $ QTsubasaCheck1 = True

    if judge_lm_condition([]):
        jump block_000001FB

    return

label block_0000023B:
    # Node: 0000023B (Random)
    $ PianoRandom = Random( 4 )

    if judge_lm_condition([{ "scope": 0, "content": "PianoRandom == 0" }]):
        jump block_00003996
    if judge_lm_condition([{ "scope": 0, "content": "PianoRandom == 1" }]):
        jump block_00000240
    if judge_lm_condition([{ "scope": 0, "content": "PianoRandom == 2" }]):
        jump block_000001E6
    if judge_lm_condition([{ "scope": 0, "content": "PianoRandom == 3" }]):
        jump block_000001E7

    return

label block_00000240:
    # Node: 00000240 (2)
    window hide

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    pause 0.3

    if sys_music2_current_file != "sound/Piano/rvl_prelude_pi.ogg":
        play music2 "sound/Piano/rvl_prelude_pi.ogg" noloop
        $ sys_music2_current_file = "sound/Piano/rvl_prelude_pi.ogg"

    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    show rs_image_94349C8B6C544C10904538FB25DCF572 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2EA8313137C646C685870CF29BCA70C5

    $ zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF = 200
    show rs_image_84F2702404A44AD5A80F28C1E0B77466 as tag_C34E445E70F4457D90AA6C86C64AF3DF at center_bottom zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_D15BB5FFD7EA4F438E7C40A8CB14E35D as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_FDF70B8E22CF4041A27D7412B58243B1 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3

    show rs_image_30D02984B514490284A3FB9E03A86AA3 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3

    show rs_image_8F4EC829E56A41B8BECF49AE2C3BE294 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    show rs_image_E3E21AE1BD2041BCBCDD8137D674DBA2 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_2747F5BE2B9349B3B578D3F290C8626F as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    show rs_image_7BBF189B287443198DF66375A8BA6633 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    hide tag_C34E445E70F4457D90AA6C86C64AF3DF
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    pause 0.4

    show rs_image_94349C8B6C544C10904538FB25DCF572 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2EA8313137C646C685870CF29BCA70C5

    $ reverse_volume("music", 1)

    if judge_lm_condition([]):
        jump block_000001E3

    return

label block_000001E6:
    # Node: 000001E6 (3)
    window hide

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    pause 0.3

    if sys_music2_current_file != "sound/Piano/rst_lacam_pi.ogg":
        play music2 "sound/Piano/rst_lacam_pi.ogg" noloop
        $ sys_music2_current_file = "sound/Piano/rst_lacam_pi.ogg"

    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    show rs_image_94349C8B6C544C10904538FB25DCF572 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2EA8313137C646C685870CF29BCA70C5

    $ zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF = 200
    show rs_image_84F2702404A44AD5A80F28C1E0B77466 as tag_C34E445E70F4457D90AA6C86C64AF3DF at center_bottom zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_D15BB5FFD7EA4F438E7C40A8CB14E35D as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_FDF70B8E22CF4041A27D7412B58243B1 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3

    show rs_image_30D02984B514490284A3FB9E03A86AA3 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3

    show rs_image_8F4EC829E56A41B8BECF49AE2C3BE294 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    show rs_image_E3E21AE1BD2041BCBCDD8137D674DBA2 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_2747F5BE2B9349B3B578D3F290C8626F as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    show rs_image_7BBF189B287443198DF66375A8BA6633 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    hide tag_C34E445E70F4457D90AA6C86C64AF3DF
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    pause 0.4

    show rs_image_94349C8B6C544C10904538FB25DCF572 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2EA8313137C646C685870CF29BCA70C5

    $ reverse_volume("music", 1)

    if judge_lm_condition([]):
        jump block_000001E3

    return

label block_000001E7:
    # Node: 000001E7 (4)
    window hide

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    pause 0.3

    if sys_music2_current_file != "sound/Piano/btb_hisou_2_pi.ogg":
        play music2 "sound/Piano/btb_hisou_2_pi.ogg" noloop
        $ sys_music2_current_file = "sound/Piano/btb_hisou_2_pi.ogg"

    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    show rs_image_94349C8B6C544C10904538FB25DCF572 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2EA8313137C646C685870CF29BCA70C5

    $ zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF = 200
    show rs_image_84F2702404A44AD5A80F28C1E0B77466 as tag_C34E445E70F4457D90AA6C86C64AF3DF at center_bottom zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_D15BB5FFD7EA4F438E7C40A8CB14E35D as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_FDF70B8E22CF4041A27D7412B58243B1 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3

    show rs_image_30D02984B514490284A3FB9E03A86AA3 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3

    show rs_image_8F4EC829E56A41B8BECF49AE2C3BE294 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    show rs_image_E3E21AE1BD2041BCBCDD8137D674DBA2 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_2747F5BE2B9349B3B578D3F290C8626F as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    show rs_image_7BBF189B287443198DF66375A8BA6633 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    hide tag_C34E445E70F4457D90AA6C86C64AF3DF
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    pause 0.4

    show rs_image_94349C8B6C544C10904538FB25DCF572 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2EA8313137C646C685870CF29BCA70C5

    $ reverse_volume("music", 1)

    if judge_lm_condition([]):
        jump block_000001E3

    return

label block_00003682:
    # Node: 00003682 (TO: Library)

    if judge_lm_condition([]):
        jump block_000001BA

    return

label block_000001BA:
    # Node: 000001BA (Library)
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

    $ set_place_title(_("图书馆"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "F5Check1 == True" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 0, "content": "C1S5Phase == 1" }]):
        jump block_00002B0A
    if judge_lm_condition([{ "scope": 0, "content": "C1S1Phase == 1" }]):
        jump block_000023AC
    if judge_lm_condition([{ "scope": 0, "content": "C1S1 == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000023AA
    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1SG1 == True" }]):
        jump block_0000119A
    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == True" }]):
        jump block_0000029B
    if judge_lm_condition([]):
        jump block_000001C4

    return

label block_00002B0A:
    # Node: 00002B0A (Library empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_258
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000038F7

    return

label block_000038F7:
    # Node: 000038F7 (TO: School inside)

    if judge_lm_condition([]):
        jump block_000038F6

    return

label block_000023AC:
    # Node: 000023AC (Library 忍 waiting)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 1/Menu/Shinobu waiting.png","hover": "","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_259
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000023AD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000038F6

    return

label block_000023AD:
    # Node: 000023AD (Waiting: 忍)
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#008000}事件{/color}{color=#0080FF}。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_000023AC

    return

label block_000023AA:
    # Node: 000023AA (Library 忍 flag)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 1/Menu/Shinobu flag.png","hover": "images/Chapter 1/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_260
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000038F7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000023A8

    return

label block_000023A8:
    # Node: 000023A8 (Flag: 忍)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1BB16A3232D24A24A336EB3F36D6DBE2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_53AE820BA9E64560B2C6D962DEE9DD33 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说起来{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#0080FF}加藤君{/color}……同班的加藤君\n好像在{color=#008080}校庭{/color}里烦恼什么的样子。"

    show rs_image_A68F7C05F10E4C54B48181328DBE7E00 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "和他谈过一次，但听不明白他想表达什么意思……"

    show rs_image_8468BF81A4B147BCB4EA3E30BCD79AD5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "稍后友也去和他谈谈。拜托了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00002AEB

    return

label block_00002AEB:
    # Node: 00002AEB (Phase ++)
    $ C1S1Phase = C1S1Phase + 1

    if judge_lm_condition([]):
        jump block_000023A9

    return

label block_000023A9:
    # Node: 000023A9 (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#008000}事件{/color}{color=#0080FF}。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_000023AC

    return

label block_0000119A:
    # Node: 0000119A (Library 忍 quest)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 1/Menu/Shinobu quest.png","hover": "images/Chapter 1/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_261
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000023C9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000038F7

    return

label block_000023C9:
    # Node: 000023C9 (小忍問題冊 1)
    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_718B13A73C1D499B8D43BB96215026E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "从刚才开始就一直和我说话……\n到底怎么了？这么想在我身边？"

    show rs_image_7B868F13B2CB4F798DA2E47EBFF0F142 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "真是的。正好看了本问题书，\n就拿来出题好了。"

    show rs_image_C13DBF06A7124E5F9654BEA657DADC36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "有{color=#0080FF}“简单”“一般”“困难”{/color}三种，\n这次就先从{color=#0080FF}“简单”{/color}开始好了。"

    window hide

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000038EC

    return

label block_000038EC:
    # Node: 000038EC (小忍問題冊)
    call block_00003837 from _call_block_00003837_1

    if judge_lm_condition([]):
        jump block_00003925

    return

label block_00003925:
    # Node: 00003925 (RESET)
    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_0000029B

    return

label block_0000029B:
    # Node: 0000029B (Library answer)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 1/Menu/Shinobu.png","hover": "images/Chapter 1/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (152, 128),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "調べる"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_262
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"調べる\"" }]):
        jump block_0000029D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000038F8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        jump block_00000217
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobuF5After == True" }]):
        jump block_000025F5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000002A0

    return

label block_0000029D:
    # Node: 0000029D (Answer)
    $ sys_lm_menu_item = [{"pos": (90, 128),"image": "images/Games/Shinobus-question-set/Easy.png","hover": "images/Games/Shinobus-question-set/Easy hover.png","name": "かんたん"}, {"pos": (490, 128),"image": "images/Games/Shinobus-question-set/Normal.png","hover": "images/Games/Shinobus-question-set/Normal hover.png","name": "ふつう"}, {"pos": (90, 328),"image": "images/Games/Shinobus-question-set/Hard.png","hover": "images/Games/Shinobus-question-set/Hard hover.png","name": "ちょいむず"}, {"pos": (490, 328),"image": "images/Games/Shinobus-question-set/Return.png","hover": "images/Games/Shinobus-question-set/Return hover.png","name": "やめておく"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_263
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"かんたん\"" }]):
        jump block_0000029C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ふつう\"" }]):
        jump block_0000029E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ちょいむず\"" }]):
        jump block_0000029F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"やめておく\"" }]):
        jump block_0000029B

    return

label block_0000029C:
    # Node: 0000029C (1)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    call shinobu_question_answer_sheet_show(0) from _call_shinobu_question_answer_sheet_show_3

    if judge_lm_condition([]):
        jump block_0000029D

    return

label block_0000029E:
    # Node: 0000029E (2)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    call shinobu_question_answer_sheet_show(1) from _call_shinobu_question_answer_sheet_show_4

    if judge_lm_condition([]):
        jump block_0000029D

    return

label block_0000029F:
    # Node: 0000029F (3)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    call shinobu_question_answer_sheet_show(2) from _call_shinobu_question_answer_sheet_show_5

    if judge_lm_condition([]):
        jump block_0000029D

    return

label block_000038F8:
    # Node: 000038F8 (TO: School inside)

    if judge_lm_condition([]):
        jump block_000038F7

    return

label block_00000217:
    # Node: 00000217 (忍 Q翼中)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_1BB16A3232D24A24A336EB3F36D6DBE2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_74FFA1FC7D7C4EDEB7565F683C1767BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_53AE820BA9E64560B2C6D962DEE9DD33 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦，翼君。"

    show rs_image_127AA1B3214F4C9AA59405C6A2B480FE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "绫濑君。那个，你好。"

    show rs_image_74FFA1FC7D7C4EDEB7565F683C1767BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A8343F8158BB4E2885E19013FD4B2809 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你好，我们家的笨蛋真是每次都麻烦你了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么什么——！等下忍——\n为什么要那么说——！"

    show rs_image_127AA1B3214F4C9AA59405C6A2B480FE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "没、没有的事。\n我才是因为友君在所以一直很高兴……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼——！\n就是就是很高兴！"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "只要我在气氛就能活跃！\nYEAH！YEAH！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C13DBF06A7124E5F9654BEA657DADC36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不过有时还是想找个\n安静悠闲的时光呐。"

    show rs_image_9BD621E351A14C56AEDB2731A3325E33 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "所以，翼君，下次\n只有我们两个午休的时候一起如何。"

    show rs_image_127AA1B3214F4C9AA59405C6A2B480FE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸，可、可以吗？{w}\n嗯嗯，谢谢，我还有很多想说的呐。"

    show rs_image_74FFA1FC7D7C4EDEB7565F683C1767BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A8343F8158BB4E2885E19013FD4B2809 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯。我会好好听你对友的抱怨的。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸、欸——！？为何会这样！！\n我也要一起！\n呐——呐——！我也要一起——！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == True" }]):
        jump block_0000029B
    if judge_lm_condition([]):
        jump block_000001C4

    return

label block_000001C4:
    # Node: 000001C4 (Library)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 1/Menu/Shinobu.png","hover": "images/Chapter 1/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_264
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000038F8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "C1QTsubasaPhase == 1" }]):
        jump block_00000217
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobuF5After == True" }]):
        jump block_000025F5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobu == 0" }]):
        jump block_000001CF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobu == 1" }]):
        jump block_000001F5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000001F6

    return

label block_000025F5:
    # Node: 000025F5 (忍 F5后)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1BB16A3232D24A24A336EB3F36D6DBE2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "每年的{color=#A8A800}和好纪念日{/color}都来我家\n一起做饭一起吃饭！\n怎么样嘛，忍♪"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_5028F6B94B4B4BC883B88492AB07115E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "如果记得的话。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……。{w}\n……{w=0.45}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "坦率一些嘛，可爱的小猫猫。"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_28087508A43843469EF6F58EAFE0A5EF as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "什！？"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "♪"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00002B34

    return

label block_00002B34:
    # Node: 00002B34 (END: TF5After)
    $ TalkShinobuF5After = False

    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == True" }]):
        jump block_0000029B
    if judge_lm_condition([]):
        jump block_000001C4

    return

label block_000001CF:
    # Node: 000001CF (忍 1)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1BB16A3232D24A24A336EB3F36D6DBE2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀呀小忍——\n头发也慢慢长回来了呐——\n结果，就那样不管了？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8468BF81A4B147BCB4EA3E30BCD79AD5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯。那也算是某种灾祸了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是嘛是嘛！我觉得那样很好啊！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "短发的忍总觉得有一种敬畏感，\n就像{color=#008080}蛋糕事件{/color}那时一样呐～{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_1FBB6733578646369AA4517D59E88468 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CBA8857325074E53AAED9ECA4918832E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……能打你一顿么？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫！？不、不用了！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2D91E64709AA4233A0D3B0D8F1C52D5B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哼。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "总、总之！忍就和现在一样就好！{w}\n{nw}"
    if sys_effect3_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "很棒很棒的！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_718B13A73C1D499B8D43BB96215026E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "好好，多谢。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过～说起来，\n当时突然就剪成了{color=#008080}那个样子{/color}呢。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_21D4771AEEE64C17B249F0E9F0EA5DEA as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我还以为肯定是受到什么不良朋友的影响了。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DCEACCC9997B48C3B9B0A54DA87D50DC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊、啊哈哈，并不是。{w}\n再说了，那孩子是个好人，气氛也相投。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "……唔、唔——……{w}\n……下次我也要去！很感兴趣！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A8343F8158BB4E2885E19013FD4B2809 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_0000023C

    return

label block_0000023C:
    # Node: 0000023C (T ++)
    $ TalkShinobu = TalkShinobu + 1

    if judge_lm_condition([]):
        jump block_000001C4

    return

label block_000001F5:
    # Node: 000001F5 (忍 2)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1BB16A3232D24A24A336EB3F36D6DBE2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_8468BF81A4B147BCB4EA3E30BCD79AD5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这么一看。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？什么？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_53AE820BA9E64560B2C6D962DEE9DD33 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，你在暑假期间……"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "胖了。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什什么！不可能！完全没有变化的！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7B868F13B2CB4F798DA2E47EBFF0F142 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，显而易见地胖了。\n看，是不是那时候点心吃多了？"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "火大——！还在念叨那件事——！！{w}\n{nw}"
    if sys_effect3_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "……既然如此……！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "哼——！\n果然对娃娃脸的忍来说\n还是头发短一些比较好？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    extend "太长了看着就像熊孩子哦——！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_28087508A43843469EF6F58EAFE0A5EF as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔。"

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_62D2A2AA61774A129B8EF3867F430DA8 "那边，安静！这里是图书馆！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3A742340BEAD415FAC80AFEA0A84B586 "对、对不起……。"

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_0000023C

    return

label block_000001F6:
    # Node: 000001F6 (忍 3)
    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_2D91E64709AA4233A0D3B0D8F1C52D5B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "都怪友才被骂了。不要过来了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_000001C4

    return

label block_000002A0:
    # Node: 000002A0 (小忍問題冊 2)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_9BD621E351A14C56AEDB2731A3325E33 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "要挑战问题吗？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide


    if judge_lm_condition([]):
        jump block_000038EC

    return

label block_00003681:
    # Node: 00003681 (TO: Toilet)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"


    if judge_lm_condition([]):
        jump block_0000378F

    return

label block_0000378F:
    # Node: 0000378F (TO: Toilet)

    if judge_lm_condition([]):
        jump block_000001BB

    return

label block_000001BB:
    # Node: 000001BB (Toilet)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("厕所"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_297E564A7C1544469FB88A41AB85B6C9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1S3Phase == 1" }]):
        jump block_000002BE
    if judge_lm_condition([{ "scope": 0, "content": "C1QSabushinPhase == 1" },{ "scope": 0, "content": "C1QSabuShin == True" },{ "scope": 1, "content": "C1S5 == False" }]):
        jump block_00000209
    if judge_lm_condition([{ "scope": 0, "content": "QSabushinCheck1 == True" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "C1SG1 and C1S4 == True" }]):
        jump block_000001FA
    if judge_lm_condition([{ "scope": 0, "content": "C1S3 == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "TalkShintaro > 0" }]):
        jump block_000002BD
    if judge_lm_condition([]):
        jump block_000001C5

    return

label block_000002BE:
    # Node: 000002BE (Toilet 慎太郎 waiting)
    $ sys_lm_menu_item = [{"pos": (368, 120),"image": "images/Chapter 1/Menu/Shintaro waiting.png","hover": "","name": "慎太郎"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_265
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_000002C0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000378C

    return

label block_000002C0:
    # Node: 000002C0 (Waiting: 慎太郎)
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#AA0055}事件{/color}{color=#0080FF}。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_000002BE

    return

label block_00000209:
    # Node: 00000209 (Toilet empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (224, 184),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "トイレ個室"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_266
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ個室\"" }]):
        jump block_0000020B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000378C

    return

label block_0000020B:
    # Node: 0000020B (Toilet single)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("厕所单间"))
    pause 0.3

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1C833F0E5AB54E79BCEE6017035686BE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0


    if judge_lm_condition([{ "scope": 0, "content": "QSabushinToiletSingle == False" },{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        jump block_00002B1A
    if judge_lm_condition([{ "scope": 0, "content": "C1QSabuShin == True" },{ "scope": 1, "content": "C1S5 == False" }]):
        jump block_00002B7D
    if judge_lm_condition([]):
        jump block_0000020E

    return

label block_00002B1A:
    # Node: 00002B1A (Q三慎ToiletSingle)
    $ QSabushinToiletSingle = True

    if judge_lm_condition([]):
        jump block_0000020C

    return

label block_0000020C:
    # Node: 0000020C (Toilet single Q三慎)
    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_DDAC922834CE43608B163CC54BD86105 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "友亲，即便是现在\n也想{color=#FF00FF}来一发{/color}吗？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "之后我一定会好好侍奉你的，\n现在请先找三酱好不好～"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("厕所单间"))

    if judge_lm_condition([]):
        jump block_0000020E

    return

label block_0000020E:
    # Node: 0000020E (Toilet single)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_267
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000001BB

    return

label block_00002B7D:
    # Node: 00002B7D (Relax Q忍后F5前)
    pause 0.2


    if judge_lm_condition([]):
        jump block_00002B7C

    return

label block_00002B7C:
    # Node: 00002B7C (選擇)
    call scb_selector(_("要放松一下么？"), [{"name":"はい", "content":_("……忍不住了")}, {"name":"いいえ", "content":_("这不合适这不合适")}]) from _call_scb_selector_27

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002B7B
    if judge_lm_condition([]):
        jump block_000001BB

    return

label block_00002B7B:
    # Node: 00002B7B (Relax)
    if sys_music2_current_file != "sound/BGM/Quest Finished.ogg":
        play music2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Quest Finished.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.8

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FF80C0}『完全放松了☆』{/color}"

    pause 0.4

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……呼♪"

    window hide

    pause 0.6

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_216D0346FF6C46758111C49C47CD49B1


    if judge_lm_condition([]):
        jump block_000001BB

    return

label block_000001FA:
    # Node: 000001FA (Toilet 慎太郎 quest)
    $ sys_lm_menu_item = [{"pos": (368, 120),"image": "images/Chapter 1/Menu/Shintaro quest.png","hover": "images/Chapter 1/Menu/Shintaro hover.png","name": "慎太郎"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_268
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00000207
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000378B

    return

label block_00000207:
    # Node: 00000207 (慎太郎)
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_02FE846751D84256A0FD1890407B87EA as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_20039C19E7B74F99B8FB8542570BB3BE as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那么～差不多是时候去抱我老婆了～"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，先说好不在屋顶哦？"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E7D86BC45AC5484380764CF9B109D0DA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "什！？为何你会知道！？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "因为刚才他说要换地方。"

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9AF09268FF81419D92C4233B1910A808 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "真心的啊，SHIT！！{w}\n现在要是不赶快抱老婆的话就无从满足了，\n怎么会这样！！"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FBC1593E8E834A79B75D1EAC80DB77D4 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "HEY！友亲！知道他去什么地方了吗！？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，这个……那个……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（不能说，太对不起猫君了……）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F39796866818471E9C1BECC000987F4D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔～……？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Eye shine 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_62F0A109F6DE4ACE87E64B59D55961F7 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "看招！{color=#FF00FF}{b}舔舔舔舔！{/b}{/color}"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Waoh 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊噫！"

    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_C9267C3226FF4A738E6FA6462C1B4A9F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……这个味道，是情报的味道。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜、呜……我投降，我投降……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "慎太郎大人，请这边走……{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "……猫君，对不起……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("厕所"))

    if judge_lm_condition([]):
        jump block_00002B19

    return

label block_00002B19:
    # Node: 00002B19 (Phase ++)
    $ C1QSabushinPhase = C1QSabushinPhase + 1

    if judge_lm_condition([]):
        jump block_00000208

    return

label block_00000208:
    # Node: 00000208 (QUEST START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托已经开始，请达成目标。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00000209

    return

label block_000002BD:
    # Node: 000002BD (Toilet 慎太郎 flag)
    $ sys_lm_menu_item = [{"pos": (368, 120),"image": "images/Chapter 1/Menu/Shintaro flag.png","hover": "images/Chapter 1/Menu/Shintaro hover.png","name": "慎太郎"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_269
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003789
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_000002C1

    return

label block_000002C1:
    # Node: 000002C1 (F3: 慎太郎)
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_02FE846751D84256A0FD1890407B87EA as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_music2_current_file != "sound/Effect Sound/Surprise 1.ogg":
        play music2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_EC028946B1E24234B3F9A7DB04F052BF as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说起来，商店街里{color=#FF00FF}那个本子店{/color}{w}\n进货了一批不错的东西（全年龄）呐☆"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！真的假的——！？"

    if sys_effect2_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_20039C19E7B74F99B8FB8542570BB3BE as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "当然！！{w}\n{nw}"
    show rs_image_EC028946B1E24234B3F9A7DB04F052BF as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "综上，帮我去买个本子如何。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，为什么。一起去不就好了嘛。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_09451D7B22D74AB5A1A4927086141825 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我是很想去，可家里还有活要干啊。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，原来如此。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F39796866818471E9C1BECC000987F4D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "再说了，要是先去买书，活可能就干不成了呢♪"

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_02FE846751D84256A0FD1890407B87EA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "来，给你钱。{w}拜托你买回来了哦☆"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide


    if judge_lm_condition([]):
        jump block_00002AFA

    return

label block_00002AFA:
    # Node: 00002AFA (Phase ++)
    $ C1S3Phase = C1S3Phase + 1

    if judge_lm_condition([]):
        jump block_000002BF

    return

label block_000002BF:
    # Node: 000002BF (FLAG START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#AA0055}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_000002BE

    return

label block_000001C5:
    # Node: 000001C5 (Toilet)
    $ sys_lm_menu_item = [{"pos": (368, 120),"image": "images/Chapter 1/Menu/Shintaro.png","hover": "images/Chapter 1/Menu/Shintaro hover.png","name": "慎太郎"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_270
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003789
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" },{ "scope": 1, "content": "TalkShintaroF3After == True" }]):
        jump block_00000301
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" },{ "scope": 1, "content": "TalkShintaro == 0" }]):
        jump block_00002AF9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_000029C1

    return

label block_00000301:
    # Node: 00000301 (慎太郎 F3后)
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_02FE846751D84256A0FD1890407B87EA as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_EC028946B1E24234B3F9A7DB04F052BF as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那个——"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    pause 0.2

    extend "那个——{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    pause 0.2

    extend "那个——{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    pause 0.2

    extend "所以说——……"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "到底是什么？怎么回事？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_02FE846751D84256A0FD1890407B87EA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……{w}……我确实拜托你帮忙买东西了，{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#FF0080}新刊{/color}呢？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "…………"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "…………"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "…………{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "O(∩_∩)O"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_17940717C136467FA9DFBBB57E6A5AE4 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好给我过来，该调教了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀————！！！"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_2D4287B2C3E44A0DAEE785D69FF62563

    pause 1

    $ set_place_title(_("厕所"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_297E564A7C1544469FB88A41AB85B6C9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002B42

    return

label block_00002B42:
    # Node: 00002B42 (END: TF3After)
    $ TalkShintaroF3After = False

    if judge_lm_condition([]):
        jump block_000001C5

    return

label block_00002AF9:
    # Node: 00002AF9 (T ++)
    $ TalkShintaro = TalkShintaro + 1

    if judge_lm_condition([]):
        jump block_000029BF

    return

label block_000029BF:
    # Node: 000029BF (慎太郎筆記 1)
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_F39796866818471E9C1BECC000987F4D as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "记下来记下来……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "在做什么笔记呢？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7A854B1E6BC849988176F91868D547BC as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    extend "啊，难道这就是传说中的{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#0080FF}慎酱恋爱笔记{/color}？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这是{color=#008A45}人物详细笔记{/color}。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{color=#FF80FF}恋爱关系笔记{/color}在别的地方，\n对小孩子的友来说还太早了。\n等你明白什么是恋爱再说。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔！什么嘛——！\n我也是有“{color=#FF00FF}电摩君{/color}”这个理想的恋人的……！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2268A2BD2C3946FA9D20376F5F2D5629 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好好明白明白。{w}\n{nw}"
    show rs_image_EC028946B1E24234B3F9A7DB04F052BF as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过，{color=#008A45}人物详细笔记{/color}的话，\n什么时候都可以看哦——"

    window hide


    if judge_lm_condition([]):
        jump block_000029C4

    return

label block_000029C4:
    # Node: 000029C4 (PREPARE)
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0


    if judge_lm_condition([]):
        jump block_000029C0

    return

label block_000029C0:
    # Node: 000029C0 (慎太郎筆記)
    call block_000027FD from _call_block_000027FD_1

    if judge_lm_condition([]):
        jump block_00003A73

    return

label block_00003A73:
    # Node: 00003A73 (RESET)
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000001C5

    return

label block_000029C1:
    # Node: 000029C1 (慎太郎筆記2)
    window show

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_FCEE734E504F47DE91B4F0B671052E93 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{color=#008A45}人物详细笔记{/color}，要看吗？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_place_title(_("厕所"))
    window hide


    if judge_lm_condition([]):
        jump block_000029C2

    return

label block_000029C2:
    # Node: 000029C2 (選擇)
    call scb_selector("", [{"name":"はい", "content":_("看")}, {"name":"いいえ", "content":_("不想看")}]) from _call_scb_selector_28

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_000029C4
    if judge_lm_condition([]):
        jump block_000001C5

    return

label block_000038FB:
    # Node: 000038FB (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003664

    return

label block_00001FD9:
    # Node: 00001FD9 (Conversation F1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "加藤酱到底怎么了呐。{w}\n好——作为班长我必须去看看！"

    window hide

    $ set_window("(標準)")

    return

label block_00000D34:
    # Node: 00000D34 (Target F1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#008A45}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00000225:
    # Node: 00000225 (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    jump block_00002B12

    return

label block_00002B12:
    # Node: 00002B12 (RESET)
    $ C1S1Phase = 0
    $ C1S2Phase = 0
    $ C1S3Phase = 0
    $ C1S4Phase = 0
    $ C1S5Phase = 0
    $ C1QTsubasaPhase = 0
    $ C1QSabushinPhase = 0
    $ C1QMatsutaPhase = 0

    if judge_lm_condition([]):
        jump block_0000378A

    return

label block_00001FE1:
    # Node: 00001FE1 (Character 友+翼)
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

label block_00002B13:
    # Node: 00002B13 (Conversation Q翼)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为什么技安总喜欢欺负翼君呐。{w}\n明明这～么可爱的说！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……一定是我做错什么了。{w}\n…………{w}\n第一次见面时还是很温柔的……"

    window hide

    $ set_window("(標準)")

    return

label block_00002B14:
    # Node: 00002B14 (Target Q翼)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『把文件交给穗海作哉。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FE3:
    # Node: 00001FE3 (Character 友+慎太郎)
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

label block_00002B1C:
    # Node: 00002B1C (Conversation Q三慎)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "上，犬五郎！把你的主人带到三酱那里去！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "汪、汪！"

    window hide

    $ set_window("(標準)")

    return

label block_00001FDF:
    # Node: 00001FDF (Character 友)
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

label block_000002FF:
    # Node: 000002FF (School inside ACTA)
    if judge_lm_condition([{ "scope": 1, "content": "C1S2Phase == 1" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, True, talk_label="block_00000D31", target_label="block_00000D36") from _call_scb_global_map_66
    elif judge_lm_condition([{ "scope": 1, "content": "C1S3Phase == 1" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, True, talk_label="block_00001FD8", target_label="block_00000D36") from _call_scb_global_map_67
    elif judge_lm_condition([{ "scope": 1, "content": "C1S5Phase == 1" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, True, talk_label="block_000023CE", target_label="block_00000D36") from _call_scb_global_map_68
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, True, talk_label="block_000002B1", target_label="block_00000D36") from _call_scb_global_map_69
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_0000368B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00003680
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_0000368C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00003682
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00003681
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_000038FB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1S2Phase == 1" }]):
        jump block_00000D31
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00000D36
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00000225
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FDF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" },{ "scope": 1, "content": "C1S2Phase == 1" }]):
        jump block_0000367D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" }]):
        jump block_00003787
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1S3Phase == 1" }]):
        jump block_00001FD8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1S5Phase == 1" }]):
        jump block_000023CE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000002B1

    return

label block_00000D31:
    # Node: 00000D31 (Conversation F2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "快点到放学后就好了呐♪"

    window hide

    $ set_window("(標準)")

    return

label block_00000D36:
    # Node: 00000D36 (Target F235)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『快进到{/color}{color=#FF8000}放学后{/color}{color=#0080FF}。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_0000367D:
    # Node: 0000367D (TO: 翼的流轉音符)

    if judge_lm_condition([]):
        jump block_000008C7

    return

label block_000008C7:
    # Node: 000008C7 (FLAG 2)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    stop music fadeout 1
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
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
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"


    if judge_lm_condition([]):
        jump block_000008BF

    return

label block_000008BF:
    # Node: 000008BF (Music room)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("音乐室"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000008C2

    return

label block_000008C2:
    # Node: 000008C2 (Music room)
    $ sys_lm_menu_item = [{"pos": (176, 288),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "ピアノ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_271
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ピアノ\"" }]):
        jump block_000008C4

    return

label block_000008C4:
    # Node: 000008C4 (Piano)

    if judge_lm_condition([]):
        jump block_000008C3

    return

label block_000008C3:
    # Node: 000008C3 (選擇)
    call scb_selector(_("要弹钢琴么？"), [{"name":" 演奏しない", "content":_("不想弹")}, {"name":"演奏する", "content":_("弹")}]) from _call_scb_selector_29

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"演奏する\"" }]):
        jump block_00001162
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \" 演奏しない\"" }]):
        jump block_000008C2

    return

label block_00001162:
    # Node: 00001162 (Piano)
    window hide

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 0.3

    if sys_music_current_file != "sound/Piano/sti_gymno_01_pi.ogg":
        play music "sound/Piano/sti_gymno_01_pi.ogg" noloop
        $ sys_music_current_file = "sound/Piano/sti_gymno_01_pi.ogg"

    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    show rs_image_3503DB118A8B44918DBD9BCA60112DB1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2EA8313137C646C685870CF29BCA70C5

    $ zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF = 200
    show rs_image_144F93E01F004839B3161F3821448089 as tag_C34E445E70F4457D90AA6C86C64AF3DF at center_bottom zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_25B1A2BEC607430AA0FF6599E92F9935 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_90FA4777E35348218E55C79DE2793463 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3

    show rs_image_9473FD21634F40548C0B791B6007C0A8 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3

    show rs_image_BDE18EC278FF466197538A5E8C10EE48 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    show rs_image_BECC49E1FF894BC0B94A831D1B0813FA as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    show rs_image_11379BC11E834A19BB1A5E7A63695828 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    show rs_image_14BECA7FDD8544EBADD5FAA7415E5641 as tag_C34E445E70F4457D90AA6C86C64AF3DF zorder zorder_tag_C34E445E70F4457D90AA6C86C64AF3DF onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    $ zorder_tag_99488938252D4BC2B7FA91D436D9159B = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_99488938252D4BC2B7FA91D436D9159B at center_bottom zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    hide tag_C34E445E70F4457D90AA6C86C64AF3DF
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    stop music fadeout 1.4
    $ sys_music_current_file = ""

    pause 0.4


    if judge_lm_condition([]):
        jump block_00003724

    return

label block_00003724:
    # Node: 00003724 (FLAG: 翼的流轉音符)
    call block_00003715 from _call_block_00003715

    if judge_lm_condition([]):
        jump block_00003723

    return

label block_00003723:
    # Node: 00003723 (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#3A00C4}“翼的流转音符”{/color}{color=#0080FF}成功结束。』{/color}"

    window hide

    pause 4

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003651

    return

label block_00003787:
    # Node: 00003787 (Twilight)
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
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"


    if judge_lm_condition([]):
        jump block_0000397A

    return

label block_0000397A:
    # Node: 0000397A (CP1 Twilight Misaki)
    call block_00000853 from _call_block_00000853

    if judge_lm_condition([]):
        jump block_000001B4

    return

label block_00001FD8:
    # Node: 00001FD8 (Conversation F3)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼。好期待放学后呐☆"

    window hide

    $ set_window("(標準)")

    return

label block_000023CE:
    # Node: 000023CE (Conversation F5)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍居然会邀请我一起，真稀奇。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天吃错什么东西了么？"

    window hide

    $ set_window("(標準)")

    return

label block_000002B1:
    # Node: 000002B1 (Conversation)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀～天好热，能赶快转凉就好了呐。"

    window hide

    $ set_window("(標準)")

    return

label block_000001B5:
    # Node: 000001B5 (School inside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "SYSReviewMode == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_000002B1", target_label="block_000031BD") from _call_scb_global_map_70
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1S1 and C1S2 and C1S3 and C1S4 and C1S5 == True" },{ "scope": 2, "content": "C1QTsubasa and C1QNewsclub and C1QKimuraConference and C1QMatsuta and CXQShinoQuestion and C1QSabuShin and CXQSabuImechen and CXQTsukiTest == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_000002B1", target_label="block_00002B1D") from _call_scb_global_map_71
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_000002B1", target_label="block_00001FDB") from _call_scb_global_map_72
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "SYSReviewMode == True" }]):
        jump block_000031BD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1S1 and C1S2 and C1S3 and C1S4 and C1S5 == True" },{ "scope": 2, "content": "C1QTsubasa and C1QNewsclub and C1QKimuraConference and C1QMatsuta and CXQShinoQuestion and C1QSabuShin and CXQSabuImechen and CXQTsukiTest == True" }]):
        jump block_00002B1D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_0000368B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00003680
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_0000368C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00003682
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00003681
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_000038FB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_000001B5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000002B1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001FDB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_000001B5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FDF

    return

label block_000031BD:
    # Node: 000031BD (Target dream)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『要想回到现实，请和鞋箱的触手A说。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00002B1D:
    # Node: 00002B1D (Target 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#3A00C4}下一个章节{/color}{color=#0080FF}正在等着！』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FDB:
    # Node: 00001FDB (Target 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『尽可能收集更多{/color}{color=#008080}事件{/color}{color=#0080FF}和{/color}{color=#FF8000}委托{/color}{color=#0080FF}！』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00002B25:
    # Node: 00002B25 (Conversation Q松田)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "麻、麻烦了！不马上去阿月那里的话！"

    window hide

    $ set_window("(標準)")

    return

label block_00002B1B:
    # Node: 00002B1B (Target Q三慎)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『找到猫山三朗的所在之处。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00002B26:
    # Node: 00002B26 (Target Q松田)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『尽快去把月找来！』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00000228:
    # Node: 00000228 (友+慎太郎)
    $ sys_ayumi_global_map_character = "tomo_shintaro"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_00000223

    return

label block_000018C0:
    # Node: 000018C0 (友)
    $ sys_ayumi_global_map_character = "tomo"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([{ "scope": 0, "content": "C1S2Phase == 1" },{ "scope": 0, "content": "C1S3Phase == 1" },{ "scope": 0, "content": "C1S5Phase == 1" }]):
        jump block_000002FF
    if judge_lm_condition([{ "scope": 0, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase > 0" },{ "scope": 0, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase > 0" }]):
        jump block_00000223
    if judge_lm_condition([]):
        jump block_000001B5

    return

label block_000024BD:
    # Node: 000024BD (Newsclub quest)
    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("新闻部活动室"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000001DC

    return

label block_00002B20:
    # Node: 00002B20 (Cancel: First)
    $ FNewsclub = False

    if judge_lm_condition([]):
        jump block_000024B7

    return

label block_000024B7:
    # Node: 000024B7 (Newsclub 1)
    $ set_window("イベントモード")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1.4

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.2

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "打扰了！不知为何就来了。"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_C95D7A9489554E95B60C95F27C1215FF as tag_DCBDF256A1E242E78A25910AE27C0954 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    show rs_image_3806F899C04B4F119D261714031BD373 as tag_CC4336DE74164173AC47C2C317367F10 at center_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哦，你是一班的森海君。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_17D19129F27249C2BFA0ACD1BA4765D2 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "欢迎来到{color=#00FFFF}新闻部{/color}。看看我们的杰作如何！"

    show rs_image_4B4CF6F6178F455DBD43D650E8EF05B0 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "请自由参观～"

    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谢谢！{w=0.5}{nw}"
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_3F533DA3CF494DEBA1146743852331E9 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……嗯嗯，哦哦——"
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯？所有报纸都是\n冈岛君和小岛君署名的。新闻部的其他人呐？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_D21F346DFFC747CBB0EE406A4CECC2A7 as tag_CC4336DE74164173AC47C2C317367F10 at center_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "嗯，因为去年刚创立，"
    show rs_image_7A6441B8DAFF4D10A64262A1C9EE1459 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "基本没什么传承，\n知道的人很少，新生也没人来……"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A669E311EB4543F48220B5C804EE7513 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "然而！总有一天我们势必会搞个大新闻，\n让所有人知道我们！！"

    show rs_image_B948584405374875B0548BD5B5989750 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "在此还要感谢刚创立就马上入部的小岛君！"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_C95D7A9489554E95B60C95F27C1215FF as tag_DCBDF256A1E242E78A25910AE27C0954 at center_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "无需感谢。从小事开始慢慢做起即可。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……好关心部长呐。"
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，这张和床一样大的纸\n是还在写的新闻？放在地上不会被弄坏吗？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_B948584405374875B0548BD5B5989750 as tag_CC4336DE74164173AC47C2C317367F10 at left_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哈！我们怎么可能会在第二学期第一刊上犯那种低级错误！"

    show rs_image_5C177DF4E0574BC994146C7CEAAC6866 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "森海君也记住绝对不许走过去啊！"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_64D8D1E21F7F40938F719E0070CF195B as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当然当然——！不会有问题的～"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_A669E311EB4543F48220B5C804EE7513 as tag_CC4336DE74164173AC47C2C317367F10 at left_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "绝对不许过去啊！过去也要避开走啊！"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没关系！我发誓要是真的不小心，\n这辈子都娶……{w=0.6}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_8DB9EBBA116648CAAA85C0A0F67B04D2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "呜，啊哇！？！？"

    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "哐当——咕噜——\n{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    extend "{nw}"
    window hide

    extend "………{nw}"
    window hide

    extend ""

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_195F518B89564C98A557F130D2E603F0

    pause 0.5

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "啊{w=0.2}\n{nw}"
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_D21F346DFFC747CBB0EE406A4CECC2A7 as tag_CC4336DE74164173AC47C2C317367F10 at center_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊。\n{w=0.2}{nw}"
    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_9226D116B4454CB6A69B36D833CB9AA6 as tag_DCBDF256A1E242E78A25910AE27C0954 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊。"

    window hide

    pause 0.5

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.7

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_4B4CF6F6178F455DBD43D650E8EF05B0 as tag_DCBDF256A1E242E78A25910AE27C0954 at center_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    pause 0.3

    rs_character_53FF68C192E3494AB005C1909579AFFB "有在反省么……森海君，还有，部长。"

    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是、是的……对不起……！"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_FB2D1F0CA559413E9A783A63C89DF060 as tag_CC4336DE74164173AC47C2C317367F10 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "为、为何我也要……"

    show rs_image_C95D7A9489554E95B60C95F27C1215FF as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "因为你在乱立FLAG。"

    pause 0.2

    if sys_effect2_current_file != "sound/Effect Sound/Onboard 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Onboard 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Onboard 1.ogg"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_CC4336DE74164173AC47C2C317367F10
    $ zorder_tag_5B6684205EA24754A986B49C70895ECD = 200
    $ zorder_tag_EB5D0582654644B7A76BB509C31DD31E = 200
    show rs_image_9226D116B4454CB6A69B36D833CB9AA6 as tag_5B6684205EA24754A986B49C70895ECD at left_top zorder zorder_tag_5B6684205EA24754A986B49C70895ECD onlayer master
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_EB5D0582654644B7A76BB509C31DD31E at right_top zorder zorder_tag_EB5D0582654644B7A76BB509C31DD31E onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_53FF68C192E3494AB005C1909579AFFB "因此，森海君。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是！"

    hide tag_5B6684205EA24754A986B49C70895ECD
    hide tag_EB5D0582654644B7A76BB509C31DD31E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_AC39FD28FE9544E49ACAE5F52BBC0936 as tag_DCBDF256A1E242E78A25910AE27C0954 at center_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "为了弥补毁掉原稿的错误，{w}\n接下来你必须帮助我们，帮助新闻部收集情报。"

    show rs_image_4B4CF6F6178F455DBD43D650E8EF05B0 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "收集到什么情报时请前来汇报，到时候就拜托了。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_4B4CF6F6178F455DBD43D650E8EF05B0 as tag_DCBDF256A1E242E78A25910AE27C0954 at left_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "在、在下听令！如果这样就能原谅我的话不管什么我都会做……"

    show rs_image_6096849E8EA746E9A5F931F019DB29FA as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "嗯，很好。"

    window hide

    pause 0.7

    $ set_window("(標準)")
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.4

    $ set_place_title(_("新闻部活动室"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B


    if judge_lm_condition([{ "scope": 0, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 1, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000024B9
    if judge_lm_condition([]):
        jump block_000001DC

    return

label block_000024B9:
    # Node: 000024B9 (Newsclub 岡島 quest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (112, 160),"image": "images/Chapter 1/Menu/Okajima quest.png","hover": "images/Chapter 1/Menu/Okajima hover.png","name": "岡島"}, {"pos": (392, 160),"image": "images/Chapter 1/Menu/Kojima.png","hover": "images/Chapter 1/Menu/Kojima hover.png","name": "小島"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_272
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000001B7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_000024BA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_000001EF

    return

label block_000024BA:
    # Node: 000024BA (新聞部 quest)
    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_F75409F6FFF94CF7A59AA6323AF2CF16 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "森海君！事不宜迟，去取材了！{w}\n这次是“{color=#FF0000}找到巨大蚯蚓{/color}”！"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_EAE298160D2D4F5DAB6346EF10E33931 as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "现在已经存在一些室外目击情报了。\n期待你的好消息。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    window hide

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#008A45}最近有人在学园内见到了巨大的蚯蚓。然而，\n所有目击者都拒绝说明情况。因此，我们需要\n你亲自去探寻巨大蚯蚓的原委，并整理为报告！{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_00002B21

    return

label block_00002B21:
    # Node: 00002B21 (Phase ++)
    $ C1QNewsclubPhase = C1QNewsclubPhase + 1

    if judge_lm_condition([]):
        jump block_000024BB

    return

label block_000024BB:
    # Node: 000024BB (QUEST START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托已经开始，请达成目标。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『该委托可以和其他任意事件、委托{/color}{color=#FF00FF}同时进行{/color}{color=#0080FF}。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『但并不能持续到{/color}{color=#FF0080}下一章{/color}{color=#0080FF}。\n所以请{/color}{color=#FF0000}务必在本章完成{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.5

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_000001DC

    return

label block_000001EF:
    # Node: 000001EF (小島 1)
    window show

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_BADBAA4F0A4C41C38EF36F3121398C07 as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "照片，要来一张吗？"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可以哦！YEAH☆CHEESE☆"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BADBAA4F0A4C41C38EF36F3121398C07 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "拍出来的照片如果有不错的，\n可以允许我们洗出来使用吗？"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？嗯，可以。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EAE298160D2D4F5DAB6346EF10E33931 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "交涉成立。\n{w=0.5}{nw}"
    show rs_image_AB8147BA99C84400ACC67EDF66ADE9FD as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那么，CHEESE。"

    pause 0.2

    if sys_effect_current_file != "sound/Effect Sound/Shoot 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shoot 1.ogg"

    show rs_image_AB8147BA99C84400ACC67EDF66ADE9FD as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.6

    show rs_image_EAE298160D2D4F5DAB6346EF10E33931 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "感谢配合。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([{ "scope": 0, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 1, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 2, "content": "C1QNewsclub == False" }]):
        jump block_000024B9
    if judge_lm_condition([]):
        jump block_000001DC

    return

label block_000001DB:
    # Node: 000001DB (Newsclub)
    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("新闻部活动室"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1QNewsclubPhase == 0" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "C1QNewsclub == False" }]):
        jump block_000024B9
    if judge_lm_condition([]):
        jump block_000001DC

    return

label block_000023BD:
    # Node: 000023BD (松田 QUEST 2)
    $ set_window("イベントモード")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_1C428704E5E24078848D388A31B861CE

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 1.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_music_current_file != "sound/BGM/Flurry 1.ogg":
        play music "sound/BGM/Flurry 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 1.ogg"

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "坏了——！松田亲说想着阿月的事情\n身体难受得不得了，开始发脾气了！"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_3D6A04F77BD14290ACB4CB84A6D7781B as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_57F7A3D31244474680A656FBC7957CCF as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么办！去不去？"

    show rs_image_04CE6801CFBD460096381A21558DE1D7 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯……看来有些想法还是没传达到啊。\n我也有同样的感觉。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_4E534C3CC3ED418EA9C8155C87F1BCBB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——！你在夫人面前说什么呢！{w}\n{nw}"
    show rs_image_952D06E912C54776B1C4F5BB577DFB95 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "空——！空觉得这样下去真的可以吗。"

    show rs_image_73F69A7FB68D4D8684029D4486A79854 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "真是的，哥哥……这么多次下来我都腻了。"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～！！阿月原来是那么花心的人！？"

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_86BB7A17393E4CA3AA3BEA8164C0DA78 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "男人就是这样的。"

    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "坏了坏了坏了——\n已经不是我等文明人能理解的了——"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_9E61D0A55E554AAC9894E8AA00A7E5A4 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "好，我去了。"

    show rs_image_256DCF0FD3C145C4BFF308F96CE078E2 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯嗯，加油哦。{w}\n{nw}"
    show rs_image_145DF74E1B2140DABD280C00261D5D85 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "这次一定要好好解决再回来哦。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend ""

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_E0D00426275740F394D32435264217E5 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这都行！空！真的不阻止？"

    show rs_image_20AA9A405C08411899D11DA9EB2EE47D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嘛，反正能满足对方，有何不可？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——成熟过头了——"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_80AC1FBCF08D4C6283030181039745BE as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……怎、怎么做才好！{w}\n作为班长、作为朋友，我到底该怎么做！"

    window hide

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.9

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    pause 0.6

    if sys_effect2_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    # Gallery unlock: images/CG/Finesse-sumo.png
    $ zorder_rs_image_1A1E430526B94BB68A38F9C6A6CE9B8C = -100
    show rs_image_1A1E430526B94BB68A38F9C6A6CE9B8C as rs_image_1A1E430526B94BB68A38F9C6A6CE9B8C zorder zorder_rs_image_1A1E430526B94BB68A38F9C6A6CE9B8C onlayer master
    hide rs_image_1A1E430526B94BB68A38F9C6A6CE9B8C

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1A1E430526B94BB68A38F9C6A6CE9B8C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.7

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "唔……！"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "呵……！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=28}结果居然是这个！！！{/size}"

    window hide

    pause 1

    $ set_window("(標準)")
    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 0.8


    if judge_lm_condition([]):
        jump block_00002B27

    return

label block_00002B27:
    # Node: 00002B27 (C1Q松田)
    $ C1QMatsuta = True
    $ C1QMatsutaPhase = 0

    if judge_lm_condition([]):
        jump block_000023BE

    return

label block_000023BE:
    # Node: 000023BE (QUEST FINISH)
    if sys_music2_current_file != "sound/BGM/Quest Finished.ogg":
        play music2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.8


    if judge_lm_condition([]):
        jump block_00003789

    return

label block_000001DF:
    # Node: 000001DF (Stairwell)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("楼梯间"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "CXQTsukiTest == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000001E0
    if judge_lm_condition([]):
        jump block_000007E8

    return

label block_000001E0:
    # Node: 000001E0 (Stairwell 月 quest)
    $ sys_lm_menu_item = [{"pos": (224, 264),"image": "images/Chapter 1/Menu/Sora.png","hover": "images/Chapter 1/Menu/Sora hover.png","name": "空"}, {"pos": (440, 256),"image": "images/Chapter 1/Menu/Tsuki quest.png","hover": "images/Chapter 1/Menu/Tsuki hover.png","name": "月"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_273
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000001B7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_000001D3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" },{ "scope": 1, "content": "TalkSora == 0" }]):
        jump block_000001D4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_0000243C

    return

label block_000001D3:
    # Node: 000001D3 (阿月測眼力 1)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_0EBE1029E4FF475191BFB073B7BE4EA5 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_0C73761CD21648FCB039C9F07947C6DA as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "森海，来得好。{w}\n现在我们在准备训练，你也一起如何？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "训练？听起来……不过我不要出汗。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F55083532FBB4E6FA28BA128771AB1CF as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "放心，是精神力训练，不是体力。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_B9C05B244A1F41E7AFDE876574238D4A as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哦，那就换一个说法……"

    show rs_image_1D44BAB200164AC5802C27FE81E9C0AE as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君，这个训练并不难，只是类似游戏一样的东西。\n如何，想不想试试？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦哦，听起来很有意思呐，我就试试好了。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))
    pause 0.8


    if judge_lm_condition([]):
        jump block_000023AE

    return

label block_000023AE:
    # Node: 000023AE (阿月測眼力)
    call block_0000116E from _call_block_0000116E_1

    if judge_lm_condition([]):
        jump block_00003835

    return

label block_00003835:
    # Node: 00003835 (RESET)
    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    $ set_place_title(_("楼梯间"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 0
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000007E8

    return

label block_000007E8:
    # Node: 000007E8 (Stairwell)
    $ sys_lm_menu_item = [{"pos": (224, 264),"image": "images/Chapter 1/Menu/Sora.png","hover": "images/Chapter 1/Menu/Sora hover.png","name": "空"}, {"pos": (440, 256),"image": "images/Chapter 1/Menu/Tsuki.png","hover": "images/Chapter 1/Menu/Tsuki hover.png","name": "月"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_274
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" },{ "scope": 1, "content": "C1QSabushinPhase == 1" }]):
        jump block_0000024E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" },{ "scope": 1, "content": "TalkTsukiSoraF1After == True" }]):
        jump block_000023B0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" },{ "scope": 1, "content": "TalkTsukiSoraF1After == True" }]):
        jump block_000023B1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000001B7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" },{ "scope": 1, "content": "TalkSora == 0" }]):
        jump block_000001D4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" },{ "scope": 1, "content": "GTsukiTestStage == 5" }]):
        jump block_00002A67
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" },{ "scope": 1, "content": "CXQTsukiTest == True" }]):
        jump block_00000300
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_0000243C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00002B45

    return

label block_0000024E:
    # Node: 0000024E (月 Q三慎)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_0EBE1029E4FF475191BFB073B7BE4EA5 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_0C73761CD21648FCB039C9F07947C6DA as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "奥村，谢谢你之前带我们去那个{color=#008080}还不错的寿司店{/color}。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_BC97C0FB4F0B4391BC8A98516A0FBF67 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "没什么，不用客气！{w}\n店长也一定会非常高兴的，\n毕竟像阿月这么帅的人光临了嘛。"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EE8DDD33A22840E38878EFBBDA5861C3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不过，真是吓了一跳。居然会有那么特别的店。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么特别？"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "靠脸吃饭！{w}\n脱几件算数，给看那个也算数，\n有各种勉强全年龄的内容哦♪"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好、好厉害……\n慎太郎的世界观果然非常人能理解……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8FA8A472B85C4BFF9AAF2B9D00DA1DF1 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不过明明吃是吃饱了，\n但总觉得作为人什么不见了。\n真是不可思议呐。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_8A7E4E552B1E4733934E6F62EC03A374 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……这到底是什么感觉呢……"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嘛嘛，不要在意细节♪"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过，还是好棒啊！真羡慕！我也要去！{w}\n只要脱就能吃到美味的寿司对不对？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那就简单了——！\n我脱起来绝对没有任何犹豫的♪"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哟♪不愧是碧池太郎♪{w}\n不过，那边的店主很很挑剔容姿的。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "友亲这种豆芽菜体型\n最多也就来个河童卷而已呐。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——！！什么意思嘛——！！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜——那慎酱为什么要去啊。{w}\n明明和我体型差不多的说。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 2.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈，因为我有足以补齐短板的其他东西哦♪"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_000007E8

    return

label block_000023B0:
    # Node: 000023B0 (月 F1后)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_0EBE1029E4FF475191BFB073B7BE4EA5 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000023AF

    return

label block_000023AF:
    # Node: 000023AF (月+空 F1后)
    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "月、空！\n之前的相扑大会，两人都好帅呐♪"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F55083532FBB4E6FA28BA128771AB1CF as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这还是多亏了大家的支持。获得了不错的回忆呢。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_B867F09D99D1483C83E80841D1EBDEA2 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "大家一起去吃的烤肉，真是美味呐——♪"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_8FA8A472B85C4BFF9AAF2B9D00DA1DF1 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……说起来，森海，\n你应该已经从空那里听说我们家的事了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，和加藤酱一起。\n月被选为道场继承人后，\n果然生活还是会有所改变嘛？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8A7E4E552B1E4733934E6F62EC03A374 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "确实。今后社团活动的时间不多了，\n必须要在道场工作。"

    show rs_image_EE8DDD33A22840E38878EFBBDA5861C3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "作为道场长，\n或许会为了一些练习和生意不得不向学校请假。"

    show rs_image_8FA8A472B85C4BFF9AAF2B9D00DA1DF1 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "在适应这一切之前或许会给大家添麻烦，\n还请多多包涵。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，不要勉强哦。{w}对了，这么一说，\n和大家一起玩的时间也会变少呐。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6199A1116B8A4046908CAA7057A391E3 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_0EBE1029E4FF475191BFB073B7BE4EA5 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "确实会。有些寂寞……但也无可奈何。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "毕竟是工作嘛，也只能这样……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……所以"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "今后和大家一起的时间，\n一定要无比珍惜地度过哦！！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F68634CC43DF49BA96B1D06D54659FD0 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君……{w}\n{nw}"
    show rs_image_1D44BAB200164AC5802C27FE81E9C0AE as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "名言。说的没错。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_0C73761CD21648FCB039C9F07947C6DA as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯。"
    show rs_image_F55083532FBB4E6FA28BA128771AB1CF as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……不过真有必须和大家一起的时候\n就直接无视其他人出门就是了。"

    show rs_image_17347653B2C64C9DB845B9D9D1ADE788 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "毕竟现在还是能撒撒娇的年纪呢。"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！正是！\n说起来阿月也是14岁的男“孩子”呐！\n都快忘掉这个设定了！"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_68FF164F74AD4362817E645450364BF5 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "什么意思。我看起来很老？"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_B867F09D99D1483C83E80841D1EBDEA2 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君，哥哥也是有和年龄相称的青涩之处的哦？"

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊！难道说是\n只有空能看到的{color=#0000A0}晚上的某某{/color}？"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_29969E8B611640C388658A23CD7F1D93 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔……{w=0.55}{nw}"
    show rs_image_2E58C1DF6B1342D386CAEB993E2D0C53 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "天知道！秘密！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_00002B2F

    return

label block_00002B2F:
    # Node: 00002B2F (END: TF1After)
    $ TalkTsukiSoraF1After = False

    if judge_lm_condition([]):
        jump block_000007E8

    return

label block_000023B1:
    # Node: 000023B1 (空 F1后)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_0C5FFEB2760549C9B7A6F47F83C0B99B as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000023AF

    return

label block_000001D4:
    # Node: 000001D4 (空 1)
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_0C5FFEB2760549C9B7A6F47F83C0B99B as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B867F09D99D1483C83E80841D1EBDEA2 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君～♪"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什～么事♪"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F59CF92171C0495BA4E334AC96BA8B63 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "给，这个。"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇～空{color=#FF8080}亲手做的点心{/color}！！{w}\n谢谢！我开动了！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……wwwwwwwwwww……{w}\n{nw}"
    if sys_effect3_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "唔！！{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    extend "好吃！{w=0.5}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    extend "好吃！！\n{w=0.6}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    extend "{size=28}{color=#FF00FF}太好吃了☆☆☆{/color}{/size}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_347F20274D09479486402421E7CD63FA as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.2

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊哈哈♪太好了～\n下次还会做的，到时候也请哦。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当然没问题！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "最近空经常做点心呐～！{w}\n果然将来是打算开点心店嘛？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_11AD9933A199448E9618DB636832D33D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔……听起来也不错。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真好啊，空已经决定了将来的梦想。\n我还什么都不知道，前途一片黑暗～{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "啊～不想长大。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F68634CC43DF49BA96B1D06D54659FD0 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君不是还有钢琴嘛。\n试着向音乐方面前进如何？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……那个啊，\n比起工作我更想当成兴趣，工作太累了……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "妈妈是职业钢琴家，\n看着就会觉得自己还远远不行。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_078B009119BE45239EF1AE1881CCE6B9 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这样。{w}\n……不过，我或许明白这种感觉。\n我也是很相似的。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_11AD9933A199448E9618DB636832D33D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不，只是我自言自语。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CD8F39552B944292A7352D0B3CC2942D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好——！为了梦想要学习做更多点心了——！"

    show rs_image_B9C05B244A1F41E7AFDE876574238D4A as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "梦想实现之时请务必光临哦！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！！\n……不过，那时候我们都早已长大了啊～{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "欸～不想那样～不想长大～"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_00002B2C

    return

label block_00002B2C:
    # Node: 00002B2C (T ++)
    $ TalkSora = TalkSora + 1

    if judge_lm_condition([{ "scope": 0, "content": "CXQTsukiTest == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000001E0
    if judge_lm_condition([]):
        jump block_000007E8

    return

label block_00002A67:
    # Node: 00002A67 (月 測試通關后)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_F55083532FBB4E6FA28BA128771AB1CF as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "走，去训练了。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_000023AE

    return

label block_00000300:
    # Node: 00000300 (阿月測眼力)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_F55083532FBB4E6FA28BA128771AB1CF as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "继续训练？"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_000024FE

    return

label block_000024FE:
    # Node: 000024FE (選擇)
    call scb_selector("", [{"name":"はい", "content":_("走，去训练了")}, {"name":"いいえ", "content":_("我很忙的")}]) from _call_scb_selector_30

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_000023AE
    if judge_lm_condition([]):
        jump block_000007E8

    return

label block_0000243C:
    # Node: 0000243C (空 2)
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_B9C05B244A1F41E7AFDE876574238D4A as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "下次一起试着做点心好了。\n友君料理水平很棒，一定会很有趣的♪"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([{ "scope": 0, "content": "CXQTsukiTest == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" }]):
        jump block_000001E0
    if judge_lm_condition([]):
        jump block_000007E8

    return

label block_00002B45:
    # Node: 00002B45 (月 F1前)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_0C73761CD21648FCB039C9F07947C6DA as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "森海，来得好。{w}\n现在我们在准备训练，你也一起……"

    show rs_image_9C6FBD9DB462411BAFEABE7C5B5F94E9 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……很想这么说不过，\n看起来现在还不是时候，抱歉。\n下次我会再来邀请你的。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_000007E8

    return

label block_000001EE:
    # Node: 000001EE (岡島 1)
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_C98DC5525B364C5B8D272173F7437DCA as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F75409F6FFF94CF7A59AA6323AF2CF16 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "任何情报请速来告知！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，说起来……"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_80DDCB83351245C2B44A943AC22567CC as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哦呀！这个反应，想到什么了对不。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "其实——之前在校庭里……{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{color=#008080}看到{/color}{size=28}{color=#008080}套套君{/color}{/size}{color=#008080}了——！{/color}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C29B9703BE7C41F5840BF23219240A16 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_560D536F2A06470C856E0D5C0557DCFB as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "唔，这种情报有点……"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_EAE298160D2D4F5DAB6346EF10E33931 as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_53FF68C192E3494AB005C1909579AFFB "森海君，请不要对纯洁的部长灌输邪恶思想。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——我还以为是个好新闻的。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_00000231

    return

label block_00000231:
    # Node: 00000231 (T ++)
    $ TalkOkajima = TalkOkajima + 1

    if judge_lm_condition([{ "scope": 0, "content": "C1QNewsclubPhase == 1" }]):
        jump block_000024BE
    if judge_lm_condition([]):
        jump block_000001DC

    return

label block_000024BE:
    # Node: 000024BE (Show quest)

    if judge_lm_condition([]):
        jump block_000001DC

    return

label block_00000214:
    # Node: 00000214 (岡島 2)
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F75409F6FFF94CF7A59AA6323AF2CF16 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "任何新情报请速来告知！"

    show rs_image_560D536F2A06470C856E0D5C0557DCFB as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "啊，记得必须是全年龄的哦。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([{ "scope": 0, "content": "C1QNewsclubPhase == 1" }]):
        jump block_000024BE
    if judge_lm_condition([]):
        jump block_000001DC

    return

label block_000024BC:
    # Node: 000024BC (小島 Q新聞部中)
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_BADBAA4F0A4C41C38EF36F3121398C07 as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "之前的委托，就拜托你了。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_000024BE

    return

label block_000001BF:
    # Node: 000001BF (Schoolhouse)
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

    $ set_place_title(_("校舍内"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1S4 == False" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "C1SG1 == True" }]):
        jump block_000002C2
    if judge_lm_condition([{ "scope": 0, "content": "C1QTsubasaPhase == 1" }]):
        jump block_000027D6
    if judge_lm_condition([]):
        jump block_000001C9

    return

label block_000002C2:
    # Node: 000002C2 (Schoolhouse 作哉 flag)
    $ sys_lm_menu_item = [{"pos": (360, 160),"image": "images/Chapter 1/Menu/Sakuya flag.png","hover": "images/Chapter 1/Menu/Sakuya hover.png","name": "作哉"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_275
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_000002C4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000364B

    return

label block_000002C4:
    # Node: 000002C4 (F4: 作哉)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_8F8B36DC5AD7424388BA16D0BF2B3B15 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_2A76BCBE9177431BA9BCAAC2C0678838 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "好了，又是散步的时间了。"

    pause 0.2

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_8EBCF49BA1C247FD9E0FEF46F073E681 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "出来！小翼——！"

    window hide

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_0117E4BD45BE4974A1BFEF7415F2DDEE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_B322EABE0E5942AE8BB001331B25E330 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "乖乖♪散步的时间到了哦——{w}\n今天也要快快乐乐地一起哦♪"

    show rs_image_8F8B36DC5AD7424388BA16D0BF2B3B15 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……嗯？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_01A79D17F985408D9F6118A06A27BC50 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    extend "……混蛋，看什么看。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦吼吼吼♪没事，你们继续。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "技安原本就是温柔善良的好孩子呐。{w}\n不过因为一直放不下矜持所以都很傲呐。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_8DB1D821008C4432A73D25AC1E984DD1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你、你个……！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_F1AE8B76A99E4FC297AF2F180FA7033F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_8EBCF49BA1C247FD9E0FEF46F073E681 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊，对不起哦小翼。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_ACB5D255F8CA4CF2A27FC6BD69B19D88 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    extend "……回头给我等着。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide


    if judge_lm_condition([]):
        jump block_00002AFE

    return

label block_00002AFE:
    # Node: 00002AFE (Phase ++)
    $ C1S4Phase = C1S4Phase + 1

    if judge_lm_condition([]):
        jump block_000002C3

    return

label block_000002C3:
    # Node: 000002C3 (FLAG START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#008A45}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.5

    pause 0.7

    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1


    if judge_lm_condition([]):
        jump block_000023C1

    return

label block_000023C1:
    # Node: 000023C1 (CP1 作哉散歩)
    call block_000002C6 from _call_block_000002C6

    if judge_lm_condition([{ "scope": 0, "content": "C1S4 == True" }]):
        jump block_000036F8
    if judge_lm_condition([]):
        jump block_0000364B

    return

label block_000036F8:
    # Node: 000036F8 (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#008A45}“不可思议！猫狗物语”{/color}{color=#0080FF}成功结束。』{/color}"

    window hide

    pause 4

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_0000364B

    return

label block_0000364B:
    # Node: 0000364B (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003653

    return

label block_00003653:
    # Node: 00003653 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003666

    return

label block_000027D6:
    # Node: 000027D6 (Schoolhouse 作哉 point)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (360, 160),"image": "images/Chapter 1/Menu/Sakuya point.png","hover": "images/Chapter 1/Menu/Sakuya hover.png","name": "作哉"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_276
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_000001FF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003653

    return

label block_000001FF:
    # Node: 000001FF (QUEST 翼)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_8F8B36DC5AD7424388BA16D0BF2B3B15 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀，技安！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_65C5ACF607854CBB86795C323016AB55 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "有事啊KUSO（混蛋）海。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2779DC2289E343EC94C9E662EA27E6A7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……啊，一之濑也……！"

    show rs_image_EC966F3B9F234F15B8767439A391E819 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……找我有事？"

    show rs_image_127AA1B3214F4C9AA59405C6A2B480FE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那个……这个……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_74FFA1FC7D7C4EDEB7565F683C1767BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F0988CA2235149BBB7560C242B59EA69 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊——？别磨了，听不见你想说什么。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的！为什么要说那么过分的话——"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A54AF084909148CF93001F0D50E1B057 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "因为很上火。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "技安真幼稚——为这种事就生气。"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_01A79D17F985408D9F6118A06A27BC50 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "再说一遍KUSO海！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你才是KUSO海！"

    if sys_effect2_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "必杀“{color=#FF0000}说别人是猪的人才是猪{/color}”！！{w}\n技安的姓『穂“{color=#0000FF}海{/color}”』也有这个字！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EC966F3B9F234F15B8767439A391E819 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你也很幼稚。再说了音节也对不上。"

    show rs_image_127AA1B3214F4C9AA59405C6A2B480FE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那个，作哉君。"

    show rs_image_74FFA1FC7D7C4EDEB7565F683C1767BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8DB1D821008C4432A73D25AC1E984DD1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……嗯？"

    show rs_image_127AA1B3214F4C9AA59405C6A2B480FE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这、这是……{w}老师给的要交给体育委员的东西……"

    show rs_image_74FFA1FC7D7C4EDEB7565F683C1767BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F8B36DC5AD7424388BA16D0BF2B3B15 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊。……这么一说我好像是被叫去了。"

    show rs_image_127AA1B3214F4C9AA59405C6A2B480FE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "事、事情就这么多，我就先……"

    show rs_image_74FFA1FC7D7C4EDEB7565F683C1767BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6E06652A48AE42A5A6FEDBA7DCF41808 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哦……{w}\n{nw}"
    show rs_image_392F8C96D4EE40B6BFF02A6941063BD5 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "谢……"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "混蛋！技安！就不知道对翼君说点什么？？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_01A79D17F985408D9F6118A06A27BC50 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……切。"
    if sys_effect2_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_ACB5D255F8CA4CF2A27FC6BD69B19D88 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "闭嘴！！\n天知道！！给我滚！！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校舍内"))

    if judge_lm_condition([]):
        jump block_00002B15

    return

label block_00002B15:
    # Node: 00002B15 (C1Q翼)
    $ C1QTsubasa = True
    $ QTsubasaCheck1 = False
    $ C1QTsubasaPhase = 0
    $ TalkTsubasaQTsubasaAfter = True

    if judge_lm_condition([]):
        jump block_00000206

    return

label block_00000206:
    # Node: 00000206 (QUEST FINISH)
    if sys_effect2_current_file != "sound/BGM/Quest Finished.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_effect2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00003653

    return

label block_000001C9:
    # Node: 000001C9 (Schoolhouse)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (360, 160),"image": "images/Chapter 1/Menu/Sakuya.png","hover": "images/Chapter 1/Menu/Sakuya hover.png","name": "作哉"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_277
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003653
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" },{ "scope": 1, "content": "TalkSakuya == 0" }]):
        jump block_000001F0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_000001F2

    return

label block_000001F0:
    # Node: 000001F0 (作哉１)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_8F8B36DC5AD7424388BA16D0BF2B3B15 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_EC966F3B9F234F15B8767439A391E819 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "出现了……果然又是你。"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就是我就是森海友啊！{w}\n……嗯？{w}“果然”是什么意思？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2A76BCBE9177431BA9BCAAC2C0678838 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "因为闻到了。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "闻！？什么？！{w}\n技安其实是狗？其实是狗么？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_65C5ACF607854CBB86795C323016AB55 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "就是狗又怎么了。{w}\n特别是你，老远就问到一股臭味。\n比其他人好认多了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么意思！{w}还是那么没礼貌！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A54AF084909148CF93001F0D50E1B057 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "闭嘴臭蛋。{w}\n你太臭了对狗是个负担。{w}\n鼻子都快塞了，一边去。"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么这么不讲道理……！{w}\n啊——不管了！还没见过这么烦人的狗！{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "呵——！！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校舍内"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000234

    return

label block_00000234:
    # Node: 00000234 (T ++)
    $ TalkSakuya = TalkSakuya + 1

    if judge_lm_condition([]):
        jump block_000001C9

    return

label block_000001F2:
    # Node: 000001F2 (作哉２)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_ACB5D255F8CA4CF2A27FC6BD69B19D88 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "给我滚！！咬死你信不信！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校舍内"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000001C9

    return

label block_00003648:
    # Node: 00003648 (TO: School door)

    if judge_lm_condition([]):
        jump block_000001C0

    return

label block_000001C0:
    # Node: 000001C0 (School door)
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

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("校门"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000001CA

    return

label block_000001CA:
    # Node: 000001CA (School door)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (96, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "屋外トイレへ"}, {"pos": (456, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "学校看板"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_278
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003652
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外トイレへ\"" }]):
        jump block_000001DD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学校看板\"" }]):
        jump block_00000219

    return

label block_000001DD:
    # Node: 000001DD (Outside toilet)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("室外厕所"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D5370D554F61451C806A39C7BC540968 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000001DE

    return

label block_000001DE:
    # Node: 000001DE (Outside toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (472, 192),"image": "images/Menu/Tokiwa.png","hover": "images/Menu/Tokiwa hover.png","name": "常磐"}, {"pos": (472, 192),"image": "images/Menu/Tokiwa.png","hover": "images/Menu/Tokiwa hover 2.png","name": "常磐"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_279
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000001C0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" },{ "scope": 1, "content": "FTokiwaHelp == True" }]):
        jump block_0000021B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase > 0" },{ "scope": 1, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase > 0" }]):
        jump block_000029B3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" }]):
        jump block_0000021C

    return

label block_0000021B:
    # Node: 0000021B (常磐 First)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_E6880BD53D33411C8F831E6238B3D5C5 as tag_3482C372784E44A89E382266A93F2B14 at center_bottom zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C223850065F6443080205D1F61C04C98 "呀，你好。看鞋子的颜色，你是二年级学生呐。{w}\n我是三年级的{color=#008A45}常磐进{/color}。"

    show rs_image_2917E94D246C4B5DBB7438FB372D005B as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C223850065F6443080205D1F61C04C98 "我喜欢打听一些各种各样的有趣的事情。{w}\n所以，如果你在寻找{color=#008080}事件{/color}或{color=#FF8000}委托{/color}时遇到了困难，\n来找我，我会给你一些{color=#FF0000}提示{/color}的。"

    show rs_image_C792083E91604DFD9FEB035D608ACFF9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C223850065F6443080205D1F61C04C98 "能帮上你的忙我也会很高兴的。\n待会见。"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外厕所"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_0000022E

    return

label block_0000022E:
    # Node: 0000022E (Cancel: First)
    $ FTokiwaHelp = False

    if judge_lm_condition([]):
        jump block_000001DE

    return

label block_000029B3:
    # Node: 000029B3 (常磐 Helpless)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 200
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 at center_bottom zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_C223850065F6443080205D1F61C04C98 "{color=#008080}事件{/color}或{color=#FF8000}委托{/color}的途中如果不知如何是好，\n就试着看看{color=#FF00FF}目标{/color}。{w=0.7}{nw}"
    show rs_image_2917E94D246C4B5DBB7438FB372D005B as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "加油哦。"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外厕所"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000001DE

    return

label block_0000021C:
    # Node: 0000021C (常磐)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 200
    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 at center_bottom zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_C223850065F6443080205D1F61C04C98 "怎么了？有什么在意的事情吗？"


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_0000021D:
    # Node: 0000021D (常磐 Help)
    call scb_selector("", [{"name":"フラグについて", "content":_("关于事件……")},{"name":"クエストについて", "content":_("关于委托……")},{"name":"なんでもない", "content":_("其实木有事")}]) from _call_scb_selector_31

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"なんでもない\"" }]):
        jump block_00002B3B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C1S1 == False" }]):
        jump block_00000220
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C1S2 == False" }]):
        jump block_000029B1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C1S3 == False" }]):
        jump block_000029B4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C1S4 == False" }]):
        jump block_000029B5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C1S5 == False" }]):
        jump block_000029B6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "C1QTsubasa == False" }]):
        jump block_000029BA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "C1QNewsclub == False" }]):
        jump block_000029BB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "C1QKimuraConference == False" }]):
        jump block_000029B7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "CXQSabuImechen == False" }]):
        jump block_000029BC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "CXQTsukiTest == False" }]):
        jump block_000029BD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "C1QMatsuta == False" },{ "scope": 2, "content": "C1S1 == True" }]):
        jump block_000029B8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "CXQShinoQuestion == False" },{ "scope": 2, "content": "C1SG1 == True" }]):
        jump block_0000021E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "C1QSabuShin == False" },{ "scope": 2, "content": "C1S4 == True" }]):
        jump block_000029BE
    if judge_lm_condition([]):
        jump block_000029B9

    return

label block_00002B3B:
    # Node: 00002B3B (Back)
    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外厕所"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000001DE

    return

label block_00000220:
    # Node: 00000220 (Flag 1)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "图书馆里的{color=#008A45}绫濑忍君{/color}\n好像有什么事情必须告诉你。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029B1:
    # Node: 000029B1 (Flag 2)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "去找中庭里的{color=#3A00C4}一之濑翼君{/color}说说话吧。\n那样肯定会发生有趣的事情的。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029B4:
    # Node: 000029B4 (Flag 3)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "先去找厕所里的{color=#AA0055}奥村慎太郎{/color}看看《人物笔记》，\n之后去别的看看再回去，好像会发生什么哦。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029B5:
    # Node: 000029B5 (Flag 4)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "校舍内的{color=#008A45}穗海作哉{/color}有事找你。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029B6:
    # Node: 000029B6 (Flag 5)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "去音乐室{color=#3A00C4}弹弹钢琴{/color}。会有人去拜访你的。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029BA:
    # Node: 000029BA (QUEST 翼)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "去音乐室{color=#FF8000}弹一下钢琴{/color}的话，\n就会有谁去拜访你哦。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029BB:
    # Node: 000029BB (新聞部任務)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "{color=#FF8000}新闻部活动室{/color}正在发生有趣的事情哦。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029B7:
    # Node: 000029B7 (木村討論會)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "首先先和{color=#FF8000}木村树君{/color}、{color=#FF8000}伊藤圭君{/color}、\n{color=#FF8000}松田健治君{/color}、{color=#FF8000}加藤准太君{/color}都谈一次话。"

    rs_character_C223850065F6443080205D1F61C04C98 "之后再和{color=#FF8000}木村君{/color}谈一次的话，\n好像就会邀请你参加一个有趣的活动哦。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029BC:
    # Node: 000029BC (三朗美髮店)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "屋顶上的{color=#FF8000}猫山三朗{/color}好像有事情想要拜托你呐。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029BD:
    # Node: 000029BD (阿月測眼力)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "去和楼梯间的{color=#FF8000}赤峰月君{/color}谈一下的话\n好像能进行什么测试的样子。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029B8:
    # Node: 000029B8 (QUEST 松田)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "体育馆里的{color=#FF8000}松田君{/color}似乎有事情想要拜托你。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_0000021E:
    # Node: 0000021E (小忍問題冊)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "去和图书馆里的{color=#FF8000}绫濑忍{/color}谈一下。\n他好像给你准备了有趣的游戏。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029BE:
    # Node: 000029BE (QUEST 三朗+慎太郎)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "先去和屋顶的{color=#FF8000}猫山三朗{/color}谈一下，\n之后再去厕所找{color=#FF8000}奥村慎太郎{/color}的话，\n一定会知道些什么的。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_000029B9:
    # Node: 000029B9 (No Help)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C223850065F6443080205D1F61C04C98 "现在已经没有什么其他有趣的事情了。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_0000021D

    return

label block_00000219:
    # Node: 00000219 (Board)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_3BE9AC227F0142FBAABEEB7605D6A3F9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}私立御咲学园是某县（省）的宝咲市所拥有的\n一所初高中男子校。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}……。\n……。\n重点是，{/color}"
    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    extend "{color=#0080FF}校内恋爱非常繁荣，赫赫有名。』{/color}"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide


    if judge_lm_condition([]):
        jump block_000001CA

    return

label block_00003785:
    # Node: 00003785 (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003790

    return

label block_00001FD4:
    # Node: 00001FD4 (Conversation F1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "加藤酱到底怎么了呐。{w}\n好——作为班长我必须去看看！"

    window hide

    $ set_window("(標準)")

    return

label block_00000D33:
    # Node: 00000D33 (Target F1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#008A45}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00000242:
    # Node: 00000242 (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_0000024B

    return

label block_0000024B:
    # Node: 0000024B (RESET)
    $ C1S1Phase = 0
    $ C1S2Phase = 0
    $ C1S3Phase = 0
    $ C1S4Phase = 0
    $ C1S5Phase = 0
    $ C1QTsubasaPhase = 0
    $ C1QSabushinPhase = 0
    $ C1QMatsutaPhase = 0

    if judge_lm_condition([]):
        jump block_00003651

    return

label block_00001FE0:
    # Node: 00001FE0 (Chatacter 友+翼)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E12C07C263114A53A918CA2B2E9A063D = 500
    show rs_image_35E25A60507C429F9D57B54949B277C1 as tag_E12C07C263114A53A918CA2B2E9A063D at center_bottom zorder zorder_tag_E12C07C263114A53A918CA2B2E9A063D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_ED234D4517E14A4EB0C635E1C4B85E12 = 500
    show rs_image_EC0A4B149A8A4350BF4B66268E95D844 as tag_ED234D4517E14A4EB0C635E1C4B85E12 at center_bottom zorder zorder_tag_ED234D4517E14A4EB0C635E1C4B85E12 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause

    hide tag_ED234D4517E14A4EB0C635E1C4B85E12
    hide tag_E12C07C263114A53A918CA2B2E9A063D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000224

    return

label block_000002B2:
    # Node: 000002B2 (Conversation Q翼)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为什么技安总喜欢欺负翼君呐。{w}\n明明这～么可爱的说！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……一定是我做错什么了。{w}\n…………{w}\n第一次见面时还是很温柔的……"

    window hide

    $ set_window("(標準)")

    return

label block_000002B3:
    # Node: 000002B3 (Target Q翼)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『把文件交给穗海作哉。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FE2:
    # Node: 00001FE2 (Character 友+慎太郎)
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

label block_000023D0:
    # Node: 000023D0 (Conversation Q三慎)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "上，犬五郎！把你的主人带到三酱那里去！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "汪、汪！"

    window hide

    $ set_window("(標準)")

    return

label block_00001FDE:
    # Node: 00001FDE (Character 友)
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

label block_000002F5:
    # Node: 000002F5 (School outside ACTA)
    if judge_lm_condition([{ "scope": 1, "content": "C1S2Phase == 1" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, True, talk_label="block_00000D32", target_label="block_00000D35") from _call_scb_global_map_73
    elif judge_lm_condition([{ "scope": 1, "content": "C1S3Phase == 1" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, True, talk_label="block_00001FD7", target_label="block_00000D35") from _call_scb_global_map_74
    elif judge_lm_condition([{ "scope": 1, "content": "C1S5Phase == 1" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, True, talk_label="block_000023CD", target_label="block_00000D35") from _call_scb_global_map_75
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, True, talk_label="block_000002B0", target_label="block_00000D35") from _call_scb_global_map_76
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00003665
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_0000365E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00003667
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00003649
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00003648
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00003785
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" },{ "scope": 1, "content": "C1S2Phase == 1" }]):
        jump block_0000367D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1S2Phase == 1" }]):
        jump block_00000D32
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00000D35
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00000242
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FDE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" }]):
        jump block_000025CB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1S3Phase == 1" }]):
        jump block_00001FD7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C1S5Phase == 1" }]):
        jump block_000023CD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000002B0

    return

label block_00000D32:
    # Node: 00000D32 (Conversation F2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "快点到放学后就好了呐♪"

    window hide

    $ set_window("(標準)")

    return

label block_00000D35:
    # Node: 00000D35 (Target F235)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『快进到{/color}{color=#FF8000}放学后{/color}{color=#0080FF}。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_000025CB:
    # Node: 000025CB (Twilight)
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
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"


    if judge_lm_condition([]):
        jump block_00003979

    return

label block_00003979:
    # Node: 00003979 (CP1 Twilight Misaki)
    call block_00000853 from _call_block_00000853_1

    if judge_lm_condition([]):
        jump block_000001B4

    return

label block_00001FD7:
    # Node: 00001FD7 (Conversation F3)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼。好期待放学后呐☆"

    window hide

    $ set_window("(標準)")

    return

label block_000023CD:
    # Node: 000023CD (Conversation F5)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍居然会邀请我一起，真稀奇。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天吃错什么东西了么？"

    window hide

    $ set_window("(標準)")

    return

label block_000002B0:
    # Node: 000002B0 (Conversation)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼～今天真是和平呐～"

    window hide

    $ set_window("(標準)")

    return

label block_000001B6:
    # Node: 000001B6 (School outside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "SYSReviewMode == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_000002B0", target_label="block_000031BC") from _call_scb_global_map_77
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1S1 and C1S2 and C1S3 and C1S4 and C1S5 == True" },{ "scope": 2, "content": "C1QTsubasa and C1QNewsclub and C1QKimuraConference and C1QMatsuta and CXQShinoQuestion and C1QSabuShin and CXQSabuImechen and CXQTsukiTest == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_000002B0", target_label="block_00002B1E") from _call_scb_global_map_78
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_000002B0", target_label="block_00001FDA") from _call_scb_global_map_79
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "SYSReviewMode == True" }]):
        jump block_000031BC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1S1 and C1S2 and C1S3 and C1S4 and C1S5 == True" },{ "scope": 2, "content": "C1QTsubasa and C1QNewsclub and C1QKimuraConference and C1QMatsuta and CXQShinoQuestion and C1QSabuShin and CXQSabuImechen and CXQTsukiTest == True" }]):
        jump block_00002B1E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00003665
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_0000365E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00003667
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00003649
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00003648
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00003785
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_000001B6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000002B0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001FDA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_000001B6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FDE

    return

label block_000031BC:
    # Node: 000031BC (Target dream)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『要想回到现实，请和鞋箱的触手A说。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00002B1E:
    # Node: 00002B1E (Target 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#3A00C4}下一个章节{/color}{color=#0080FF}正在等着！』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FDA:
    # Node: 00001FDA (Target 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『尽可能收集更多{/color}{color=#008080}事件{/color}{color=#0080FF}和{/color}{color=#FF8000}委托{/color}{color=#0080FF}！』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_000023D1:
    # Node: 000023D1 (Conversation Q松田)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "麻、麻烦了！不马上去阿月那里的话！"

    window hide

    $ set_window("(標準)")

    return

label block_000023CF:
    # Node: 000023CF (Target Q三慎)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『找到猫山三朗的所在之处。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_000023D2:
    # Node: 000023D2 (Target Q松田)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『尽快去把月找来！』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_0000022A:
    # Node: 0000022A (友+慎太郎)
    $ sys_ayumi_global_map_character = "tomo_shintaro"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_00000224

    return

label block_000018C1:
    # Node: 000018C1 (友)
    $ sys_ayumi_global_map_character = "tomo"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([{ "scope": 0, "content": "C1S2Phase == 1" },{ "scope": 0, "content": "C1S3Phase == 1" },{ "scope": 0, "content": "C1S5Phase == 1" }]):
        jump block_000002F5
    if judge_lm_condition([{ "scope": 0, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase > 0" },{ "scope": 0, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase > 0" }]):
        jump block_00000224
    if judge_lm_condition([]):
        jump block_000001B6

    return

