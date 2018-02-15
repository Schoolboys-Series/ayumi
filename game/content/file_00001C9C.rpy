# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00001C9C (CP3 Twilight 作哉)

label block_00001C9D:
    # Node: 00001C9D (開始)
    $ TalkToiletF4 = False

    if judge_lm_condition([]):
        jump block_00001C9F

    return

label block_00001C9F:
    # Node: 00001C9F (School outside)
    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

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

    $ sys_ayumi_global_map_character = "sakuya"
    $ sys_ayumi_global_map_time = "twilight"

    if judge_lm_condition([]):
        jump block_00001CCA

    return

label block_00001CCA:
    # Node: 00001CCA (School outside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_00001CCD", target_label="block_00001CCE") from _call_scb_global_map_153
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00001CA6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_00001CA7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00001CA8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_000027EA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00001CA5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00001C9E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001CCE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00001CCA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00001CCD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001CCA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001F8C

    return

label block_00001CA6:
    # Node: 00001CA6 (Gym outside)
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
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1084DAF07A574EC18C0EDEF9E03F423C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001CAE

    return

label block_00001CAE:
    # Node: 00001CAE (Gym outside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (144, 208),"image": "images/Chapter 3/Menu/F4/Shinobu.png","hover": "images/Chapter 3/Menu/F4/Shinobu hover.png","name": "しのぶ"}, {"pos": (336, 187),"image": "images/Chapter 3/Menu/F4/Tsuki.png","hover": "images/Chapter 3/Menu/F4/Tsuki hover.png","name": "月"}, {"pos": (527, 176),"image": "images/CHAPTER 2/MENU/Matsuta gym outside.png","hover": "images/CHAPTER 2/MENU/Matsuta gym outside hover.png","name": "松田"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_581
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C9F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_00001CF4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00001CF5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00001CF6

    return

label block_00001CF4:
    # Node: 00001CF4 (松田)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_F74587AF3C5D4336B5497ADD0EDFD9BA as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "好像很有意思。{w}不过眉间皱纹太多\n可是会拉低颜值的哦？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001CAE

    return

label block_00001CF5:
    # Node: 00001CF5 (忍)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_B6AB8ED7C4FF45F685270512420E0C03 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友好像又引起麻烦了呐，这次就随便你了。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001CAE

    return

label block_00001CF6:
    # Node: 00001CF6 (月)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_92C3F2E1288740358CA42B1A6DDF3C97 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "要注意森海是不是，交给我了。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001CAE

    return

label block_00001CA7:
    # Node: 00001CA7 (Atrium)
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
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_819903C0E7144FDDADE04672BA6B63AE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001CAF

    return

label block_00001CAF:
    # Node: 00001CAF (Atrium 空)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (407, 149),"image": "images/Chapter 3/Menu/F4/Sora.png","hover": "images/Chapter 3/Menu/F4/Sora hover.png","name": "空"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_582
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C9F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_00001CF3

    return

label block_00001CF3:
    # Node: 00001CF3 (空)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_12BF0FC7B4CD4AC882419641BAF15F11 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_DD262412FCB24C70AC8A06C17B24813B as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊——又是那么恐怖的表情。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "呼……哈……{w}还不是你们干的。\n刚才那个闹剧到底是什么。"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0128BB8EAA3541469E1CD433C1215308 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "是为了作哉君着想的事哦。\n"
    show rs_image_E5B7B6FE0DF64E6CB5D98406AB347699 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "真是的，为什么你就不能坦率一些呐。"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "唔……你、你不也是。{w}\n明白不？就是这么回事。"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_92F96C9DBA8F4B2A87A3EE761E965D76 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸……啊……{w=0.6}{nw}"
    show rs_image_C2B55344314A4CA8AF5B1B2EA8D3D191 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "唔……"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你也是，抓紧回家找你哥哥\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "{color=#FF00FF}“我～最喜欢～哥哥了～♪”{/color}\n这么说不就完了。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_05964974698647618D474B73FDA403FA as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我、我才不会那么说！\n"
    show rs_image_8A87E197C01548FD9A2F0AD374E89CE6 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "再、再说了，我才没有不坦率。\n别把我和你混为一谈。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001CAF

    return

