# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00002B80 (朔洞窟)

label block_00002B81:
    # Node: 00002B81 ()
    $ CaveRandomResult = 0

    if judge_lm_condition([]):
        jump block_00002B83

    return

label block_00002B83:
    # Node: 00002B83 (Cave)
    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.5

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    stop effect3 fadeout 0.7
    $ sys_effect3_current_file = ""

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
    show rs_image_2AFA63D89C89459BA222524E0ABC7F77 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002B82

    return

label block_00002B82:
    # Node: 00002B82 (Cave)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (408, 312),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "洞窟へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.5, 0.2) from _call_lm_menu_781
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"洞窟へ\"" }]):
        jump block_00002B86
    if judge_lm_condition([]):
        jump block_00002C24

    return

label block_00002B86:
    # Node: 00002B86 (Cave near)
    stop effect2 fadeout 0.7
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_music2_current_file != "sound/BGM/Nori cave.ogg":
        play music2 "sound/BGM/Nori cave.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Nori cave.ogg"

    $ set_place_title(_("洞窟"))
    show rs_image_8FCB009B37544F0CBE00E320317FE419 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Cave 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cave 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Cave 1.ogg"


    if judge_lm_condition([]):
        jump block_00002B85

    return

label block_00002B85:
    # Node: 00002B85 (Cave near)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (384, 272),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "洞窟へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_782
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"洞窟へ\"" },{ "scope": 1, "content": "FEnterDream == False" }]):
        jump block_00002BC8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"洞窟へ\"" },{ "scope": 1, "content": "IsCaveMemoAvailable == True" }]):
        jump block_00003CC5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"洞窟へ\"" }]):
        jump block_00003CC6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00002B83

    return

label block_00002BC8:
    # Node: 00002BC8 (Skip)

    if judge_lm_condition([]):
        jump block_00002BC7

    return

label block_00002BC7:
    # Node: 00002BC7 (選擇)
    call scb_selector(_("是否跳过寻路？"), [{"name":"はい", "content":_("好的没问题")}, {"name":"いいえ", "content":_("中途还有东西没拿到呢")}]) from _call_scb_selector_84

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002BAB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" },{ "scope": 1, "content": "IsCaveMemoAvailable == True" }]):
        jump block_00003CC5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00003CC6
    if judge_lm_condition([]):
        jump block_00002B85

    return

label block_00002BAB:
    # Node: 00002BAB (Cave inside)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_62272429BE0E491AB48B3734A8ECF1EF
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_8382B2402B5D44C5B31249AF7209A499 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002BAA

    return

label block_00002BAA:
    # Node: 00002BAA (Cave inside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (384, 304),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "洞窟へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_783
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00002B83
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"洞窟へ\"" },{ "scope": 1, "content": "FEnterDream == True" }]):
        jump block_00003CD0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"洞窟へ\"" }]):
        jump block_00002BD5

    return

label block_00003CD0:
    # Node: 00003CD0 (Cancel: First)
    $ FEnterDream = False

    if judge_lm_condition([]):
        jump block_00002C29

    return

label block_00002C29:
    # Node: 00002C29 (朔 Home First)
    $ set_window("イベントモード")
    stop music2 fadeout 1.5
    $ sys_music2_current_file = ""

    stop effect2 fadeout 1.5
    $ sys_effect2_current_file = ""

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5E4B22942A284109B65800E46DBB8782 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    if sys_music2_current_file != "sound/BGM/Hotel 2.ogg":
        play music2 "sound/BGM/Hotel 2.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Hotel 2.ogg"

    pause 0.9

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 200
    show rs_image_EDB46CC6778D4FE0858464DE11647DF8 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_62324AD297554FE987C680452CEE232E "还以为是谁，原来是{color=#00FFFF}那时{/color}的弃子……{w}记忆确实应当消除了，\n不过是怎么找到这里来的呢。"

    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "真是的，那时候拜你所赐可真是难堪。"

    show rs_image_3149C4BF55744A498D9A6BE1CAAF3483 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "本想说不想看到你……{w=0.6}{nw}"
    show rs_image_1D53D375130B48DEA5EC714EDF7E13DD as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "算你运气好，\n今天我心情很不错。"

    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_62324AD297554FE987C680452CEE232E "其实，某个实验刚刚成功了。{w}\n{w=0.4}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.3

    extend "……你，现在有没有{color=#AA0055}想做的梦{/color}？"

    pause 0.3

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    rs_character_62324AD297554FE987C680452CEE232E "思念的力量可以化为能量。\n这股力量终究将会推动文明进步发展。"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Battle 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 2.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 200
    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    show rs_image_413C8C98D42C410191B4808466E63981 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 0.3

    rs_character_62324AD297554FE987C680452CEE232E "来这边。特别给你看个有意思的东西。{w}\n这是从某神社取到的梦的样本。"

    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "欸？想要看{color=#FF80C0}回到少年时代参加学园祭{/color}的梦？\n"
    show rs_image_1D53D375130B48DEA5EC714EDF7E13DD as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "呵呵，那个下次再说……"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_6D71784C723F4F21A0E2717D3503E19E as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "祝你顺利。希望你在{color=#00FFFF}某人{/color}梦的世界里安好。"

    window hide

    pause 0.7

    stop music2 fadeout 2.5
    $ sys_music2_current_file = ""

    $ set_place_title(False)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 0.8


    if judge_lm_condition([]):
        jump block_00002C3B

    return

label block_00002C3B:
    # Node: 00002C3B (Random)
    $ CaveRandomResult = Random(8)

    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 0" }]):
        jump block_00002C2B
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 1" }]):
        jump block_00002C2E
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 2" }]):
        jump block_00002C32
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 3" }]):
        jump block_00002C2F
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 4" }]):
        jump block_00002C38
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 5" }]):
        jump block_00002C37
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 6" }]):
        jump block_00002C39
    if judge_lm_condition([]):
        jump block_00002C3A

    return

label block_00002C2B:
    # Node: 00002C2B (友)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_top zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_6A29046AAF4844D9A3A453B1C6A13175

    pause 0.4


    if judge_lm_condition([]):
        jump block_00002C2A

    return

label block_00002C2A:
    # Node: 00002C2A (Name)
    $ _lm_input_result = lm_input(_("告诉我名字好不好ーー！"), [_("姓氏"), _("名字")], [persistent.LastName, persistent.FirstName])
    $ persistent.LastName = _lm_input_result[0]
    $ persistent.FirstName = _lm_input_result[1]
    $ del _lm_input_result

    if judge_lm_condition([]):
        jump block_00002C2C

    return

label block_00002C2C:
    # Node: 00002C2C (Dream)
    pause 0.5

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_20A8817D51644BE6A7913BD30673F110

    pause 1


    if judge_lm_condition([]):
        jump block_00002BC2

    return

label block_00002BC2:
    # Node: 00002BC2 (Dream)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music2_current_file != "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg":
        play music2 "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg"

    $ set_place_title(False)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_00002BC4

    return

label block_00002BC4:
    # Node: 00002BC4 (Dream)
    call scb_global_map("daytime", "empty", "dream", False, True, False, False, break_confirm=False) from _call_scb_global_map_178

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"室内ゾーン１\"" }]):
        jump block_00002BC5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"室内ゾーン２\"" }]):
        jump block_00002BCA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外ゾーン１\"" }]):
        jump block_00002BCB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外ゾーン２\"" }]):
        jump block_00002BCD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"花乃湯ゾーン\"" }]):
        jump block_00002BD0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"プールゾーン\"" }]):
        jump block_00002BD1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00002C17

    return

label block_00002BC5:
    # Node: 00002BC5 (Inside 1)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    $ set_place_title(_("室内1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3FA0EF08402B43E5AD742025746788F9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002BC6

    return

label block_00002BC6:
    # Node: 00002BC6 (Inside 1)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (130, 320),"image": "images/Dream/Menu/Nori.png","hover": "images/Dream/Menu/Nori hover.png","name": "朔"}, {"pos": (238, 334),"image": "images/Dream/Menu/Kai.png","hover": "images/Dream/Menu/Kai hover.png","name": "晦"}, {"pos": (375, 245),"image": "images/Dream/Menu/Sumoto+Rikuta.png","hover": "images/Dream/Menu/Sumoto+Rikuta hover.png","name": "漫才"}, {"pos": (610, 233),"image": "images/Dream/Menu/Tokiwa.png","hover": "images/Dream/Menu/Tokiwa hover 2.png","name": "常磐"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_784
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"朔\"" }]):
        jump block_00002BD8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"晦\"" }]):
        jump block_00002BD9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"漫才\"" }]):
        jump block_00002BD6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" }]):
        jump block_00002BD7
    if judge_lm_condition([]):
        jump block_00002BC2

    return

label block_00002BD8:
    # Node: 00002BD8 (朔)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_F316E85AE3FC493590B6B3DE8738DF71 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_62324AD297554FE987C680452CEE232E "[persistent.FirstName]。你的能量非常充盈，\n以后记得常来找我。"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_4AD6306DD8134C169B274EC478FB2307 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "放心。{w=0.45}我是在夸奖你。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室内1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BC6

    return

label block_00002BD9:
    # Node: 00002BD9 (晦)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_DA01EB2317F848BC8DD0093F575CFE5C as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_EE1903694D624E399209772C95A20AAA "[persistent.FirstName]桑，\n弟弟一直给你添麻烦了。\n"
    show rs_image_D4ED0C618EBF40FCA554D84C3D15E59D as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "对了，[persistent.FirstName]桑成年了么？"

    window hide


    if judge_lm_condition([]):
        jump block_00002BDA

    return

label block_00002BDA:
    # Node: 00002BDA (選擇)
    call scb_selector("", [{"name":"成年", "content":_("成年了")}, {"name":"未成年", "content":_("我还未成年……")}]) from _call_scb_selector_85

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"未成年\"" }]):
        jump block_00002BDC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"成年\"" }]):
        jump block_00002BDB

    return

