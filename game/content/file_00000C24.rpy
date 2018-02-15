# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00000C24 (CP2 Daytime 慎太郎)

label block_00000C25:
    # Node: 00000C25 (開始)

    if judge_lm_condition([{ "scope": 0, "content": "C2S3Phase == 99" }]):
        jump block_000017FD
    if judge_lm_condition([]):
        jump block_00003BCA

    return

label block_000017FD:
    # Node: 000017FD (BGM 2)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"


    if judge_lm_condition([]):
        jump block_00000C27

    return

label block_00000C27:
    # Node: 00000C27 (School outside)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ set_place_title(False)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "shintaro"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([{ "scope": 0, "content": "C2S3Phase == 99" }]):
        jump block_00001788
    if judge_lm_condition([]):
        jump block_00000C79

    return

label block_00001788:
    # Node: 00001788 (School outside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_00001771", target_label="block_000016AD") from _call_scb_global_map_173
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00003B04
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00000C2F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_00000C31
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00000C30
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00000C32
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00000C33
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00001788
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00001771
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_000016AD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001788
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FAC

    return

label block_00003B04:
    # Node: 00003B04 (TO: School inside)

    if judge_lm_condition([]):
        jump block_00000C26

    return

label block_00000C26:
    # Node: 00000C26 (School inside)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "shintaro"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([{ "scope": 0, "content": "C2S3Phase == 99" }]):
        jump block_0000178C
    if judge_lm_condition([]):
        jump block_00000C78

    return

label block_0000178C:
    # Node: 0000178C (School inside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_00003B09", target_label="block_00003B0A") from _call_scb_global_map_174
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" },{ "scope": 1, "content": "TalkTomoF3 == 0" },{ "scope": 1, "content": "TalkTomoF3 == 2" }]):
        jump block_00000C2E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" },{ "scope": 1, "content": "TalkTomoF3 == 1" }]):
        jump block_00001094
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00003B0B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" },{ "scope": 1, "content": "TalkSaburoF3 == True" }]):
        jump block_0000241C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00000C2A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00000C2B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_00000C2C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00000C2D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_0000178C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00003B09
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00003B0A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_0000178C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FAD

    return

label block_00000C2E:
    # Node: 00000C2E (Toilet 1)
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

    $ set_place_title(_("厕所"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_297E564A7C1544469FB88A41AB85B6C9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkTomoF3 == 2" }]):
        jump block_0000241B
    if judge_lm_condition([]):
        jump block_00000D11

    return

label block_0000241B:
    # Node: 0000241B (Toilet 友 sage)
    $ sys_lm_menu_item = [{"pos": (368, 120),"image": "images/Chapter 2/Menu/F3/Tomo sage.png","hover": "images/Chapter 2/Menu/F3/Tomo sage hover.png","name": "友"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_738
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友\"" }]):
        jump block_00000D29
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B05

    return

label block_00000D29:
    # Node: 00000D29 (友)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_316F7A10366C4C87B989B800C63113DB as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.5

    window show

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊，这位是{color=#808000}贤者大人{/color}。{w}\n真是辛苦了。"

    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_316F7A10366C4C87B989B800C63113DB as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "免礼。"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("厕所"))

    if judge_lm_condition([]):
        jump block_0000241B

    return

label block_00003B05:
    # Node: 00003B05 (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003B04

    return

label block_00000D11:
    # Node: 00000D11 (Toilet 友)
    $ sys_lm_menu_item = [{"pos": (368, 120),"image": "images/Chapter 2/Menu/F3/Tomo.png","hover": "images/Chapter 2/Menu/F3/Tomo hover.png","name": "友"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_739
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B05
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友\"" }]):
        jump block_00000D28

    return

label block_00000D28:
    # Node: 00000D28 (友)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_24C711A2BE52475F8507DA19607EEE0E as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "坐立难安……"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "怎么了？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EAA37886FF234C5AB35992304EE98E9B as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什、什么都没有——！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "（太明显了。）"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("厕所"))

    if judge_lm_condition([{ "scope": 0, "content": "TalkTomoF3 == 0" }]):
        jump block_00002CA6
    if judge_lm_condition([]):
        jump block_00000D11

    return

