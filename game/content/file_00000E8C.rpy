# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00000E8C (CP2 Daytime 空)

label block_00000E8D:
    # Node: 00000E8D (開始)
    $ TalkIzuKatoMatsuF1 = False
    $ TalkSaburoF1 = False
    $ TalkOkajimaKojimaF1 = False

    if judge_lm_condition([]):
        jump block_0000190F

    return

label block_0000190F:
    # Node: 0000190F (BGM2)
    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"


    if judge_lm_condition([]):
        jump block_00000E8F

    return

label block_00000E8F:
    # Node: 00000E8F (School outside)
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

    $ sys_ayumi_global_map_character = "sora"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_00000ECB

    return

label block_00000ECB:
    # Node: 00000ECB (School outside XCTX)
    if judge_lm_condition([{ "scope": 1, "content": "C2S1Phase == 99" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S1Phase == 99" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_00001918", target_label="block_00001917") from _call_scb_global_map_15
    elif judge_lm_condition([{ "scope": 1, "content": "C2S1Phase == 99" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_00001918", target_label="block_0000191D") from _call_scb_global_map_16
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C2S1Phase == 99" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_0000191E", target_label="block_00001917") from _call_scb_global_map_17
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_0000191E", target_label="block_0000191D") from _call_scb_global_map_18
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00000E96
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_00000E97
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00000E98
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00000E99
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00000E95
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00000E8E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00000ECB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C2S1Phase == 99" }]):
        jump block_00001917
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2S1Phase == 99" }]):
        jump block_00001918
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00000ECB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FA9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_0000191E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_0000191D

    return

label block_00000E96:
    # Node: 00000E96 (Gym outside)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EA0

    return

label block_00000EA0:
    # Node: 00000EA0 (Gym outside)
    $ sys_lm_menu_item = [{"pos": (168, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "体育館へ"}, {"pos": (416, 208),"image": "images/Chapter 2/Menu/Sato.png","hover": "images/Chapter 2/Menu/Sato hover.png","name": "　佐藤"}, {"pos": (664, 280),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "柔道場へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_152
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" },{ "scope": 1, "content": "TalkIzuKatoMatsuF1 == True" }]):
        jump block_00002430
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" }]):
        jump block_00000EA6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"　佐藤\"" },{ "scope": 1, "content": "C2S1Phase == 99" }]):
        jump block_00000EB7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"柔道場へ\"" }]):
        jump block_00000EE1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"　佐藤\"" }]):
        jump block_00000EBC

    return

label block_00002430:
    # Node: 00002430 (Gym 2)
    window show

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "别打扰他们练习了。\n还是去别的地方好了。"

    window hide

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000EA0

    return

label block_00003A5A:
    # Node: 00003A5A (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A59

    return

label block_00003A59:
    # Node: 00003A59 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00000E8F

    return

label block_00000EA6:
    # Node: 00000EA6 (Gym 1)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("体育馆"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_24188CBA120A4166B08F8A3535548A8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EA7

    return

