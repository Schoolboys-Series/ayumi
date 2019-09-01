# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00001105 (CP2 Daytime 三朗)

label block_00001106:
    # Node: 00001106 (開始)
    $ TalkShoeCupboardF4 = False
    $ TalkPEWarehouseF4 = False
    $ TalkAtriumF4 = False
    $ TalkJudoF4 = False
    $ TalkGymF4 = False
    $ TalkAisle2F4 = False
    $ TalkToiletF4 = False
    $ TalkOkajimaKojimaF4 = False
    $ TalkSakuyaMatsutaF4 = False
    $ TalkTomoShinoTsubaF4 = False
    $ TalkItouKimuraF4 = False
    $ TalkTsukiSoraF4 = False
    $ TalkSatouF4 = False
    $ TalkKatouIzumiF4 = False
    $ F4Check1 = False

    if judge_lm_condition([{ "scope": 0, "content": "C2S4Phase == 98" }]):
        jump block_000017F4
    if judge_lm_condition([]):
        jump block_000017F3

    return

label block_000017F4:
    # Node: 000017F4 (BGM 2)
    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg"

    pause 0.7

    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""


    if judge_lm_condition([]):
        jump block_00001108

    return

label block_00001108:
    # Node: 00001108 (School outside)
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

    $ sys_ayumi_global_map_character = "saburo"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([{ "scope": 0, "content": "C2S4Phase == 98" }]):
        jump block_00001140
    if judge_lm_condition([]):
        jump block_00001794

    return

label block_00001140:
    # Node: 00001140 (School outside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_000017F6", target_label="block_000017F8") from _call_scb_global_map_146
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_0000110E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_0000110F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00001111
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00001112
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00001107
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00001140
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001140
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FA3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_000017F8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000017F6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" },{ "scope": 1, "content": "TalkOkajimaKojimaF4 and TalkTomoShinoTsubaF4 and TalkItouKimuraF4 and TalkTsukiSoraF4 and TalkSatouF4 and TalkKatouIzumiF4 == True" },{ "scope": 2, "content": "TalkSakuyaMatsutaF4 == False" }]):
        jump block_00001130
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_00001110

    return

label block_0000110E:
    # Node: 0000110E (Shoe cupboard 2)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S4Phase == 99" }]):
        jump block_0000240F
    if judge_lm_condition([]):
        jump block_00001117

    return

label block_0000240F:
    # Node: 0000240F (Shoe cupboard empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_541
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_0000111C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3A

    return

label block_0000111C:
    # Node: 0000111C (Playground)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("校庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S4Phase == 99" }]):
        jump block_0000111D
    if judge_lm_condition([{ "scope": 0, "content": "TalkItouKimuraF4 == False" }]):
        jump block_000023FD
    if judge_lm_condition([]):
        jump block_00001B85

    return