label block_00002BDC:
    # Node: 00002BDC (未成年)
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_E45D451256FF481488D26744D096F84D as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_EE1903694D624E399209772C95A20AAA "真年轻，真羡慕。\n"
    show rs_image_66868581860740FC9D4CFB165B14D0CC as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "这个梦是全年龄的，\n所以放心即可。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室内1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BC6

    return

label block_00002BDB:
    # Node: 00002BDB (成年)
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_66868581860740FC9D4CFB165B14D0CC as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_EE1903694D624E399209772C95A20AAA "哦！那下次和我去喝一杯如何。{w}\n梅咲那边行不行？等你答复。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室内1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BC6

    return

label block_00002BD6:
    # Node: 00002BD6 (陸田+杉本)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FC79A5CE091B4681B5BEA00BE2FD8126 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "哇——杉本这个笨蛋——！！\n把毛巾还给我——！！！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FCED7919C7D74DAFB499305724AE0C2D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "这是服务观众♪好不容易\n有这个机会，大家记得好好看好好看♪"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_8E2179926DAA41D7AA205BBEBC72B590 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "说什么鬼话笨蛋杉本！！\n"
    show rs_image_FBE63FCB9954473E8F82B02D8AF1560F as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "唔——！[persistent.LastName]桑也说他点什么！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室内1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BC6

    return

label block_00002BD7:
    # Node: 00002BD7 (常磐)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_73436332C7964E32AE4D224E7A80CD02 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_C223850065F6443080205D1F61C04C98 "[persistent.LastName]桑，这次真的太辛苦你了。\n"
    show rs_image_5EA387970FD64DAAAFDC384D8ADBA852 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "既然能来到这里，\n肯定已经知道我是什么人了。"

    show rs_image_BCF196F60E0B4024A83160B1BA39C955 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C223850065F6443080205D1F61C04C98 "……不过，看，可以摸到我哦。\n"
    show rs_image_761CAD23249C466B87E1A2BF9E4DBEFC as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "没有穿过去，能感受到心脏的跳动。\n这就是梦的力量。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室内1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BC6

    return

label block_00002BCA:
    # Node: 00002BCA (Inside 2)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    $ set_place_title(_("室内2"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_81ED01C4F6294142A4FDFD3EE1B45A74 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002BC9

    return

label block_00002BC9:
    # Node: 00002BC9 (Inside 2)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (226, 298),"image": "images/Dream/Menu/Sato+Okajima-senior.png","hover": "images/Dream/Menu/Sato+Okajima-senior hover.png","name": "佐藤たち"}, {"pos": (410, 266),"image": "images/Dream/Menu/Okajima.png","hover": "images/Dream/Menu/Okajima hover.png","name": "岡島"}, {"pos": (553, 292),"image": "images/Dream/Menu/Kojima.png","hover": "images/Dream/Menu/Kojima hover.png","name": "小島"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_785
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"佐藤たち\"" }]):
        jump block_00002BDD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_00002BE1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_00002BE2
    if judge_lm_condition([]):
        jump block_00002BC2

    return

label block_00002BDD:
    # Node: 00002BDD (佐藤+岡島前輩)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_D6F07ED473C24FD39A67003E664A2E56 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "[persistent.LastName]酱，辛苦了——！"
    show rs_image_7D2C09CBCA184873B85F08A72918DE3A as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "如何？\n我和前辈的活跃，最后看到了吗？"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_E36A7958E94745E9AC545E69F70771FC as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "那时候引起了各种事情真是抱歉。\n我也知道我的第一印象坏透了。\n算是我自作自受。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_B182B1B5629B402A8368C36B70E40577 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "真是的！不要提过去的事了！\n请不要老这么折腾自己，\n弄得我也没兴致了。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_5B52E85CDD5E4B4AA18C135751CED708 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "对不起对不起。\n还是那么严格呐——你这家伙。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室内2"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BC9

    return

label block_00002BE1:
    # Node: 00002BE1 (岡島)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7F149D627F92448D94283DF1FBB9F6A5 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "[persistent.LastName]桑！我们新闻部的委托\n你都好好完成了吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002BE0

    return

label block_00002BE0:
    # Node: 00002BE0 (選擇)
    call scb_selector("", [{"name":"はい", "content":_("当然")}, {"name":"いいえ", "content":_("力不从心……")}]) from _call_scb_selector_86

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002BDE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00002BDF

    return

label block_00002BDE:
    # Node: 00002BDE (Yes)
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_5CD1009483F843F68944312BEE771D80 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哦哦！不愧是[persistent.LastName]桑！\n能努力到最后真的非常感谢！"

    show rs_image_CB5A198A2F5A438A8724BEDAEF07A7FC as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "[persistent.LastName]桑要是有什么烦恼\n请一定让我们帮忙\n"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_7F149D627F92448D94283DF1FBB9F6A5 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "对于亲爱的你我们什么都会听的！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_A460DCEFEF494632BA864ECA43AC5308 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "部长，不要用“什么都会”这种词。"

    show rs_image_A2F50214C9D84034952E4F0FE1191A94 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "[persistent.LastName]桑不会这么做，\n但世界上确实存在利用这种言辞的人，\n请一定小心。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_9145D024DE0B49F688035D3307C297C3 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "明、明白，我会注意的。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室内2"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BC9

    return

label block_00002BDF:
    # Node: 00002BDF (No)
    show rs_image_CB5A198A2F5A438A8724BEDAEF07A7FC as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "原来如此。\n那梦醒之后记得继续挑战！\n期待你的活跃！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_A2F50214C9D84034952E4F0FE1191A94 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "部长，委托的对象不是\n[persistent.LastName]桑是森海同学才对吧？"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_9145D024DE0B49F688035D3307C297C3 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "嗯？这个……{w=0.45}哦，也对。\n接受的是森海君，然后[persistent.LastName]桑是……\n"
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_25AA685FA607402AB43135E8CA943179 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "管他呢，现在就算接受了。就这样。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室内2"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BC9

    return

label block_00002BE2:
    # Node: 00002BE2 (小島)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_A2F50214C9D84034952E4F0FE1191A94 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_53FF68C192E3494AB005C1909579AFFB "问我为什么带着相机？{w}\n……不是说好不问了嘛。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室内2"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BC9

    return

label block_00002BCB:
    # Node: 00002BCB (Outside 1)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    $ set_place_title(_("室外1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D4432B16E35E47258C2CEA7F3A01BE50 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002BCC

    return

label block_00002BCC:
    # Node: 00002BCC (Outside 1)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (151, 316),"image": "images/Dream/Menu/Yuuhi+Mamoru.png","hover": "images/Dream/Menu/Yuuhi+Mamoru hover.png","name": "ユウヒマモル"}, {"pos": (347, 235),"image": "images/Dream/Menu/Nakayama-senior.png","hover": "images/Dream/Menu/Nakayama-senior hover.png","name": "中山先輩"}, {"pos": (473, 270),"image": "images/Dream/Menu/Izumi.png","hover": "images/Dream/Menu/Izumi hover.png","name": "泉"}, {"pos": (582, 310),"image": "images/Dream/Menu/Nakayama.png","hover": "images/Dream/Menu/Nakayama hover.png","name": "中山"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_786
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ユウヒマモル\"" }]):
        jump block_00002BE3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中山先輩\"" }]):
        jump block_00002BEA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_00002BED
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中山\"" }]):
        jump block_00002BF2
    if judge_lm_condition([]):
        jump block_00002BC2

    return

label block_00002BE3:
    # Node: 00002BE3 (夕阳+守)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_774A8364A43E47C7AB7D019D05D212B9 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "[persistent.FirstName]！给我老实回答！"

    show rs_image_257572183CFA40CB9CFAFC484A49205E as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "{color=#FF8000}见习魔法师的任务{/color}系列，\n以及{color=#008080}SCHOOLBOYS!{/color}系列，{w}\n你喜欢的是？"

    window hide


    if judge_lm_condition([]):
        jump block_00002BE6

    return

label block_00002BE6:
    # Node: 00002BE6 (選擇)
    call scb_selector("", [{"name":"スクボ", "content":_("《SCHOOLBOYS!》")}, {"name":"魔術師", "content":_("《见习魔法师的任务》")}]) from _call_scb_selector_87

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"スクボ\"" }]):
        jump block_00002BE4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"魔術師\"" }]):
        jump block_00002BE5

    return

label block_00002BE4:
    # Node: 00002BE4 (SCB)
    if sys_effect2_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_56D9C0922FE448D29210CE1A75E0E9A6 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_AE2879D336AC4FEF9997D54F17B41E88

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔……我想也是。\n果然还是那边人气更旺。{w}\n{size=16}{/size}{size=16}{color=#808080}……{/color}{/size}{color=#808080}明明是我们先发行的{/color}{size=16}{color=#808080}……{/color}{/size}"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_5FE387652A0E42B5BD94AF7F07B607D4 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_57471360F48A413AB843A4E46D8C5541 "夕阳，鼓起信心。\n"
    show rs_image_9820675F1AAD4D419E2725E6DAB6FD12 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "尽管出场率压倒性的不足，\n我们也可以制造大新闻打败他们。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_257572183CFA40CB9CFAFC484A49205E as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "有、有道理。\n"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_8460AD54099F4EF9B8E2AB45100A90A4 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "[persistent.FirstName]，给我等着！\n我一定会用正义之力把你变成{color=#FF8000}魔法师派{/color}！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCC

    return

label block_00002BE5:
    # Node: 00002BE5 (魔法師)
    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7C9C298DE347467CB019F1914945CAF2 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "真的吗！！{w}\n守，快听！太好了！\n我们以后也会继续努力的！！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 100
    show rs_image_B9704F2CFE814015832AC3371E69E9EF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "[persistent.FirstName]桑，谢谢你这么支持我们。\n"
    show rs_image_FC7660B3151148A28E60EA0463D8F8A0 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "我还是个新人，以后一定会加倍努力的，\n请多多关照。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCC

    return

label block_00002BEA:
    # Node: 00002BEA (中山前輩)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_2E02CC5D5C8C4A8EA94059F8C1C3255B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A751683772E84A83B9CDA0EADC2D57CE "我基本没怎么出场……{w}\n[persistent.LastName]桑记得我\n出场是在什么时候吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002BE9

    return

label block_00002BE9:
    # Node: 00002BE9 (選擇)
    call scb_selector("", [{"name":"覚えてる", "content":_("当然，你是……")}, {"name":"覚えてない", "content":_("呃…………………………")}]) from _call_scb_selector_88

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"覚えてる\"" }]):
        jump block_00002BE8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"覚えてない\"" }]):
        jump block_00002BE7

    return