label block_00000EA7:
    # Node: 00000EA7 (Gym 加藤)
    $ sys_lm_menu_item = [{"pos": (256, 200),"image": "images/Chapter 2/Menu/Izumi.png","hover": "images/Chapter 2/Menu/Izumi hover.png","name": "泉"}, {"pos": (432, 202),"image": "images/Chapter 2/Menu/Matsuta.png","hover": "images/Chapter 2/Menu/Matsuta hover.png","name": "松田"}, {"pos": (560, 200),"image": "images/Chapter 2/Menu/Katou gym.png","hover": "images/Chapter 2/Menu/Katou gym hover.png","name": "加藤"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_153
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000E96
    if judge_lm_condition([]):
        jump block_00002C45

    return

label block_00002C45:
    # Node: 00002C45 (T -> T)
    $ TalkIzuKatoMatsuF1 = True

    if judge_lm_condition([]):
        jump block_00000EA9

    return

label block_00000EA9:
    # Node: 00000EA9 (泉・加藤・松田)
    pause 0.45

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_8698F0F8B5CF421B91218546390F2E26 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_0364D19042AC45CCA8C6BF99EF5EA070 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "……攻击！！"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    pause 0.8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_7AF8B6819D0F4889AEC03FD7D8B3FA6F as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_47F94BD279D84A6F95AE78C34FA94D72

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "哇哦！？{w}泉、泉啊，\n是不是用力太大了！？"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_6B3637450A254E26B3FE58D8EA24C639 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "啊，抱歉……"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_ED1123A4A4404155ABBDBFA9983E6A38 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "泉，又带上个人感情了。"

    show rs_image_36FA043A9D13453B8E531655A8BDDE10 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "为了帮你降压我们才在这里陪你的，\n要不要先暂停一下？"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_DB7EB752E3A446FE9E0FC7B5FB53A5AC as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "……抱歉。我会认真做的，请继续！"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_5690F6AF976C4AEB8FC348FA1E25466F as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "哦哦！"
    show rs_image_21A5A72FBBD8459A863B99B859A0013F as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……所以，\n和他到底发生什么了啊。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_F74587AF3C5D4336B5497ADD0EDFD9BA as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "等下我们会好好听的。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（怎么看也不是能插话的样子。去别的地方好了。）"

    window hide

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000E96

    return

label block_00000EB7:
    # Node: 00000EB7 (佐藤 1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_EBC00E6C111C45A6830591C1B1D82AC6 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_bottom zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "诶？什么什么，女装？\n欸，很有趣的样子哦！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_1E6988844B884E2B88D92837EA789B61 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "不过不行哦。\n因为要参加社团活动所以没有空余时间哦。"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000EA0

    return

label block_00000EE1:
    # Node: 00000EE1 (Judo)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_153E9CF7193C4513869D54FA898561FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EE2

    return

label block_00000EE2:
    # Node: 00000EE2 (Judo 月)
    $ sys_lm_menu_item = [{"pos": (320, 232),"image": "images/Chapter 2/Menu/Tsuki.png","hover": "images/Chapter 2/Menu/Tsuki hover.png","name": "月"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_154
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000E96
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_0000108F

    return

label block_0000108F:
    # Node: 0000108F (月)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_8F17CE9B9953435FA745F57FC7AB45AC as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空最近好冷淡，哥哥我很伤心哦。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("柔道场外"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000EE2

    return

label block_00000EBC:
    # Node: 00000EBC (佐藤 2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 300
    show rs_image_E9DA1A925CE140459A40C853C70AA406 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_bottom zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "诶？穗海喜欢的东西？\n"
    show rs_image_F454E39E17AB417EAFAD03FC09D7C631 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……不清楚，请问别人。"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000EA0

    return

label block_00000E97:
    # Node: 00000E97 (Atrium)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EA1

    return

label block_00000EA1:
    # Node: 00000EA1 (Atrium)
    $ sys_lm_menu_item = [{"pos": (216, 160),"image": "images/Chapter 2/Menu/Tsubasa.png","hover": "images/Chapter 2/Menu/Tsubasa hover.png","name": "つばさ"}, {"pos": (488, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "食堂へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_155
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"食堂へ\"" }]):
        jump block_00000EAB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_00000EB4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5A

    return

label block_00000EAB:
    # Node: 00000EAB (Canteen)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ set_place_title(_("食堂"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D138810390DC4843A14969EAD39A7E06 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EAC

    return

label block_00000EAC:
    # Node: 00000EAC (Canteen)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_156
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000E97

    return

label block_00000EB4:
    # Node: 00000EB4 (翼)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_43C2A5DA4B5D4815BEC6FE1DA10014AC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（啊，一之濑君似乎很适合女装的样子♪{w}\n……{w=0.5}不过眉毛要是再细一些就好了呐……）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.45

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8DECB50317B14BD6B1D99221FBD7089C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哈……我为什么总是……\n"
    show rs_image_C1F668B282CC46B789CFCE1FCEC65D91 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "这样下去会被讨厌的……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（！？怎么看也不像是能上去搭话的样子！{w}\n怎、怎么做，要不要上去问问……）"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（……{w=0.4}算了，这种要和更加亲近的人之间商量。）"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（就算是和关系并不怎么好的我说话也只会觉得不适。{w}\n……这里只能回避。）"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000EA1

    return

label block_00000E98:
    # Node: 00000E98 (Schoolhouse)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S1Phase == 99" }]):
        jump block_00000EA2
    if judge_lm_condition([]):
        jump block_00002F45

    return

label block_00000EA2:
    # Node: 00000EA2 (Schoolhouse 作哉 point)
    $ sys_lm_menu_item = [{"pos": (360, 160),"image": "images/Chapter 2/Menu/Sakuya point.png","hover": "images/Chapter 2/Menu/Sakuya hover.png","name": "作哉"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_157
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_00000EBA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5A

    return

label block_00000EBA:
    # Node: 00000EBA (并駛之舟 2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_5FFD58FCBF734135AA883B505D03EB3E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_757DAFA361824FA590E148B0796C4A27 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊，过来，说你呢。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯？有什么事吗。"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DFF6C096971C4020B3AD59E666124B0B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "昨天关于抽烟的事，谁也不许说。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_FA0B9B4460AF4FBE8A2F85195E30819C as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "还有，告诉你家大哥他的“脑肌”挺不错的。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "“脑肌”？这是什么？"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C3058DD2310F448EBB3F52DA2113AB2E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈哈，某种表扬的词，\n赞美他一身肌肉很不错的意思。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哦、哦，好的。"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（果然这个人说话总是带刺。\n好不容易长了张还算可爱的脸，\n这下都浪费了……）"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（啊！他的话，说不定……！）"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（……嗯，肯定很合适！不过，被拒绝的可能性很高……）"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（更别说是他的话，肯定不会接受的。）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……总而言之，还是先回慎酱那里去。"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))
    pause 0.8

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.5

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    $ set_window("イベントモード")
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6EA78EC2093A46F097116A0C2CBB397C as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_3B13044431874BE09020F9368D6A8C29 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦哦！选了一个不错的突破口嘛！！"

    show rs_image_9387C2EF08BB4EFABA360A19A1E02C8B as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "要让那个傲娇君穿上女装什么的……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "吼吼，和那个性格一样，\n之后的冲击力肯定也会非常强呐～"

    show rs_image_8AF97BE15B524E50A2E2C8FC106F60FD as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "剩下的，就是该怎么拜托才会被接受了。"

    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "就用最经典的，等价交换如何？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_6EA78EC2093A46F097116A0C2CBB397C as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不错！嗯！就这么做。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_D88BEA8DA4D145D5B87F3A179B88BE87 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦、哦。"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不要不管我说什么都直接接受，真的可以？"

    show rs_image_CCE2DFCDE5EE495CB0367ED4ED7DCA8B as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "没问题！我对甜食的执念也是很深的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0725D9DCFAF4402882B4880A327CD79 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不管使用什么手段，最后一定会成功的。"

    window hide

    pause 0.65

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_D3230CCCAA744196B463EF066186F3A0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_195F518B89564C98A557F130D2E603F0

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "唔，总觉得有股不怀好意的气息……"

    window hide

    pause 0.8

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1


    if judge_lm_condition([]):
        jump block_00002C44

    return

label block_00002C44:
    # Node: 00002C44 (Phase --)
    $ C2S1Phase = C2S1Phase-1

    if judge_lm_condition([]):
        jump block_00001910

    return

label block_00001910:
    # Node: 00001910 (BGM3)
    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"


    if judge_lm_condition([]):
        jump block_00003A5A

    return

label block_00002F45:
    # Node: 00002F45 (Schoolhouse)
    $ sys_lm_menu_item = [{"pos": (360, 160),"image": "images/Chapter 2/Menu/Sakuya.png","hover": "images/Chapter 2/Menu/Sakuya hover.png","name": "作哉"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_158
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_00002F46

    return

label block_00002F46:
    # Node: 00002F46 (作哉)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_5FFD58FCBF734135AA883B505D03EB3E as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（……穗海君喜欢的东西……{w}\n唔……{w=0.45}嗯————……）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1A5E3A7F00B546FE8A7423BB9C2B93DB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "怎、怎么了。这么看着别人很糟心啊。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（啊，还是那么不留口德……）"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "穗海君好不容易有一张可爱的脸，\n不觉得这样就可惜了吗？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8C3DB2F9BABD40D396DB3B634865E972 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "诶。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "呃、这个……\n好像什么时候什么人说过这句话\n还是没说过这句话什么的……"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EB9D3849888641E78C28DA84B16F2AC8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……{w=0.4}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    extend "莫名其妙。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔……{w}\n（说了多余的话，看来我也没有指责哥哥的立场……）"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校舍内"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F45

    return

label block_00000E99:
    # Node: 00000E99 (School door)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EA3

    return

label block_00000EA3:
    # Node: 00000EA3 (School door)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (96, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "屋外トイレへ"}, {"pos": (456, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "学校看板"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_159
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外トイレへ\"" }]):
        jump block_00000EAF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学校看板\"" }]):
        jump block_00000EC1

    return

label block_00000EAF:
    # Node: 00000EAF (Outside toilet)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("室外厕所"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D5370D554F61451C806A39C7BC540968 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EB0

    return

label block_00000EB0:
    # Node: 00000EB0 (Outside toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (472, 192),"image": "images/Menu/Tokiwa.png","hover": "images/Menu/Tokiwa hover.png","name": "常磐"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_160
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000E99
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" }]):
        jump block_00000EC2

    return

label block_00000EC2:
    # Node: 00000EC2 (常磐)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_2D587EAE6EC3401995D5F3F45B1E69E1 as tag_3482C372784E44A89E382266A93F2B14 at center_bottom zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C223850065F6443080205D1F61C04C98 "最近，“伪娘”这个词突然流行起来了。\n现在的孩子们思维还真是活跃……"

    show rs_image_B7BD90C9E0F94D39B930CB8F323D6C2F as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "对于那方面的人们，\n“女装”和“伪娘”似乎还是不一样的。{w}\n这对我来说有点太难了，不是很能理解。"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外厕所"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000EB0

    return

label block_00000EC1:
    # Node: 00000EC1 (Board)
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
        jump block_00000EA3

    return

label block_00000E95:
    # Node: 00000E95 (Shoe cupboard)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000E9F

    return

label block_00000E9F:
    # Node: 00000E9F (Shoe cupboard)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_161
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_00000EA4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5A

    return

label block_00000EA4:
    # Node: 00000EA4 (Playground)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EA5

    return

label block_00000EA5:
    # Node: 00000EA5 (Playground)
    $ sys_lm_menu_item = [{"pos": (632, 208),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "体育倉庫"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_162
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000E95
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" }]):
        jump block_00000EB2

    return

label block_00000EB2:
    # Node: 00000EB2 (PE warehouse)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("体育仓库"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F36816057C4848709177D4C457D25726 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EB3

    return

label block_00000EB3:
    # Node: 00000EB3 (PE warehouse)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_163
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000EA4

    return

label block_00000E8E:
    # Node: 00000E8E (School inside)
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

    $ sys_ayumi_global_map_character = "sora"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_00000ECA

    return

label block_00000ECA:
    # Node: 00000ECA (School inside XCTX)
    if judge_lm_condition([{ "scope": 1, "content": "C2S1Phase == 99" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S1Phase == 99" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_00003A5B", target_label="block_00003A5C") from _call_scb_global_map_19
    elif judge_lm_condition([{ "scope": 1, "content": "C2S1Phase == 99" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_00003A5B", target_label="block_00003A5F") from _call_scb_global_map_20
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C2S1Phase == 99" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_00003A60", target_label="block_00003A5C") from _call_scb_global_map_21
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_00003A60", target_label="block_00003A5F") from _call_scb_global_map_22
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00000E90
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00000E91
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_00000E92
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00000E93
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00000E94
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00000E8F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00000ECA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2S1Phase == 99" }]):
        jump block_00003A5B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C2S1Phase == 99" }]):
        jump block_00003A5C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00000ECA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FAA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00003A60
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00003A5F

    return

label block_00000E90:
    # Node: 00000E90 (Aisle 2)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000E9A

    return

label block_00000E9A:
    # Node: 00000E9A (Aisle 2)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (152, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "踊り場へ"}, {"pos": (376, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "新聞部へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_164
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部へ\"" },{ "scope": 1, "content": "TalkOkajimaKojimaF1 == True" },{ "scope": 1, "content": "C2S1Phase == 98" },{ "scope": 1, "content": "TalkSaburoF1 == False" }]):
        jump block_0000242F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部へ\"" },{ "scope": 1, "content": "TalkSaburoF1 == True" }]):
        jump block_00000EAD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"踊り場へ\"" }]):
        jump block_00000EB1

    return

