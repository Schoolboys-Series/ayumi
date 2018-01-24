# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00000F71 (CP1 Daytime Misaki 四朗)

label block_00000F72:
    # Node: 00000F72 (開始)
    $ ConversationState = 0
    $ ShoppingStreetEvent = False
    $ SpringWaterParkEvent = False
    $ HananoEvent = False
    $ RiverEvent = False

    if judge_lm_condition([]):
        jump block_00000F75

    return

label block_00000F75:
    # Node: 00000F75 (Misaki)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "shiro_tsubasachan"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_00000F76

    return

label block_00000F76:
    # Node: 00000F76 (Misaki XCTX)
    if judge_lm_condition([{ "scope": 1, "content": "ConversationState == 0" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", False, False, talk_label="block_00000F73", target_label="block_00000F74") from _call_scb_global_map_113
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", False, False, talk_label="block_0000192C", target_label="block_00000F74") from _call_scb_global_map_114
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲学園\"" }]):
        jump block_000024D7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"住宅街\"" }]):
        jump block_00000F77
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲駅\"" }]):
        jump block_00000FAF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" }]):
        jump block_00000F7A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" },{ "scope": 1, "content": "ShoppingStreetEvent == False" }]):
        jump block_00000F89
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" }]):
        jump block_000023D9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "ConversationState == 0" }]):
        jump block_00000F73
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_0000192C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00000F74
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00000F76
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"昼休み不可\"" }]):
        jump block_00000F76
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FBB

    return

label block_000024D7:
    # Node: 000024D7 (Misaki school)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不要不要！我不要回学校！"

    window hide

    if judge_lm_condition([]):
        jump block_00000F75

    return

label block_00000F77:
    # Node: 00000F77 (Residential street)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000F7D

    return

label block_00000F7D:
    # Node: 00000F7D (Residential street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (552, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (696, 360),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_442
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00000F99
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003670
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000F91

    return

label block_00000F99:
    # Node: 00000F99 (Square)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3B5A1C5EC3AA4BC08F04842878E1A1F0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000F9A

    return

label block_00000F9A:
    # Node: 00000F9A (Square)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (624, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "泉の公園"}, {"pos": (120, 328),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "？？？"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_443
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉の公園\"" },{ "scope": 1, "content": "SpringWaterParkEvent == False" }]):
        jump block_00000FA6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉の公園\"" }]):
        jump block_000023DA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"？？？\"" }]):
        jump block_00000F9B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000F77

    return

label block_00000FA6:
    # Node: 00000FA6 (Spring water park)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4C85C2BFFE134BFDADEC528506A90841 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000FA7

    return

label block_00000FA7:
    # Node: 00000FA7 (Spring water park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (368, 168),"image": "images/Menu/Nori.png","hover": "images/Menu/Nori hover.png","name": "朔"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_444
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000F99
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"朔\"" }]):
        jump block_00000FAD

    return

label block_00000FAD:
    # Node: 00000FAD (朔１)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D7B35A9D4B274A52A4297801D3F24C5B as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_bottom zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_3C5D0D4B799A4546B33A77278DFD1EB2 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_bottom zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯？\n这个人！和我有一样的气味！{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_C27A7CEBB53D42A2BA196ABBF51FA578 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "为什么呐？？（闻）……！"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_0F53470581014EDC915440D02B59BEA0 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_bottom zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_62324AD297554FE987C680452CEE232E "呜哇！？突然干什么！{w}\n{nw}"
    show rs_image_B1728541CB614DC3B3B8761531DAF257 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "嗯？这身衣服为什么会在你……"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "回来！！对不认识的人干什么！！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "快走了！{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "对不起给你添麻烦了！\n请容我们告退！"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 0.8

    $ set_place_title(_("广场"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3B5A1C5EC3AA4BC08F04842878E1A1F0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002B05

    return

label block_00002B05:
    # Node: 00002B05 (SpringWaterParkEvent)
    $ SpringWaterParkEvent = True

    if judge_lm_condition([]):
        jump block_00000F9A

    return

label block_000023DA:
    # Node: 000023DA (朔2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "刚才那个人很生气的样子，\n先不要过去了！"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3C5D0D4B799A4546B33A77278DFD1EB2 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "欸——！明明气味一样，\n还以为会是同伴的说——！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("广场"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000F9A

    return

label block_00000F9B:
    # Node: 00000F9B (Forest)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7D781D05099A4C93AF6B1D005359F3E9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000F9C

    return

label block_00000F9C:
    # Node: 00000F9C (Forest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_445
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000F99

    return

label block_00003670:
    # Node: 00003670 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_0000366F

    return

label block_0000366F:
    # Node: 0000366F (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00000F75

    return

label block_00000F91:
    # Node: 00000F91 (Residential street turning)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A4E74E94E7C549809795CEBC732E6326 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000F92

    return

label block_00000F92:
    # Node: 00000F92 (Residential street turning)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (120, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "花乃湯"}, {"pos": (512, 320),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "神社"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_446
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"花乃湯\"" }]):
        jump block_00000F9F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"神社\"" }]):
        jump block_00000F9D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000F77

    return