label block_00002BE8:
    # Node: 00002BE8 (Yes)
    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3BED6A144E76490CADEF5544A36AC595 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A751683772E84A83B9CDA0EADC2D57CE "欸！真的？\n{w=0.45}{nw}"
    show rs_image_C2938CDBEEDD4450A1E7F525CCAAC3EF as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "哈哈，谢谢，有点小开心呐。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCC

    return

label block_00002BE7:
    # Node: 00002BE7 (No)
    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_FAD1DBCCA2E642E4911DA5C668A3492C as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A751683772E84A83B9CDA0EADC2D57CE "唔……\n{w=0.45}{nw}"
    show rs_image_2E02CC5D5C8C4A8EA94059F8C1C3255B as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "谢谢你如实回答……"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCC

    return

label block_00002BED:
    # Node: 00002BED (泉)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_B1E36CE006F245C1AD051ED3F7624AF4 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "这次登场人物有四十多个，\n[persistent.LastName]桑和大家都见过面了吗？"

    show rs_image_F72974FCF15B40A6BC8A092ECB10E868 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "大家都个性十足，我就有些\n不显眼了，总觉得有点担心。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_346D6C9DE10D4B0BAD376B0CDFE4387A as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_A751683772E84A83B9CDA0EADC2D57CE "没有这回事。对我来说\n翔一直都是最闪耀的！！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_930CA2AEA3114B4F8605CB14E033B8D7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "前、前辈……谢谢。{w}\n……{w=0.5}{nw}"
    show rs_image_B5425E9EB7AD435ABC0FA0E814579982 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "回家再说吧，[persistent.LastName]还在呢。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCC

    return

label block_00002BF2:
    # Node: 00002BF2 (中山)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_1C47F6FEE7E8424FBFB03BACB5B787B2 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "呐——呐——\n[persistent.LastName]是{color=#FF0000}S{/color}还是{color=#0000FF}M{/color}？"

    window hide


    if judge_lm_condition([]):
        jump block_00002BF1

    return

label block_00002BF1:
    # Node: 00002BF1 (選擇)
    call scb_selector("", [{"name":"S", "content":_("当然是S")}, {"name":"M", "content":_("其实是M")}]) from _call_scb_selector_89

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"S\"" }]):
        jump block_00002BEF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"M\"" }]):
        jump block_00002BF0

    return

label block_00002BEF:
    # Node: 00002BEF (S)
    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_ACE43FC2F75844ACAC2D953D64760365 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "什么嘛——好无聊——"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCC

    return

label block_00002BF0:
    # Node: 00002BF0 (M)
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_34216517833549F1BBFB1FF0D8023E7F as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "欸——这样啊♪\n"
    show rs_image_1C47F6FEE7E8424FBFB03BACB5B787B2 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不错我很感兴趣——♪\n记得等下给我搓背哦——"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外1"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCC

    return

label block_00002BCD:
    # Node: 00002BCD (Outside 2)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    $ set_place_title(_("室外2"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2669DA35CB3D4B5F8C704DE789FD3022 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002BCE

    return

label block_00002BCE:
    # Node: 00002BCE (Outisde 2)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (168, 275),"image": "images/Dream/Menu/Katou.png","hover": "images/Dream/Menu/Katou hover.png","name": "加藤たち"}, {"pos": (465, 272),"image": "images/Dream/Menu/Itou+Kimura.png","hover": "images/Dream/Menu/Itou+Kimura hover.png","name": "木村たち"}]
    $ sys_lm_menu_sound = {"click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_787
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤たち\"" }]):
        jump block_00002BF6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村たち\"" }]):
        jump block_00002BF7
    if judge_lm_condition([]):
        jump block_00002BC2

    return

label block_00002BF6:
    # Node: 00002BF6 (加藤+松田)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_4F844253D6A4407793B716CD3AE5757C as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "唔……\n结果到最后我还是在单恋。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_AF2ECCEDD2F74CAB98D0B8AEDF3043EF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "我也没能找到对象。\n"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_85BFF668331146CE82DFF22E2A86273D as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "说起来，[persistent.FirstName]有恋人么？"

    window hide


    if judge_lm_condition([]):
        jump block_00002BF4

    return

label block_00002BF4:
    # Node: 00002BF4 (選擇)
    call scb_selector("", [{"name":"いる", "content":_("和你不一样我有哦")}, {"name":"いない", "content":_("唔……没有")}]) from _call_scb_selector_90

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いる\"" }]):
        jump block_00002BF3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いない\"" }]):
        jump block_00002BF5

    return

label block_00002BF3:
    # Node: 00002BF3 (Yes)
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_AF2ECCEDD2F74CAB98D0B8AEDF3043EF as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_81D16F74A3C44B8982DB528D7D934850 "唔……真的假的。\n"
    show rs_image_D0F9EF5EAF014E139F5C36AFCF4082A5 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "哈、哈、哈、哈……"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外2"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCE

    return

label block_00002BF5:
    # Node: 00002BF5 (No)
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E90746911EBC46FDB99A7900CD21FF09 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_81D16F74A3C44B8982DB528D7D934850 "哦！真的假的！太好了——！\n那我们就是“找不到对象同盟”了♪\n{size=14}（League of NullPointerException）{/size}"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_9294A035C75647BD9E8AE84AD3893DCC as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "听起来太悲伤了，快住口。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外2"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCE

    return

label block_00002BF7:
    # Node: 00002BF7 (伊藤+木村)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_934C948EFC684F6FAB2A071642289630 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "多亏[persistent.LastName]桑努力到现在，\n我才能抓住自己的幸福。"

    show rs_image_7BEC5F4E59484E24A1D93A3C8F3C3AA9 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "真的非常感谢。{w}\n快，木村也来道谢。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_A8107EC8FB344131ABB4FA34BE153E48 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸？为什么？\n再说了这人是谁？"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_DFDC0262AECB4DFCBB5810FC6CAF4C4C as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_710A38AC94C841779DB701B5AC1010FD "你这家伙！思路再给我开阔点！\n"
    show rs_image_06B46EF83FB249798008FF7045DD2D0E as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "对不起[persistent.LastName]桑，这家伙这个样。\n等下我会好好说他的。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外2"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCE

    return

label block_00002BD0:
    # Node: 00002BD0 (花乃湯)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    $ set_place_title(_("花乃汤（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_29D91D003E174A2686DE6ED750B0787F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002BCF

    return

label block_00002BCF:
    # Node: 00002BCF (花乃湯)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (125, 202),"image": "images/Dream/Menu/Shintaro.png","hover": "images/Dream/Menu/Shintaro hover.png","name": "慎太郎"}, {"pos": (471, 234),"image": "images/Dream/Menu/Kiyo.png","hover": "images/Dream/Menu/Kiyo hover.png","name": "清"}, {"pos": (266, 295),"image": "images/Dream/Menu/Tsuki+Sora.png","hover": "images/Dream/Menu/Tsuki+Sora hover.png","name": "双子"}, {"pos": (562, 312),"image": "images/Dream/Menu/Shinobu.png","hover": "images/Dream/Menu/Shinobu hover.png","name": "しのぶ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_788
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00002BF8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"清\"" }]):
        jump block_00002BF9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"双子\"" }]):
        jump block_00002BFC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00002BFE
    if judge_lm_condition([]):
        jump block_00002BC2

    return

label block_00002BF8:
    # Node: 00002BF8 (慎太郎)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_8BA03B65CF5640D3BACABEC675ADDE09 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "[persistent.FirstName]酱！欢迎来到花乃汤{color=#FF80C0}（梦中版）{/color}☆{w}\n至今为止努力的一切\n都可以在这里如愿以偿。"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F8104A750A8348579BF2BAB10F75E1BC as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦，对了，毛巾的库存用完了。\n"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "对不起不过，暂时就裸着好了☆"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCF

    return

label block_00002BF9:
    # Node: 00002BF9 (清)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_DDB9157C029A46A3B5B11A276571878D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D34F60C882F0425E93252349E8C3BC8D "你、你好，[persistent.LastName]桑。\n"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_C45FBA1639DA495CB9659FD22BFF63F1 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "啊，请不要误会，我不是露出狂。"

    show rs_image_DDB9157C029A46A3B5B11A276571878D as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "只是毛巾已经没有库存了所以……\n"
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_B4877E9991234246810EC881355FCB03 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "呜……还是好羞耻……"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCF

    return

label block_00002BFC:
    # Node: 00002BFC (月+空)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_58C9F6EA34E543A09272A57E9CE632A1 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "[persistent.FirstName]桑，\n不许对空眉来眼去。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_A6EC34A4813A43E8B43CADCFEFDE778F as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不不，他看的不是我，\n他看的应该是哥哥才对。\n"
    show rs_image_62A75CACEABE40EF93680498F1FF1B06 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "对不对？[persistent.FirstName]桑。"

    window hide


    if judge_lm_condition([]):
        jump block_00002BFB

    return

label block_00002BFB:
    # Node: 00002BFB (選擇)
    call scb_selector("", [{"name":"月", "content":_("其实我是在看月")}, {"name":"空", "content":_("对，我看的就是空")}]) from _call_scb_selector_91

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00002BFD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_00002BFA

    return