label block_00003A5E:
    # Node: 00003A5E (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003A5D

    return

label block_00003A5D:
    # Node: 00003A5D (TO: School inside)

    if judge_lm_condition([]):
        jump block_00000E8E

    return

label block_0000242F:
    # Node: 0000242F (Newsclub 2)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Key 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Key 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『锁着门进不去。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00000E9A

    return

label block_00000EAD:
    # Node: 00000EAD (Newsclub)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("新闻部活动室"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EAE

    return

label block_00000EAE:
    # Node: 00000EAE (Newsclub)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (112, 160),"image": "images/Chapter 2/Menu/Okajima.png","hover": "images/Chapter 2/Menu/Okajima hover.png","name": "岡島"}, {"pos": (392, 160),"image": "images/Chapter 2/Menu/Kojima.png","hover": "images/Chapter 2/Menu/Kojima hover.png","name": "小島"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_165
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000E90
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_00000EB8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_00000EB9

    return

label block_00000EB8:
    # Node: 00000EB8 (岡島)
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_6EACDBA5EB7B44D7A7699633252E6B7E as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000242E

    return

label block_0000242E:
    # Node: 0000242E (小島 event)
    window show

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.3

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（……啊！二班的小岛君！\n他肯定很适合女装的！）"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6EACDBA5EB7B44D7A7699633252E6B7E as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哦呀？赤峰君的弟弟君。找我们有事？"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "其实……\n其实是有想要和小岛君商量的事……"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A3D0E6087D6B4C4DA8B5F544E1F3B782 as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "？"

    window hide

    pause 0.5

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1.3

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.5

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_53FF68C192E3494AB005C1909579AFFB "原来如此。\n真是语不惊人死不休的挑战。{w}\n不过很有意思，我也不是不能接受。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "真、真的？非常感谢！帮大忙了！"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6BEAA3D38A204EAE8EFEE059FD541711 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "小岛君的女装……\n根本想像不出来。\n到底会是什么样呢。"

    show rs_image_07383DF7F5A94166BAD98FE0E71F4768 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "说起来从刚才就一直很在意了，\n赤峰弟弟手上拿的是什么？"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "{color=#FF00FF}假发{/color}。刚才猫山君给的。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "对了！作为练习给小岛君试一下如何？"

    window hide

    pause 0.5

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_CC4336DE74164173AC47C2C317367F10
    $ set_place_title("")
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 1

    # Gallery unlock: images/CG/Kojima-dress1.png
    $ zorder_rs_image_9E2ECBA71A44401F9A87C7DF41500965 = -100
    show rs_image_9E2ECBA71A44401F9A87C7DF41500965 as rs_image_9E2ECBA71A44401F9A87C7DF41500965 zorder zorder_rs_image_9E2ECBA71A44401F9A87C7DF41500965 onlayer master
    hide rs_image_9E2ECBA71A44401F9A87C7DF41500965

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_9E2ECBA71A44401F9A87C7DF41500965 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    # Gallery unlock: images/CG/Kojima-dress2.png
    $ zorder_rs_image_ACC7BF001A154359B4A9C008A8F9B628 = -100
    show rs_image_ACC7BF001A154359B4A9C008A8F9B628 as rs_image_ACC7BF001A154359B4A9C008A8F9B628 zorder zorder_rs_image_ACC7BF001A154359B4A9C008A8F9B628 onlayer master
    hide rs_image_ACC7BF001A154359B4A9C008A8F9B628

    show rs_image_ACC7BF001A154359B4A9C008A8F9B628 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 0.7

    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/The hope.ogg":
        play music "sound/BGM/The hope.ogg" loop
        $ sys_music_current_file = "sound/BGM/The hope.ogg"

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哇♪好可爱！不管怎么看都是女孩子哦！"

    rs_character_53FF68C192E3494AB005C1909579AFFB "是嘛，谢谢。"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "比、比想像中变化还大啊……唔。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "只要再换好衣服就完美了！这个样子就算不化妆也没关系哦！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "当天拜托了！好期待呐～♪"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "唔……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    extend "…………不、不行！！这次作为新闻部部长我不允许！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "诶诶？！为、为何？"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "那个……怎么说……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "总、总之就是不行！\n不许把这个样子的小岛君暴露在公众视线下！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "怎、怎么这样……！"

    rs_character_53FF68C192E3494AB005C1909579AFFB "嘛——"

    rs_character_53FF68C192E3494AB005C1909579AFFB "抱歉赤峰君，不知为何部长不愿意呐。这件事就这么算了吧。"

    window hide

    pause 0.8

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ set_window("(標準)")
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.6

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    window show

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊——啊，被赶出来了。{w}\n算了，找其他人去。"

    window hide

    $ set_place_title(_("二楼走廊"))
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002C47

    return