label block_00002CA6:
    # Node: 00002CA6 (T ++)
    $ TalkTomoF3 = TalkTomoF3 + 1

    if judge_lm_condition([{ "scope": 0, "content": "TalkTomoF3 == 2" }]):
        jump block_00001095
    if judge_lm_condition([]):
        jump block_00000D11

    return

label block_00001095:
    # Node: 00001095 (Toilet empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_740
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B06

    return

label block_00003B06:
    # Node: 00003B06 (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003B05

    return

label block_00001094:
    # Node: 00001094 (Toilet 2)
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

    $ set_place_title(_("厕所"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_531E9A5102504415AD59CA198E9086DB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002CA6

    return

label block_00003B0B:
    # Node: 00003B0B (TO: School outside)

    if judge_lm_condition([]):
        jump block_00000C27

    return

label block_0000241C:
    # Node: 0000241C (三朗 event 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "现在就悄悄地不要去打扰了♪{w}\n我还真是贴心呐！"

    window hide


    jump block_00000C26

    return

label block_00000C78:
    # Node: 00000C78 (School inside XCTA)
    call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00003B07", target_label="block_00003B08") from _call_scb_global_map_175
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" },{ "scope": 1, "content": "TalkTomoF3 == 0" },{ "scope": 1, "content": "TalkTomoF3 == 2" }]):
        jump block_00000C2E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" },{ "scope": 1, "content": "TalkTomoF3 == 1" }]):
        jump block_00001094
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00000C2A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" },{ "scope": 1, "content": "TalkSaburoF3 == True" }]):
        jump block_0000241C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00000C2B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_00000C2C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00000C2D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00003B0B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00000C78
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00003B07
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00003B08
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00003B0F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FAD

    return

label block_00000C2A:
    # Node: 00000C2A (Aisle 2)
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
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000C34

    return

label block_00000C34:
    # Node: 00000C34 (Aisle 2)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (152, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "踊り場へ"}, {"pos": (376, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "新聞部へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_741
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B06
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部へ\"" }]):
        jump block_00000C4A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"踊り場へ\"" }]):
        jump block_00000C4E

    return

