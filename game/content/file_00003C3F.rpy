# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003C3F (CP2 Daytime Hotel 朔)

label block_00003C40:
    # Node: 00003C40 ()
    $ TalkTentacleAF6 = False
    $ TalkTentacleBF6 = False

    if judge_lm_condition([]):
        jump block_00003C41

    return

label block_00003C41:
    # Node: 00003C41 (Hotel)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Hotel 1.ogg":
        play music "sound/BGM/Hotel 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "nori"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_00003C44

    return

label block_00003C44:
    # Node: 00003C44 (Hotel XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "hotel", False, False, talk_label="block_00003C45", target_label="block_00003C4E") from _call_scb_global_map
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00003C44
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00003C44
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00003C4E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00003C45
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ロビー\"" }]):
        jump block_00003C42
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00003C54

    return

label block_00003C4E:
    # Node: 00003C4E (Target)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『去找酒店的主人。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003C45:
    # Node: 00003C45 (Conversation)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_62324AD297554FE987C680452CEE232E "…………"

    window hide

    $ set_window("(標準)")

    return

label block_00003C42:
    # Node: 00003C42 (Lobby)
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
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("大厅"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F1E694F9D98E4371B8F767497249ECEE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003C43

    return

label block_00003C43:
    # Node: 00003C43 (Lobby)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (248, 216),"image": "images/Chapter 2/Menu/F6/Tentacle-earthworm.png","hover": "images/Chapter 2/Menu/F6/Tentacle-earthworm hover.png","name": "触手A"}, {"pos": (464, 216),"image": "images/Chapter 2/Menu/F6/Tentacle-starfish.png","hover": "images/Chapter 2/Menu/F6/Tentacle-starfish hover.png","name": "触手B"}, {"pos": (144, 264),"image": "images/MOVING/ACTIONS/Moving 4.png","hover": "images/MOVING/ACTIONS/Moving 4 hover.png","name": "広間"}, {"pos": (632, 248),"image": "images/MOVING/ACTIONS/Moving 4.png","hover": "images/MOVING/ACTIONS/Moving 4 hover.png","name": "食堂"}, {"pos": (640, 32),"image": "images/MOVING/ACTIONS/Moving 4.png","hover": "images/MOVING/ACTIONS/Moving 4 hover.png","name": "廊下"}, {"pos": (376, 32),"image": "images/MOVING/ACTIONS/Moving 3.png","hover": "images/MOVING/ACTIONS/Moving 3 hover.png","name": "主"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"広間\"" }]):
        jump block_00003C4B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"食堂\"" }]):
        jump block_00003C4A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00003C4D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003C41
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"主\"" }]):
        jump block_00003C50
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手A\"" },{ "scope": 1, "content": "TalkTentacleAF6 == True" }]):
        jump block_00003C52
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手A\"" }]):
        jump block_00003C47
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手B\"" },{ "scope": 1, "content": "TalkTentacleBF6 == True" }]):
        jump block_00003C55
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手B\"" }]):
        jump block_00003C51

    return

label block_00003C4B:
    # Node: 00003C4B (Room large)
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

    $ set_place_title(_("休息室"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0042BB20CCDD47659859214E44A4ACEB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003C4C

    return

label block_00003C4C:
    # Node: 00003C4C (Room large)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_1
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003C42

    return

label block_00003C4A:
    # Node: 00003C4A (Dining room)
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

    $ set_place_title(_("餐厅"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0FFAFB81CEF94E09AE209050BCCD9627 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003C58

    return

label block_00003C58:
    # Node: 00003C58 (Dining room)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (336, 208),"image": "images/Chapter 2/Menu/F6/Item 3.png","hover": "images/Chapter 2/Menu/F6/Item 3 hover.png","name": "人形"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_2
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003C42
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"人形\"" }]):
        jump block_00003C56

    return

label block_00003C56:
    # Node: 00003C56 (Doll)
    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_29FBADE3ABAF49A397417CC9873A8C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……说起来还真能做得到呐。{w}\n只是这个布偶是在是太身长腿短了，\n很难活动。"

    rs_character_62324AD297554FE987C680452CEE232E "好几次都差点要原地转圈了。"

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("大厅"))

    if judge_lm_condition([]):
        jump block_00003C58

    return

label block_00003C4D:
    # Node: 00003C4D (Aisle)
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

    $ set_place_title(_("二楼走廊"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D0D6BB8ECA3845E1834C17E7B58AE5EB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003C4F

    return

label block_00003C4F:
    # Node: 00003C4F (Aisle)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (552, 224),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "額縁"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_3
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003C42
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"額縁\"" }]):
        jump block_00003C5A

    return

label block_00003C5A:
    # Node: 00003C5A (Letter)
    show rs_image_29FBADE3ABAF49A397417CC9873A8C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_62324AD297554FE987C680452CEE232E "……有一张纸夹在里面。"

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    rs_character_62324AD297554FE987C680452CEE232E "……。"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8FDE67688F4540199AB99417908CBF4D "{color=#800040}『房间一览表上“Sweet Room”写错了哦。\n还是和原来一样，我很安心哦♪』{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    show rs_image_29FBADE3ABAF49A397417CC9873A8C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "唔……那不是我是触手写的。{w}真气人。"

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二楼走廊"))

    if judge_lm_condition([]):
        jump block_00003C4F

    return