label block_00001CA8:
    # Node: 00001CA8 (Schoolhouse)
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
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_51A12E9EAB2B492E9FD30BC2C01A5C1B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001CB0

    return

label block_00001CB0:
    # Node: 00001CB0 (Schoolhouse)
    $ sys_lm_menu_item = [{"pos": (384, 168),"image": "images/Menu/Tsubasa-chan CP3.png","hover": "images/Menu/Tsubasa-chan CP3 hover.png","name": "ツバサ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_583
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C9F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ツバサ\"" }]):
        jump block_00001CF2

    return

label block_00001CF2:
    # Node: 00001CF2 (小翼)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_FA45AF5788214DF5991FE141D6F0805C as tag_A469B787E7E7466FA1613F380A4CBF41 at center_bottom zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_5DE0260CCB144839AFC115F333936DDB as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪！"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "对不起，小翼。现在不能陪你玩。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "得赶紧找到那家伙，\n不捏个粉碎不解气。"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DD161C694A914549AB92CE52B2C0D272 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪——"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "要是能带上小翼的话\n那家伙的位置马上就能知道，\n可也不能就这么带着你在学校里来回走。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001CB0

    return

label block_000027EA:
    # Node: 000027EA (School door)
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

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("校门"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F95856ACBC5A49B2B61D4DBB1E7B4294 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000027E9

    return

label block_000027E9:
    # Node: 000027E9 (School door)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (96, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "屋外トイレへ"}, {"pos": (456, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "学校看板"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_584
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外トイレへ\"" },{ "scope": 1, "content": "TalkToiletF4 == False" }]):
        jump block_000027E8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外トイレへ\"" }]):
        jump block_000027EC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学校看板\"" }]):
        jump block_00001CC0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C9F

    return

label block_000027E8:
    # Node: 000027E8 (Outiside toilet)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("室外厕所"))
    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AC86D4E564124F9A8DE5EF0A5293F191 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.7

    pause 0.3

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……嗯？这地方有个厕所来着？"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外厕所"))
    pause 0.2


    if judge_lm_condition([]):
        jump block_0000316D

    return

label block_0000316D:
    # Node: 0000316D (T ++)
    $ TalkToiletF4 = True

    if judge_lm_condition([]):
        jump block_000027EB

    return

label block_000027EB:
    # Node: 000027EB (Outside toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_585
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000027EA

    return

label block_000027EC:
    # Node: 000027EC (Outside toilet)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("室外厕所"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AC86D4E564124F9A8DE5EF0A5293F191 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000027EB

    return

label block_00001CC0:
    # Node: 00001CC0 (Board)
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
        jump block_000027E9

    return

label block_00001CA5:
    # Node: 00001CA5 (Shoe cupboard)
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
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E9592A382F574338BCE51B690BEBEF00 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001CAD

    return

