# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00001C51 (CP3 作哉散歩)

label block_00001C52:
    # Node: 00001C52 (開始)

    if judge_lm_condition([]):
        jump block_00001C55

    return

label block_00001C55:
    # Node: 00001C55 (Misaki)
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
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "sakuya_tsubasachan"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_00001C56

    return

label block_00001C56:
    # Node: 00001C56 (Misaki XCTA)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", False, True, talk_label="block_00001C53", target_label="block_00001C54") from _call_scb_global_map_13
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲学園\"" }]):
        jump block_00001C59
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"住宅街\"" }]):
        jump block_00001C57
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" }]):
        jump block_00001C61
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" }]):
        jump block_00001C5A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲駅\"" }]):
        jump block_00002795
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"昼休み不可\"" }]):
        jump block_00001C56
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00001C53
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001C54
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_0000422B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001F87

    return

label block_00001C59:
    # Node: 00001C59 (Misaki school)
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


    if judge_lm_condition([{ "scope": 0, "content": "C3S4 == True" },{ "scope": 1, "content": "C3QSakuyaWalk1 == False" }]):
        jump block_0000278C
    if judge_lm_condition([]):
        jump block_00001C58

    return

label block_0000278C:
    # Node: 0000278C (School door 翼 point)
    $ sys_lm_menu_item = [{"pos": (296, 252),"image": "images/Chapter 3/Menu/Tsubasa school door point.png","hover": "images/Chapter 3/Menu/Tsubasa school door hover.png","name": "つばさ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_124
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_0000278E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00004229

    return

label block_0000278E:
    # Node: 0000278E (翼)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_58B570C730E34F7D910E94E19D4A143A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_E5980AB1AA3E484A93A2EBD2139A77FE as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君，现在正在散步吗？\n请注意安全，等下再见。"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊，哦，谢谢{w}……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "那个，你要不要一起来？\n{w=0.5}毕竟也是饲育系的。"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5949B5B78A4A498996EECB708FE12ECF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "真的可以吗？太好了。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 100
    show rs_image_3FF5037A502D4C24A92D108FA6E56C70 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-180, yalign=1.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_FA45AF5788214DF5991FE141D6F0805C as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=170, yalign=1.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "小翼酱，今天要和我一起哦。请多指教。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_0701C7A0E7A94630B00823C49B275DA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "汪！"

    window hide

    pause 0.8

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    $ set_window("イベントモード")
    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4E74502696E847418F9F14C16FA3311B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3CEFCC6E25854EAF8539000CAB15A346 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_music_current_file != "sound/BGM/The hope.ogg":
        play music "sound/BGM/The hope.ogg" loop
        $ sys_music_current_file = "sound/BGM/The hope.ogg"

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "汪汪♪"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_E3D2D87C0D4C4A54B7016B01E2AC7D10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_D4AF6091BD0341CFBF561C2744F3FD83 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "小翼酱今天很开心呐。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "因为三人一起很高兴。{w}慢点小翼，\n别太闹腾了，衣服会散开的。"

    show rs_image_F0AF18EA5ED94E6B9426EA7B01961357 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那件衣服是作哉君买的吗？"

    show rs_image_AA7BE8B3E89D43F6AC40550A8222044B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嗯，在伊丹咲的购物中心买的。\n还不错？可是很贵的——"

    show rs_image_3C4C246AAFC1459DBB1711584019784D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯，非常可爱！\n"
    show rs_image_9071DE7B7E5343C897D93F24F8DF7BAF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过作哉君，请千万不要对自己太苛刻。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我从猫山那里听说作哉君为了\n买给小翼酱的东西{color=#008080}完全顾不上身体过{/color}。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FC5BB2AA35B44ADFBC8F0E8552F94744 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F93680E6233E49F4ABCA8E90EE52A220 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "总觉得这种说法好下流——"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_C197AB750EF8424887D8CF5ECCE7226B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "真、真是的！好好听我说话！"

    show rs_image_AA7BE8B3E89D43F6AC40550A8222044B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈哈，抱歉抱歉，不过我没事的。\n现在必要的东西学校那边会配给小翼。"

    show rs_image_4E2835E547304DD1A4EE59EDDEA933C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……不过，确实还是很复杂。\n总觉得无论如何也不想放开小翼。"

    show rs_image_3C4C246AAFC1459DBB1711584019784D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哈哈，作哉君的独占欲很强呐。"

    show rs_image_B276F958003A43A59D0E1DAFE5CCAA4E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "这该说你。"

    show rs_image_E3D2D87C0D4C4A54B7016B01E2AC7D10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不过，小翼酱最喜欢作哉君了。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君也最喜欢小翼酱，\n所以就这样也没什么不好。"

    show rs_image_4E2835E547304DD1A4EE59EDDEA933C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……唔……也对……\n"
    show rs_image_D7279DBAD79D48199C2509989B89EA00 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "但终归不可能永远在一起的。"

    show rs_image_93384CF7101E46B99C76C26B616C4A01 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊……{w=0.5}{nw}"
    show rs_image_8D9EAB710DF84DAAA58AA16DC9ADFC74 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "小翼酱现在是学校在养，\n如果毕业了……"

    show rs_image_938B36C37FE5472AAA76BF86253DFDCD as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嗯……不知道我上高中时能不能领走。"

    show rs_image_186B19EF8A8141319DE9B5EB9DE2BAC0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这个或许……"

    show rs_image_5B75C21196E6494E82DFA6A82B22212D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "骗你的，我也知道肯定带不走。\n"
    show rs_image_4E2835E547304DD1A4EE59EDDEA933C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "剩下的四年里我必须做好心理准备了。"

    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "四年？\n{w=0.45}{nw}"
    show rs_image_F0AF18EA5ED94E6B9426EA7B01961357 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "啊，作哉君是要直升高中部来着。"

    show rs_image_93E7311915BC403AAFABACFA29A7DDB1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你要怎么做？"

    show rs_image_54984C82CD7C4D86A32BA7AFE5015CD1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那个……我……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我还没决定好，不过应该也是一样的。"

    show rs_image_AA7BE8B3E89D43F6AC40550A8222044B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那就决定了，\n你直到高中毕业都得和我待在饲育系。"
    show rs_image_F0AF18EA5ED94E6B9426EA7B01961357 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……{w=0.4}{nw}"
    show rs_image_E3D2D87C0D4C4A54B7016B01E2AC7D10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "好，当然。我们会一起努力的。"

    window hide

    pause 1

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 1.7


    if judge_lm_condition([]):
        jump block_0000278D

    return

label block_0000278D:
    # Node: 0000278D (QUEST FINISH)
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
        jump block_00003045

    return

label block_00003045:
    # Node: 00003045 (C3Q作哉散歩)
    $ C3QSakuyaWalk1 = True

    if judge_lm_condition([]):
        jump block_0000422D

    return

label block_0000422D:
    # Node: 0000422D ()

    return

label block_00004229:
    # Node: 00004229 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00004228

    return

label block_00004228:
    # Node: 00004228 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00001C55

    return

label block_00001C58:
    # Node: 00001C58 (Misaki school empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_125
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00004229

    return

label block_00001C57:
    # Node: 00001C57 (Residential street)
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


    if judge_lm_condition([{ "scope": 0, "content": "C1S4 == True" }]):
        jump block_00001C5B
    if judge_lm_condition([]):
        jump block_00001C91

    return

label block_00001C5B:
    # Node: 00001C5B (Residential street)
    $ sys_lm_menu_item = [{"pos": (152, 288),"image": "images/Chapter 3/Menu/Yukio.png","hover": "images/Chapter 3/Menu/Yukio hover.png","name": "雪緒"}, {"pos": (312, 290),"image": "images/Chapter 3/Menu/Shiro.png","hover": "images/Chapter 3/Menu/Shiro hover.png","name": "四朗"}, {"pos": (552, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (696, 360),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_126
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00004229
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001C64
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00001C6A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"四朗\"" }]):
        jump block_00001C5F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"雪緒\"" }]):
        jump block_00001C8F

    return