label block_00002BFD:
    # Node: 00002BFD (月)
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_C231CCE247EB4EE3B8028A0B53AAD12A as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "看，果然。{w}毕竟哥哥肌肉很结实。\n腹肌也锻炼得非常硬，\n等下请务必摸摸看。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCF

    return

label block_00002BFA:
    # Node: 00002BFA (空)
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_66D0DA05E7054834949C3003033034C1 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "算了，我明白你的心情。\n退一百步，看就看。\n"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_EEB21BBE1BDE472F9E2F1BA6A81F402C as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "但，绝对不许靠近空。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCF

    return

label block_00002BFE:
    # Node: 00002BFE (忍)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_0E3C15D5FB774AEBA28E3386D60563E7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你好，[persistent.FirstName]桑。\n谢谢你收集大家的“脚步”到现在。"

    show rs_image_36BE7A7285544EFA9FB1A1D76B12326B as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "可以的话我等下帮你搓背好了。\n"
    show rs_image_3A45A23BDC54493E92675E2EA0AD68DB as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "到时候请务必谈谈你至今为止的感想。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"


    if judge_lm_condition([]):
        jump block_00002BCF

    return

label block_00002BD1:
    # Node: 00002BD1 (Swimming pool)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    $ set_place_title(_("泳池（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A10A26C5A73D447BBC9F30BFAE830922 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002BD2

    return

label block_00002BD2:
    # Node: 00002BD2 (Swimming pool)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (152, 221),"image": "images/Dream/Menu/Tomo.png","hover": "images/Dream/Menu/Tomo hover.png","name": "友"}, {"pos": (312, 229),"image": "images/Dream/Menu/Saburo.png","hover": "images/Dream/Menu/Saburo hover.png","name": "三朗"}, {"pos": (461, 329),"image": "images/Dream/Menu/Kobayashi+Minami.png","hover": "images/Dream/Menu/Kobayashi+Minami hover.png","name": "小林たち"}, {"pos": (446, 258),"image": "images/Dream/Menu/Sakuya+Tsubasa.png","hover": "images/Dream/Menu/Sakuya+Tsubasa hover.png","name": "さくつば"}, {"pos": (682, 269),"image": "images/Dream/Menu/Shiro+Yukio.png","hover": "images/Dream/Menu/Shiro+Yukio hover.png","name": "四朗たち"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_789
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友\"" }]):
        jump block_00002C03
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_00002C04
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林たち\"" }]):
        jump block_00002C08
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"四朗たち\"" }]):
        jump block_00002C0C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"さくつば\"" }]):
        jump block_00002C0D
    if judge_lm_condition([]):
        jump block_00002BC2

    return

label block_00002C03:
    # Node: 00002C03 (友)
    stop effect2 fadeout 0.8
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_86004ABC32D14A438B7BE04E07D2DA30 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "[persistent.FirstName]——！终于来到这里了——！\n真是很辛苦的时间呐！谢谢！"

    show rs_image_2339211CC2BE4EC098068EB1C550DA90 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这个梦的世界可以和喜欢的孩子\n开心自由过上一阵子哦♪\n"
    show rs_image_841DCEF8953649BBBE7AFFA3C4306A86 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "对了，[persistent.FirstName]最喜欢谁？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C02

    return

label block_00002C02:
    # Node: 00002C02 (選擇)
    call scb_selector("", [{"name":"友１", "content":_("还用问，当然是友了！")}, {"name":"友２", "content":_("不是只能选友君嘛！")}, {"name":"友３", "content":_("怎么选都只有友君的！")}, {"name":"友以外", "content":_("谁都可以，除了你")}]) from _call_scb_selector_92

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友以外\"" }]):
        jump block_00002C00
    if judge_lm_condition([]):
        jump block_00002C01

    return

label block_00002C00:
    # Node: 00002C00 (Not 友)
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_6CE9618D379F40C5BA3E437A6683AE34 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "失落……\n明明……是我先来的……"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("泳池（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002BD2

    return

label block_00002C01:
    # Node: 00002C01 (友)
    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_86004ABC32D14A438B7BE04E07D2DA30 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真的！？太好了——♪♪\n"
    show rs_image_9E176C86696D43C1988EAC0D52195B9F as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我可是这部作品的主角！！\n当然是我了♪"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("泳池（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002BD2

    return

label block_00002C04:
    # Node: 00002C04 (三朗)
    stop effect2 fadeout 0.8
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_5D881B5229DA409E963D4AADC9AC9E1A as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦，[persistent.FirstName]！"

    show rs_image_18A411FFABA0492C9C987A7F77C52B03 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呀——多亏[persistent.FirstName]\n一路走到现在，我也算\n认清了自己的真实感情。"

    show rs_image_69184BAC639146468121B62B79C8D882 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "谢了——我以后会和奥村一起努力的！\n你也记得来花乃汤贡献营业额哟♪\n"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_5AD0A4A48CFF45BBB9610417EE87DA81 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我指的是现实世界，不是梦里。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("泳池（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002BD2

    return

label block_00002C08:
    # Node: 00002C08 (小林+南)
    stop effect2 fadeout 0.8
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D623C2B2D2A64C9EB2AAB807CA16DBBF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EA79386263E543A88D4DC03B8BD44485 "哇——♪呐——呐——！和我们一起玩！！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_FF3E7E3AA545427BB27537F62784917E as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "等等，小林酱。我还有个问题呐。"

    show rs_image_54677CB572CC4C4DBD11E354D9B14D0B as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "请问，\n{w=0.45}我们该叫[persistent.FirstName]{color=#0000FF}哥哥{/color}还是[persistent.FirstName]{color=#AA0055}姐姐{/color}呢？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C07

    return

label block_00002C07:
    # Node: 00002C07 (選擇)
    call scb_selector("", [{"name":"お兄ぃ", "content":_("哥哥")}, {"name":"お姉ぇ", "content":_("姐姐")}]) from _call_scb_selector_93

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"お兄ぃ\"" }]):
        jump block_00002C05
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"お姉ぇ\"" }]):
        jump block_00002C06

    return

label block_00002C05:
    # Node: 00002C05 (兄)
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_09DFACE80DB94326A1CC80E159721DDC as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_9A978AAD07624C598B6179F23F51FB2D "明白了——！\n[persistent.FirstName]哥！请多指教♪"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D86C69A03A194CDCAA7046C945160CDD as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "来来——[persistent.FirstName]哥！\n和我们玩25米游泳竞赛——！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("泳池（梦）"))

    if judge_lm_condition([]):
        jump block_00002BD2

    return

label block_00002C06:
    # Node: 00002C06 (姉)
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_09DFACE80DB94326A1CC80E159721DDC as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_9A978AAD07624C598B6179F23F51FB2D "明白了——！\n[persistent.FirstName]姐！请多指教♪"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D86C69A03A194CDCAA7046C945160CDD as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "那个——[persistent.FirstName]姐！\n和我们玩25米游泳竞赛吧——！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("泳池（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002BD2

    return

label block_00002C0C:
    # Node: 00002C0C (雪緒+四朗)
    stop effect2 fadeout 0.8
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_BDD54F85A00545779E475A3D058E3B3C as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "我们小学的泳装是四角裤型的，\n中学生的大家都是三角形呐——{w}\n[persistent.LastName]桑喜欢什么样的——？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C0B

    return

label block_00002C0B:
    # Node: 00002C0B (選擇)
    call scb_selector("", [{"name":"ボックス型", "content":_("四角裤型")}, {"name":"ブーメラン型", "content":_("三角形")}]) from _call_scb_selector_94

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ボックス型\"" }]):
        jump block_00002C09
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ブーメラン型\"" }]):
        jump block_00002C09

    return

label block_00002C09:
    # Node: 00002C09 (After selection)
    show rs_image_EADA86EB4F1945C2A54DEB1C5860493D as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "欸——这样——"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_26AF4439EAB44277A12190D8C29C8406 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "没兴趣就别问。\n别浪费[persistent.FirstName]桑的时间。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("泳池（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002BD2

    return

label block_00002C0D:
    # Node: 00002C0D (作哉+翼)
    stop effect2 fadeout 0.8
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_C199DDFF19C644C2ABB11903E5961C43 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "救救我，[persistent.FirstName]桑～！\n作哉君一直在欺负我……"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_A188AA52436642DD9D35DFBB20A91864 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "别说那么难听，我只是在实话实说。"

    show rs_image_8789FDB15F9C4C8DB6CC0412F4A60781 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "过来[persistent.LastName]。\n在你看来一之濑的“那个”也很大对不。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_440CF516BBBB46A5ACF9F368F3CFD7BE as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "才不是很普通的——！{w}\n……{w=0.45}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_8CAF4C546EAC42E0B5AD7BF4557D1137 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "倒是作哉君是不是很小呢？"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BC6670AB81BA4659995CA6663BB08ABC as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "什！？说什么胡话——！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("泳池（梦）"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002BD2

    return

label block_00002C17:
    # Node: 00002C17 (Back)
    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_20A8817D51644BE6A7913BD30673F110

    pause 1

    $ set_place_title(_("朔的家"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5E4B22942A284109B65800E46DBB8782 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    if sys_music2_current_file != "sound/BGM/Nori cave.ogg":
        play music2 "sound/BGM/Nori cave.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Nori cave.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "IsCaveRollbackAvailable == True" }]):
        jump block_000031AB
    if judge_lm_condition([]):
        jump block_00002BD4

    return

label block_000031AB:
    # Node: 000031AB (Cave 朔 觸手A 觸手B)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (416, 216),"image": "images/End of semester/Menu/Nori cave.png","hover": "images/End of semester/Menu/Nori cave hover.png","name": "朔"}, {"pos": (520, 208),"image": "images/End of semester/Menu/Tentacle-earthworm cave.png","hover": "images/End of semester/Menu/Tentacle-earthworm cave hover.png","name": "触手A"}, {"pos": (230, 208),"image": "images/End of semester/Menu/Tentacle-starfish cave.png","hover": "images/End of semester/Menu/Tentacle-starfish cave hover.png","name": "触手B"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_790
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"朔\"" }]):
        jump block_00003608
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手A\"" },{ "scope": 1, "content": "E_TalkTentacleACave == 1" }]):
        jump block_000031AA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手A\"" }]):
        jump block_000031A8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手B\"" },{ "scope": 1, "content": "E_TalkTentacleBCave == 1" }]):
        jump block_00003FBE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手B\"" }]):
        jump block_000031A9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00002C18

    return