label block_00001CAD:
    # Node: 00001CAD (Shoe cupboard)
    $ sys_lm_menu_item = [{"pos": (160, 96),"image": "images/Menu/Nameko.png","hover": "images/Menu/Nameko hover.png","name": "滑子"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_586
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C9F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_00001CB2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" }]):
        jump block_00001CD0

    return

label block_00001CB2:
    # Node: 00001CB2 (Playground)
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
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F6470A84AD8845BE97EAAA615A68C2F5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001CB3

    return

label block_00001CB3:
    # Node: 00001CB3 (Playground)
    $ sys_lm_menu_item = [{"pos": (112, 144),"image": "images/CHAPTER 2/MENU/F4/Itou.png","hover": "images/CHAPTER 2/MENU/F4/Itou hover.png","name": "伊藤"}, {"pos": (272, 152),"image": "images/CHAPTER 2/MENU/Katou.png","hover": "images/CHAPTER 2/MENU/Katou hover.png","name": "加藤"}, {"pos": (472, 144),"image": "images/CHAPTER 2/MENU/F4/Kimura.png","hover": "images/CHAPTER 2/MENU/F4/Kimura hover.png","name": "木村"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (664, 224),"image": "images/MOVING/ACTIONS/Moving 4.png","hover": "images/MOVING/ACTIONS/Moving 4 hover.png","name": "体育倉庫"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_587
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001CA5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" }]):
        jump block_00001CB6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" }]):
        jump block_00001CF1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_00001CDA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_00001CDB

    return

label block_00001CB6:
    # Node: 00001CB6 (加藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_CF9552A127F84B139910618B1FE71819 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_1DB6078B9236425482D8C50AB190159F as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_81D16F74A3C44B8982DB528D7D934850 "诶？班长？\n"
    show rs_image_21A5A72FBBD8459A863B99B859A0013F as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "是、是不是和以前一样去厕所了啊？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001CB3

    return

label block_00001CF1:
    # Node: 00001CF1 (PE warehouse)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Key 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Key 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Key 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.7

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_4D6C0781022E46CA9AF15C613D7158EB as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯……？\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CA1F2CFC913843C1AECB091F978FC9DC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，等等穗海！"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "怎、怎么了。"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_797E55E06BC246B8B79C4A3E846A9E72 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "不、那个……所以说……"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_21A5A72FBBD8459A863B99B859A0013F as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "那个啊，我们这种\n要用操场的运动部的仓库里是很乱的。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_C01826114A8B4A66B7637170605A577C as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "对，对对。所以接下来要进行大扫除，\n现在里面又黑又乱还是不要进去为好哦。"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊——是这样。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AD32BE71FC11444A8598BBF482AF95D0 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸？有大扫除这种事来着？"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_6AC542E194714D3B9139FB8ED959EF70 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_36E75A5BA4504559920E625E0462334C as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "……"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_AD32BE71FC11444A8598BBF482AF95D0 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001CB3

    return

label block_00001CDA:
    # Node: 00001CDA (伊藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_4D6C0781022E46CA9AF15C613D7158EB as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_84ECEC41D074460088D334B076B5152D as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_710A38AC94C841779DB701B5AC1010FD "诶，有没有看见过森海？\n"
    show rs_image_6AC542E194714D3B9139FB8ED959EF70 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不、没有～不知道。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001CB3
    if judge_lm_condition([]):
        jump block_00001CB3

    return

label block_00001CDB:
    # Node: 00001CDB (木村)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_770FBE957C624A43B0FADE9DB660E0E2 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_AD32BE71FC11444A8598BBF482AF95D0 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_E3F6ADD43DE44A428E1224756613C694 "在找森海？{w}那样的话那边……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_AC0CEBD610B64118B8D2BC90484E5801 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "哇——！！住嘴笨蛋！！！"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7AF8B6819D0F4889AEC03FD7D8B3FA6F as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "班长现在行踪不明！\n没有其他情报了！！"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_142079CDA33F4DC78D096D731F4B657B as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "以上！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001CB3

    return

label block_00001CD0:
    # Node: 00001CD0 (滑子)
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4E68A2DC06DC4980B15518EDB26D1FCD as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "穗海！走廊里别跑！！"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "对、对不起。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))

    if judge_lm_condition([]):
        jump block_00001CAD

    return

label block_00001C9E:
    # Node: 00001C9E (School inside)
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

    $ sys_ayumi_global_map_character = "sakuya"
    $ sys_ayumi_global_map_time = "twilight"

    if judge_lm_condition([]):
        jump block_00001CC9

    return

label block_00001CC9:
    # Node: 00001CC9 (School inside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_00004236", target_label="block_00004237") from _call_scb_global_map_154
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00001CA0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00001CA1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_00001EB8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00001CA3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00001CA4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00001C9F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00001CC9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00004236
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00004237
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001CC9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00003173

    return

label block_00001CA0:
    # Node: 00001CA0 (Aisle 2)
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
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4B5F763E9F424591A5E354CF41830363 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001CAA

    return

label block_00001CAA:
    # Node: 00001CAA (Aisle 2)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (142, 184),"image": "images/Chapter 3/Menu/F4/Okajima point.png","hover": "images/Chapter 3/Menu/F4/Okajima hover.png","name": "岡島"}, {"pos": (353, 182),"image": "images/Chapter 3/Menu/F4/Sato point.png","hover": "images/Chapter 3/Menu/F4/Sato hover.png","name": "佐藤"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_588
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C9E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_00001CEF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"佐藤\"" }]):
        jump block_00001CEE

    return

label block_00001CEF:
    # Node: 00001CEF (岡島)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 300
    show rs_image_6EACDBA5EB7B44D7A7699633252E6B7E as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_bottom zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00004238

    return

label block_00004238:
    # Node: 00004238 ()
    $ del TalkToiletF4

    return

label block_00001CEE:
    # Node: 00001CEE (佐藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 300
    show rs_image_2E24765C23544B69A9391DC51FE38194 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_bottom zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00004238

    return

label block_00001CA1:
    # Node: 00001CA1 (Roof)
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

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C5A69FE639934E6FB6B6BCD7FD68AD03 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001EB7

    return

label block_00001EB7:
    # Node: 00001EB7 (Empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_589
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C9E

    return

label block_00001EB8:
    # Node: 00001EB8 (Music room)
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
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001EB7

    return

label block_00001CA3:
    # Node: 00001CA3 (Library)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『正在补习，还是不要进去了。』{/color}"

    window hide

    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 200
    $ zorder_tag_88D3209FDD1D4A2E8369A5A61DF50852 = 400


    if judge_lm_condition([]):
        jump block_00001C9E

    return

label block_00001CA4:
    # Node: 00001CA4 (Toilet)
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
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3D19FEC65E254A0DB387C645D1A07434 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001CAC

    return

label block_00001CAC:
    # Node: 00001CAC (Toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (224, 184),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "トイレ個室"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_590
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001C9E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ個室\"" }]):
        jump block_00001F0A

    return