label block_0000111D:
    # Node: 0000111D (Playground empty)
    $ sys_lm_menu_item = [{"pos": (632, 208),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "体育倉庫"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_542
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B4B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" },{ "scope": 1, "content": "TalkPEWarehouseF4 == False" }]):
        jump block_000023F8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" }]):
        jump block_00002418

    return

label block_00003B4B:
    # Node: 00003B4B (TO: Shoe cupboard 2)

    if judge_lm_condition([]):
        jump block_00003B4A

    return

label block_00003B4A:
    # Node: 00003B4A (TO: Shoe cupboard 2)

    if judge_lm_condition([]):
        jump block_0000110E

    return

label block_000023F8:
    # Node: 000023F8 (PE warehouse 1)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F36816057C4848709177D4C457D25726 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "等等！有人来了！"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呜哇！？"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊咧？你们俩在这种地方干什么呢？"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "不、那个！这是……这个……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_75C80A83F7F041D68B6E846A9F01B148 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_0FEF4A90E57948179FD23929AD85763D as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "整理田径部的东西。\n好了好了！无关人员就别打扰了快出去！"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_5FBD78374DA74E3DAE8DB6DA14DD5616 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "原来如此。不过，可以的话那边就别动了，\n我还得用它睡午觉。"

    show rs_image_C9317C0E65354F3E9224B31EF2E574BD as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "好好，明白了，我会告诉他们的。\n"
    show rs_image_75C80A83F7F041D68B6E846A9F01B148 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "来伊藤，继续收拾！"

    show rs_image_D7BB405DB3414FDEBB860FB2D50A49B9 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯、嗯。要赶快收拾完！"

    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "真是闲啊——拜拜。{w=0.3}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend ""

    pause 0.5

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……伊藤酱，真的想快点结束吗？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_DB38897E47104CBDB5C47922CC6869D1 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "……欺负人。"

    pause 0.3

    window show

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00002EF1

    return

label block_00002EF1:
    # Node: 00002EF1 (T ++)
    $ TalkPEWarehouseF4 = True

    if judge_lm_condition([]):
        jump block_0000111C

    return

label block_00002418:
    # Node: 00002418 (PE warehouse 2)
    $ set_window("(標準)")
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好像很忙的样子，去别的地方好了。"

    window hide

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("イベントモード")

    if judge_lm_condition([]):
        jump block_0000111D

    return

label block_000023FD:
    # Node: 000023FD (Playground 伊藤+木村 point)
    $ sys_lm_menu_item = [{"pos": (160, 144),"image": "images/Chapter 2/Menu/F4/Itou point.png","hover": "images/Chapter 2/Menu/F4/Itou hover.png","name": "伊藤"}, {"pos": (352, 144),"image": "images/Chapter 2/Menu/F4/Kimura point.png","hover": "images/Chapter 2/Menu/F4/Kimura hover.png","name": "木村"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (664, 224),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "体育倉庫"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_543
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_000023FF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_000023FE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" }]):
        jump block_0000112A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B4B

    return

label block_000023FF:
    # Node: 000023FF (木村)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_770FBE957C624A43B0FADE9DB660E0E2 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002406

    return

label block_00002406:
    # Node: 00002406 (伊藤+木村)
    window show

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_48D8C5CECCB84B739099EE1FBE060B20 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哈，早上就出了好多汗呐。\n"
    show rs_image_AD32BE71FC11444A8598BBF482AF95D0 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "怎么？有汗臭？"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_EB52490B1A0A4E33BC3D00AD5EFD78E1 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯，去厕所弄点除臭剂或者洗洗如何？"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_7E33B6A2BAF943F9980E42242F194C48 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸～总觉得伊藤酱有点嫌恶的样子呐？不觉得很冷淡吗？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_1990EB79915C41699DBA3A20A151B949 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哦，说不定刚才{color=#FF00FF}那个{/color}才是原因……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "为这样的两位介绍最合适你们的\n御咲市有名的澡堂“花乃汤”哦！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不会有汗味，清洁舒爽！身心暖暖！\n今天放学后去试试如何？"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2E6A3EE5956E43A190B30C9165AF538D as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "唔——可是没钱啊——"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_EB52490B1A0A4E33BC3D00AD5EFD78E1 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "木村，今天放学后和我去那家店的话刚才的事就原谅你。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_952F244A7CFB4533820FFCEB6B3D761A as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸——！！有那么生气？！\n"
    show rs_image_4271CF98C3494E2FA007048FB141D469 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_692C028CA3784566A15437BC68BB11B1 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "好，奢侈一点无所谓了♪\n你那还不错的身体就让我看看好了。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_84ECEC41D074460088D334B076B5152D as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "什！！{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_AC0CEBD610B64118B8D2BC90484E5801 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    extend "{size=16}{/size}{color=#808080}笨蛋笨蛋笨蛋{/color}{size=16}{color=#808080}！！\n{/color}{/size}{color=#808080}被这么说还真有点高兴的{/color}{size=16}{color=#808080}！！！{/color}{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "？？{w}不是很明白，欢迎来哦两位♪"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002EF9

    return

label block_00002EF9:
    # Node: 00002EF9 (T ++)
    $ TalkItouKimuraF4 = True

    if judge_lm_condition([]):
        jump block_00001B85

    return

label block_00001B85:
    # Node: 00001B85 (Playground 伊藤 木村)
    $ sys_lm_menu_item = [{"pos": (160, 144),"image": "images/Chapter 2/Menu/F4/Itou.png","hover": "images/Chapter 2/Menu/F4/Itou hover.png","name": "伊藤"}, {"pos": (352, 144),"image": "images/Chapter 2/Menu/F4/Kimura.png","hover": "images/Chapter 2/Menu/F4/Kimura hover.png","name": "木村"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (664, 224),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "体育倉庫"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_544
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B4B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" }]):
        jump block_0000112A
    if judge_lm_condition([]):
        jump block_00002411

    return

label block_0000112A:
    # Node: 0000112A (PE warehouse)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("体育仓库"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F36816057C4848709177D4C457D25726 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_0000112B

    return

label block_0000112B:
    # Node: 0000112B (PE warehouse empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_545
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000111C

    return

label block_00002411:
    # Node: 00002411 (伊藤+木村 2)
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好，去找下一个了！"

    window hide

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00001B85

    return

label block_000023FE:
    # Node: 000023FE (伊藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_4D6C0781022E46CA9AF15C613D7158EB as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002406

    return

label block_00003B3A:
    # Node: 00003B3A (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003B39

    return

label block_00003B39:
    # Node: 00003B39 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00001108

    return

label block_00001117:
    # Node: 00001117 (Shoe cupboard)
    $ sys_lm_menu_item = [{"pos": (160, 96),"image": "images/Menu/Nameko.png","hover": "images/Menu/Nameko hover.png","name": "滑子"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_546
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" }]):
        jump block_0000114F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_0000111C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3A

    return

label block_0000114F:
    # Node: 0000114F (滑子)
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "上课前五分钟记得回教室。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))

    if judge_lm_condition([]):
        jump block_00001117

    return

label block_0000110F:
    # Node: 0000110F (Gym outside)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S4Phase == 99" }]):
        jump block_00001118
    if judge_lm_condition([{ "scope": 0, "content": "TalkSatouF4 == False" }]):
        jump block_00001B82
    if judge_lm_condition([]):
        jump block_0000240B

    return

label block_00001118:
    # Node: 00001118 (Gym outside empty)
    $ sys_lm_menu_item = [{"pos": (168, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "体育館へ"}, {"pos": (664, 280),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "柔道場へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_547
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" },{ "scope": 1, "content": "TalkGymF4 == False" }]):
        jump block_000023F9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"柔道場へ\"" },{ "scope": 1, "content": "TalkJudoF4 == False" }]):
        jump block_00001150
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"柔道場へ\"" }]):
        jump block_00002419
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" }]):
        jump block_0000241A

    return

label block_000023F9:
    # Node: 000023F9 (Gym)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_24188CBA120A4166B08F8A3535548A8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_F2F289CF5EBE488D8F81EC2E0A88201D as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at left_top zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "前辈这个……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_FDDBBE41E4AF406FB23C17D6792B9C00 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5289B24F34504122B98A53A1F59E1000 as tag_FDDBBE41E4AF406FB23C17D6792B9C00 at right_top zorder zorder_tag_FDDBBE41E4AF406FB23C17D6792B9C00 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "笨蛋——！！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.3

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}攻击！！{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_FDDBBE41E4AF406FB23C17D6792B9C00
    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "噫！？！"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2725024970704D6093D5E37A46BCDEEA as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at left_top zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    show rs_image_24188CBA120A4166B08F8A3535548A8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_195F518B89564C98A557F130D2E603F0

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "啊！！！抱、抱歉！还好吗……？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你！！突然干嘛呢！很危险的！无视运动员精神啊！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_6BEDE232AC5D4CA6AF91A160A7EFC9E6 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "真的很抱歉……只是发生了太多事，心理不太舒服……"

    show rs_image_AAC229C565304B76BADD3819ED261CD1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "到底咋了，前辈什么东西的……社团里跟人拌嘴了？"

    show rs_image_47A1CF95832441F79773CE6246CC941C as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "不，不是社团的问题……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊，难道说那个前辈是你的……\n{w=0.4}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_4D1311D27FDA4670AB1582678631B9C9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "“{color=#FF00FF}那个♂{/color}”……么？"

    show rs_image_39E6D29FE80C465594D4446F8137BE4F as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "欸！……啊，嗯，是的。\n"
    show rs_image_47A1CF95832441F79773CE6246CC941C as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "为什么会知道？"

    show rs_image_2B49DF326D8641F283BDF0EC54525573 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你是一班的泉是不？从你们班那个叫奥村那儿\n听说了你和前辈有问题的事。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_93217C419AFE4718A53050BCB5A26025 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "啊、是吗。\n要是能不在学校里传开就好了，有点不好意思呐。"

    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "反正奥村又管不住嘴。那家伙真的很喜欢这种话题。\n"
    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "男同志之间的八卦什么的……"

    show rs_image_39E6D29FE80C465594D4446F8137BE4F as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "没、没有那回事。前辈很喜欢我的。"

    show rs_image_AAC229C565304B76BADD3819ED261CD1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦——那刚才那发攻击又是咋了。"

    show rs_image_6BEDE232AC5D4CA6AF91A160A7EFC9E6 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "那是……"
    show rs_image_26C754426240474DB9C3EDFE51B5E3DF as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……小矛盾当然是有的，\n不过，喜欢就是喜欢。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_7303A840CCBB4DFCA4E6D8A50257852D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "即便都是男的？"

    show rs_image_AAF0783ACAFC489AB4B14909E0CA248A as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "……和这个没有关系。\n倒不如说，为什么会觉得男人之间不能相爱？"

    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不，那个，普通都会这么想不是嘛。\n只是这个学校太诡异了。"

    show rs_image_47A1CF95832441F79773CE6246CC941C as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "确实这在世界上算少数派，我也不敢……和家里说……"

    show rs_image_6BEDE232AC5D4CA6AF91A160A7EFC9E6 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_8D9249CA1389416BAF6A122851E276D0 "可是……喜欢就是喜欢。"

    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔……{w=0.4}{nw}"
    show rs_image_5FBD78374DA74E3DAE8DB6DA14DD5616 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "抱、抱歉，有些问过头了。"

    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那、那么热心的话，肯定能和前辈好好发展的！嗯！"

    show rs_image_47A1CF95832441F79773CE6246CC941C as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "……嗯。"

    pause 0.3

    window show

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00002EEE

    return

label block_00002EEE:
    # Node: 00002EEE (T ++)
    $ TalkGymF4 = True

    if judge_lm_condition([]):
        jump block_00003B3B

    return

label block_00003B3B:
    # Node: 00003B3B (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003B3A

    return

label block_00001150:
    # Node: 00001150 (Judo)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_153E9CF7193C4513869D54FA898561FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_8AF97BE15B524E50A2E2C8FC106F60FD as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_B7DA8760D1894ADDAD4A804423AB38E0 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "呐，哥哥，今天妈妈要出门，家里谁都不在哦？"

    show rs_image_77C99743D39944F9AD8542E6C1310363 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯，晚饭吃什么好？\n之前和绫濑去的那家寿司店也不错……"

    show rs_image_3F24CEDBC21C4B519C252D275DFA946D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_DE0FC0104A974EE08D0C45E9C71B65B8 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "{color=#FF00FF}“一起度过的时光，才会弥足珍贵，才更需要珍惜”{/color}{w}\n哥哥是这么说过了。"

    show rs_image_33C65BBD622D4D51B8D81050A5F71B11 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "！{w=0.5}{nw}"
    show rs_image_F89A04A6DC494AEF9DDB0A6A99F3D02A as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……是、是啊。\n今天、就珍重地对待好了。"
    show rs_image_EF8501E4A7CC48B4A436E60E2F08C005 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……嗯。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_F59CF92171C0495BA4E334AC96BA8B63 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_71FE39D448264F1B86FB7E3459E84840 "……"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_4426ECB7E6A8443FB128590CB7FEBB64 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_23541E50BF3A40A9A131DAD5602777AF as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "换、换这种说法有些不好意思啊。\n这种事还是更自然一点……"

    show rs_image_80E9D115E1B24DF5B2326F12AB148766 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不是的哦，哥哥。{w}能自然地处理那些事，珍重地处理那些事，\n有这样的自觉也是很重要的。"

    show rs_image_04E624D1BB754C8BB64C742A705F8CAE as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是、是啊……好久没有这样的心情了。"

    show rs_image_F89A04A6DC494AEF9DDB0A6A99F3D02A as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "刚开始交往的恋人们是不是也会有这样的感觉呐。"

    show rs_image_CCE2DFCDE5EE495CB0367ED4ED7DCA8B as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……我们做的事其实也和他们差不多。"

    pause 0.4

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "真的假的……那两个人……噫……"

    pause 0.3

    window show

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00002EED

    return

label block_00002EED:
    # Node: 00002EED (T ++)
    $ TalkJudoF4 = True

    if judge_lm_condition([]):
        jump block_00003B3B

    return

label block_00002419:
    # Node: 00002419 (Judo 2)
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "快去别的地方……"

    window hide

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00001118

    return

label block_0000241A:
    # Node: 0000241A (Gym 2)
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "快去别的地方……"

    window hide

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00001118

    return

label block_00001B82:
    # Node: 00001B82 (Gym outside 佐藤 point)
    $ sys_lm_menu_item = [{"pos": (168, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "体育館へ"}, {"pos": (416, 208),"image": "images/Chapter 2/Menu/F3/Sato point.png","hover": "images/Chapter 2/Menu/Sato hover.png","name": "　佐藤"}, {"pos": (664, 280),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "柔道場へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_548
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"　佐藤\"" }]):
        jump block_0000112D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" }]):
        jump block_0000111E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"柔道場へ\"" }]):
        jump block_000023F3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3A

    return

label block_0000112D:
    # Node: 0000112D (佐藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 300
    show rs_image_2E24765C23544B69A9391DC51FE38194 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_bottom zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "YO，佐藤君。\n如何，今天放学后要不要去“花乃汤”？？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_41D4BC08F852455E8DE11A7C412BEE6F as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "诶，突然说什么呢。"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "其实……\n{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_402BC7F34E6E45CCA1CD7E9670AA1F56

    extend "如此如此这般这般……{w=0.6}{nw}"
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_E9DA1A925CE140459A40C853C70AA406 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_402BC7F34E6E45CCA1CD7E9670AA1F56

    extend ""

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "诶——是嘛。\n不过我社团活动结束很晚，家住得也很远，不太能去哦。"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊——这样。等有时间的时候请务必来看看哦。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你和冈岛他们关系挺不错的，顺便把他们也带过去。"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F454E39E17AB417EAFAD03FC09D7C631 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "也是呢。一群人一起去洗个澡有时也不错。\n"
    show rs_image_BB8AF3FC831D491CB97BFAC1E2913125 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=14}……不知前辈会怎么想。{/size}"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "社团的前辈？"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1E6988844B884E2B88D92837EA789B61 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "没什么。辛苦你宣传了，我会考虑的。"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002EF6

    return

label block_00002EF6:
    # Node: 00002EF6 (T ++)
    $ TalkSatouF4 = True

    if judge_lm_condition([]):
        jump block_0000240B

    return

label block_0000240B:
    # Node: 0000240B (Gym outside)
    $ sys_lm_menu_item = [{"pos": (168, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "体育館へ"}, {"pos": (416, 208),"image": "images/Chapter 2/Menu/Sato.png","hover": "images/Chapter 2/Menu/Sato hover.png","name": "　佐藤"}, {"pos": (664, 280),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "柔道場へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_549
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"柔道場へ\"" }]):
        jump block_000023F3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" }]):
        jump block_0000111E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3A
    if judge_lm_condition([]):
        jump block_00002410

    return

label block_000023F3:
    # Node: 000023F3 (Judo)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_153E9CF7193C4513869D54FA898561FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkTsukiSoraF4 == False" }]):
        jump block_00001151
    if judge_lm_condition([]):
        jump block_00002405

    return

label block_00001151:
    # Node: 00001151 (Judo 月+空 point)
    $ sys_lm_menu_item = [{"pos": (320, 232),"image": "images/Chapter 2/Menu/Tsuki point.png","hover": "images/Chapter 2/Menu/Tsuki hover.png","name": "月"}, {"pos": (497, 230),"image": "images/Chapter 2/Menu/F4/Sora point.png","hover": "images/Chapter 2/Menu/Sora hover.png","name": "空"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_550
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_0000115C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_0000115D

    return

label block_00003B3C:
    # Node: 00003B3C (TO: Gym outside)

    if judge_lm_condition([]):
        jump block_0000110F

    return

label block_0000115C:
    # Node: 0000115C (空)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_EC040B7182804790B7750A3172C04105 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002404

    return

label block_00002404:
    # Node: 00002404 (月+空)
    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "早上好——！大街小巷的知名人物赤峰兄弟！{w}\n两人当然也知道同班的奥村家经营着“花乃汤”对不……？"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_25DD39CE556B4EC69227B2977E0220CB as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "知道哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "想想也是呐——！！{w}\n倒不如说已经去过……？"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C55DDE5781304E9BBC5E1E1C55EB2DEB as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……很多次了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是嘛——！！\n啊，太好了！今后也请多多光临哦！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "其实我现在开始在奥村那里打工了！{w}以后也要多多来店哦♪"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F761F888C5034F26880B624E1477BF17 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸？是这样啊！不过为什么突然就？"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嘛，发生了很多事。{w}\n啊，对了！两位可都是重要的客人，有句话必须得提醒。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "以后花乃汤内将会禁止不纯{color=#FF00FF}异性{/color}和{color=#FF00FF}同性{/color}行为。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "两位的心情我当然也非常——非常——了解，\n但以后还是请在家里做，稍微忍耐一下"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_636B1CDA2DAE45C69D984C637B3E0DCA as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "什么什么什么！？{w}说说说、说什么呢！\n我不管在家还是在什么别的地方都没那么做过！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不用藏了不用藏了♪{w}\n只要守规矩，剩下的全是各位的自由哦♪"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("柔道场外"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002EF7

    return

label block_00002EF7:
    # Node: 00002EF7 (T ++)
    $ TalkTsukiSoraF4 = True

    if judge_lm_condition([]):
        jump block_00002405

    return

label block_00002405:
    # Node: 00002405 (Judo 月)
    $ sys_lm_menu_item = [{"pos": (320, 232),"image": "images/Chapter 2/Menu/Tsuki.png","hover": "images/Chapter 2/Menu/Tsuki hover.png","name": "月"}, {"pos": (497, 230),"image": "images/Chapter 2/Menu/Sora.png","hover": "images/Chapter 2/Menu/Sora hover.png","name": "空"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_551
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3D
    if judge_lm_condition([]):
        jump block_00002412

    return

label block_00003B3D:
    # Node: 00003B3D (TO: Gym outside)

    if judge_lm_condition([]):
        jump block_00003B3C

    return

label block_00002412:
    # Node: 00002412 (月+空 2)
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好，去找下一个了！"

    window hide

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002405

    return

label block_0000115D:
    # Node: 0000115D (月)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_FF2F05BF45D647239862F7725764481C as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002404

    return

label block_0000111E:
    # Node: 0000111E (Gym)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("体育馆"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_24188CBA120A4166B08F8A3535548A8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkKatouIzumiF4 == False" }]):
        jump block_00001B83
    if judge_lm_condition([]):
        jump block_00002403

    return

label block_00001B83:
    # Node: 00001B83 (Gym 泉+加藤 point)
    $ sys_lm_menu_item = [{"pos": (296, 211),"image": "images/Chapter 2/Menu/Izumi point.png","hover": "images/Chapter 2/Menu/Izumi hover.png","name": "泉"}, {"pos": (464, 216),"image": "images/Chapter 2/Menu/F4/Katou point.png","hover": "images/Chapter 2/Menu/Katou hover.png","name": "加藤"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_552
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" }]):
        jump block_00001B84
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_00001121
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3C

    return

label block_00001B84:
    # Node: 00001B84 (加藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_CF9552A127F84B139910618B1FE71819 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002402

    return

label block_00002402:
    # Node: 00002402 (加藤+泉)
    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好呀好呀两位！你们是一班的？和奥村同班呢！{w}\n既然如此知道他家经营着“花乃汤”对不♪"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_581796CAD76B4C929577B4C1D581EF10 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯、嗯，是这样没错。突然怎么了？"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A886E64725024E519334B46B47F7F928 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "说起来我好像从没去过奥村家的店呢。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CF9552A127F84B139910618B1FE71819 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "是吗？我去过很多次了，\n挺不错的，也挺安心的{w=0.55}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_28ED053AA884497180A83F8D246CFEE2 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "{size=14}……年龄层也挺高的。{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦！多谢多谢！多谢光临。以后还请多多关照哦！"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_4CAFD25A1F5E4405A36AFD06AA87C091 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这位的话，以后有机会请务必光临哦。{w}\n能轻松扫平一天积累的所有疲劳哦。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_21A5A72FBBD8459A863B99B859A0013F as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "说起来为什么你要这么卖力宣传？"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊，算我没说清楚。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "我、猫山三朗，现在开始就是花乃汤的营业员了。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "今后还请多多关照。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D668AB5BCE7641D598E5B719952F1E93 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "是嘛。那下次我也和前辈一起去好了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊！之前那个前辈嘛！请便请便！请务必光临！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "坦诚相见的次数越多和前辈的关系就会越好哦。\n肯定的♪"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_00002EF8

    return

label block_00002EF8:
    # Node: 00002EF8 (T ++)
    $ TalkKatouIzumiF4 = True

    if judge_lm_condition([]):
        jump block_00002403

    return

label block_00002403:
    # Node: 00002403 (Gym 加藤)
    $ sys_lm_menu_item = [{"pos": (296, 211),"image": "images/Chapter 2/Menu/Izumi.png","hover": "images/Chapter 2/Menu/Izumi hover.png","name": "泉"}, {"pos": (464, 216),"image": "images/Chapter 2/Menu/Katou gym.png","hover": "images/Chapter 2/Menu/Katou gym hover.png","name": "加藤"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_553
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000110F
    if judge_lm_condition([]):
        jump block_00002413

    return

label block_00002413:
    # Node: 00002413 (加藤+泉 2)
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好，去找下一个了！"

    window hide

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002403

    return

label block_00001121:
    # Node: 00001121 (泉)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_4CAFD25A1F5E4405A36AFD06AA87C091 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002402

    return

label block_00002410:
    # Node: 00002410 (佐藤 2)
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好，去找下一个了！"

    window hide

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000240B

    return

label block_00001111:
    # Node: 00001111 (Schoolhouse)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_0000111A

    return

label block_0000111A:
    # Node: 0000111A (Schoolhouse)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_554
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3A

    return

label block_00001112:
    # Node: 00001112 (School door)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("校门"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_0000111B

    return

label block_0000111B:
    # Node: 0000111B (School door)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (96, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "屋外トイレへ"}, {"pos": (456, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "学校看板"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_555
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外トイレへ\"" }]):
        jump block_00001127
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学校看板\"" }]):
        jump block_00001136

    return

label block_00001127:
    # Node: 00001127 (Outside toilet)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("室外厕所"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D5370D554F61451C806A39C7BC540968 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001128

    return

label block_00001128:
    # Node: 00001128 (Outside toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (472, 192),"image": "images/Menu/Tokiwa.png","hover": "images/Menu/Tokiwa hover.png","name": "常磐"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_556
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" },{ "scope": 1, "content": "C2S4Phase == 99" }]):
        jump block_0000240C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" }]):
        jump block_00001137
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001112

    return

label block_0000240C:
    # Node: 0000240C (常磐 1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_C6DBBEE764574D17ABDD9C37FCFB0144 as tag_3482C372784E44A89E382266A93F2B14 at center_bottom zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C223850065F6443080205D1F61C04C98 "这座学园……不，这个城镇，是那种\n不管什么都不需隐藏会被好好接受的地方呐。\n"
    show rs_image_2917E94D246C4B5DBB7438FB372D005B as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "非常棒，不管怎么看都这么觉得。"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外厕所"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001128

    return

label block_00001137:
    # Node: 00001137 (常磐 2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_C6DBBEE764574D17ABDD9C37FCFB0144 as tag_3482C372784E44A89E382266A93F2B14 at center_bottom zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C223850065F6443080205D1F61C04C98 "泡澡啊……这么一说好久没做过了呢。\n"
    show rs_image_B7BD90C9E0F94D39B930CB8F323D6C2F as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "最后一次应该是在……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_2D587EAE6EC3401995D5F3F45B1E69E1 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "啊……不、不是你想的那样哦？\n绝对不是我不爱干净，这里面是有很多原因的！"

    show rs_image_C792083E91604DFD9FEB035D608ACFF9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "完全不臭对不对？对不对？？\n被那样想我会受伤的所以请不要误解哦……"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外厕所"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001128

    return

label block_00001136:
    # Node: 00001136 (Board)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_3BE9AC227F0142FBAABEEB7605D6A3F9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000111B

    return

label block_00001107:
    # Node: 00001107 (School inside)
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

    $ sys_ayumi_global_map_character = "saburo"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([{ "scope": 0, "content": "C2S4Phase == 98" }]):
        jump block_0000113F
    if judge_lm_condition([]):
        jump block_00001795

    return

label block_0000113F:
    # Node: 0000113F (School inside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_00003B48", target_label="block_00003B49") from _call_scb_global_map_147
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" },{ "scope": 1, "content": "TalkSakuyaMatsutaF4 == False" },{ "scope": 1, "content": "F4Check1 == True" }]):
        jump block_00001109
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" },{ "scope": 1, "content": "TalkSakuyaMatsutaF4 == True" }]):
        jump block_00002EFB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_0000110A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_0000110B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_0000110C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_0000110D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00001108
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00001107
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001107
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FA4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00003B49
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00003B48

    return

label block_00001109:
    # Node: 00001109 (Aisle 2-3)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001113

    return

label block_00001113:
    # Node: 00001113 (Aisle 2)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (152, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "踊り場へ"}, {"pos": (376, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "新聞部へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_557
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B4D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部へ\"" }]):
        jump block_00001125
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"踊り場へ\"" }]):
        jump block_00001129

    return