label block_00003608:
    # Node: 00003608 (Random)
    $ CaveRandomResult = Random(5)

    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 0" }]):
        jump block_00003606
    if judge_lm_condition([]):
        jump block_00002C19

    return

label block_00003606:
    # Node: 00003606 (朔 2)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_299C8BA1038447799D6C4BCB27B6A6BB as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_62324AD297554FE987C680452CEE232E "要不要看{color=#008080}“梦之温泉设施”{/color}的梦？\n"
    show rs_image_1F690B307ECA4450A3C108BA53BF04F7 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过，今天机器状态不好。\n不保证不出错……"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("朔的家"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"


    if judge_lm_condition([]):
        jump block_00003607

    return

label block_00003607:
    # Node: 00003607 (選擇)
    call scb_selector("", [{"name":"はい", "content":_("反正是买BUG送游戏")}, {"name":"いいえ", "content":_("哇，好不安，我不要")}]) from _call_scb_selector_95

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" },{ "scope": 1, "content": "IsCaveRollbackAvailable == True" }]):
        jump block_000031AB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003609
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00002BD4

    return

label block_00003609:
    # Node: 00003609 (小熊猫)
    pause 0.5

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_20A8817D51644BE6A7913BD30673F110

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    if sys_effect_current_file != "sound/Effect Sound/Warning 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Warning 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Warning 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FF0000}系统崩了！！{/color}"

    window hide

    pause 1

    stop effect fadeout 2
    $ sys_effect_current_file = ""

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DCD8B79F49964D74AC066FB7F605BC72

    pause 2

    show rs_image_092C46B7A72E4AFEB49017870F0978E6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BAF3BF757577455980E802743F48D2F9

    pause 0.5

    $ set_place_title(_("迷之地点"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    if sys_music2_current_file != "sound/BGM/Ailurus fulgens.ogg":
        play music2 "sound/BGM/Ailurus fulgens.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Ailurus fulgens.ogg"

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_0000360A

    return

label block_0000360A:
    # Node: 0000360A (Gymno)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (154, 271),"image": "images/End of semester/Menu/Be--.png","hover": "images/End of semester/Menu/Be-- hover.png","name": "ベー"}, {"pos": (454, 236),"image": "images/End of semester/Menu/He--.png","hover": "images/End of semester/Menu/He-- hover.png","name": "へー"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_791
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ベー\"" }]):
        jump block_0000360B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"へー\"" }]):
        jump block_0000360C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00002C17

    return

label block_0000360B:
    # Node: 0000360B (貝ー)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_BC99B0ED590743F2B5BB46826572A7BB as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_7F5086B0A4E249BF8230B6A6D47A3C3F as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "你好哟，好好放松就好哟。{w}去找黑——的话\n{nw}"
    show rs_image_47F53B04B0F54144A4CB509D966110C3 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "会给你SCHOOLBOYS!步\n的原画和资料哟。"

    show rs_image_BC99B0ED590743F2B5BB46826572A7BB as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "黑——的脾气有些怪，\n每次都会给不同的画，\n记得多看看哟。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("迷之地点"))

    if judge_lm_condition([]):
        jump block_0000360A

    return

label block_0000360C:
    # Node: 0000360C (黑ー)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_C20C60D10A1F42FEBDF38A429667EBB3 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_8BBC857C6E294BDE95097DFAE78C001F "呵……。"

    window hide


    if judge_lm_condition([]):
        jump block_00003636

    return

label block_00003636:
    # Node: 00003636 (Random)
    $ CaveRandomResult = Random(40)

    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 1" }]):
        jump block_0000360D
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 2" }]):
        jump block_0000360F
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 3" }]):
        jump block_00003610
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 4" }]):
        jump block_00003611
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 5" }]):
        jump block_00003613
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 6" }]):
        jump block_00003612
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 7" }]):
        jump block_00003614
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 8" }]):
        jump block_00003615
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 9" }]):
        jump block_00003616
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 10" }]):
        jump block_00003617
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 11" }]):
        jump block_00003618
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 12" }]):
        jump block_00003619
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 13" }]):
        jump block_0000361A
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 14" }]):
        jump block_0000361B
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 15" }]):
        jump block_0000361C
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 16" }]):
        jump block_0000361D
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 17" }]):
        jump block_0000362A
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 18" }]):
        jump block_0000362B
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 19" }]):
        jump block_0000362C
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 20" }]):
        jump block_0000362D
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 21" }]):
        jump block_00003625
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 22" }]):
        jump block_00003624
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 23" }]):
        jump block_00003626
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 24" }]):
        jump block_00003627
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 25" }]):
        jump block_00003620
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 26" }]):
        jump block_00003621
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 27" }]):
        jump block_00003622
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 28" }]):
        jump block_00003628
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 29" }]):
        jump block_0000361E
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 30" }]):
        jump block_0000361F
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 31" }]):
        jump block_00003623
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 32" }]):
        jump block_00003629
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 33" }]):
        jump block_00003632
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 34" }]):
        jump block_00003633
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 35" }]):
        jump block_00003634
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 36" }]):
        jump block_00003635
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 37" }]):
        jump block_0000362F
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 38" }]):
        jump block_0000362E
    if judge_lm_condition([{ "scope": 0, "content": "CaveRandomResult == 39" }]):
        jump block_00003630
    if judge_lm_condition([]):
        jump block_00003631

    return

label block_0000360D:
    # Node: 0000360D (1)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_F1981AC557C44FC8A2ABAA04BE15237A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是“傲娇男孩子的激效疗”的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003CDD:
    # Node: 00003CDD (TO: Gymno)

    if judge_lm_condition([]):
        jump block_00003CDC

    return

label block_00003CDC:
    # Node: 00003CDC (TO: Gymno)
    window hide

    pause 0.3

    $ set_window("(標準)")
    $ set_place_title(_("迷之地点"))
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_ADDD50687F2F422986F3008E9377DC19 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B


    if judge_lm_condition([]):
        jump block_0000360A

    return

label block_0000360F:
    # Node: 0000360F (2)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_384110320D88436D85BA6DD5CF0A8435 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是绫濑忍的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003610:
    # Node: 00003610 (3)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_A53D804CC56747C7B006BD044477BDEF as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是一之濑翼的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003611:
    # Node: 00003611 (4)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_4E85C530D8D3473DB853E92E42796808 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是“翼的流转音符”的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003613:
    # Node: 00003613 (5)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3262E71B2B41479FB27CE43CCBF7B189 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是“并驶之舟”的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003612:
    # Node: 00003612 (6)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_E5B055DF37B64D26B11EB9B89F704A70 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是“傲娇男孩子的特效药”的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003614:
    # Node: 00003614 (7)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_800477D8DD234D089E75B62F656949E1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是绫濑忍内衣的资料插画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003615:
    # Node: 00003615 (8)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_9636410129FE480CBA1E59A712BEAD28 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是一之濑翼内衣的资料插画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003616:
    # Node: 00003616 (9)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_D3530EED7E9746AE988E85D4F0DE8B73 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是猫山三朗内衣的资料插画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003617:
    # Node: 00003617 (10)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_84E941EFAF2341FBA1876BD94A4F6BBC as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是穗海作哉内衣的资料插画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003618:
    # Node: 00003618 (11)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_C9DB106858CA41B7B4003E9BB91805CE as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是森海友内衣的资料插画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003619:
    # Node: 00003619 (12)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_E1F6B9536B3B46CFB788215144C17757 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是奥村慎太郎内衣的资料插画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000361A:
    # Node: 0000361A (13)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_A75F058C925546EA80745EB269CC1348 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是赤峰月内衣的资料插画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000361B:
    # Node: 0000361B (14)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_E90C95C60FB84F6581E3983A55891E3A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是赤峰空内衣的资料插画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000361C:
    # Node: 0000361C (15)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3EBC47A896DC499AACB49E4BDEEA71E5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是“不可思议！猫狗物语”的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000361D:
    # Node: 0000361D (16)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_E353046D8C9B48A79F1CE40AC14306B8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是猫山三朗的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000362A:
    # Node: 0000362A (17)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_7E24A8BF425C4ECF96EB373C24D3B0F9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是中山紫音和中山花音的设定图。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000362B:
    # Node: 0000362B (18)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_108BC9AB06154A98B5D0E6AF7C206B1A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是中山花音和清武一的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000362C:
    # Node: 0000362C (19)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_88FBE2AD63014EEEB2F9AAFDEEDB4ACD as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是伊藤圭的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000362D:
    # Node: 0000362D (20)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_96F74F3655E3406F8286DD4EEB8C1414 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是穗海作哉的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003625:
    # Node: 00003625 (21)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_8A1E3E8BA3A84167937C2FDB116C182A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是第二章夕阳委托的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003624:
    # Node: 00003624 (22)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3F2F151021B244738CFDD665A3532FD3 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是加藤准太的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003626:
    # Node: 00003626 (23)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_DCDFF79DB7C046CCAC7748431CBCB991 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是小林和南的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003627:
    # Node: 00003627 (24)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_C6C8C885A44845BC8BA99B2306A68425 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是森海友的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003620:
    # Node: 00003620 (25)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_C6EE398796BD481693E61537FF94EF7A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是赤峰空和赤峰月的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003621:
    # Node: 00003621 (26)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_2F05CFBAD2B24921A29B2B49F146826D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是猫山四朗的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003622:
    # Node: 00003622 (27)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_CD5D380D46B34EBBBC6B6159A4B934EF as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是“久远回忆”的假想画的线稿。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003628:
    # Node: 00003628 (28)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_326CA88282F046A98440AE961D1C9A41 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是冈岛雄介和冈岛直弥的设定图。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000361E:
    # Node: 0000361E (29)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_D08D7328B09B4232BA91A2C8053B89A4 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是九尾和常磐前辈某个场景的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000361F:
    # Node: 0000361F (30)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_4CF90A90A642482CAEBB21AED1D90F57 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是奥村慎太郎的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003623:
    # Node: 00003623 (31)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_2B7ED78C0768479A8DBAE3BD2378B02A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是朔和晦某个场景的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003629:
    # Node: 00003629 (32)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_4343694156FA4167BDAD2CF46F897112 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是赤峰月的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003632:
    # Node: 00003632 (33)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_BF5DCEFE0B0743998188F334C9C89A22 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是“大家来相扑”的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003633:
    # Node: 00003633 (34)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_A34DFAB0833F42ACB26EDA7961051617 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是忍和朔的女仆装的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003634:
    # Node: 00003634 (35)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_BE4FB2A05C384DFBA71C9A3A710E2151 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是赤峰空的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003635:
    # Node: 00003635 (36)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_8153229E03B04FE3BBCB54618CFB5C79 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是木村树的立绘的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000362F:
    # Node: 0000362F (37)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_4F39883A3878471C8FFCC23735B11F2B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是“欢迎来到食人狼之馆”的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_0000362E:
    # Node: 0000362E (38)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_AEE8C568685B46CBA46B41724696644A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是“大家来相扑”的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003630:
    # Node: 00003630 (39)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_6754DC016A9148B39DA671836650F496 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是一二班所有人在一起的两张图的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00003631:
    # Node: 00003631 (40)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_D9087FDD699D4BC2A3F43E07DAE67CA0 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.5

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}这是体育祭某个场景的原画。{/color}"


    if judge_lm_condition([]):
        jump block_00003CDD

    return