label block_00001C64:
    # Node: 00001C64 (Residential street turning)
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
        jump block_00001C65

    return

label block_00001C65:
    # Node: 00001C65 (Residential street turning)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (120, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "花乃湯"}, {"pos": (512, 320),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "神社"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_127
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"花乃湯\"" }]):
        jump block_00001C70
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"神社\"" }]):
        jump block_00001C6E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C57

    return

label block_00001C70:
    # Node: 00001C70 (花乃湯)
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


    if judge_lm_condition([{ "scope": 0, "content": "C3S5 == True" },{ "scope": 1, "content": "C3QSakuyaWalk2 == False" }]):
        jump block_00002796
    if judge_lm_condition([]):
        jump block_00001C71

    return

label block_00002796:
    # Node: 00002796 (花乃湯 翔銀時 point)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "ポスター"}, {"pos": (232, 272),"image": "images/Chapter 3/Menu/Shougintoki point.png","hover": "images/MENU/Shougintoki hover.png","name": "翔銀時"}, {"pos": (80, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_128
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C64
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001C7C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ポスター\"" }]):
        jump block_00001F7D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"翔銀時\"" }]):
        jump block_00002798

    return

label block_00001C7C:
    # Node: 00001C7C (River)
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
        jump block_00001C7D

    return