label block_00003C50:
    # Node: 00003C50 (Room main)
    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ set_place_title(_("主房前"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_835DAD3C655F4DBB95F23A9F8C21051B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003C59

    return

label block_00003C59:
    # Node: 00003C59 (Room main)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (368, 96),"image": "images/MOVING/ACTIONS/Moving 3.png","hover": "images/MOVING/ACTIONS/Moving 3 hover.png","name": "主"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_4
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003C42
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"主\"" }]):
        jump block_00003C53

    return

label block_00003C53:
    # Node: 00003C53 (終了)
    $ del TalkTentacleAF6
    $ del TalkTentacleBF6

    return

label block_00003C52:
    # Node: 00003C52 (触手A 2)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    show rs_image_5171C4277664485482367CFD06553623 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_466219A035C44D62AD2743E9F494A2F2 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_FB87619C890441AEA41E279A1B588CAC "快快，那位大人正在房间里等着呐，\n请快点过去。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("大厅"))

    if judge_lm_condition([]):
        jump block_00003C43

    return

label block_00003C47:
    # Node: 00003C47 (触手A)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    show rs_image_5171C4277664485482367CFD06553623 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_A7C4CBC5126342CD8A04FA3A8072EE5F as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_FB87619C890441AEA41E279A1B588CAC "朔大人，前几天的演戏实在是非常棒。\n能完成计划真是太恭喜了。"

    show rs_image_29FBADE3ABAF49A397417CC9873A8C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "还没完全完成。\n必须要确认那个人是不是真的满意了。"

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5171C4277664485482367CFD06553623 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_FB87619C890441AEA41E279A1B588CAC "哦呀哦呀，那可要快点去呐。\n"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_FBB2DF0BB74746A29EA713F11F92C1A4 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……希望那件事能不要被在意。"

    show rs_image_29FBADE3ABAF49A397417CC9873A8C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……{w}我明白。"

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A7C4CBC5126342CD8A04FA3A8072EE5F as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_FB87619C890441AEA41E279A1B588CAC "就算不常在一起也算是朔大人身边的人，\n某种程度上请把握好分寸哦。"

    show rs_image_29FBADE3ABAF49A397417CC9873A8C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "嗯，其实没什么……\n那只是一时兴起罢了。"

    rs_character_62324AD297554FE987C680452CEE232E "这之上这之下的事情都不会有，不要误解了。"

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_466219A035C44D62AD2743E9F494A2F2 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_FB87619C890441AEA41E279A1B588CAC "呼呼呼。在下明白了。\n最近，朔大人的一时兴起还真是多呢。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("大厅"))

    if judge_lm_condition([]):
        jump block_00003C49

    return

label block_00003C49:
    # Node: 00003C49 (T ++)
    $ TalkTentacleAF6 = True

    if judge_lm_condition([]):
        jump block_00003C43

    return

label block_00003C55:
    # Node: 00003C55 (触手B２)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    show rs_image_E13853D2180E41B9ACC256B3BB300547 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_89A27AFA4F7E47CC9A112A624C28664F as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_740EF5739095488C9C0AA2EF1A78CB35 "和那个人谈话时请务必把我们的报酬也包括在内！"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("大厅"))

    if judge_lm_condition([]):
        jump block_00003C43

    return

label block_00003C51:
    # Node: 00003C51 (触手B)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    show rs_image_E13853D2180E41B9ACC256B3BB300547 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_82701B6A5D3A481EA46BEB07FBCD3DEE as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_740EF5739095488C9C0AA2EF1A78CB35 "啊——身上到处都疼……肌肉也疼。"

    show rs_image_29FBADE3ABAF49A397417CC9873A8C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "也是别无他法，{w}\n本来那并不是你们通常的使用方法。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8E0497C6CBFB4101A6F299814800A568 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_740EF5739095488C9C0AA2EF1A78CB35 "不，可是，有点高兴呢。\n我很憧憬前辈们集合在一起巨大化的姿态。"

    show rs_image_29FBADE3ABAF49A397417CC9873A8C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "而且，做的也不错。"

    rs_character_62324AD297554FE987C680452CEE232E "结果，直到最后也没人发现导游其实是触手的集合体。"

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AABC61A64D824347A6C9F24EC2351CC3 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_740EF5739095488C9C0AA2EF1A78CB35 "被扫帚打的时候很难受不过，\n本来那东西就不怎么结实，\n真是帮大忙了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_72BE0B1E9DFC429CBD1C3DDA16C6FAD9 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_740EF5739095488C9C0AA2EF1A78CB35 "这次我很努力了，我会期待报酬的！"

    show rs_image_29FBADE3ABAF49A397417CC9873A8C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "没能趁乱打劫？"

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_82701B6A5D3A481EA46BEB07FBCD3DEE as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_740EF5739095488C9C0AA2EF1A78CB35 "最开始的那个孩子还勉勉强强……\n后面的根本就没这个余力……"

    show rs_image_29FBADE3ABAF49A397417CC9873A8C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "这还请节哀。"

    rs_character_62324AD297554FE987C680452CEE232E "不过，再怎么说\n这次他们是客人，我们是员工。{w}\n这次就接受现状了。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_9AD26C1731624773BC6D95775F8CD478 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("大厅"))

    if judge_lm_condition([]):
        jump block_00003C5B

    return

label block_00003C5B:
    # Node: 00003C5B (T ++)
    $ TalkTentacleBF6 = True

    if judge_lm_condition([]):
        jump block_00003C43

    return

label block_00003C54:
    # Node: 00003C54 (Character)
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