label block_00001F0A:
    # Node: 00001F0A (Toilet single)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    pause 0.4

    pause 0.6

    window show

    if sys_effect_current_file != "sound/Effect Sound/Search 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Search 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Search 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "（刷刷……）"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "（这个声音是……！）\n"
    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "混蛋森海！在里面是不！？滚出来！！"

    rs_character_9EDF48057FB84D428D56198A69E2880E "！？"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "装不在没用。{w}\n要是门能从这边开你早就……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "不、不是的等等！！认错人了！！"

    rs_character_9EDF48057FB84D428D56198A69E2880E "所以门就不要开了——！\n至少开门请绝对不要……！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊……{w}抱、抱歉，认错人了。{w}\n多有打扰，请慢用……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "（……{w}那家伙之外居然也有会在学校做{color=#008080}这个{/color}的……）{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_13F7DE943DC546C1B5F88F02D5A346DC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("厕所"))

    if judge_lm_condition([]):
        jump block_00001CAC

    return

label block_00004236:
    # Node: 00004236 (Conversation)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那个混蛋，这次一定要把他废了……！"

    window hide

    $ set_window("(標準)")

    return

label block_00004237:
    # Node: 00004237 (Target)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『找出森海友废了他。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003173:
    # Node: 00003173 (Character)
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

label block_00001CCE:
    # Node: 00001CCE (Target)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『找出森海友废了他。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001CCD:
    # Node: 00001CCD (Conversation)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那个混蛋，这次一定要把他废了……！"

    window hide

    $ set_window("(標準)")

    return

label block_00001F8C:
    # Node: 00001F8C (Character)
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