label block_00001C7D:
    # Node: 00001C7D (River)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_129
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C70

    return

label block_00001F7D:
    # Node: 00001F7D (Poster)
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


    if judge_lm_condition([{ "scope": 0, "content": "C3S5 == True" },{ "scope": 1, "content": "C3QSakuyaWalk2 == False" }]):
        jump block_00002796
    if judge_lm_condition([]):
        jump block_00001C71

    return

label block_00001C71:
    # Node: 00001C71 (花乃湯)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "ポスター"}, {"pos": (232, 272),"image": "images/Menu/Shougintoki.png","hover": "images/Menu/Shougintoki hover.png","name": "翔銀時"}, {"pos": (80, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_130
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C64
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001C7C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"翔銀時\"" }]):
        jump block_00001C79
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ポスター\"" }]):
        jump block_00001F7D

    return

label block_00001C79:
    # Node: 00001C79 (翔銀時)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_D7825E4D13D149599171D72320D84152 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "你好。你是御咲学园的学生呐。\n学校生活如何？\n我还在上学的时候也很不守规矩的。"

    show rs_image_27A65FC15594414F8E6CF36C64C026E2 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "当时学校里流传着{color=#3A00C4}禁忌之箱{/color}的传说。"

    show rs_image_D7825E4D13D149599171D72320D84152 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "于是和朋友在夜里偷偷四处寻找，\n结果反而被老师逮到，骂了个狗血淋头。"

    show rs_image_4E1328DF58984CDDB873E6CA9A162506 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "现在想来也是一段不错的回忆。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001C71

    return