label block_00002C47:
    # Node: 00002C47 (T -> T)
    $ TalkOkajimaKojimaF1 = True

    if judge_lm_condition([]):
        jump block_00000E9A

    return

label block_00000EB9:
    # Node: 00000EB9 (小島)
    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000242E

    return

label block_00000EB1:
    # Node: 00000EB1 (Playground)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("楼梯间"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000EE3

    return

label block_00000EE3:
    # Node: 00000EE3 (Playground)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_166
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000E90

    return

label block_00000E91:
    # Node: 00000E91 (Roof)
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

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S1Phase == 99" },{ "scope": 1, "content": "TalkSaburoF1 == True" }]):
        jump block_00002F42
    if judge_lm_condition([{ "scope": 0, "content": "C2S1Phase == 99" }]):
        jump block_0000242D
    if judge_lm_condition([]):
        jump block_00000E9B

    return

label block_00002F42:
    # Node: 00002F42 (Roof empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_167
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5E

    return

label block_0000242D:
    # Node: 0000242D (Roof)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (264, 160),"image": "images/Chapter 2/Menu/Saburo.png","hover": "images/Chapter 2/Menu/Saburo hover.png","name": "三朗"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_168
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_0000242C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5E

    return

label block_0000242C:
    # Node: 0000242C (三朗)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_68F81BC3017742E799ED8AE7F25D401B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊——嗯嗯——？\n在找适合穿女装的家伙——？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_14CD0F42E7E7472DA340494245426445 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "意义不明，理解不能。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_48F9BE60F5244821B20C0F50155C0114 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "说是这么说，我还是乐于助人的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_62D35A6C85144BF796E08D1132E03CA7 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "来，小兄弟，拿好这个{color=#FF00FF}假发{/color}。{w}\n找个看着还行的人扣上去\n看看咋样就行了。"

    show rs_image_8F0ABED26B9142DE9C9E509E0AE738E6 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那，加油了。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("屋顶"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002C46

    return

label block_00002C46:
    # Node: 00002C46 (T -> T)
    $ TalkSaburoF1 = True

    if judge_lm_condition([]):
        jump block_00002F42

    return

label block_00000E9B:
    # Node: 00000E9B (Roof 三朗 point)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (264, 160),"image": "images/Chapter 2/Menu/Saburo point.png","hover": "images/Chapter 2/Menu/Saburo hover.png","name": "三朗"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_169
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_00000EBB

    return

label block_00000EBB:
    # Node: 00000EBB (三朗)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_40479E0C330041AC8509957328C06B21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_72F7100FF0804EEE980DC61BF9E3B2A0 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "穗海喜欢的东西？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_8F0ABED26B9142DE9C9E509E0AE738E6 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那种事儿，当然，\n肯定是对白痴呆毛的{w=0.4}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Waoh 1.ogg"

    show rs_image_8F0ABED26B9142DE9C9E509E0AE738E6 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "{size=24}{color=#FF0080}『爱』{/color}{/size}。"

    show rs_image_48F9BE60F5244821B20C0F50155C0114 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我也得给那家伙的恋爱加油啊♪"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("屋顶"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001927

    return

label block_00001927:
    # Node: 00001927 (選擇)
    call scb_selector(_("要采纳这个意见吗？"), [{"name":"参考にする", "content":_("可以")}, {"name":"参考にしない", "content":_("明显不行")}]) from _call_scb_selector_8

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"参考にしない\"" }]):
        jump block_00000E9B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"参考にする\"" }]):
        jump block_00001913

    return