label block_00003B4D:
    # Node: 00003B4D (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003B4C

    return

label block_00003B4C:
    # Node: 00003B4C (TO: School inside)

    if judge_lm_condition([]):
        jump block_00001107

    return

label block_00001125:
    # Node: 00001125 (Newsclub)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("新闻部活动室"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkOkajimaKojimaF4 == False" }]):
        jump block_00001B80
    if judge_lm_condition([]):
        jump block_0000240A

    return

label block_00001B80:
    # Node: 00001B80 (Newsclub 岡島+小島 point)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (112, 160),"image": "images/Chapter 2/Menu/F4/Okajima point.png","hover": "images/Chapter 2/Menu/Okajima hover.png","name": "岡島"}, {"pos": (392, 160),"image": "images/Chapter 2/Menu/F4/Kojima point.png","hover": "images/Chapter 2/Menu/Kojima hover.png","name": "小島"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_558
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_0000112F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_0000112E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001109

    return

label block_0000112F:
    # Node: 0000112F (小島)
    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002409

    return

label block_00002409:
    # Node: 00002409 (岡島+小島)
    window show

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "早上好呀！失礼了。{w}\n有个想和新闻部各位宣传的事，现在有空么？"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BB675405870B497F958414550471B4BF as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哦哦，什么事？"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "其实啊，我现在开始在御咲神社附近的“花乃汤”打工了。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "为了增加客人现在正在宣传中哦。\n你们要是觉得好的话请务必光临哦！"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_07383DF7F5A94166BAD98FE0E71F4768 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哦哦，花乃汤。\n离家很近的，小学生的时候去过几次。"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DF83E8681DAD43B1BF6C0CF0E3555C11 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "那时候经常有不认识的大叔帮忙洗身体，\n{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    extend "临走的时候还会叫我一起回家之类的。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C99B8AC50B2B4ED58FF270D7376A67EE as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "……什么……？"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_AF867A4937BD47B085C2FBD0F564E665 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "既然猫山君也在，下次我就久违地去看看好了。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "部长如果想去的话请务必带上我。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_C99B8AC50B2B4ED58FF270D7376A67EE as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "必须。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那、那个啊，店里也加强了管理，\n那种奇怪的客人应该不会出现了，两位放心就好。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "还有，请务必也和新闻部的各位宣传一下！{w}\n拜托了哦！"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_00002EF3

    return

label block_00002EF3:
    # Node: 00002EF3 (T ++)
    $ TalkOkajimaKojimaF4 = True

    if judge_lm_condition([]):
        jump block_0000240A

    return

label block_0000240A:
    # Node: 0000240A (Newsclub)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (112, 160),"image": "images/Chapter 2/Menu/Okajima.png","hover": "images/Chapter 2/Menu/Okajima hover.png","name": "岡島"}, {"pos": (392, 160),"image": "images/Chapter 2/Menu/Kojima.png","hover": "images/Chapter 2/Menu/Kojima hover.png","name": "小島"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_559
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001109
    if judge_lm_condition([]):
        jump block_0000240D

    return

label block_0000240D:
    # Node: 0000240D (岡島+小島 2)
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好，去找下一个了！"

    window hide

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000240A

    return

label block_0000112E:
    # Node: 0000112E (岡島)
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_6EACDBA5EB7B44D7A7699633252E6B7E as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002409

    return

label block_00001129:
    # Node: 00001129 (Stairwell)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("楼梯间"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkSakuyaMatsutaF4 == True" }]):
        jump block_000018B0
    if judge_lm_condition([]):
        jump block_00002EFC

    return

label block_000018B0:
    # Node: 000018B0 (Stairwell movable)
    $ sys_lm_menu_item = [{"pos": (184, 400),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "一階"}, {"pos": (488, 216),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "三階"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_560
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001109
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"一階\"" }]):
        jump block_000018AF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三階\"" }]):
        jump block_000018BB

    return