label block_00002BD4:
    # Node: 00002BD4 (Cave 朔)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (416, 216),"image": "images/End of semester/Menu/Nori cave.png","hover": "images/End of semester/Menu/Nori cave hover.png","name": "朔"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_792
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00002C18
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"朔\"" }]):
        jump block_00003608

    return

label block_00002C18:
    # Node: 00002C18 (TO: Cave inside)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_music2_current_file != "sound/BGM/Nori cave.ogg":
        play music2 "sound/BGM/Nori cave.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Nori cave.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Cave 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cave 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Cave 1.ogg"


    if judge_lm_condition([]):
        jump block_00002BAB

    return

label block_00002C19:
    # Node: 00002C19 (朔)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_299C8BA1038447799D6C4BCB27B6A6BB as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_62324AD297554FE987C680452CEE232E "要不要看{color=#008080}“梦之温泉设施”{/color}的梦？"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("朔的家"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"


    if judge_lm_condition([]):
        jump block_00002C1A

    return

label block_00002C1A:
    # Node: 00002C1A (選擇)
    call scb_selector("", [{"name":"はい", "content":_("梦之温泉设施？听起来好有趣")}, {"name":"いいえ", "content":_("听起来好可疑")}]) from _call_scb_selector_96

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002C2C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" },{ "scope": 1, "content": "IsCaveRollbackAvailable == True" }]):
        jump block_000031AB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00002BD4

    return

label block_000031AA:
    # Node: 000031AA (触手A 2)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 200
    show rs_image_5171C4277664485482367CFD06553623 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_FB87619C890441AEA41E279A1B588CAC "要看{color=#FF00FF}回到过去{/color}的梦么？"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("朔的家"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"


    if judge_lm_condition([]):
        jump block_000031AF

    return

label block_000031AF:
    # Node: 000031AF (選擇)
    call scb_selector("", [{"name":"Chapter 1", "content":_("第一章")}, {"name":"Chapter 2", "content":_("第二章")}, {"name":"Chapter 3", "content":_("第三章")}, {"name":"Back", "content":_("我对过去没有留恋")}]) from _call_scb_selector_97

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Chapter 1\"" }]):
        jump block_00003CD8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Chapter 2\"" }]):
        jump block_00003CD9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Chapter 3\"" }]):
        jump block_00003CDA
    if judge_lm_condition([]):
        jump block_000031AB

    return

label block_00003CD8:
    # Node: 00003CD8 (Chapter 1)
    $ SYSReviewChapter = 1

    if judge_lm_condition([]):
        jump block_000031B8

    return

label block_000031B8:
    # Node: 000031B8 (CLEAR)
    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_CB56E573F5D34F039682091C43399E19


    if judge_lm_condition([]):
        jump block_00003CD2

    return

label block_00003CD2:
    # Node: 00003CD2 (Cache profile)
    $ SYSReviewMode = True
    $ UserStoryCache = [0] * 44
    $ UserStoryCache[0] = C1S1
    $ UserStoryCache[1] = C1S2
    $ UserStoryCache[2] = C1S3
    $ UserStoryCache[3] = C1S4
    $ UserStoryCache[4] = C1S5
    $ UserStoryCache[5] = C2S1
    $ UserStoryCache[6] = C2S2
    $ UserStoryCache[7] = C2S3
    $ UserStoryCache[8] = C2S4
    $ UserStoryCache[9] = C2S5
    $ UserStoryCache[10] = C2S6
    $ UserStoryCache[11] = C3S1
    $ UserStoryCache[12] = C3S2
    $ UserStoryCache[13] = C3S3
    $ UserStoryCache[14] = C3S4
    $ UserStoryCache[15] = C3S5
    $ UserStoryCache[16] = C3S6
    $ UserStoryCache[17] = C0SShinobu
    $ UserStoryCache[18] = C1SSabuShin
    $ UserStoryCache[19] = C2SNori
    $ UserStoryCache[20] = C2SYuuhi
    $ UserStoryCache[21] = C3SSabuShin
    $ UserStoryCache[22] = C3SPark
    $ UserStoryCache[23] = C3SPhoto
    $ UserStoryCache[24] = C3SYukiToki
    $ UserStoryCache[25] = C3SShiroYuki
    $ UserStoryCache[26] = C1QNewsclub
    $ UserStoryCache[27] = C1QKimuraConference
    $ UserStoryCache[28] = C1QSabuShin
    $ UserStoryCache[29] = C1QTsubasa
    $ UserStoryCache[30] = C1QMatsuta
    $ UserStoryCache[31] = C2QNewsclub
    $ UserStoryCache[32] = C2QKimuraConference
    $ UserStoryCache[33] = C2QYuuhi
    $ UserStoryCache[34] = C2QSakuya
    $ UserStoryCache[35] = C2QSora
    $ UserStoryCache[36] = C3QNewsclub
    $ UserStoryCache[37] = C3QKimuraConference
    $ UserStoryCache[38] = C3QSakuyaWalk1
    $ UserStoryCache[39] = C3QSakuyaWalk2
    $ UserStoryCache[40] = C3QShiro
    $ UserStoryCache[41] = C3QNakayama
    $ UserStoryCache[42] = C3QYakyuken
    $ UserStoryCache[43] = C3QNori

    if judge_lm_condition([]):
        jump block_00003CD3

    return

label block_00003CD3:
    # Node: 00003CD3 (Reset profile)
    if SYSReviewChapter == 1:
        $ C1S1 = False
        $ C1S2 = False
        $ C1S3 = False
        $ C1S4 = False
        $ C1S5 = False
        $ C0SShinobu = False
        $ C1SSabuShin = False
        $ C1QNewsclub = False
        $ C1QKimuraConference = False
        $ C1QSabuShin = False
        $ C1QTsubasa = False
        $ C1QMatsuta = False
        $ C1SG1 = False
        $ C1SG2 = False
    if SYSReviewChapter == 2:
        $ C2S1 = False
        $ C2S2 = False
        $ C2S3 = False
        $ C2S4 = False
        $ C2S5 = False
        $ C2S6 = False
        $ C2SNori = False
        $ C2SYuuhi = False
        $ C2QNewsclub = False
        $ C2QKimuraConference = False
        $ C2QYuuhi = False
        $ C2QSakuya = False
        $ C2QSora = False
        $ C2SG1 = False
        $ C2SG2 = False
    if SYSReviewChapter == 3:
        $ C3S1 = False
        $ C3S2 = False
        $ C3S3 = False
        $ C3S4 = False
        $ C3S5 = False
        $ C3S6 = False
        $ C3SSabuShin = False
        $ C3SPark = False
        $ C3SPhoto = False
        $ C3SYukiToki = False
        $ C3SShiroYuki = False
        $ C3QNewsclub = False
        $ C3QKimuraConference = False
        $ C3QSakuyaWalk1 = False
        $ C3QSakuyaWalk2 = False
        $ C3QShiro = False
        $ C3QNakayama = False
        $ C3QYakyuken = False
        $ C3QNori = False
        $ C3SG1 = False
        $ C3SG2 = False

    if judge_lm_condition([{ "scope": 0, "content": "SYSReviewChapter == 1" }]):
        jump block_00003CD6
    if judge_lm_condition([{ "scope": 0, "content": "SYSReviewChapter == 2" }]):
        jump block_00003CD4
    if judge_lm_condition([{ "scope": 0, "content": "SYSReviewChapter == 3" }]):
        jump block_00003CD5

    return

label block_00003CD6:
    # Node: 00003CD6 (CHAPTER 1)
    call block_00003985 from _call_block_00003985

    if judge_lm_condition([]):
        jump block_00003CD7

    return