label block_00001913:
    # Node: 00001913 (Wrong)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好的，就以这个为基础与穗海君交涉！"

    window hide

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    with rs_effect_8835C10B7CA8414B824EA2190042A792

    pause 1

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_5A7F5C8B6FD54332874DDE552BDE0C4D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    pause 0.15

    show rs_image_C2C1144118BB4361A1A71D2CA3C86C7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_29AA11E0CF3E427CAE25F425D5D19C08 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_E9E1E58492594DC0BCC92CA9299E318F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_57AADDFB9FD64F1D97E9A335DECC2B16 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    show rs_image_5A7F5C8B6FD54332874DDE552BDE0C4D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_C2C1144118BB4361A1A71D2CA3C86C7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_29AA11E0CF3E427CAE25F425D5D19C08 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_E9E1E58492594DC0BCC92CA9299E318F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_57AADDFB9FD64F1D97E9A335DECC2B16 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    stop effect2 fadeout 0.6
    $ sys_effect2_current_file = ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 200
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_02CC0EBCB4BD407082D06D6C95D57796 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_241AF4B67B0B4452B97B2944C6D13AFE zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("イベントモード")
    pause 0.4

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "绝对不————干！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_F59CF92171C0495BA4E334AC96BA8B63 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_F07A39EE5E0349388B25FF826142935C as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……看来不行啊……再换一个。"

    window hide

    pause 0.3

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.5


    if judge_lm_condition([]):
        jump block_00001910

    return