label block_00002798:
    # Node: 00002798 (翔銀時)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 = 300
    show rs_image_4E1328DF58984CDDB873E6CA9A162506 as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 at center_bottom zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_CA5DCF09EC6F43D3BF094A232BE224FB as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "从这里走向河边的途中\n有一家{color=#FF8000}很小的点心店{/color}，\n你们知道吗？"

    show rs_image_27A65FC15594414F8E6CF36C64C026E2 as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "小时候我经常和朋友在附近玩闹，\n不过现在它也快停业了。"

    show rs_image_1DB126B964544691AE7B64404BF2995F as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "现在再也不能像那时候一样无忧无虑，\n成了让我觉得寂寞的地方。"

    show rs_image_D7825E4D13D149599171D72320D84152 as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "像你们这样年轻的孩子，\n就算是最后也好能去看看吗？"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哦、哦……"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4E1328DF58984CDDB873E6CA9A162506 as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "那家店带狗也可以，请务必考虑一下。"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "好，那就恭敬不如从命了。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_ACAAB0A43F254041BE2C5833D3FC0CE4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤"))
    pause 0.8

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    hide tag_ACAAB0A43F254041BE2C5833D3FC0CE4
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    $ set_window("イベントモード")
    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F47427D826C04309BFF6F67F8BD7B5E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_2A8CFCB3518F4B1B8CF01BE489B15614 as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_96008F8E7DAF407BA911D5C58BC9CB39 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_D4AF6091BD0341CFBF561C2744F3FD83 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_311C0DF0CF504684BAB1C36398430D4D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸——这种地方居然会有粗点心店，\n我还是第一次听说。"

    rs_character_7009C1117C004F51829614A203C67DE7 "真厉害。\n这种店电视上是看不到的。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_17BE89E1E45A45008C16668BC9724267 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你们快看，这个只要10日元（五毛）。\n哦，这个方便面只有30日元（一块七）！"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5E2E79FDD0B34262B8021229C4B2D2EF as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_D14C1328F4484EBE997C5CE2D0C119BD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_B0AE196FCA0347DEACA52C0CB36FB8EE as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_2DF3B619CE3348E0991798902A52CAA9 "好便宜——！！"

    show rs_image_AA7BE8B3E89D43F6AC40550A8222044B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "居然会有这种好地方，\n要是早知道就好了。"

    show rs_image_25B4CA5E7DB54A70B991383AB9E2522F as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_D4AF6091BD0341CFBF561C2744F3FD83 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_C040277FC7FE48E19FB154ABD798FD6D as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "谢谢你们专程过来。{w}\n作为额外服务给你们做{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "{color=#FF80FF}“章鱼煎饼”{/color}好了。"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_3DE6DC5E51F14E4F86F96E18DE4838E6 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "章鱼……煎饼？没听说过。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "在薄薄的煎饼上加满香料和蛋黄酱……\n"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3DE6DC5E51F14E4F86F96E18DE4838E6 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……好，做出来了♪"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "注意不要沾到衣服上，小心点吃。"

    show rs_image_25B4CA5E7DB54A70B991383AB9E2522F as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_8AD2DDD7544B43C4A6A69B2DAC1465E5 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "唔……（吞）……{w=0.55}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_311C0DF0CF504684BAB1C36398430D4D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_F03237FB10EB44FDB0C2E3F6C4B4F5D2 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    extend "哇——好好吃。\n看起来很简单味道却非常好呐～"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_A079030308E04EE6997F57E2BB27CB8C as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_486F70F1E27D43BC868FA3ADA0B574BE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊，等等，小翼不能吃。\n"
    show rs_image_93E7311915BC403AAFABACFA29A7DDB1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "这个多少钱一个？"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "{color=#00FFFF}30日元{/color}。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E62168EC90B7417CB5F5DD87BA487392 as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_35ACEB15A07B41568764DA8D74ECEF47 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_A39671BE6D8246F5ACCB45CA04C8C3D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_BFC4A160DFDF465C82BD02885E29367D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6FFBDD573FFA4A549C1850B3788382F2 "好便宜——！！"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "除了点心，10日元的游戏也有，要不要试试。"

    pause 0.3

    show rs_image_2A8CFCB3518F4B1B8CF01BE489B15614 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_3CEFCC6E25854EAF8539000CAB15A346 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_AA7BE8B3E89D43F6AC40550A8222044B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_12FA5E6A33CF436D8BF3D03325E739EE as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 1.35

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 = 200
    show rs_image_B7E2FD9714DF4EF0A712370A5AEFF12A as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 at center_top zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.4

    if sys_music2_current_file != "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg":
        play music2 "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg"

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "太好了，那个少年带了朋友过来。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "哦，诹访部先生，欢迎光临。\n多亏你最近来这里的孩子越来越多了。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "之前月君空君还有慎太郎亲\n也难得来了一次。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "对了，由实大姐也特地从宝咲过来了。"

    show rs_image_7197DF88471C4D66A7505D8DFC72D61F as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "那真是太好了。{w}这里对我来说也是充满了回忆的地方。\n应该会成为我珍藏的记忆吧。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "这样啊。诹访部先生，\n以前我经常在外面的长椅上看到你和朋友聊天呢。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "有着祖母绿宝石般晶莹瞳孔的朋友。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "你们都那么帅，每天走过的御咲女学院的学生\n都不得不被你们迷住呢。"

    show rs_image_B7E2FD9714DF4EF0A712370A5AEFF12A as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "哈哈哈，我还真没注意到。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "那时候我还没到那个年纪。{w}\n请问朋友那边还好么？"

    show rs_image_118EF028EE994EDF9E40B23583115EC5 as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "……很久以前{w=0.5}{nw}"
    show rs_image_CC61CB4A283E4FCD8F2E04E37E005917 as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……还是中学生的时候，\n因为一场意外去了我不可及的地方。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "这样……抱歉让你想起这些。"

    show rs_image_118EF028EE994EDF9E40B23583115EC5 as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "当时传得满城风雨，连新闻都报导过……"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Bell 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "……你说的该不会是御咲学园过去那起……？"

    window hide

    pause 0.6

    hide tag_ACAAB0A43F254041BE2C5833D3FC0CE4
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_FFC620A1302E417EBD9CB71C6CDE9274

    pause 0.4

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 400
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 100
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 100
    show rs_image_ABB2A951B8D345A092CC374396221386 as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_A079030308E04EE6997F57E2BB27CB8C as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_4E2835E547304DD1A4EE59EDDEA933C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_A7D458B112A543F691F4223B8946B813 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_F7C0A55C2AAD46A09EC5C9F64521E3DB

    pause 0.5

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "欸……我们学校发生过那样的事，我完全不知道……"

    show rs_image_BFC4A160DFDF465C82BD02885E29367D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "御咲学园好像发生过各种古怪的事情呢。"

    rs_character_7009C1117C004F51829614A203C67DE7 "……"

    if sys_effect3_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_1AB0074A0ABB40A7B797779771DF877D = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C94C15F70ECD4CCBBA838E6B1352ED84 as tag_1AB0074A0ABB40A7B797779771DF877D at right_top zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_74A39D760C4A4450A49ACE936895FF00

    pause 0.35

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『原来如此，其竟有如此过去，实乃艰辛。』"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 400
    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "（呐，九尾，要不要和那个人做朋友？）"

    show rs_image_741DD1CD8B8948359D329B0A50F15E14 as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『呼呼呼，可笑。』"

    show rs_image_5BF57DBE5ED14CE2AFADF67B50D75DA7 as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『高傲尊贵之九尾怎可屈尊结交缚于地者？』"

    show rs_image_ABB2A951B8D345A092CC374396221386 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "（可是，听上去太可怜了。"
    show rs_image_1F46FB7004DE45F98059A018EE0BD1C7 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "再说了，\n要是你真那么伟大，就拿出点气量来。）"

    show rs_image_44AB1722C8A84482A52D4E6D6159C34B as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "（我可是听说能人胸怀宽广的。）"

    show rs_image_83DC2938B261446EA7DA8E7BEDD8F68F as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『吾非人也……"
    show rs_image_C94C15F70ECD4CCBBA838E6B1352ED84 as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "然闻汝言，或可稍作思量。』"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_741DD1CD8B8948359D329B0A50F15E14 as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『仅为死后之人，且为美人♪』"

    window hide

    pause 1

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_1AB0074A0ABB40A7B797779771DF877D
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2


    if judge_lm_condition([]):
        jump block_00002797

    return

label block_00002797:
    # Node: 00002797 (QUEST FINISH)
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
        jump block_00003046

    return

label block_00003046:
    # Node: 00003046 (C3Q作哉)
    $ C3QSakuyaWalk2 = True

    if judge_lm_condition([]):
        jump block_0000422E

    return

label block_0000422E:
    # Node: 0000422E ()

    return

label block_00001C6E:
    # Node: 00001C6E (Jinja)
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
        jump block_00001C6F

    return

label block_00001C6F:
    # Node: 00001C6F (Jinja)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_131
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C64

    return

label block_00001C6A:
    # Node: 00001C6A (Square)
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
        jump block_00001C6B

    return

label block_00001C6B:
    # Node: 00001C6B (Square)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (624, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "泉の公園"}, {"pos": (120, 328),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "？？？"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_132
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉の公園\"" }]):
        jump block_00001C77
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C57
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"？？？\"" }]):
        jump block_00001C6C

    return