label block_000018AF:
    # Node: 000018AF (Aisle 1)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("一楼走廊"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AEF730D86D5343AF81880AC735BAFAC6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4


    if judge_lm_condition([]):
        jump block_00003AAF

    return

label block_00003AAF:
    # Node: 00003AAF ()
    $ del TalkShoeCupboardF4
    $ del TalkPEWarehouseF4
    $ del TalkAtriumF4
    $ del TalkJudoF4
    $ del TalkGymF4
    $ del TalkAisle2F4
    $ del TalkToiletF4
    $ del TalkOkajimaKojimaF4
    $ del TalkSakuyaMatsutaF4
    $ del TalkTomoShinoTsubaF4
    $ del TalkItouKimuraF4
    $ del TalkTsukiSoraF4
    $ del TalkSatouF4
    $ del TalkKatouIzumiF4
    $ del F4Check1

    return

label block_000018BB:
    # Node: 000018BB (Aisle 3)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("三楼走廊"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_3AD71FD0B91B482CBB280A8611C2741C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4


    if judge_lm_condition([]):
        jump block_000018BA

    return

label block_000018BA:
    # Node: 000018BA (Aisle 3)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_561
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001129

    return

label block_00002EFC:
    # Node: 00002EFC (Stairwell empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_562
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([]):
        jump block_00001109

    return