label block_00000E92:
    # Node: 00000E92 (Music room)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S1Phase == 99" }]):
        jump block_00001FE9
    if judge_lm_condition([]):
        jump block_00000E9C

    return

label block_00001FE9:
    # Node: 00001FE9 (Music room)
    $ sys_lm_menu_item = [{"pos": (432, 184),"image": "images/Chapter 2/Menu/Tomo music room.png","hover": "images/Chapter 2/Menu/Tomo music room hover.png","name": "友"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_170
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友\"" }]):
        jump block_00001FE8

    return

label block_00001FE8:
    # Node: 00001FE8 (友)
    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_8F83EC71B001467B872FED4ED3234658 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（啊，友君应该很适合女装！\n气氛也不错，似乎是能接受的样子。）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君，那个，\n我有一件想要拜托的事……"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_161861BE26EE4669A63E9B716A605EB3 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦？什么什么？友A梦不管什么都会听的哦。"

    window hide

    pause 0.5

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1.3

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.5

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……就是这样……{w}可以吗？"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_24C711A2BE52475F8507DA19607EEE0E as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友、友君的话肯定很合适的。\n一定能开心地度过这段时间的。"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_EAA37886FF234C5AB35992304EE98E9B as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    extend "不要！\n{w=0.6}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_695C24CD86734F19B914C47F42DDAF6F as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "绝对不要！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "咦！为、为什么。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_577EB13059BE43C7AD7A57B57B489B3F as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不要就是不要——！{w}\n女装的话空自己来不就好了嘛——"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我、我肯定不合适的。所以才会来拜托友君……"

    if sys_music2_current_file != "sound/Effect Sound/Strike 1.ogg":
        play music2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Strike 1.ogg"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（唔……有些意外，继续强求也不好。{w}\n找其他人好了。）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("音乐室"))

    if judge_lm_condition([]):
        jump block_00001FE9

    return