label block_00000F9F:
    # Node: 00000F9F (花乃湯)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BB828FFB3AED43E6BB07C3169278015F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "HananoEvent == False" }]):
        jump block_00002B3E
    if judge_lm_condition([]):
        jump block_00000FA0

    return

label block_00002B3E:
    # Node: 00002B3E (HananoEvent)
    $ HananoEvent = True

    if judge_lm_condition([]):
        jump block_000023DB

    return

label block_000023DB:
    # Node: 000023DB (Sub event)
    pause 0.3

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    pause 0.5

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_E7FB89F14D554B59971676B5C3A3F54D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不知道为什么，这栋建筑物里\n有一种令人镇定下来的气氛呐！"

    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这里是澡堂。我还一次都没来过呢。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "说起来，哥哥和父亲都来过，\n而且大喊着“再也不来了”，为什么呢。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000FA0

    return

label block_00000FA0:
    # Node: 00000FA0 (花乃湯)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "ポスター"}, {"pos": (80, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_447
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000F91
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000FAB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ポスター\"" }]):
        jump block_00001F76

    return

label block_00000FAB:
    # Node: 00000FAB (River)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_788AB1D278244B129D0C9F9230156AD7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "RiverEvent == False" }]):
        jump block_00002B08
    if judge_lm_condition([]):
        jump block_00002933

    return

label block_00002B08:
    # Node: 00002B08 (RiverEvent)
    $ RiverEvent = True

    if judge_lm_condition([]):
        jump block_0000192D

    return