label block_00002EFB:
    # Node: 00002EFB (Aisle 2-4)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    window show

    rs_character_065976138EB54B28BD31055407272C67 "呐呐，他们好像已经来了！"

    rs_character_804320518EF943369A23DB093FCC9E41 "真的？可马上就要打铃了……"

    rs_character_065976138EB54B28BD31055407272C67 "快走还来得及！走走♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "（似乎朝一楼去了……发生什么了？）"

    window hide

    $ set_place_title(_("二楼走廊"))
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002F5F

    return

label block_00002F5F:
    # Node: 00002F5F (F4Check1)
    $ F4Check1 = True

    if judge_lm_condition([]):
        jump block_00001113

    return

label block_0000110A:
    # Node: 0000110A (Roof)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001114

    return

label block_00001114:
    # Node: 00001114 (Roof)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_563
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B4D

    return

label block_0000110B:
    # Node: 0000110B (Music room)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S4Phase == 99" }]):
        jump block_00002400
    if judge_lm_condition([{ "scope": 0, "content": "TalkTomoShinoTsubaF4 == False" }]):
        jump block_00001115
    if judge_lm_condition([]):
        jump block_00002408

    return

label block_00002400:
    # Node: 00002400 (Music room empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_564
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B4D

    return

label block_00001115:
    # Node: 00001115 (Music room 友+翼+忍 point)
    $ sys_lm_menu_item = [{"pos": (325, 184),"image": "images/Chapter 2/Menu/Tomo music room point.png","hover": "images/Chapter 2/Menu/Tomo music room hover.png","name": "友"}, {"pos": (528, 184),"image": "images/Chapter 2/Menu/Tsubasa music room point.png","hover": "images/Chapter 2/Menu/Tsubasa hover.png","name": "つばさ"}, {"pos": (136, 192),"image": "images/Chapter 2/Menu/Shinobu music room point.png","hover": "images/Chapter 2/Menu/Shinobu music room hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_565
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B4E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00001159
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友\"" }]):
        jump block_0000115A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_0000112C

    return

label block_00003B4E:
    # Node: 00003B4E (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003B4D

    return

label block_00001159:
    # Node: 00001159 (忍)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_22306BD9E0624D81A1CFFFB486C5BAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002407

    return

label block_00002407:
    # Node: 00002407 (友+翼+忍)
    window show

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_89C8C20323A646FB80CB32423F9C342F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "下次我们三个一起去玩如何——！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_73951BCA78C0428BB2D52C4797A62C65 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哇，好啊！\n那个，要玩的话去什么地方好呢。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E7A48E4B115D4F53A61CCC7B11022DE9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，说的是呐。友又坐不来游乐园的刺激项目……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那“花乃汤”如何！{w}\n坦诚相见！身心坦荡，友情一定会进一步加深的！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_65886B0DDD844CEF8CB130AC05A09545 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "坦、坦诚相见——！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_95FC6FFC5BDE4EABB5152ECB6A0F08B1 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_E7E001D277D64764A4BCEA631004A1D7

    extend "……不行，对我来说刺激太强了……！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9EDC3EE156E74145AE331B832A3FECD5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "花乃汤啊——！还从没和忍以及翼君一起去过呐，\n去一次也不错嘛！\n"
    show rs_image_A2A2562FBABF4208B2B506D085FAA1E9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那个，星期几之外是安全的来着？"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "白痴呆毛，那种事已经不会发生了所以不用担心。\n下次可以找奥村详细打听。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5B939D04A51E43ABA98E60D5AF8C04B5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！是嘛？好高兴，不过也好寂寞！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CE498AFB1E3D4DA78B270436EF373DE6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "澡堂……确实想去一次不过，\n"
    show rs_image_9A5BB450BFF940D3A659C94F81A93685 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "我就……找一天自己去好了。\n友就和翼君两个人去。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AD8CFA3B3632464BA96A924CD8D32A10 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "绫濑君……！"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3FFA42ECEDF14A378835CC5A7CEED291 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    extend "啊，不过还是不行。只有两个人\n{w=0.5}{nw}"
    show rs_image_8DECB50317B14BD6B1D99221FBD7089C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "我肯定会进医院的所以还是和我们一起……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A28CBCA902704F978F416697C605F321 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就是啊，装什么独立——！\n"
    show rs_image_D60429DAF0284BDCB5B611CF6A797177 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "大家一起去的话，互相搓背、\n桑拿忍耐什么的很有意思的！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_9B4FF27A80E146DEB08AE0DD62B3DB87 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当然泡泡浴啊还有{color=#FF00FF}那什么{/color}也绝对不能错过呐♪"

    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗯嗯！{w=0.5}……嗯？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不不不！被发现的瞬间可就会被赶出去的！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("音乐室"))

    if judge_lm_condition([]):
        jump block_00002EFA

    return