label block_00001C77:
    # Node: 00001C77 (Spring water park)
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

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4C85C2BFFE134BFDADEC528506A90841 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001C78

    return

label block_00001C78:
    # Node: 00001C78 (Spring water park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_133
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C6A

    return

label block_00001C6C:
    # Node: 00001C6C (Forest)
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
        jump block_00001C6D

    return

label block_00001C6D:
    # Node: 00001C6D (Forest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_134
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C6A

    return

label block_00001C5F:
    # Node: 00001C5F (四郎)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_D78063E41074477191182CBC87962C7C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_bottom zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "等我进入御咲学园后每天都要和小翼一起玩哦！"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "是呐。那四郎干脆也来饲育系帮忙好了。\n现在小翼是学校在养。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "现在只有我和一之濑，非常缺值得信赖的人手。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CE2AA99006A14FB68F9A5BA7EB0C8B29 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸，翼前辈也在！\n"
    show rs_image_41A84CEAB4B9488D918E907B63CC8E1A as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那种好动的人真的能干饲育系么。\n感觉他才是该被养的那一边……"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_CD2255EE7C77442EA5D34AF3CB25F51A as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "算了，不管了。\n我入学后也要加入饲育系！\n我会去帮忙的！"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "？{w=0.5}嗯，等着你。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("住宅街"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001C5B

    return

label block_00001C8F:
    # Node: 00001C8F (雪緒)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_AEF29DAA216E47B98629F2356997D217 as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "作哉前辈，下午好～"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    $ zorder_tag_49886B5191F044E1BF6A40972149F4D8 = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 100
    show rs_image_C36C23E5F50647C4A1A9C68D0CF3AF78 as tag_49886B5191F044E1BF6A40972149F4D8 at Transform(xpos=-180, yalign=1.0) zorder zorder_tag_49886B5191F044E1BF6A40972149F4D8 onlayer master
    show rs_image_5DE0260CCB144839AFC115F333936DDB as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=170, yalign=1.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！"

    hide tag_49886B5191F044E1BF6A40972149F4D8
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_15CDCB84318E4484BD0CA713DD1E7EA7 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=-180, yalign=1.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "乖乖，不要乱叫。\n"
    show rs_image_8BCAEF624622485E87EDCA1DB4125701 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "来，到这边来。\n小翼酱，来抱抱♪"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_0701C7A0E7A94630B00823C49B275DA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪♪"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    show rs_image_415D182241854807A3375D2199A1DA38 as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_7009C1117C004F51829614A203C67DE7 "……那个四郎……\n{w=0.4}不久之前还是{color=#008080}那样{/color}的……{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_1EC572F128FB424698C108E78BAB8E38 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……很迷。"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5149B5E9A8F345E7BF603D076168C24F as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "确实很迷……"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("住宅街"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001C5B

    return

label block_00001C91:
    # Node: 00001C91 (Residential street empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (552, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (696, 360),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_135
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001C64
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00001C6A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00004229

    return

label block_00001C61:
    # Node: 00001C61 (Shopping street)
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
        jump block_00001C62

    return

label block_00001C62:
    # Node: 00001C62 (Shopping street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (104, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_136
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00004229
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001C69

    return

label block_00001C69:
    # Node: 00001C69 (Inside)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "STAY，小翼。{w}\n前面人太多，太危险了。"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F1AE8B76A99E4FC297AF2F180FA7033F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00001C62

    return

label block_00001C5A:
    # Node: 00001C5A (Park)
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


    if judge_lm_condition([{ "scope": 0, "content": "C2QSakuya == True" }]):
        jump block_00001C96
    if judge_lm_condition([]):
        jump block_00001C5C

    return

label block_00001C96:
    # Node: 00001C96 (Park movable)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (160, 184),"image": "images/Menu/Kobayashi.png","hover": "images/Menu/Kobayashi hover.png","name": "小林"}, {"pos": (320, 184),"image": "images/Menu/Minami.png","hover": "images/Menu/Minami hover.png","name": "南"}, {"pos": (696, 200),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_137
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" }]):
        jump block_00002790
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" }]):
        jump block_00002791
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00004229
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00001C99

    return

label block_00002790:
    # Node: 00002790 (小林)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_F3C56AC05CFF4764BCEAA3638847A04F as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000278F

    return

label block_0000278F:
    # Node: 0000278F (小林・南)
    window show

    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1FF2B98C6C1E44809702A907624A30EB as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "呐——听说河边出现了\n野生的{color=#FF8000}小熊猫{/color}哦。\n是不是真的呐！"

    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_19B48A464F434AC7830B9BFFF091AB3F as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "小林酱又在这么说了。\n小熊猫是濒危物种，都在动物园里的。"

    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_01E6B401CB594D718954325CD26D9680 as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "可是真的有看到——！{w}\n那种样子见过一次肯定忘不掉！\n我现在也记着的！"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "C2QSakuya == True" }]):
        jump block_00001C96
    if judge_lm_condition([]):
        jump block_00001C5C

    return