label block_00000C4A:
    # Node: 00000C4A (Newsclub)
    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("新闻部活动室"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000C4B

    return

label block_00000C4B:
    # Node: 00000C4B (Newsclub)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (112, 160),"image": "images/Chapter 2/Menu/Okajima.png","hover": "images/Chapter 2/Menu/Okajima hover.png","name": "岡島"}, {"pos": (392, 160),"image": "images/Chapter 2/Menu/Kojima.png","hover": "images/Chapter 2/Menu/Kojima hover.png","name": "小島"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_742
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000C2A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_00000C5B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" },{ "scope": 1, "content": "TalkOkajimaKojimaF3 == True" }]):
        jump block_00000C5C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_000023F1

    return

label block_00000C5B:
    # Node: 00000C5B (岡島)
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_6EACDBA5EB7B44D7A7699633252E6B7E as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000023F2

    return

label block_000023F2:
    # Node: 000023F2 (岡島+小島)
    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好呀！新闻部的两人♪"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BB675405870B497F958414550471B4BF as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "呀，欢迎，奥村君！\n"
    show rs_image_6EACDBA5EB7B44D7A7699633252E6B7E as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哦，对了。小岛君，把那个东西给他。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "明白了。{w}\n奥村同学，感谢一直为我们提供情报。"

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_A3D0E6087D6B4C4DA8B5F544E1F3B782 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.4

    rs_character_53FF68C192E3494AB005C1909579AFFB "这是一点谢意。"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "谢了♪这次会是什么照片呢，好激动☆"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DF83E8681DAD43B1BF6C0CF0E3555C11 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "奥村君总是这个样子呐。\n也是多亏了你我们得到了很大帮助。\n今后也要继续拜托了。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说什么见外的话！\n每次的礼物品质都那么好♪\n今后也要长期合作哦！"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_00002F3F

    return

label block_00002F3F:
    # Node: 00002F3F (T ++)
    $ TalkOkajimaKojimaF3 = True

    if judge_lm_condition([]):
        jump block_00000C4B

    return

label block_00000C5C:
    # Node: 00000C5C (小島 2)
    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说起来啊，小岛亲。"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A3D0E6087D6B4C4DA8B5F544E1F3B782 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "怎么了？"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我至今收到的所有作为礼物的照片里，\n从没出现过冈岛亲的……"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "为何？"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "哦呀哦呀，如奥村同学这样的人居然都看不透我的感情。\n"
    show rs_image_9511CC62DD3C41CB9B75011464423CB6 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "真是失望。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼呼，开玩笑的～只是试着问问罢了♪"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6BEAA3D38A204EAE8EFEE059FD541711 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "嗯？在说什么？"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1654C244584349A6B0811665076020BD as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_F16EFBE20FE44A87BB46D6DA57694BF4 "什么也没有（哦）。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_00000C4B

    return

label block_000023F1:
    # Node: 000023F1 (小島)
    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000023F2

    return

label block_00000C4E:
    # Node: 00000C4E (Stairwell)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("楼梯间"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S3Phase == 99" }]):
        jump block_00000D02
    if judge_lm_condition([]):
        jump block_00000D2C

    return

label block_00000D02:
    # Node: 00000D02 (Stairwell)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_743
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000C2A

    return

label block_00000D2C:
    # Node: 00000D2C (Stairwell 木村 flag)
    $ sys_lm_menu_item = [{"pos": (344, 216),"image": "images/Chapter 2/Menu/F3/Kimura flag.png","hover": "images/Chapter 2/Menu/F3/Kimura hover.png","name": "木村"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_744
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_00000D2A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000C2A

    return

label block_00000D2A:
    # Node: 00000D2A (F3: 木村)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_4263ADF3DB8F476795DD48ECB73A8A2E as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4263ADF3DB8F476795DD48ECB73A8A2E as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦～～呜～～姆～～呜～～……"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哇！怎么了木村亲？！到底怎么了！？"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4263ADF3DB8F476795DD48ECB73A8A2E as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_59AAF132B57B402BB1B9171904F5D5B2

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "我……我最后还是和那孩子分手了！！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸！？等等到底怎么回事！？\n之前不是都亲过了么！"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4271CF98C3494E2FA007048FB141D469 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "就是在那之后开始出的问题……"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "总、总之先从头说！"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))
    pause 0.8

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91


    if judge_lm_condition([]):
        jump block_00003B16

    return

label block_00003B16:
    # Node: 00003B16 (FLAG: CP2F3)
    call block_00003B11 from _call_block_00003B11_1

    if judge_lm_condition([]):
        jump block_00003B1C

    return

label block_00003B1C:
    # Node: 00003B1C (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#AA0055}“RUN☆RUN☆LOVERS”{/color}{color=#0080FF}成功结束。』{/color}"

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
        jump block_00003B1D

    return

label block_00003B1D:
    # Node: 00003B1D ()

    return

label block_00000C2B:
    # Node: 00000C2B (Roof)
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

    $ set_place_title(_("屋顶"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkSaburoF3 == False" }]):
        jump block_00000C5E

    return

label block_00000C5E:
    # Node: 00000C5E (三朗 event)
    pause 0.7

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦呀呀？"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CBFB350257CD4F1A9A0611CD76675A37 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "ZZz……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.3

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这孩子还真是喜欢午睡～{w}\n这么没有防备可就别怪我了哦～？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……"

    window hide

    pause 0.6

    $ set_window("イベントモード")
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 500
    show rs_image_905E9C679FD7435E8DF16A4ECBCB85EA as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.7

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "算了，{w}看在可爱的睡脸上这次就不了。"

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1.4

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"

    window hide

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002CA5

    return

label block_00002CA5:
    # Node: 00002CA5 (T ++)
    $ TalkSaburoF3 = True

    if judge_lm_condition([]):
        jump block_00003B06

    return

label block_00000C2C:
    # Node: 00000C2C (Music room)
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
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000C36

    return

label block_00000C36:
    # Node: 00000C36 (Music room 忍+翼)
    $ sys_lm_menu_item = [{"pos": (376, 200),"image": "images/Chapter 2/Menu/Shinobu music room.png","hover": "images/Chapter 2/Menu/Shinobu music room hover.png","name": "しのぶ"}, {"pos": (192, 192),"image": "images/Chapter 2/Menu/Tsubasa music room.png","hover": "images/Chapter 2/Menu/Tsubasa hover.png","name": "つばさ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_745
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B06
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_0000241F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_0000241E

    return

label block_0000241F:
    # Node: 0000241F (忍)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_22306BD9E0624D81A1CFFFB486C5BAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000241D

    return

label block_0000241D:
    # Node: 0000241D (忍+翼)
    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊咧——？两位在这里有何贵干？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A43C35FAF6E4488E87E8829D5D8E84E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "在听翼君弹钢琴。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3FFA42ECEDF14A378835CC5A7CEED291 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊哈哈，还完全不行呐。{w}\n毕竟从友君开始教我到现在\n才不过几个月……"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦——总觉得好意外。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C2A28861C0A44DC6AAE17E0ABA1BE61C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "意外？"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我还以为你们两人的关系一定不会这么好。{w}\n毕竟，你看，喜欢上同一个人了嘛。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AD8CFA3B3632464BA96A924CD8D32A10 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜呜。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8FD0C8C99F91493DB85D4EB39544B538 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "都说了我对那家伙并没有这种感情。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不该出现点{color=#800080}某深夜动画{/color}那样的柴刀展开？\n"
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_56A9AF7A39F14E9D8BB98BE49AEEBE8D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    pause 0.3

    extend "特别是翼亲一定要努力！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "再说了，病娇手边常备一两个专属武器才是最基本的。\n这方面翼亲还是太嫩了～"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12E3E3C881C34AC09EF31505C89F7982 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "什么乱七八糟的。"
    show rs_image_18DB531342D94D37B18E5E70E8724066 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "我说啊，\n我和翼君到现在可一直都是{color=#008080}友好交流{/color}的。\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_5D6DDBFC5BD94344881F3CC2CFB02044 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    pause

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_32A6171EED0D4A9F920F16574ED46630 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "对不对，翼君。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_41E510B2D9524FDFA7C309AE72C92A02 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯，关系很好哦。\n一直以来忍君都在关照着我哦。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀——……"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "嘛算了！\n那种诚哥展开对我们不合适♪\n今后也要和和气气地度过每一天哦！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("音乐室"))

    if judge_lm_condition([]):
        jump block_00000C36

    return

label block_0000241E:
    # Node: 0000241E (翼)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_43C2A5DA4B5D4815BEC6FE1DA10014AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000241D

    return

label block_00000C2D:
    # Node: 00000C2D (Library)
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
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000C37

    return

label block_00000C37:
    # Node: 00000C37 (Library)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_746
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B05

    return

label block_00003B07:
    # Node: 00003B07 (Converstion)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那么那么～\n该去暗中观察那些迷途羔羊了♪"

    window hide

    $ set_window("(標準)")

    return

label block_00003B08:
    # Node: 00003B08 (Target)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『试着去倾听朋友们的烦恼。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003B0F:
    # Node: 00003B0F (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_00003B0D

    return

label block_00003B0D:
    # Node: 00003B0D (RESET)
    $ C2S1Phase = 0
    $ C2S2Phase = 0
    $ C2S3Phase = 0
    $ C2S4Phase = 0
    $ C2S5Phase = 0
    $ C2S6Phase = 0

    if judge_lm_condition([]):
        jump block_00003B0C

    return

label block_00003B0C:
    # Node: 00003B0C (終了)

    return

label block_00001FAD:
    # Node: 00001FAD (Character)
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

label block_00003B09:
    # Node: 00003B09 (Conversation)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这样——\n木村亲和那孩子最后还是分手了呐。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "也确实。\n一开始就觉得相性不是很好……"

    window hide

    $ set_window("(標準)")

    return

label block_00003B0A:
    # Node: 00003B0A (Target)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『找到可能对这件事感兴趣的人，\n然后看他的反应！』』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00000C2F:
    # Node: 00000C2F (Shoe cupboard)
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
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000C39

    return

label block_00000C39:
    # Node: 00000C39 (Shoe cupboard)
    $ sys_lm_menu_item = [{"pos": (160, 96),"image": "images/Menu/Nameko.png","hover": "images/Menu/Nameko hover.png","name": "滑子"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_747
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003AFD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_00000C3E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" }]):
        jump block_00000CEE

    return

label block_00003AFD:
    # Node: 00003AFD (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003AFC

    return

label block_00003AFC:
    # Node: 00003AFC (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003AFB

    return

label block_00003AFB:
    # Node: 00003AFB (TO: School outside)

    if judge_lm_condition([]):
        jump block_00000C27

    return

label block_00000C3E:
    # Node: 00000C3E (Playground)
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
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000D12

    return

label block_00000D12:
    # Node: 00000D12 (Playground)
    $ sys_lm_menu_item = [{"pos": (328, 140),"image": "images/Chapter 2/Menu/Katou.png","hover": "images/Chapter 2/Menu/Katou hover.png","name": "加藤"}, {"pos": (632, 208),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "体育倉庫"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_748
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" }]):
        jump block_00000C47
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" }]):
        jump block_00000C50
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000C2F

    return

label block_00000C47:
    # Node: 00000C47 (加藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_CF9552A127F84B139910618B1FE71819 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_1230EA82690842C19B5D31327B9A64D9 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "怎么才能顺利追到大人呢……"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "多少岁的？\n20？30？还是说40以上？"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D530673622A94BAABCC7B824142E3D26 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯……还没想到那么细。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "基本上，大人和孩子是不同的，\n他们很明确地明白自己的喜好。{w}\n作为对象{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "出局的一瞬，基本上就没有下文了。"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1DB6078B9236425482D8C50AB190159F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "这样。"
    show rs_image_3B212EC295AB46A7854BCF9A8DE13F22 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "也就是说\n在知道那个人究竟喜不喜欢年下之前\n积极展开攻击是不行的。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不不，只是这样的话，没戏。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "在此之上还要细分，\n是喜欢{color=#FF0000}杰尼斯（中性）{/color}系、\n{color=#FF0000}体育会{/color}系、{color=#FF0000}短发{/color}、亦或是{color=#FF0000}长发{/color}。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "边边角角都要关注到，\n确定是不是真的满足自己的喜好，\n否则大人是很难做出决定的～"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_581796CAD76B4C929577B4C1D581EF10 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "欸……比想像中还要麻烦……"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "顺便一提，根据喜欢年轻孩子的大人们的意见，\n{color=#0080FF}20岁左右的喜欢范围比较窄{/color}，{color=#008A45}30岁就广了一些{/color}，\n{color=#800080}40岁以后，基本上只要年轻谁都可以了{/color}。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "差不多就是这个样子。"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_36E75A5BA4504559920E625E0462334C as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "原来如此……\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5690F6AF976C4AEB8FC348FA1E25466F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那么，就从难度最低的\n40岁以上开始攻略！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "诶。真的可以？行不行？"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C5C9A2538FCB4FCB827FE1BBFE20727F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "哦，没问题！\n"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_720C0D06E4A146109B2FB898D5464241 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "仔细想想，倒不如说\n成熟的类型正是我的菜。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……加藤酱这种呆呆的地方，\n我还是觉得不错的哦。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000D12

    return

label block_00000C50:
    # Node: 00000C50 (PE warehouse)
    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("体育仓库"))
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F36816057C4848709177D4C457D25726 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000C51

    return

label block_00000C51:
    # Node: 00000C51 (PE warehouse)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_749
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000C3E

    return

label block_00000CEE:
    # Node: 00000CEE (滑子)
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_9C78AB751CDB49FDA83251FA5B4A3825 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "奥村，可别由着自己的性子玩太过火了啊。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "没关系滑子Teacher！{w}\n自己这么说有点不好意思，\n这点事情我还是知道的——♪"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_18143FE53E3243FE85CB8033C5618253 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "嗯，那就好。\n你看上去就是不太令人放心的样子。{w}\n一定注意不要太勉强自己。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))

    if judge_lm_condition([]):
        jump block_00000C39

    return

label block_00000C31:
    # Node: 00000C31 (Atrium)
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
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S3Phase == 99" }]):
        jump block_00000D25
    if judge_lm_condition([]):
        jump block_00001F4C

    return

label block_00000D25:
    # Node: 00000D25 (Atrium 伊藤 point)
    $ sys_lm_menu_item = [{"pos": (480, 152),"image": "images/Chapter 2/Menu/F3/Itou point.png","hover": "images/Chapter 2/Menu/F3/Itou hover.png","name": "伊藤"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_750
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003AFD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_00003B1B

    return

label block_00003B1B:
    # Node: 00003B1B ()

    return

label block_00001F4C:
    # Node: 00001F4C (Atrium)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_751
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003AFC

    return

label block_00000C30:
    # Node: 00000C30 (Gym outside)
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
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000C3A

    return

label block_00000C3A:
    # Node: 00000C3A (Gym outside 松田)
    $ sys_lm_menu_item = [{"pos": (168, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "体育館へ"}, {"pos": (384, 184),"image": "images/Chapter 2/Menu/Matsuta gym outside.png","hover": "images/Chapter 2/Menu/Matsuta gym outside hover.png","name": "松田"}, {"pos": (664, 280),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "柔道場へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_752
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003AFD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" }]):
        jump block_00000C40
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_00000D27
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"柔道場へ\"" }]):
        jump block_00000D00

    return

label block_00000C40:
    # Node: 00000C40 (Gym)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("体育馆"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_24188CBA120A4166B08F8A3535548A8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S3Phase == 99" }]):
        jump block_00002428
    if judge_lm_condition([]):
        jump block_00000D26

    return

label block_00002428:
    # Node: 00002428 (Gym outside empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_753
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([]):
        jump block_00000C30

    return

label block_00000D26:
    # Node: 00000D26 (Gym 泉)
    $ sys_lm_menu_item = [{"pos": (296, 208),"image": "images/Chapter 2/Menu/Izumi.png","hover": "images/Chapter 2/Menu/Izumi hover.png","name": "泉"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_754
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_00000C44
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000C30

    return

label block_00000C44:
    # Node: 00000C44 (泉)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_4CAFD25A1F5E4405A36AFD06AA87C091 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀吼——！泉！{w}\n最近怎么样？\n和那个前辈交往顺利么？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D668AB5BCE7641D598E5B719952F1E93 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "嗯，{w}这都是多亏\n{color=#008080}奥村同学在背后推了我一把{/color}呢。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_36B84EE543EB42D985409657831B8327 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦吼吼♪理所当然哦！\n我的使命可是让御咲学园所有学生\n全都恩恩爱爱在一起哦♪"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "还有什么烦恼记着找我哦！"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4CAFD25A1F5E4405A36AFD06AA87C091 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "嗯。"
    show rs_image_A886E64725024E519334B46B47F7F928 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "那个，和前辈是没什么……"

    show rs_image_9AF02379E9534E1FB204413A9C8F2675 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "不过，{w}\n其实前辈的弟弟似乎对我们有意见。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀——好麻烦——\n嗯——这个嘛…………{w}\n……{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "这种时候就要！！"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A886E64725024E519334B46B47F7F928 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "嗯、嗯。"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{color=#FF0080}把握住侵犯与被侵犯的权利☆{/color}"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5345B1A31CF144EC8F0B037DDCA0098B as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_0364D19042AC45CCA8C6BF99EF5EA070 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "这、这怎么可以！！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈哈——开玩笑的♪"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "前辈的弟弟君啊……{w}\n他应该也是有男朋友的，按说应该能接受\n你们的关系才对吧。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "可能只是对哥哥被夺走吃醋了。{w}\n也说不定是和男朋友相处不愉快\n只是在没事找事而已。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我会关注一下的。\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    extend "嘛，虽说问题很多，但这就是恋爱。\n加油哦——泉♪"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_78EAE7781AEB4E259E9665DF655EBB18 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_8D9249CA1389416BAF6A122851E276D0 "嗯，是呢。\n谢谢，我会努力的。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_00000D26

    return

label block_00000D27:
    # Node: 00000D27 (松田)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_F74587AF3C5D4336B5497ADD0EDFD9BA as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "奥村，最近如何？"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不好不坏——说起来，松田亲呢？"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "还满足于之前说的\n“{color=#FF00FF}从远处看着喜欢的人就好{/color}”？"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_21F3DA87B080401888872AA61FC24963 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "当然。只要他幸福，我是无所谓的。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "还是那么帅呐。{w}\n不过，如果松田亲行动起来，\n说不定那孩子会更幸福呐？"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_670819AC463C49439D1F729E8DF40D29 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "也许？\n现在还没有这种感觉不过\n"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_D2AEEBD45B8A4EA28C01CA659F7995E6 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "如果真的是这样，我一定会一冲到底。"

    if sys_effect2_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    show rs_image_251FE1E33C4F42E8AD83D63A46894F82 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "肉食系全开的情况下♪"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀～☆好帅！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "能被松田亲这样的男子汉发掘……\n不对，{w}是被迷上的孩子\n真是幸福羡慕呐～"

    show rs_image_F74587AF3C5D4336B5497ADD0EDFD9BA as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "谢谢，就算是客套话也谢了。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000C3A

    return

label block_00000D00:
    # Node: 00000D00 (Judo)
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

    $ set_place_title(_("柔道场外"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_153E9CF7193C4513869D54FA898561FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000D01

    return

label block_00000D01:
    # Node: 00000D01 (Judo 月)
    $ sys_lm_menu_item = [{"pos": (320, 232),"image": "images/Chapter 2/Menu/Tsuki.png","hover": "images/Chapter 2/Menu/Tsuki hover.png","name": "月"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_755
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000C30
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00001F4B

    return

label block_00001F4B:
    # Node: 00001F4B (月)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_FF2F05BF45D647239862F7725764481C as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7838A3FA6F98494CACA2B6E04E3C82B2 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "奥村，有事和你说。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……好严肃，怎么了？"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F63E385A95E44F529E8174DDE5CC8B81 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "其实……"

    window hide

    pause 0.4

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 1

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.4

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这样。一个人真努力呐。"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7838A3FA6F98494CACA2B6E04E3C82B2 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我是因为有必须去做的责任。\n"
    show rs_image_4F3E2E3628734329904C89EF6859F2DC as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……那么，问题就在这里。"

    show rs_image_9CD666B82870491B8A8E86DEB16BE5D2 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我到底该怎么对空表述。再说了空真的会接受么。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯……{w}小空会发火的话……\n{w=0.7}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "也只有在{color=#FF00FF}阿月想要一个人“包揽”全部{/color}\n的时候不是吗？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "其他事一定会被接受的。"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B1FC5F4C1C12446FA8B2429310BFC93F as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是吗。{w=0.5}{nw}"
    show rs_image_225455F87C6D4EB5BE746486367900D8 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "要是这样就好了。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "似乎很困难，但只要再努力一下就好。{w}\n阿月都努力到这里了，一定可以的！"

    show rs_image_F68AF26120614B7DBF610FDFDB886987 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "谢谢……！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("柔道场外"))

    if judge_lm_condition([]):
        jump block_00000D01

    return

label block_00000C32:
    # Node: 00000C32 (Schoolhouse)
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
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000C3C

    return

label block_00000C3C:
    # Node: 00000C3C (Schoolhouse)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_756
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003AFD

    return

label block_00000C33:
    # Node: 00000C33 (School door)
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
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000C3D

    return

label block_00000C3D:
    # Node: 00000C3D (School door)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (96, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "屋外トイレへ"}, {"pos": (456, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "学校看板"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_757
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003AFC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外トイレへ\"" }]):
        jump block_00000C4C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学校看板\"" }]):
        jump block_00000C6F

    return

label block_00000C4C:
    # Node: 00000C4C (Outside toilet)
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
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D5370D554F61451C806A39C7BC540968 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000C4D

    return

label block_00000C4D:
    # Node: 00000C4D (Outside toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (472, 192),"image": "images/Menu/Tokiwa.png","hover": "images/Menu/Tokiwa hover.png","name": "常磐"}, {"pos": (472, 192),"image": "images/Menu/Tokiwa.png","hover": "images/Menu/Tokiwa hover 2.png","name": "常磐"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_758
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000C33
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" }]):
        jump block_00000C70

    return

label block_00000C70:
    # Node: 00000C70 (常磐)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 at center_bottom zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_2917E94D246C4B5DBB7438FB372D005B as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C223850065F6443080205D1F61C04C98 "总觉得最近周围大家都很热衷恋爱呐。"

    show rs_image_B7BD90C9E0F94D39B930CB8F323D6C2F as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "不过，我对“恋爱”是什么并不确定。"

    show rs_image_E6880BD53D33411C8F831E6238B3D5C5 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "当然我确实有重要的人……{w}\n可那究竟是爱情还是友情，我并不清楚。"

    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "似乎大家都能分清的样子，\n果然大家很厉害呢。"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外厕所"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000C4D

    return

label block_00000C6F:
    # Node: 00000C6F (Board)
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
        jump block_00000C3D

    return

label block_00001771:
    # Node: 00001771 (Conversation)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这样——\n木村亲和那孩子最后还是分手了呐。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "也确实。\n一开始就觉得相性不是很好……"

    window hide

    $ set_window("(標準)")

    return

label block_000016AD:
    # Node: 000016AD (Target)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『找到可能对这件事感兴趣的人，\n然后看他的反应！』』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FAC:
    # Node: 00001FAC (Character)
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

label block_00000C79:
    # Node: 00000C79 (School outside XCTA)
    call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_00000CDF", target_label="block_00000CE0") from _call_scb_global_map_176
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00000C30
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00000C32
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00000C33
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00000C2F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00003B04
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00000C79
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00000CDF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00000CE0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00003AFE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FAC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_00000C31

    return

label block_00000CDF:
    # Node: 00000CDF (Converstion)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那么那么～\n该去暗中观察那些迷途羔羊了♪"

    window hide

    $ set_window("(標準)")
    
    return

label block_00000CE0:
    # Node: 00000CE0 (Target)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『试着去倾听朋友们的烦恼。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003AFE:
    # Node: 00003AFE (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_00003B01

    return

label block_00003B01:
    # Node: 00003B01 (RESET)
    $ C2S1Phase = 0
    $ C2S2Phase = 0
    $ C2S3Phase = 0
    $ C2S4Phase = 0
    $ C2S5Phase = 0
    $ C2S6Phase = 0

    if judge_lm_condition([]):
        jump block_00003B02

    return

label block_00003B02:
    # Node: 00003B02 (終了)

    return

label block_00003BCA:
    # Node: 00003BCA (PREPARE)
    if Not(VarExists("TalkOkajimaKojimaF3")):
        $ TalkOkajimaKojimaF3 = False
    if Not(VarExists("TalkSaburoF3")):
        $ TalkSaburoF3 = False
    if Not(VarExists("TalkTomoF3")):
        $ TalkTomoF3 = 0

    if judge_lm_condition([]):
        jump block_000017FC

    return

label block_000017FC:
    # Node: 000017FC (BGM 1)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_00000C27

    return