label block_00002EFA:
    # Node: 00002EFA (T ++)
    $ TalkTomoShinoTsubaF4 = True

    if judge_lm_condition([]):
        jump block_00002408

    return

label block_00002408:
    # Node: 00002408 (Music room 友+翼+忍)
    $ sys_lm_menu_item = [{"pos": (325, 184),"image": "images/Chapter 2/Menu/Tomo music room.png","hover": "images/Chapter 2/Menu/Tomo music room hover.png","name": "友"}, {"pos": (528, 184),"image": "images/Chapter 2/Menu/Tsubasa music room.png","hover": "images/Chapter 2/Menu/Tsubasa hover.png","name": "つばさ"}, {"pos": (136, 192),"image": "images/Chapter 2/Menu/Shinobu music room.png","hover": "images/Chapter 2/Menu/Shinobu music room hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_566
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B4E
    if judge_lm_condition([]):
        jump block_0000240E

    return

label block_0000240E:
    # Node: 0000240E (友+翼+忍 2)
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好，去找下一个了！"

    window hide

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002408

    return

label block_0000115A:
    # Node: 0000115A (友)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_8F83EC71B001467B872FED4ED3234658 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002407

    return

label block_0000112C:
    # Node: 0000112C (翼)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_43C2A5DA4B5D4815BEC6FE1DA10014AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002407

    return

label block_0000110C:
    # Node: 0000110C (Library)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_0000115B

    return

label block_0000115B:
    # Node: 0000115B (Library)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_567
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B4D

    return

label block_0000110D:
    # Node: 0000110D (Toilet)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_297E564A7C1544469FB88A41AB85B6C9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001116

    return

label block_00001116:
    # Node: 00001116 (Toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (224, 184),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "トイレ個室"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_568
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B4D
    if judge_lm_condition([]):
        jump block_00002414

    return

label block_00002414:
    # Node: 00002414 (Toilet single)
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "结果还是不知道之前厕所里那两个究竟是谁……"

    window hide

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00001116

    return

label block_00001FA4:
    # Node: 00001FA4 (Character)
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

label block_00001795:
    # Node: 00001795 (School inside ACTX)
    if judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "TalkShoeCupboardF4 and TalkPEWarehouseF4 and TalkAtriumF4 and TalkJudoF4 and TalkGymF4 and TalkAisle2F4 and TalkToiletF4 == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, False, talk_label="block_00003B3F", target_label="block_00003B42") from _call_scb_global_map_148
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, False, talk_label="block_00003B3F", target_label="block_00003B41") from _call_scb_global_map_149
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" },{ "scope": 1, "content": "TalkAisle2F4 == False" }]):
        jump block_000023F7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00002417
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_0000110A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_0000110B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_0000110C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" },{ "scope": 1, "content": "TalkToiletF4 == False" }]):
        jump block_000023F5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00001108
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FA4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00002416
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "TalkShoeCupboardF4 and TalkPEWarehouseF4 and TalkAtriumF4 and TalkJudoF4 and TalkGymF4 and TalkAisle2F4 and TalkToiletF4 == True" }]):
        jump block_00003B40
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00003B3F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "TalkShoeCupboardF4 and TalkPEWarehouseF4 and TalkAtriumF4 and TalkJudoF4 and TalkGymF4 and TalkAisle2F4 and TalkToiletF4 == True" }]):
        jump block_00003B42
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00003B41
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" },{ "scope": 1, "content": "TalkShoeCupboardF4 and TalkPEWarehouseF4 and TalkAtriumF4 and TalkJudoF4 and TalkGymF4 and TalkAisle2F4 and TalkToiletF4 == True" }]):
        jump block_00003AA8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" }]):
        jump block_00003B3E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001107

    return