label block_00003CD7:
    # Node: 00003CD7 (Recover profile)
    $ SYSReviewMode = False
    $ C1S1 = C1S1 or UserStoryCache[0]
    $ C1S2 = C2S2 or UserStoryCache[1]
    $ C1S3 = C1S3 or UserStoryCache[2]
    $ C1S4 = C1S4 or UserStoryCache[3]
    $ C1S5 = C1S5 or UserStoryCache[4]
    $ C2S1 = C2S1 or UserStoryCache[5]
    $ C2S2 = C2S2 or UserStoryCache[6]
    $ C2S3 = C2S3 or UserStoryCache[7]
    $ C2S4 = C2S4 or UserStoryCache[8]
    $ C2S5 = C2S5 or UserStoryCache[9]
    $ C2S6 = C2S6 or UserStoryCache[10]
    $ C3S1 = C3S1 or UserStoryCache[11]
    $ C3S2 = C3S2 or UserStoryCache[12]
    $ C3S3 = C3S3 or UserStoryCache[13]
    $ C3S4 = C3S4 or UserStoryCache[14]
    $ C3S5 = C3S5 or UserStoryCache[15]
    $ C3S6 = C3S6 or UserStoryCache[16]
    $ C0SShinobu = C0SShinobu or UserStoryCache[17]
    $ C1SSabuShin = C1SSabuShin or UserStoryCache[18]
    $ C2SNori = C2SNori or UserStoryCache[19]
    $ C2SYuuhi = C2SYuuhi or UserStoryCache[20]
    $ C3SSabuShin = C3SSabuShin or UserStoryCache[21]
    $ C3SPark = C3SPark or UserStoryCache[22]
    $ C3SPhoto = C3SPhoto or UserStoryCache[23]
    $ C3SYukiToki = C3SYukiToki or UserStoryCache[24]
    $ C3SShiroYuki = C3SShiroYuki or UserStoryCache[25]
    $ C1QNewsclub = C1QNewsclub or UserStoryCache[26]
    $ C1QKimuraConference = C1QKimuraConference or UserStoryCache[27]
    $ C1QSabuShin = C1QSabuShin or UserStoryCache[28]
    $ C1QTsubasa = C1QTsubasa or UserStoryCache[29]
    $ C1QMatsuta = C1QMatsuta or UserStoryCache[30]
    $ C2QNewsclub = C2QNewsclub or UserStoryCache[31]
    $ C2QKimuraConference = C2QKimuraConference or UserStoryCache[32]
    $ C2QYuuhi = C2QYuuhi or UserStoryCache[33]
    $ C2QSakuya = C2QSakuya or UserStoryCache[34]
    $ C2QSora = C2QSora or UserStoryCache[35]
    $ C3QNewsclub = C3QNewsclub or UserStoryCache[36]
    $ C3QKimuraConference = C3QKimuraConference or UserStoryCache[37]
    $ C3QSakuyaWalk1 = C3QSakuyaWalk1 or UserStoryCache[38]
    $ C3QSakuyaWalk2 = C3QSakuyaWalk2 or UserStoryCache[39]
    $ C3QShiro = C3QShiro or UserStoryCache[40]
    $ C3QNakayama = C3QNakayama or UserStoryCache[41]
    $ C3QYakyuken = C3QYakyuken or UserStoryCache[42]
    $ C3QNori = C3QNori or UserStoryCache[43]
    $ del UserStoryCache
    $ del SYSReviewChapter
    $ Chapter = 4

    if judge_lm_condition([]):
        jump block_00003CDE

    return

label block_00003CDE:
    # Node: 00003CDE (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_25

    if judge_lm_condition([]):
        jump block_00003CDB

    return

label block_00003CDB:
    # Node: 00003CDB (CLEAR)
    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_CB56E573F5D34F039682091C43399E19


    if judge_lm_condition([]):
        jump block_00002C17

    return

label block_00003CD4:
    # Node: 00003CD4 (CHAPTER 2)
    call block_00003962 from _call_block_00003962

    if judge_lm_condition([]):
        jump block_00003CD7

    return

label block_00003CD5:
    # Node: 00003CD5 (CHAPTER 3)
    call block_00003C76 from _call_block_00003C76

    if judge_lm_condition([]):
        jump block_00003CD7

    return

label block_00003CD9:
    # Node: 00003CD9 (Chapter 2)
    $ SYSReviewChapter = 2
    $ C2TalkOkajimaInitNumber = 0
    $ C2TalkOkajimaInitNumber = E_TAG_TalkOkajimaInitNumber

    if judge_lm_condition([]):
        jump block_000031B8

    return

label block_00003CDA:
    # Node: 00003CDA (Chapter 3)
    $ SYSReviewChapter = 3
    if E_TAG_C3AllowTriggleSukimotoTalk == True:
        $ C3AllowTriggleSukimotoTalk = True
    $ C3StudyCountInitValue = 0
    $ C3StudyCountInitValue = E_TAG_StudyCount
    $ C3TalkOkajimaInitNumber = 0
    $ C3TalkOkajimaInitNumber = E_TAG_TalkOkajimaInitNumber

    if judge_lm_condition([]):
        jump block_000031B8

    return

label block_000031A8:
    # Node: 000031A8 (触手A 1)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 200
    show rs_image_5171C4277664485482367CFD06553623 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_466219A035C44D62AD2743E9F494A2F2 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_FB87619C890441AEA41E279A1B588CAC "其实，我们还入手了别的有趣的梦。"

    show rs_image_A7C4CBC5126342CD8A04FA3A8072EE5F as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_FB87619C890441AEA41E279A1B588CAC "梦的内容大概是{color=#FF00FF}“回到过去”{/color}，\n你希望看看么？"

    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}从过去返回后，数据将会和现有合并。\n因此可以通过此方法收集落下的剧情。』{/color}"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("朔的家"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"


    if judge_lm_condition([]):
        jump block_000031AD

    return

label block_000031AD:
    # Node: 000031AD (T ++)
    $ E_TalkTentacleACave = E_TalkTentacleACave + 1

    if judge_lm_condition([]):
        jump block_000031AB

    return