label block_0000192D:
    # Node: 0000192D (向左向右看)
    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    stop music fadeout 2
    $ sys_music_current_file = ""

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    stop music2 fadeout 0.5
    $ sys_music2_current_file = ""

    pause 2

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7E3D907127E64F2DB3E6C14E4C1388FF as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "姆——！{nw}"
    if sys_music_current_file != "sound/BGM/Ailurus fulgens.ogg":
        play music "sound/BGM/Ailurus fulgens.ogg" loop
        $ sys_music_current_file = "sound/BGM/Ailurus fulgens.ogg"

    extend ""

    if sys_effect2_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "！？！？\n这是什么！？野、野生的狸猫！？？"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_298F816878E34C759D6E19B5B8CBCCC8 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EDF48057FB84D428D56198A69E2880E "姆呼——姆呼、呼！"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_E7FB89F14D554B59971676B5C3A3F54D as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "啊♪是{color=#FF8000}贝——{/color}！好久不见♪"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_7F5086B0A4E249BF8230B6A6D47A3C3F as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆呼姆呼♪"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸，翼桑认识这只狸猫？"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_79EEC8AD62B24332A4A9362795A61DC8 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不是狸猫是小熊猫哦！是我的朋友哦！"

    show rs_image_C27A7CEBB53D42A2BA196ABBF51FA578 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "贝——，我来介绍。\n这是人类“四朗”哦，是我的新朋友！"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_47F53B04B0F54144A4CB509D966110C3 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆呼——呼呼！"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E7FB89F14D554B59971676B5C3A3F54D as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "他说“请多关照”哦。\n能好好相处就好了呐四朗——！"

    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸、哦……请多指教……"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7F5086B0A4E249BF8230B6A6D47A3C3F as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆吼姆吼！"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_79EEC8AD62B24332A4A9362795A61DC8 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "对的对的，是那样的哦！\n来玩游戏哦！四朗也要来！{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_B482954028BA467A9D2603A10B6B5EE3 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "开始了哦——！{color=#FF8000}“向左向右看♪”{/color}"

    window hide

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_E36043F8C80E4415B6B2D5553D497F8B

    pause 0.8


    if judge_lm_condition([]):
        jump block_000024E2

    return

label block_000024E2:
    # Node: 000024E2 (向左向右看)
    call block_00002493 from _call_block_00002493_2

    if judge_lm_condition([]):
        jump block_00002933

    return

label block_00002933:
    # Node: 00002933 (River 貝ー)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (336, 352),"image": "images/Menu/Be-- river.png","hover": "images/Menu/Be-- river hover.png","name": "ベー"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_448
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000F9F
    if judge_lm_condition([]):
        jump block_00002934

    return

label block_00002934:
    # Node: 00002934 (貝ー)
    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_7F5086B0A4E249BF8230B6A6D47A3C3F as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆呼——呼呼♪"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_79EEC8AD62B24332A4A9362795A61DC8 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "“再来玩哦”这样说的！"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("河边"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"


    if judge_lm_condition([]):
        jump block_00002933

    return

label block_00001F76:
    # Node: 00001F76 (Poster)
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
        jump block_00000FA0

    return

label block_00000F9D:
    # Node: 00000F9D (神社)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_65FB514C0D3B40558703DF2D35F42E17 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000F9E

    return

label block_00000F9E:
    # Node: 00000F9E (神社)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_449
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000F91

    return

label block_00000FAF:
    # Node: 00000FAF (Misaki station)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_07BACEE3C1C64F1DAD61CD240DF0C2E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000FB3

    return

label block_00000FB3:
    # Node: 00000FB3 (Misaki station)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (336, 352),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_450
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000F75
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000FBC

    return

label block_00000FBC:
    # Node: 00000FBC (Inside)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_E7FB89F14D554B59971676B5C3A3F54D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哇！这里面有什么呢——！"

    if sys_effect_current_file != "sound/Effect Sound/Key 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Key 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Key 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}KA{/size}{size=28}{b}！{/b}{/size}"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_DCB59A032B7444DFAAC956549741C4BB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "咦！？被关在外面了！"

    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "没买票当然，{w}去其他地方了。"

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3C5D0D4B799A4546B33A77278DFD1EB2 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "好～的。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("御咲站"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000FB3

    return

label block_00000F7A:
    # Node: 00000F7A (Park)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AC1A95BA21694004A67885C809E98CFF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000F7E

    return

label block_00000F7E:
    # Node: 00000F7E (Park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (160, 184),"image": "images/Chapter 1/Menu/Kobayashi point.png","hover": "images/MENU/Kobayashi hover.png","name": "小林"}, {"pos": (320, 184),"image": "images/Chapter 1/Menu/Minami point.png","hover": "images/MENU/Minami hover.png","name": "南"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_451
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000F75
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" }]):
        jump block_000036F5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" }]):
        jump block_000036F5

    return

label block_000036F5:
    # Node: 000036F5 ()
    $ del ConversationState
    $ del ShoppingStreetEvent
    $ del SpringWaterParkEvent
    $ del HananoEvent
    $ del RiverEvent

    return

label block_00000F89:
    # Node: 00000F89 (Shopping street 1)
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

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5F022B91486841699EAC5FE3BDC0F5CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B482954028BA467A9D2603A10B6B5EE3 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_bottom zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哇——！哇——♪哇——☆"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "稍、稍微冷静一点。"

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E7FB89F14D554B59971676B5C3A3F54D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "因为我还是第一次来这里嘛！{w}\n{nw}"
    show rs_image_3C5D0D4B799A4546B33A77278DFD1EB2 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "以前想来的时候都会被\n“不行——”这样怒吼的说。"

    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不会有那么莫名其妙的事。{w}\n……啊，翼桑快看！那边在拍电视节目！"

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_83F2ED08764F40D5B62DD199AB889D39 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "电视？"

    window hide

    pause 0.6

    stop music fadeout 2
    $ sys_music_current_file = ""

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1.4

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D5FE65484D524DF0ACA6C31DC2F622E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 200
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_1561FC74CECA43F896E80A6050FD4EB8 as tag_0C07D2341065492CB0EDF00452D574E1 at right_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    $ set_window("イベントモード")
    if sys_music2_current_file != "sound/BGM/Manzai.ogg":
        play music2 "sound/BGM/Manzai.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Manzai.ogg"

    pause 0.3

    window show

    rs_character_7C178421D3DA4E2CB70D4336919888FB "好的，今天的“好孩子！”也要开始了！{w}\n主持是我，杉本！以及……"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "我是陆田！"

    show rs_image_09DED7760EFE4B239C4CB18C936E91D7 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "今天我们来到了那座因所有出演者都是男性的有名的\n宝咲歌剧院所在的宝咲附近的御咲哦。"

    show rs_image_A6BDA5B155414D99AB52F15BEBCC03D6 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "究竟会在这里遇到什么样的事情呢，敬请期待！"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不过啊，御咲这座城镇真的被独特的气氛包围着呐。\n说起来，那个传闻是真的？"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "男性和男性{size=16}……{/size}"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_0C07D2341065492CB0EDF00452D574E1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_5F022B91486841699EAC5FE3BDC0F5CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_CBD2AF53D136432CA26466E5BD1ED8E7 as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "那是什么呀！奇怪的一群人哦！\n拿着奇怪的箱子（摄影机）和奇怪的棒子（话筒）呐！"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "等等！翼桑！声音太大了！会妨碍到他们的！"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_81749C79DF1A40F3BF020F0ACBD64CA8 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=460, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_98373C4281014E34B4600634ECD299A4 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=280, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 300
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_C8A2A17D9A5D48678ABA0AF50A691023 as tag_0C07D2341065492CB0EDF00452D574E1 at Transform(xpos=80, yalign=0.0) zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.2

    rs_character_7C178421D3DA4E2CB70D4336919888FB "哦呀？这么快就发现两位可爱的男孩子了♪\n和传闻一样美少年很多呢！"

    show rs_image_A6BDA5B155414D99AB52F15BEBCC03D6 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "请多关照，是放学回家？请问如何称呼？"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_98373C4281014E34B4600634ECD299A4 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=460, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_356ECD8406BB49698A4D9CAD3C494C73 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=280, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "诶，啊，嗯！我是御咲小学六年级二班的猫山四朗。"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "啊啦啊啦♪知书达理的男孩子！\n健康的肤色和短发！闪耀着的眼睛和决定性的短裤！"

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "电视机前的某些观众肯定无比兴奋了！"

    show rs_image_EAA2EF7FB3CF4DC8B7F90D9F76D373E7 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "瞎说什么呢。{w}\n{nw}"
    show rs_image_11BEE6BBB8CC4F83AB49ED12C7653EDB as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "请问旁边那位，该怎么称呼？"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=460, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=280, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "我吗？那个、我叫翼哦！饲主是作哉！"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_81749C79DF1A40F3BF020F0ACBD64CA8 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_6B387DE0988444BA9024CD57D9D7D7D2 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    show rs_image_D7414D2091574B1EB8E73CCE2D059C48 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E0C80C17CC249E2A7A71BB4349C957B "饲主！？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哇——！！请、请不要在意！！这、这只是他独有的玩笑！！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_AE2879D336AC4FEF9997D54F17B41E88

    rs_character_3B4C660F421B4BE392BB540B580F0339 "翼桑这个笨蛋笨蛋！不许在电视机前败坏前辈的名誉！"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呐——呐——四朗！这些人都是好人哦！{w}\n没有责怪一开始我们的大声叫喊哦！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "刚才对你们大叫对不起！我会帮你们舔干净的原谅我们——！"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    $ zorder_tag_8D4484ABFF9C41728D11D060291F5AA6 = 200
    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 300
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_8D4484ABFF9C41728D11D060291F5AA6 at Transform(xpos=280, yalign=0.0) zorder zorder_tag_8D4484ABFF9C41728D11D060291F5AA6 onlayer master
    show rs_image_D7FF18D0A8E140CE95D5B9C6EE2CC48D as tag_0C07D2341065492CB0EDF00452D574E1 at Transform(xpos=80, yalign=0.0) zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "诶！？哇、哇啊啊！？{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_8D4484ABFF9C41728D11D060291F5AA6
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "突然做什么！？好、好、好痒！快住手快住手！"

    if sys_effect2_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D7414D2091574B1EB8E73CCE2D059C48 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "呀啊啊啊！为什么要这么做！？快起来！给我起来——！"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "哦哦！意料之外的突发事件！这下子收视率肯定上去了♪\n陆田君也很高兴的样子完全没有问题呐！"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这、这、这不是直播对不对！？一定不是！！\n请把这些镜头全部剪掉！拜托了！"

    window hide

    pause 0.9

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    stop music2 fadeout 1.5
    $ sys_music2_current_file = ""

    pause 1.8


    if judge_lm_condition([]):
        jump block_00002B03

    return

label block_00002B03:
    # Node: 00002B03 (ShoppingStreetEvent)
    $ ShoppingStreetEvent = True

    if judge_lm_condition([]):
        jump block_00003670

    return

label block_000023D9:
    # Node: 000023D9 (Shopping street 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不许再去商店街了。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "欸——！好不容易变成人类了的说！"

    window hide


    if judge_lm_condition([]):
        jump block_00000F75

    return

label block_00000F73:
    # Node: 00000F73 (Conversation 1)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "散步好高兴♪"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "等等，翼桑，不是那边是这边！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唉……看来真的需要找根绳牵着啊。"

    window hide

    $ set_window("(標準)")

    return

label block_00002B02:
    # Node: 00002B02 (ConversationState: 1)
    $ ConversationState = 1

    if judge_lm_condition([]):
        jump block_00000F76

    return

label block_0000192C:
    # Node: 0000192C (Conversation 2)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪！汪！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不要乱叫！！{w}\n……到底为什么要叫啊。"

    window hide

    $ set_window("(標準)")

    return

label block_00002B04:
    # Node: 00002B04 (ConversationState: 0)
    $ ConversationState = 0

    if judge_lm_condition([]):
        jump block_00000F76

    return

label block_00000F74:
    # Node: 00000F74 (Target)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『带小翼到处去玩玩。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FBB:
    # Node: 00001FBB (Character)
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