label block_000023F7:
    # Node: 000023F7 (Aisle 2-1)
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

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_48B621B61D744137AB3444EC6DA27FB0 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    show rs_image_A95A56566BE747DEBB035CC1B94ADE68 as tag_CC4336DE74164173AC47C2C317367F10 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    show rs_image_8D5A9887A2D74B788AF161574F70EF1D as tag_DCBDF256A1E242E78A25910AE27C0954 at center_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "你们两位进展如何了？"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "进展？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_0A1BC250AF51455791A38A520909E1DC as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "传闻说啊～"

    rs_character_EA9AA88E88D84B559B925363E2931756 "放学后新闻部紧缩门扉并不是{color=#00FFFF}公事{/color}，\n而是为了好好{color=#FF00FF}LU{/color}什么的♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_B39F35D20D9C4757BBAD349BA7DBED23 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1A71CDD16705479CADC0B5AE6CAF3F69 as tag_B39F35D20D9C4757BBAD349BA7DBED23 at center_top zorder zorder_tag_B39F35D20D9C4757BBAD349BA7DBED23 onlayer master
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "那是什么传闻！？详细说来听听！"

    show rs_image_2FAEAC19AC5347FDA2819CA4500CD703 as tag_B39F35D20D9C4757BBAD349BA7DBED23 zorder zorder_tag_B39F35D20D9C4757BBAD349BA7DBED23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "连在新闻部的我都不知道……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_04BBD0AABA25450B9004531DD4019381 as tag_B39F35D20D9C4757BBAD349BA7DBED23 zorder zorder_tag_B39F35D20D9C4757BBAD349BA7DBED23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "还有“LU”到底是什么意思！？"

    hide tag_B39F35D20D9C4757BBAD349BA7DBED23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_2FAEAC19AC5347FDA2819CA4500CD703 as tag_CC4336DE74164173AC47C2C317367F10 at left_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    show rs_image_F90988F5C6754C53A9B5FB1BE164894B as tag_DCBDF256A1E242E78A25910AE27C0954 at right_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "部长，请不要为了无来由的情报太过激动。\n请忘记那些话。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_CC4336DE74164173AC47C2C317367F10
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_44EC1146BFE94EB1A8DBB6E8D8771338 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    show rs_image_96013754928A470894D94BAC81A99E0D as tag_346FE7CD97BB4FB18CB50E78275F4E23 at left_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_53FF68C192E3494AB005C1909579AFFB "佐藤君，就是这样的。这位非常纯洁，\n连我也无法出手。而且，这是礼仪。"

    show rs_image_89F334479C0B443DB4509C2A29D021C9 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "是吗……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A86787761B4F4226AFB3C2FA698779F2 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "话说你准备出手啊！\n恐怖的家伙。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_6EB06386B3BF438184595D042608116A as tag_346FE7CD97BB4FB18CB50E78275F4E23 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    show rs_image_A95A56566BE747DEBB035CC1B94ADE68 as tag_CC4336DE74164173AC47C2C317367F10 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    show rs_image_9E6AF824075F4EB3B240BE13A1C54165 as tag_DCBDF256A1E242E78A25910AE27C0954 at center_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "以后不要对部长说这种莫名其妙的事了。\n让纯白的部长染上颜色的必须是我。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_2FAEAC19AC5347FDA2819CA4500CD703 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "纯白？染？"

    show rs_image_44EC1146BFE94EB1A8DBB6E8D8771338 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "这些词的意思，等时机到来我自然会亲身教授的，\n请放心，部长。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_9B6EA9CA0C0541BAAD8AE6254AB5AC9D as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_EA9AA88E88D84B559B925363E2931756 "……得告诉{color=#00FFFF}冈岛前辈{/color}他的弟弟要出事了。"

    pause 0.3

    window show

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00002F5C

    return

label block_00002F5C:
    # Node: 00002F5C (T ++)
    $ TalkAisle2F4 = True

    if judge_lm_condition([]):
        jump block_00003B4D

    return

label block_00002417:
    # Node: 00002417 (Aisle 2-2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "快去别的地方……"

    window hide


    if judge_lm_condition([]):
        jump block_00001107

    return

label block_000023F5:
    # Node: 000023F5 (Toilet 1)
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

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_531E9A5102504415AD59CA198E9086DB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Search 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Search 1.ogg"

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 400
    show rs_image_B97A3992A1D24282B85B44E0C876F034 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.3

    window show

    rs_character_1625FACDCC1E4EF88C78A65FC4D4B7A6 "悉悉索索……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊？单间里有俩人……为啥？ "

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Search 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Search 1.ogg"

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 400
    show rs_image_B97A3992A1D24282B85B44E0C876F034 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_065976138EB54B28BD31055407272C67 "……被发现了。"

    rs_character_804320518EF943369A23DB093FCC9E41 "……暴露了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你、你们……在干嘛？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Search 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Search 1.ogg"

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 400
    show rs_image_B97A3992A1D24282B85B44E0C876F034 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_065976138EB54B28BD31055407272C67 "……快乐的事。"

    rs_character_804320518EF943369A23DB093FCC9E41 "……舒服的事。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_241AF4B67B0B4452B97B2944C6D13AFE zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    rs_character_1625FACDCC1E4EF88C78A65FC4D4B7A6 "{size=28}{color=#FF0000}你也要来吗？{/color}{/size}"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_241AF4B67B0B4452B97B2944C6D13AFE zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "噫——！我、我就不用了——！！"

    window hide

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.6


    if judge_lm_condition([]):
        jump block_00002EF2

    return

label block_00002EF2:
    # Node: 00002EF2 (T ++)
    $ TalkToiletF4 = True

    if judge_lm_condition([]):
        jump block_00003B4D

    return

label block_00002416:
    # Node: 00002416 (Toilet 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "快去别的地方……"

    window hide


    if judge_lm_condition([]):
        jump block_00001107

    return

label block_00003B40:
    # Node: 00003B40 (Coversation 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊……为什么到处都是同志……"

    window hide


    if judge_lm_condition([]):
        jump block_00001107

    return

label block_00003B3F:
    # Node: 00003B3F (Conversation 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "刚才会那么说都是木天蓼的错！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔……散散步消消神好了……"

    window hide

    $ set_window("(標準)")

    return

label block_00003B42:
    # Node: 00003B42 (Target 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『快进到放学后。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003B41:
    # Node: 00003B41 (Target 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『找学校里的人说说话散散心。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003AA8:
    # Node: 00003AA8 ()
    $ del TalkShoeCupboardF4
    $ del TalkPEWarehouseF4
    $ del TalkAtriumF4
    $ del TalkJudoF4
    $ del TalkGymF4
    $ del TalkAisle2F4
    $ del TalkToiletF4
    $ del TalkOkajimaKojimaF4
    $ del TalkSakuyaMatsutaF4
    $ del TalkTomoShinoTsubaF4
    $ del TalkItouKimuraF4
    $ del TalkTsukiSoraF4
    $ del TalkSatouF4
    $ del TalkKatouIzumiF4
    $ del F4Check1

    return

label block_00003B3E:
    # Node: 00003B3E (Afternoon abadon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "还有些空余时间……\n再转转好了，就当打发时间。"

    window hide


    if judge_lm_condition([]):
        jump block_00001107

    return

label block_00003B49:
    # Node: 00003B49 (Target 3)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『在全学校奔走宣传花乃汤。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003B48:
    # Node: 00003B48 (Conversation 3)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "I LOVE 奥村！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好！把感情变为动力的话，\n在全校宣传也不过就是散散步！"

    window hide

    $ set_window("(標準)")

    return

label block_00001FA3:
    # Node: 00001FA3 (Character)
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

label block_00001794:
    # Node: 00001794 (School outside ACTX)
    if judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "TalkShoeCupboardF4 and TalkPEWarehouseF4 and TalkAtriumF4 and TalkJudoF4 and TalkGymF4 and TalkAisle2F4 and TalkToiletF4 == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, False, talk_label="block_00001147", target_label="block_00001796") from _call_scb_global_map_150
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, False, talk_label="block_00001147", target_label="block_00001148") from _call_scb_global_map_151
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_0000110F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00001111
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00001112
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00001107
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" },{ "scope": 1, "content": "TalkAtriumF4 == False" }]):
        jump block_000023F6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_00002415
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" },{ "scope": 1, "content": "TalkShoeCupboardF4 == False" }]):
        jump block_000023F4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_0000110E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "TalkShoeCupboardF4 and TalkPEWarehouseF4 and TalkAtriumF4 and TalkJudoF4 and TalkGymF4 and TalkAisle2F4 and TalkToiletF4 == True" }]):
        jump block_00001796
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001148
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "TalkShoeCupboardF4 and TalkPEWarehouseF4 and TalkAtriumF4 and TalkJudoF4 and TalkGymF4 and TalkAisle2F4 and TalkToiletF4 == True" }]):
        jump block_00001799
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00001147
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" },{ "scope": 1, "content": "TalkShoeCupboardF4 and TalkPEWarehouseF4 and TalkAtriumF4 and TalkJudoF4 and TalkGymF4 and TalkAisle2F4 and TalkToiletF4 == True" }]):
        jump block_00003AA8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" }]):
        jump block_00002F3C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FA3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001108

    return

label block_000023F6:
    # Node: 000023F6 (Atrium 1)
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

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    show rs_image_69C5819C14CC4EB9A5FE5FDB1475DEFC as tag_61A891D6A6D047DC93695DA12E13CC75 at right_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_4DBEB4DFB776458C84C13F7A2269B2D1 as tag_724406A84D7141298EFF0D864FAE1534 at left_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_554DE31DA9EA412EB667D4EF459DEFDC = 200
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_315AF115B4B942DB852541A1351DDC87 as tag_554DE31DA9EA412EB667D4EF459DEFDC at center_top zorder zorder_tag_554DE31DA9EA412EB667D4EF459DEFDC onlayer master
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D6BC962AE17948D893E50BE9B4670973

    window show

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "啊……SUMIRE学园的教练，超美型的啊～……。\n那身肌肉，真憧憬啊～"

    hide tag_554DE31DA9EA412EB667D4EF459DEFDC
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    show rs_image_315AF115B4B942DB852541A1351DDC87 as tag_61A891D6A6D047DC93695DA12E13CC75 at right_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_8FFD17943DFD449881D8513C0F30D13E as tag_724406A84D7141298EFF0D864FAE1534 at left_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "一点都没变还是那么迷恋啊，你。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2CFDB0300F544C37859649BF2D34724B as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "是男人肯定会憧憬！就算看看也是保养眼睛……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_7B5C5A077F444A129B34E79C86B664D1 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    show rs_image_315AF115B4B942DB852541A1351DDC87 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "说是这么说，真想上去摸摸。"

    show rs_image_8EE7142C4184467CB3B458996136342D as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "结果还是以身体为目标。功利的家伙。\n加藤君，人是要看内在的。"

    show rs_image_E81EA15E904A462294C3D31D7E13FC74 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "呵，装什么清高！身体的契合度\n也是决定能不能交往的重要因素！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_C16547297FF840538E7675A4823EEF0A as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "……之前奥村这么说过。"

    show rs_image_4DBEB4DFB776458C84C13F7A2269B2D1 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "哦——就是说你要打起精神去追那个棒球部教练了？{w}\n多大的？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DF96421CE7794741B625312E67460A76 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "没多大，也就五十五。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7B5C5A077F444A129B34E79C86B664D1 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "……你还真是……倒不如说，比我想像得还要……"

    pause 0.3

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00002EEC

    return

label block_00002EEC:
    # Node: 00002EEC (T ++)
    $ TalkAtriumF4 = True

    if judge_lm_condition([]):
        jump block_00003B3A

    return

label block_00002415:
    # Node: 00002415 (Atrium 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "快去别的地方……"

    window hide


    if judge_lm_condition([]):
        jump block_00001108

    return