label block_00003FBE:
    # Node: 00003FBE (觸手B 2)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 200
    show rs_image_89A27AFA4F7E47CC9A112A624C28664F as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_740EF5739095488C9C0AA2EF1A78CB35 "要看{color=#FF0000}通关得分{/color}么？"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("朔的家"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"


    if judge_lm_condition([]):
        jump block_00003FC0

    return

label block_00003FC0:
    # Node: 00003FC0 (選擇)
    call scb_selector("", [{"name":"はい", "content":_("没问题")}, {"name":"いいえ", "content":_("还有其他事情没做完")}]) from _call_scb_selector_98

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_0000425D
    if judge_lm_condition([]):
        jump block_000031AB

    return

label block_0000425D:
    # Node: 0000425D (CLEAR)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_20A8817D51644BE6A7913BD30673F110


    if judge_lm_condition([]):
        jump block_00003FC1

    return

label block_00003FC1:
    # Node: 00003FC1 (Final score)
    call block_00003F3E from _call_block_00003F3E_1

    if judge_lm_condition([]):
        jump block_00002C17

    return

label block_000031A9:
    # Node: 000031A9 (触手B 1)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    show rs_image_E13853D2180E41B9ACC256B3BB300547 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_89A27AFA4F7E47CC9A112A624C28664F as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_740EF5739095488C9C0AA2EF1A78CB35 "说起来，为何你能找到这里？\n"
    show rs_image_72BE0B1E9DFC429CBD1C3DDA16C6FAD9 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "一般人是绝对找不到的。"

    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 200
    show rs_image_5171C4277664485482367CFD06553623 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_FB87619C890441AEA41E279A1B588CAC "哦？{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_3E0CBD2C9B6745D4BABE60C027B35BD1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "你手里的那张纸是……\n"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    show rs_image_0F246856A6A34A9DAF7BFB17CCD91C95 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那不是给朔大人用的防迷路地图么！"

    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    show rs_image_7D064AD324A44E08AF6B1A05446398E6 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_740EF5739095488C9C0AA2EF1A78CB35 "本来应该是朔大人带着的。\n也就是说……"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_AABC61A64D824347A6C9F24EC2351CC3 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "（观察中）"

    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_90E13CCE039E4A09B13F2E09593276FF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "唔……\n"
    show rs_image_2D9D55E1273147FD916194309B9601B8 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "别、别管了，失败人人都有。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("朔的家"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"


    if judge_lm_condition([]):
        jump block_00003FBF

    return

label block_00003FBF:
    # Node: 00003FBF (T ++)
    $ E_TalkTentacleBCave = E_TalkTentacleBCave + 1

    if judge_lm_condition([]):
        jump block_000031AB

    return

label block_00002C2E:
    # Node: 00002C2E (忍)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_top zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_6A29046AAF4844D9A3A453B1C6A13175

    pause 0.4


    if judge_lm_condition([]):
        jump block_00002C2D

    return

label block_00002C2D:
    # Node: 00002C2D (Name)
    $ _lm_input_result = lm_input(_("请说出你的名字。"), [_("姓氏"), _("名字")], [persistent.LastName, persistent.FirstName])
    $ persistent.LastName = _lm_input_result[0]
    $ persistent.FirstName = _lm_input_result[1]
    $ del _lm_input_result

    if judge_lm_condition([]):
        jump block_00002C2C

    return

label block_00002C32:
    # Node: 00002C32 (作哉)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_486F70F1E27D43BC868FA3ADA0B574BE as tag_F12981B3CF794DEA86CFB94275B48CFB at center_top zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_6A29046AAF4844D9A3A453B1C6A13175

    pause 0.4


    if judge_lm_condition([]):
        jump block_00002C31

    return

label block_00002C31:
    # Node: 00002C31 (Name)
    $ _lm_input_result = lm_input(_("别磨蹭快说。"), [_("姓氏"), _("名字")], [persistent.LastName, persistent.FirstName])
    $ persistent.LastName = _lm_input_result[0]
    $ persistent.FirstName = _lm_input_result[1]
    $ del _lm_input_result

    if judge_lm_condition([]):
        jump block_00002C2C

    return

label block_00002C2F:
    # Node: 00002C2F (翼)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_186B19EF8A8141319DE9B5EB9DE2BAC0 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_top zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_6A29046AAF4844D9A3A453B1C6A13175

    pause 0.4


    if judge_lm_condition([]):
        jump block_00002C30

    return

label block_00002C30:
    # Node: 00002C30 (Name)
    $ _lm_input_result = lm_input(_("请、请告诉我你的名字好不好？"), [_("姓氏"), _("名字")], [persistent.LastName, persistent.FirstName])
    $ persistent.LastName = _lm_input_result[0]
    $ persistent.FirstName = _lm_input_result[1]
    $ del _lm_input_result

    if judge_lm_condition([]):
        jump block_00002C2C

    return

label block_00002C38:
    # Node: 00002C38 (月)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_top zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_6A29046AAF4844D9A3A453B1C6A13175

    pause 0.4


    if judge_lm_condition([]):
        jump block_00002C34

    return

label block_00002C34:
    # Node: 00002C34 (Name)
    $ _lm_input_result = lm_input(_("说出你的名字。"), [_("姓氏"), _("名字")], [persistent.LastName, persistent.FirstName])
    $ persistent.LastName = _lm_input_result[0]
    $ persistent.FirstName = _lm_input_result[1]
    $ del _lm_input_result

    if judge_lm_condition([]):
        jump block_00002C2C

    return

label block_00002C37:
    # Node: 00002C37 (空)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_1CDBF9A281F54418A7363E36408C7DD5 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_top zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_6A29046AAF4844D9A3A453B1C6A13175

    pause 0.4


    if judge_lm_condition([]):
        jump block_00002C33

    return

label block_00002C33:
    # Node: 00002C33 (Name)
    $ _lm_input_result = lm_input(_("我想知道怎么称呼你。"), [_("姓氏"), _("名字")], [persistent.LastName, persistent.FirstName])
    $ persistent.LastName = _lm_input_result[0]
    $ persistent.FirstName = _lm_input_result[1]
    $ del _lm_input_result

    if judge_lm_condition([]):
        jump block_00002C2C

    return

label block_00002C39:
    # Node: 00002C39 (三朗)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_602B12F1C445477F861182BD846DB0BD as tag_F12981B3CF794DEA86CFB94275B48CFB at center_top zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_6A29046AAF4844D9A3A453B1C6A13175

    pause 0.4


    if judge_lm_condition([]):
        jump block_00002C35

    return

label block_00002C35:
    # Node: 00002C35 (Name)
    $ _lm_input_result = lm_input(_("抱歉，你的名字是？"), [_("姓氏"), _("名字")], [persistent.LastName, persistent.FirstName])
    $ persistent.LastName = _lm_input_result[0]
    $ persistent.FirstName = _lm_input_result[1]
    $ del _lm_input_result

    if judge_lm_condition([]):
        jump block_00002C2C

    return

label block_00002C3A:
    # Node: 00002C3A (慎太郎)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_29B059D0AECE4F3FBF86EE5DA29B17DF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_top zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_6A29046AAF4844D9A3A453B1C6A13175

    pause 0.4


    if judge_lm_condition([]):
        jump block_00002C36

    return

label block_00002C36:
    # Node: 00002C36 (Name)
    $ _lm_input_result = lm_input(_("告诉我名字好不好☆"), [_("姓氏"), _("名字")], [persistent.LastName, persistent.FirstName])
    $ persistent.LastName = _lm_input_result[0]
    $ persistent.FirstName = _lm_input_result[1]
    $ del _lm_input_result

    if judge_lm_condition([]):
        jump block_00002C2C

    return

label block_00002BD5:
    # Node: 00002BD5 (朔 Home)
    stop music fadeout 1.5
    $ sys_music_current_file = ""

    stop effect2 fadeout 0.7
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("朔的家"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5E4B22942A284109B65800E46DBB8782 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "IsCaveRollbackAvailable == True" }]):
        jump block_000031AB
    if judge_lm_condition([]):
        jump block_00002BD4

    return

label block_00003CC5:
    # Node: 00003CC5 (Map)
    $ zorder_tag_62272429BE0E491AB48B3734A8ECF1EF = 500
    show rs_image_F613DEA7595D4499A4821020298A09E4 as tag_62272429BE0E491AB48B3734A8ECF1EF at center_bottom zorder zorder_tag_62272429BE0E491AB48B3734A8ECF1EF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003CC6

    return

label block_00003CC6:
    # Node: 00003CC6 (Prepare)
    $ StepList = 0
    $ StepList = [0] * 10
    $ StepList[0] = 0
    $ StepList[1] = 2
    $ StepList[2] = 2
    $ StepList[3] = 1
    $ StepList[4] = 0
    $ StepList[5] = 0
    $ StepList[6] = 1
    $ StepList[7] = 2
    $ StepList[8] = 2
    $ StepList[9] = 1
    $ CurrentStep = -1

    if judge_lm_condition([]):
        jump block_00003CC4

    return

label block_00003CC4:
    # Node: 00003CC4 (Update)
    $ CurrentStep = CurrentStep + 1
    if IsCaveMemoAvailable == True:
        $ StatusY = 0
        $ renpy.hide("Pointer")
        if CurrentStep == 9:
            $ StatusY = 82
        elif CurrentStep == 8:
            $ StatusY = 128
        elif CurrentStep == 7:
            $ StatusY = 174
        elif CurrentStep == 6:
            $ StatusY = 220
        elif CurrentStep == 5:
            $ StatusY = 274
        elif CurrentStep == 4:
            $ StatusY = 321
        elif CurrentStep == 3:
            $ StatusY = 360
        elif CurrentStep == 2:
            $ StatusY = 406
        elif CurrentStep == 1:
            $ StatusY = 452
        elif CurrentStep == 0:
            $ StatusY = 504
        $ renpy.show("images/Cave/Pointer.png", at_list=[Transform(xpos=652, ypos=StatusY)], what=renpy.easy.displayable("images/Cave/Pointer.png"), tag="Pointer", zorder=1000)
        $ del StatusY

    if judge_lm_condition([{ "scope": 0, "content": "CurrentStep < 5" }]):
        jump block_00003CC7
    if judge_lm_condition([{ "scope": 0, "content": "CurrentStep < 10" }]):
        jump block_00003CC8
    if judge_lm_condition([]):
        jump block_00003CCA

    return

label block_00003CC7:
    # Node: 00003CC7 (Cave 1)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2E5B21E5FC4042A6A211C911987D2995 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003CCB

    return

label block_00003CCB:
    # Node: 00003CCB (選擇)
    $ sys_lm_menu_item = [{"pos": (341, 286),"image": "images/Selection/Cave/Up.png","hover": "images/Selection/Cave/Up hover.png","name": "上"}, {"pos": (418, 403),"image": "images/Selection/Cave/Right.png","hover": "images/Selection/Cave/Right hover.png","name": "右"}, {"pos": (238, 403),"image": "images/Selection/Cave/Left.png","hover": "images/Selection/Cave/Left hover.png","name": "左"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_793
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([]):
        jump block_00003CCC

    return

label block_00003CCC:
    # Node: 00003CCC (Check)
    if (_lm_selected_value == "上" and (StepList[CurrentStep] <> 0)) or (_lm_selected_value == "左" and (StepList[CurrentStep] <> 1)) or (_lm_selected_value == "右" and (StepList[CurrentStep] <> 2)):
        $ _lm_selected_value = "Wrong"
    else:
        $ _lm_selected_value = "Correct"

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Correct\"" }]):
        jump block_00003CCE
    if judge_lm_condition([]):
        jump block_00002B8A

    return

label block_00003CCE:
    # Node: 00003CCE (TO: Update)

    if judge_lm_condition([]):
        jump block_00003CC4

    return

label block_00002B8A:
    # Node: 00002B8A (Caught)
    pause 0.5

    stop effect2 fadeout 0.8
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Tentacle 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Tentacle 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Tentacle 1.ogg"

    # Gallery unlock: images/CG/Cave caught.png
    $ zorder_rs_image_D8781686D9AC4CE7B6A0E90C3986C44F = -100
    show rs_image_D8781686D9AC4CE7B6A0E90C3986C44F as rs_image_D8781686D9AC4CE7B6A0E90C3986C44F zorder zorder_rs_image_D8781686D9AC4CE7B6A0E90C3986C44F onlayer master
    hide rs_image_D8781686D9AC4CE7B6A0E90C3986C44F

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_62272429BE0E491AB48B3734A8ECF1EF
    hide Pointer
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_D8781686D9AC4CE7B6A0E90C3986C44F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_3ADD2F6A88DE49EE938D3528913A8DDD

    pause 1

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FF0000}『被触手抓到了！{/color}\n{w=0.5}{color=#FF0000}被运回洞口了！』{/color}"

    window hide

    pause 0.7

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_3ADD2F6A88DE49EE938D3528913A8DDD

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002B83

    return

label block_00003CC8:
    # Node: 00003CC8 (Cave 2)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_132497727EC347A7B5DC72054FFACE31 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003CCB

    return

label block_00003CCA:
    # Node: 00003CCA (Cave 3)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_62272429BE0E491AB48B3734A8ECF1EF
    hide Pointer
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_8382B2402B5D44C5B31249AF7209A499 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003CCF

    return

label block_00003CCF:
    # Node: 00003CCF (CLEAR)
    $ del StepList
    $ del CurrentStep

    if judge_lm_condition([]):
        jump block_00002BAA

    return

label block_00002C24:
    # Node: 00002C24 (Back)
    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003CD1

    return

label block_00003CD1:
    # Node: 00003CD1 ()
    $ del CaveRandomResult

    return