label block_00000E9C:
    # Node: 00000E9C (Music room empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_171
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5E

    return

label block_00000E93:
    # Node: 00000E93 (Library)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S1Phase == 99" }]):
        jump block_00001FEA
    if judge_lm_condition([]):
        jump block_00000E9D

    return

label block_00001FEA:
    # Node: 00001FEA (Library)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 2/Menu/Shinobu.png","hover": "images/Chapter 2/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_172
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00001FEB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5E

    return

label block_00001FEB:
    # Node: 00001FEB (忍 1)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_22306BD9E0624D81A1CFFFB486C5BAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（果然这次也只能啊拜托忍君……！）"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（……{w=0.45}……还是算了。\n{color=#008080}之前那件事{/color}真的令他很失落，{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 400
    show rs_image_4BE5CE14EA26458EB355BEA5CC395BF4 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""
    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "都快变成心灵创伤了。）"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "（……必须找其他人。）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C2A28861C0A44DC6AAE17E0ABA1BE61C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00001FEA

    return

label block_00000E9D:
    # Node: 00000E9D (Library 友 point)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 2/Menu/Shinobu.png","hover": "images/Chapter 2/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (488, 179),"image": "images/Chapter 2/Menu/Tomo library point.png","hover": "images/Chapter 2/Menu/Tomo library hover.png","name": "友"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_173
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000010FA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友\"" }]):
        jump block_000010FB

    return

label block_000010FA:
    # Node: 000010FA (忍 2)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A43C35FAF6E4488E87E8829D5D8E84E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "穗海君喜欢的东西？\n"
    show rs_image_C2A28861C0A44DC6AAE17E0ABA1BE61C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不，我并不了解。\n友，你有什么头绪？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_695C24CD86734F19B914C47F42DDAF6F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不知道不知道不知道——！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_F3E109E6C4624269B4F22936B1279BBF as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "真是的，消停消停。\n"
    show rs_image_9133C483CCA9460C804D7FCD561DE619 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "抱歉，所以我们并不清楚。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00000E9D

    return