label block_00001C5C:
    # Node: 00001C5C (Park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (160, 184),"image": "images/Menu/Kobayashi.png","hover": "images/Menu/Kobayashi hover.png","name": "小林"}, {"pos": (320, 184),"image": "images/Menu/Minami.png","hover": "images/Menu/Minami hover.png","name": "南"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_138
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00004229
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" }]):
        jump block_00002790
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" }]):
        jump block_00002791

    return

label block_00002791:
    # Node: 00002791 (南)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_BEF9DE93926B41AEA207953580E58EC3 as tag_063DF7E916A1424E84C7F9FED562D399 at center_bottom zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000278F

    return

label block_00001C99:
    # Node: 00001C99 (Park Hill)
    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("公园内山"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A924E6FB7A0740108CE21D8D0C0FC8D2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001C97

    return

label block_00001C97:
    # Node: 00001C97 (Park Hill)
    $ sys_lm_menu_item = [{"pos": (216, 88),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_139
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001C98
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C5A

    return

label block_00001C98:
    # Node: 00001C98 (Park Hill Lake)
    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("公园湖边"))
    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Wave 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wave 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7639E4BE73E34BBD9D978953E896CF0C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001C9A

    return

label block_00001C9A:
    # Node: 00001C9A (Park Hill Lake)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_140
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C99

    return

label block_00002795:
    # Node: 00002795 (御咲站)
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
        jump block_00002792

    return

label block_00002792:
    # Node: 00002792 (御咲站)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (336, 352),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (200, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "路線図"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_141
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00002794
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"路線図\"" }]):
        jump block_00002793
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00004229

    return

label block_00002794:
    # Node: 00002794 (Inside)
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

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不过，像是导盲犬那种\n受过训练的可以进去的样子。"

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
        jump block_00002792

    return

label block_00002793:
    # Node: 00002793 (Map)
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
        jump block_00002792

    return

label block_00001C53:
    # Node: 00001C53 (Conversation)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "越来越冷了……{w}\n买了新衣服真好，对不对，小翼。"

    window hide

    $ set_window("(標準)")

    return

label block_00001C54:
    # Node: 00001C54 (Target)
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

label block_0000422B:
    # Node: 0000422B (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_0000422A

    return

label block_0000422A:
    # Node: 0000422A (終了)

    return

label block_00001F87:
    # Node: 00001F87 (Character)
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