label block_000023F4:
    # Node: 000023F4 (Shoe cupboard 1)
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

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B97A3992A1D24282B85B44E0C876F034 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_174D79C3A78E4614A51BFD2F8EDAB6F5 "啊，对了对了，{w}我和那家伙分手了。"

    rs_character_455603C2553D4277B6ECD554559077B5 "是、是吗？为什么？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_174D79C3A78E4614A51BFD2F8EDAB6F5 "问得好！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    rs_character_174D79C3A78E4614A51BFD2F8EDAB6F5 "那个人突然就把我带到厕所的单间里强吻了！{w}\n没想到是那么野蛮的人！"

    rs_character_455603C2553D4277B6ECD554559077B5 "啊……那确实会吓人一跳。"

    rs_character_455603C2553D4277B6ECD554559077B5 "不过，都交往了亲吻也会做的。虽说太快也不好……"

    rs_character_174D79C3A78E4614A51BFD2F8EDAB6F5 "但我并不想。"

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦哦，确实一年级就亲还太早了！"

    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不过，真是强硬的肉食系女生啊～"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "御咲女学院的学生？{w}能追到别的学校的，不错嘛小子。"

    pause 0.3

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_174D79C3A78E4614A51BFD2F8EDAB6F5 "我们学校全是些想要肉体关系的欲求不满的家伙！{w}\n下次要找校外的人交往了。"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 400
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_241AF4B67B0B4452B97B2944C6D13AFE zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "！？！？"

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00002EEF

    return

label block_00002EEF:
    # Node: 00002EEF (T ++)
    $ TalkShoeCupboardF4 = True

    if judge_lm_condition([]):
        jump block_00003B3B

    return

label block_00001796:
    # Node: 00001796 (Target 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『快进到放学后。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001148:
    # Node: 00001148 (Target 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『找学校里的人说说话散散心。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001799:
    # Node: 00001799 (Coversation 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊……为什么到处都是同志……"

    window hide

    $ set_window("(標準)")


    if judge_lm_condition([]):
        jump block_00001108

    return

label block_00001147:
    # Node: 00001147 (Conversation 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "刚才会那么说都是木天蓼的错！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔……散散步消消神好了……"

    window hide

    $ set_window("(標準)")

    return

label block_00002F3C:
    # Node: 00002F3C (Afternoon abadon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "还有些空余时间……\n再转转好了，就当打发时间。"

    window hide


    if judge_lm_condition([]):
        jump block_00001108

    return

label block_000017F8:
    # Node: 000017F8 (Target 3)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『在全学校奔走宣传花乃汤。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_000017F6:
    # Node: 000017F6 (Conversation 3)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "I LOVE 奥村！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好！把感情变为动力的话，\n在全校宣传也不过就是散散步！"

    window hide

    $ set_window("(標準)")

    return

label block_00001130:
    # Node: 00001130 (Atrium 4)
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
    with rs_effect_1C428704E5E24078848D388A31B861CE

    stop music fadeout 1
    $ sys_music_current_file = ""

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    pause 1.5

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_93E7311915BC403AAFABACFA29A7DDB1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_4DBEB4DFB776458C84C13F7A2269B2D1 as tag_724406A84D7141298EFF0D864FAE1534 at left_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.6

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊……穗海，松田……"

    show rs_image_A4E2B01D0ECA431CB76DADC3863D74BF as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    show rs_image_B276F958003A43A59D0E1DAFE5CCAA4E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_8EE7142C4184467CB3B458996136342D as tag_724406A84D7141298EFF0D864FAE1534 at left_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "怎么？看上去挺郁闷的。"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "哈哈哈，泡妹子又失败了？"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    show rs_image_B276F958003A43A59D0E1DAFE5CCAA4E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_8EE7142C4184467CB3B458996136342D as tag_724406A84D7141298EFF0D864FAE1534 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不是！\n"
    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    extend "……{nw}"
    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    extend "……{nw}"
    show rs_image_A4E2B01D0ECA431CB76DADC3863D74BF as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_D02AAE0ED05540B9A0B6272846859C36 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    show rs_image_A39671BE6D8246F5ACCB45CA04C8C3D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_BE8486E53367484D8879711D82BE0D21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    extend "我，想退出社团。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_82F3AE3F9EEC4200A3BCB76CF8459E0A "啊！？"

    show rs_image_A4E2B01D0ECA431CB76DADC3863D74BF as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "其实……"

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 1.5

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_0083F1173FE24946A0ADCEAEB5FE3937 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    show rs_image_D7279DBAD79D48199C2509989B89EA00 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_A4E2B01D0ECA431CB76DADC3863D74BF as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……真的假的……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "突然这么说抱歉……真的。"

    show rs_image_4E2835E547304DD1A4EE59EDDEA933C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "就算你这么说……"

    show rs_image_EC8C8115C6F445299F0B9B009DD1A60D as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "问题就是问题，\n我不会说像你在那边也要加油之类的话。"

    show rs_image_CFCEEA46658B45C38D3ED429DE9FF37D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "说、说的也是……"

    show rs_image_B276F958003A43A59D0E1DAFE5CCAA4E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_AA7BE8B3E89D43F6AC40550A8222044B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg"

    extend "那下次社团里的大家就一起去妨碍营业好了。{w}\n真觉得抱歉就来好好孝顺我们。"

    show rs_image_8EE7142C4184467CB3B458996136342D as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "妨碍营业……直接普通点说“去洗澡”不就好了。"

    show rs_image_8F6CED4DA3F244518DD038888FC89CED as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "不过三朗也终于成现充了呐。\n真是做梦也没想到会被你抢先。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_5B75C21196E6494E82DFA6A82B22212D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "活动后马上洗澡，而且基山也冷气逼人，完全不想去啊——♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那个，基山什么的别叫了。\n因为就是事实所以也没法吐槽，气氛会很奇怪的。"

    show rs_image_1A85A28E47C848F89EFC14B670331197 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我不管你自己好好处理。不是想成为艺人嘛。"

    show rs_image_87B0DE188F4A48C885965C78384BEF53 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "哈哈哈，作哉好严厉。\n这下子三朗也不得不好好努力了呢，我很期待哦。"

    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……哈哈哈。"

    window hide

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00002EF4

    return

label block_00002EF4:
    # Node: 00002EF4 (T ++)
    $ TalkSakuyaMatsutaF4 = True

    if judge_lm_condition([]):
        jump block_00003B3A

    return

label block_00001110:
    # Node: 00001110 (Atrium 3)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkSakuyaMatsutaF4 == False" }]):
        jump block_00002401
    if judge_lm_condition([]):
        jump block_000023FA

    return

label block_00002401:
    # Node: 00002401 (Atrium empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_569
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3A

    return

label block_000023FA:
    # Node: 000023FA (Atrium 作哉 松田)
    $ sys_lm_menu_item = [{"pos": (216, 168),"image": "images/Chapter 2/Menu/Matsuta gym outside.png","hover": "images/Chapter 2/Menu/Matsuta gym outside hover.png","name": "松田"}, {"pos": (416, 168),"image": "images/Chapter 2/Menu/F4/Sakuya.png","hover": "images/Chapter 2/Menu/F4/Sakuya hover.png","name": "作哉"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_570
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_00002422
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B3A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_00002421

    return

label block_00002422:
    # Node: 00002422 (松田)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_F74587AF3C5D4336B5497ADD0EDFD9BA as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "作哉还是那么不坦率呢。{w}\n嘛，那也算是那家伙的一个优点了。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000023FA

    return

label block_00002421:
    # Node: 00002421 (作哉)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_A1E5ACA746C942F3A9F51B2AF04B0001 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CD9A9B1423D0463AA2EB596EBC4A4796 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……先说好，艺人什么的只是开玩笑。{w}\n其实是想走美容路线的……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_573C19B20D334CB2A4B5E6AE92FDD27C as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "是吗？我倒是无所谓。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_AC7C2C2FBDC44355B4C657BEDE530F98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好冷淡……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000023FA

    return

label block_000017F3:
    # Node: 000017F3 (BGM 1)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_00001108

    return