label block_000010FB:
    # Node: 000010FB (友)
    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_8F83EC71B001467B872FED4ED3234658 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_A28CBCA902704F978F416697C605F321 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶——技安喜欢的东西？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_695C24CD86734F19B914C47F42DDAF6F as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我怎么可能知道那种家伙喜欢的东西！\n哼——！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w=0.45}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_A28CBCA902704F978F416697C605F321 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，不过，之前，\n他好像说过想要狗用防寒套装来着……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00001926

    return

label block_00001926:
    # Node: 00001926 (選擇)
    call scb_selector(_("要采纳这个意见吗？"), [{"name":"参考にする", "content":_("可以")}, {"name":"参考にしない", "content":_("明显不行")}]) from _call_scb_selector_9

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"参考にしない\"" }]):
        jump block_00000E9D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"参考にする\"" }]):
        jump block_00001912

    return

label block_00001912:
    # Node: 00001912 (Success)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好的，就以这个为基础与穗海君交涉！"

    window hide

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    with rs_effect_8835C10B7CA8414B824EA2190042A792

    pause 1

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_5A7F5C8B6FD54332874DDE552BDE0C4D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    pause 0.15

    show rs_image_C2C1144118BB4361A1A71D2CA3C86C7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_29AA11E0CF3E427CAE25F425D5D19C08 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_E9E1E58492594DC0BCC92CA9299E318F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_57AADDFB9FD64F1D97E9A335DECC2B16 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    show rs_image_5A7F5C8B6FD54332874DDE552BDE0C4D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_C2C1144118BB4361A1A71D2CA3C86C7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_29AA11E0CF3E427CAE25F425D5D19C08 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_E9E1E58492594DC0BCC92CA9299E318F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.15

    show rs_image_57AADDFB9FD64F1D97E9A335DECC2B16 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    stop effect2 fadeout 0.6
    $ sys_effect2_current_file = ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Correct 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Correct 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_64C987B3866E43999077769BDA7EB8C7 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 1.5

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_33B29DADC6B34A568FACE045089AA837

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    pause 2


    if judge_lm_condition([]):
        jump block_00003A62

    return

label block_00003A62:
    # Node: 00003A62 ()
    $ del TalkIzuKatoMatsuF1
    $ del TalkSaburoF1
    $ del TalkOkajimaKojimaF1

    return

label block_00000E94:
    # Node: 00000E94 (Toilet)
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
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_297E564A7C1544469FB88A41AB85B6C9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000E9E

    return

label block_00000E9E:
    # Node: 00000E9E (Toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (224, 184),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "トイレ個室"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_174
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A5E
    if judge_lm_condition([]):
        jump block_00000EBF

    return

label block_00000EBF:
    # Node: 00000EBF (Toilet single)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("厕所单间"))
    pause 0.3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1C833F0E5AB54E79BCEE6017035686BE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0


    if judge_lm_condition([]):
        jump block_00000EC0

    return

label block_00000EC0:
    # Node: 00000EC0 (Toilet single)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_175
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000E94

    return

label block_00003A5B:
    # Node: 00003A5B (Conversation 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不愧是慎酱！很不错的建议嘛♪"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "女装啊……谁最合适呢。"

    window hide

    $ set_window("(標準)")

    return

label block_00003A5C:
    # Node: 00003A5C (Target 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『找到适合女装的人。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FAA:
    # Node: 00001FAA (Character)
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

label block_00003A60:
    # Node: 00003A60 (Conversation 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "送东西引诱别人上钩，好像不是很厚道……"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "为了甜食！强硬一些也没关系的♪"

    window hide

    $ set_window("(標準)")

    return

label block_00003A5F:
    # Node: 00003A5F (Target 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『与知道穗海作哉喜欢什么的人谈话，\n再决定是否要参考他们的意见。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001917:
    # Node: 00001917 (Target 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『找到适合女装的人。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001918:
    # Node: 00001918 (Conversation 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不愧是慎酱！很不错的建议嘛♪"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "女装啊……谁最合适呢。"

    window hide

    $ set_window("(標準)")

    return

label block_00001FA9:
    # Node: 00001FA9 (Character)
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

label block_0000191E:
    # Node: 0000191E (Conversation 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "送东西引诱别人上钩，好像不是很厚道……"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "为了甜食！强硬一些也没关系的♪"

    window hide

    $ set_window("(標準)")

    return

label block_0000191D:
    # Node: 0000191D (Target 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『与知道穗海作哉喜欢什么的人谈话，\n再决定是否要参考他们的意见。』{/color}"

    window hide

    $ set_window("(標準)")

    return

