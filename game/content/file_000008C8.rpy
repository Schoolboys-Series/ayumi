# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000008C8 (CP2 Daytime)

label block_000008C9:
    # Node: 000008C9 (開始)
    $ PianoRandom = 0

    if judge_lm_condition([]):
        jump block_000008CC

    return

label block_000008CC:
    # Node: 000008CC (School outside)
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


    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase > 0" }]):
        jump block_000018C7
    if judge_lm_condition([]):
        jump block_000018C6

    return

label block_000018C7:
    # Node: 000018C7 (BGM 2)
    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"


    if judge_lm_condition([]):
        jump block_000018C2

    return

label block_000018C2:
    # Node: 000018C2 (友)
    $ sys_ayumi_global_map_character = "tomo"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" }]):
        jump block_000018C5
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase == 1" },{ "scope": 0, "content": "C2S4Phase == 1" }]):
        jump block_0000093B
    if judge_lm_condition([{ "scope": 0, "content": "C2S1Phase == 1" },{ "scope": 0, "content": "C2S6Phase == 1" }]):
        jump block_00000A02
    if judge_lm_condition([]):
        jump block_000008CE

    return

label block_000018C5:
    # Node: 000018C5 (School outside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_000018CF", target_label="block_000018CE") from _call_scb_global_map_115
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00003A38
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_00003A03
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00003A2D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00003A3B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00003A04
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00003A3C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_000018C5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000018CF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_000018CE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_000018C5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FB9

    return

label block_00003A38:
    # Node: 00003A38 (TO: Shoe cupboard)

    if judge_lm_condition([]):
        jump block_000008D4

    return

label block_000008D4:
    # Node: 000008D4 (Shoe cupboard)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "SYSReviewMode == True" }]):
        jump block_000031C1
    if judge_lm_condition([{ "scope": 0, "content": "C2SG1 == True" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 1, "content": "TalkNamekoF2 == 0" }]):
        jump block_000008DE
    if judge_lm_condition([]):
        jump block_00001F21

    return

label block_000031C1:
    # Node: 000031C1 (Shoe cupboard 觸手A)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}, {"pos": (216, 184),"image": "images/Menu/Tentacle-earthworm.png","hover": "images/Menu/Tentacle-earthworm hover.png","name": "触手A"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_452
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手A\"" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" }]):
        jump block_000031C0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手A\"" }]):
        jump block_00003288
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_000008E3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A31

    return

label block_000031C0:
    # Node: 000031C0 (触手A)
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 200
    show rs_image_5171C4277664485482367CFD06553623 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_FB87619C890441AEA41E279A1B588CAC "你想要从梦中醒来，回到现实吗？"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))

    if judge_lm_condition([]):
        jump block_000031BF

    return

label block_000031BF:
    # Node: 000031BF (選擇)
    call scb_selector("", [{"name":"はい", "content":_("嗯，我要回去")}, {"name":"いいえ", "content":_("再等一会")}]) from _call_scb_selector_43

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_000031C1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003A37

    return

label block_00003A37:
    # Node: 00003A37 ()
    $ del PianoRandom

    return

label block_00003288:
    # Node: 00003288 (触手A 劇情中)
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
        jump block_000031C1

    return

label block_000008E3:
    # Node: 000008E3 (Playground)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 1, "content": "TalkKatouF2 == 0" }]):
        jump block_00001F4A
    if judge_lm_condition([]):
        jump block_000008E4

    return

label block_00001F4A:
    # Node: 00001F4A (Playground 加藤 point)
    $ sys_lm_menu_item = [{"pos": (328, 140),"image": "images/Chapter 2/Menu/F2/Katou point.png","hover": "images/Chapter 2/Menu/Katou hover.png","name": "加藤"}, {"pos": (632, 208),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "体育倉庫"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_453
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" }]):
        jump block_000008F9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008D4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" }]):
        jump block_00001F49

    return

label block_000008F9:
    # Node: 000008F9 (PE warehouse)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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


    if judge_lm_condition([]):
        jump block_000008FA

    return

label block_000008FA:
    # Node: 000008FA (PE warehouse)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_454
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008E3

    return

label block_00001F49:
    # Node: 00001F49 (加藤 F2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_CF9552A127F84B139910618B1FE71819 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_81D16F74A3C44B8982DB528D7D934850 "怎么了班长。"

    pause 0.3

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『听取了加藤的意见』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『用并不怎么有趣的{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "{color=#0080FF}{/color}{u}{color=#FF0000}大把无所谓的言论{/color}{/u}{color=#0080FF}尝试说服。』{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001F47

    return

label block_00001F47:
    # Node: 00001F47 (選擇)
    call scb_selector(_("这种意见可否？"), [{"name":"はい", "content":_("就是这个")}, {"name":"いいえ", "content":_("太微妙了，算了")}]) from _call_scb_selector_44

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00001F4A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002C6E

    return

label block_00002C6E:
    # Node: 00002C6E (TF2)
    $ TalkKatouF2 = 1

    if judge_lm_condition([]):
        jump block_00003A33

    return

label block_00003A33:
    # Node: 00003A33 (FLAG: CP2F2)
    call block_00003A0E from _call_block_00003A0E

    if judge_lm_condition([]):
        jump block_00003A34

    return

label block_00003A34:
    # Node: 00003A34 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A31

    return

label block_00003A31:
    # Node: 00003A31 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A09

    return

label block_00003A09:
    # Node: 00003A09 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A07

    return

label block_00003A07:
    # Node: 00003A07 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A06

    return

label block_00003A06:
    # Node: 00003A06 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A05

    return

label block_00003A05:
    # Node: 00003A05 (TO: School outside)

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 20" },{ "scope": 1, "content": "VarExists(\"C2S2Phase\") == False" }]):
        jump block_00003C82
    if judge_lm_condition([{ "scope": 0, "content": "VarExists(\"C2QNewsclubRedirect\") == True" }]):
        jump block_00003CE1
    if judge_lm_condition([]):
        jump block_000008CC

    return

label block_00003C82:
    # Node: 00003C82 ()
    $ del PianoRandom

    return

label block_00003CE1:
    # Node: 00003CE1 (Check: Newsclub)

    if judge_lm_condition([{ "scope": 0, "content": "C2QNewsclubRedirect == True" }]):
        jump block_00003ACD
    if judge_lm_condition([]):
        jump block_000008CC

    return

label block_00003ACD:
    # Node: 00003ACD (TO: Newsclub)

    if judge_lm_condition([]):
        jump block_00002F24

    return

label block_00002F24:
    # Node: 00002F24 (Cancel: Redirect)
    $ del C2QNewsclubRedirect

    if judge_lm_condition([]):
        jump block_00002511

    return

label block_00002511:
    # Node: 00002511 (Newsclub)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (112, 160),"image": "images/Chapter 2/Menu/Okajima.png","hover": "images/Chapter 2/Menu/Okajima hover.png","name": "岡島"}, {"pos": (392, 160),"image": "images/Chapter 2/Menu/Kojima.png","hover": "images/Chapter 2/Menu/Kojima hover.png","name": "小島"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_455
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A97
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" },{ "scope": 1, "content": "C2QNewsclubPhase == 1" }]):
        jump block_0000250A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_0000250B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" },{ "scope": 1, "content": "TalkOkajima == 0" }]):
        jump block_0000250D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_0000250C

    return

label block_00003A97:
    # Node: 00003A97 (TO: Aisle 2)

    if judge_lm_condition([]):
        jump block_00003A8E

    return

label block_00003A8E:
    # Node: 00003A8E (TO: Aisle 2)

    if judge_lm_condition([]):
        jump block_00003A8D

    return

label block_00003A8D:
    # Node: 00003A8D (TO: Aisle 2)

    if judge_lm_condition([]):
        jump block_000008CF

    return

label block_000008CF:
    # Node: 000008CF (Aisle 2)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
        jump block_000008D9

    return

label block_000008D9:
    # Node: 000008D9 (Aisle 2)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (152, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "踊り場へ"}, {"pos": (376, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "新聞部へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_456
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A8C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部へ\"" },{ "scope": 1, "content": "C2QNewsclubPhase == 1" },{ "scope": 2, "content": "C2S2Phase == 0" }]):
        jump block_00002518
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部へ\"" },{ "scope": 1, "content": "FNewsclub == True" },{ "scope": 2, "content": "C2S2Phase == 0" }]):
        jump block_00002C84
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部へ\"" }]):
        jump block_00002514
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"踊り場へ\"" }]):
        jump block_000008F7

    return

label block_00003A8C:
    # Node: 00003A8C (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003A8B

    return

label block_00003A8B:
    # Node: 00003A8B (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003A3D

    return

label block_00003A3D:
    # Node: 00003A3D (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003AC8

    return

label block_00003AC8:
    # Node: 00003AC8 (TO: School inside)

    if judge_lm_condition([]):
        jump block_000008CB

    return

label block_000008CB:
    # Node: 000008CB (School inside)
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


    if judge_lm_condition([]):
        jump block_000018C3

    return

label block_000018C3:
    # Node: 000018C3 (友)
    $ sys_ayumi_global_map_character = "tomo"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" }]):
        jump block_000018C4
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase == 1" },{ "scope": 0, "content": "C2S4Phase == 1" }]):
        jump block_0000093A
    if judge_lm_condition([{ "scope": 0, "content": "C2S1Phase == 1" },{ "scope": 0, "content": "C2S6Phase == 1" }]):
        jump block_00000A03
    if judge_lm_condition([]):
        jump block_000008CD

    return

label block_000018C4:
    # Node: 000018C4 (School inside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_00003ACE", target_label="block_00003ACF") from _call_scb_global_map_116
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00003A8D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00003A9E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_00003A84
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00003AC7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00003ABD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00003ACC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_000018C4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00003ACE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00003ACF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_000018C4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FBA

    return

label block_00003A9E:
    # Node: 00003A9E (TO: Roof)

    if judge_lm_condition([]):
        jump block_000008D0

    return

label block_000008D0:
    # Node: 000008D0 (Roof)
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

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" }]):
        jump block_0000090B
    if judge_lm_condition([{ "scope": 0, "content": "CXQSabuImechen == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C2S4 == True" }]):
        jump block_00002CC4
    if judge_lm_condition([{ "scope": 0, "content": "C2S4 == True" }]):
        jump block_0000254F
    if judge_lm_condition([{ "scope": 0, "content": "C2S4Phase == 1" }]):
        jump block_00000A12
    if judge_lm_condition([{ "scope": 0, "content": "CXQSabuImechen == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" }]):
        jump block_00002763
    if judge_lm_condition([]):
        jump block_000008DA

    return

label block_0000090B:
    # Node: 0000090B (Roof empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_457
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A99

    return

label block_00003A99:
    # Node: 00003A99 (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003A8B

    return

label block_00002CC4:
    # Node: 00002CC4 (Roof 慎太郎 三朗 quest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 160),"image": "images/Chapter 2/Menu/Saburo quest.png","hover": "images/Chapter 2/Menu/Saburo hover.png","name": "三朗"}, {"pos": (104, 160),"image": "images/Chapter 2/Menu/Shintaro roof.png","hover": "images/Chapter 2/Menu/Shintaro roof hover.png","name": "慎太郎"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_458
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A9A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_0000252A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00002ED7

    return

label block_00003A9A:
    # Node: 00003A9A (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003A99

    return

label block_0000252A:
    # Node: 0000252A (三朗美髮店 1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_40479E0C330041AC8509957328C06B21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_D0ED4462025945CB876E95E9B02C154A as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那个，白痴呆毛～♪{w}\n有件事想拜托你，能听听不～？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么——什么事——？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2F053DD5EF4C49B388E430ED01FE5A69 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "给我弄弄……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呃、呃？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shock 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_14CD0F42E7E7472DA340494245426445 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_948E8AC6EDB8420188E805D9D94D89F9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
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
        jump block_00003A9B

    return

label block_00003A9B:
    # Node: 00003A9B (PREPAR)
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
        jump block_00003A9C

    return

label block_00003A9C:
    # Node: 00003A9C (三朗美髮店)
    call block_00001194 from _call_block_00001194_3

    if judge_lm_condition([]):
        jump block_00003A9D

    return

label block_00003A9D:
    # Node: 00003A9D (RESET)
    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_000008D0

    return

label block_00002ED7:
    # Node: 00002ED7 (慎太郎筆記)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_FD2C0CA41CDB4FD99334DB3AB5756355 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{color=#008A45}人物详细笔记{/color}，要看吗？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("屋顶"))
    window hide


    if judge_lm_condition([]):
        jump block_00002ED8

    return

label block_00002ED8:
    # Node: 00002ED8 (選擇)
    call scb_selector("", [{"name":"はい", "content":_("看")}, {"name":"いいえ", "content":_("不想看")}]) from _call_scb_selector_45

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002ED9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" },{ "scope": 1, "content": "CXQSabuImechen == False" },{ "scope": 2, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 3, "content": "C2S4 == True" }]):
        jump block_00002CC4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_0000254F

    return

label block_00002ED9:
    # Node: 00002ED9 (PREPARE)
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0


    if judge_lm_condition([]):
        jump block_00002EDA

    return

label block_00002EDA:
    # Node: 00002EDA (慎太郎筆記)
    $ renpy.block_rollback()
    call screen shintarou_notebook()

    if judge_lm_condition([]):
        jump block_00003780

    return

label block_00003780:
    # Node: 00003780 (RESET)
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000008D0

    return

label block_0000254F:
    # Node: 0000254F (Roof 慎太郎)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 160),"image": "images/Chapter 2/Menu/Saburo.png","hover": "images/Chapter 2/Menu/Saburo hover.png","name": "三朗"}, {"pos": (104, 160),"image": "images/Chapter 2/Menu/Shintaro roof.png","hover": "images/Chapter 2/Menu/Shintaro roof hover.png","name": "慎太郎"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_459
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A9F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" },{ "scope": 1, "content": "TalkSaburoF6After == True" }]):
        jump block_000025FE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" },{ "scope": 1, "content": "TalkShintaroF6After == True" }]):
        jump block_00002600
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" },{ "scope": 1, "content": "TalkSaburoF4After == True" }]):
        jump block_00002550
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" },{ "scope": 1, "content": "TalkShintaroF4After == True" }]):
        jump block_00002552
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" },{ "scope": 1, "content": "CXQSabuImechen == False" }]):
        jump block_00002EE7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_0000252B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00002ED7

    return

label block_00003A9F:
    # Node: 00003A9F (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003A99

    return

label block_000025FE:
    # Node: 000025FE (慎太郎 F6后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_888F059A76394ED3AA6121005A67D206 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000025FF

    return

label block_000025FF:
    # Node: 000025FF (F6后)
    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_402B3A34DCAC41AD846641A233A33DED as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呀——真是不错的旅行呐。能再去一次就好了～"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_A0B1A1AC4435401CBBA1DCA96F7AFD50 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "拜此所赐没法专心回到学习了。\n一直在发呆。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……。{w}呐——你们两个，\n{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "在酒店的时候做过{w=0.35}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Gun 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Gun 1.ogg"

    extend "{color=#FF00FF}○○○{/color}了没有？"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_48C5F16710344F4F8A8167B1D88A30CD as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-180, yalign=1.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_341ABC40D2704A7A868A7B5314969CB9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=170, yalign=1.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}{color=#FF8000}慎太郎：不——告——诉——你——！{/color}{/size}\n{size=28}{color=#0080C0}三朗：天——知——道——！！{/color}{/size}"

    window hide

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("屋顶"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002CC3

    return

label block_00002CC3:
    # Node: 00002CC3 (END: TalkF6After)
    $ TalkSaburoF6After = False
    $ TalkShintaroF6After = False

    if judge_lm_condition([{ "scope": 0, "content": "CXQSabuImechen == False" }]):
        jump block_00002CC4
    if judge_lm_condition([]):
        jump block_0000254F

    return

label block_00002600:
    # Node: 00002600 (三朗 F6后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_40479E0C330041AC8509957328C06B21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000025FF

    return

label block_00002550:
    # Node: 00002550 (三朗 F4后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_40479E0C330041AC8509957328C06B21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000009E0

    return

label block_000009E0:
    # Node: 000009E0 (F4后)
    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "慎酱和猫君。\n{w=0.5}……啊，难道我打扰你们了？"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_402B3A34DCAC41AD846641A233A33DED as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不需要你多做关心。你也过来。"

    window hide

    pause 0.6

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    $ set_window("イベントモード")
    stop music fadeout 1.5
    $ sys_music_current_file = ""

    pause 1.5

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg"

    pause 0.8

    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那个～上次体育课那会真是对不起了。"

    show rs_image_35B9BEFBF42E474DB41387E9345C36B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没事的，我说的有些太不吉利了。"

    show rs_image_A15B5B9C211846009204F1689FC8781E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那件事我也听说了，三酱奇袭友亲。"

    show rs_image_46B09605979B44EBA877032E0832F21E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "友亲做的当然不太对，但实话说我还是很高兴的。"

    show rs_image_350F6A2B48EE49C8B631CE0B02F5BC2C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "毕竟那就说明猫君到底是多为慎酱着想了呢。"

    show rs_image_C5F31BAC461D43B9A8E59CAB2E60793D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈哈——就是就是。"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 200
    $ zorder_tag_24B3A49A9E5E4F6283DD3ADAF445EC35 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at right_top zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    show rs_image_08C43A31F7C049DDB885DFB2FB7A471D as tag_24B3A49A9E5E4F6283DD3ADAF445EC35 at left_top zorder zorder_tag_24B3A49A9E5E4F6283DD3ADAF445EC35 onlayer master
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说起来，我不是开玩笑的，\n我去医院看了没问题，可友亲如何？"

    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔，没、没问题的。我又不像慎酱那么重口。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_9387C2EF08BB4EFABA360A19A1E02C8B as tag_24B3A49A9E5E4F6283DD3ADAF445EC35 zorder zorder_tag_24B3A49A9E5E4F6283DD3ADAF445EC35 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "真的？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真的！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_24B3A49A9E5E4F6283DD3ADAF445EC35
    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "白痴呆毛，你也……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "真是的！你们两个都太不检点了！！"

    show rs_image_BE8486E53367484D8879711D82BE0D21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "下次要是被我知道，就等着重重的惩罚好了。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_350F6A2B48EE49C8B631CE0B02F5BC2C as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "他这么说哦，慎酱♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_4D1311D27FDA4670AB1582678631B9C9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你也是，白痴呆毛。要是被我知道，\n你就等着被你们班那个会空手道的教训好了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_E1E1F08446C54DCAAC86BEA1B671549E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫！只、只有这个请饶了我～！"

    show rs_image_46B09605979B44EBA877032E0832F21E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不用担心，我再也不会那样做了。\n再怎么说，我已经有重要的人了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦，哦。这样。有好好负起责任呢。当然我也会的。"

    show rs_image_7D82D2EF95ED49EA821B9751FF70275C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "切，真好啊。我也想要那种能谈情说爱的对象啊——"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_2E376F844FB64EF7B7A9097279B923E6 "不是有电摩嘛。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_CA176C5A71144199A2E3AE0C60846C57 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对对♪是只有一个按钮还能好好安慰我的亲爱的……\n{w=0.55}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_E7E6E31C347642E086AADC4895CE778C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不对！！"

    window hide

    pause 0.8

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 1.3

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_00002CC2

    return

label block_00002CC2:
    # Node: 00002CC2 (END: TalkF4After)
    $ TalkSaburoF4After = False
    $ TalkShintaroF4After = False

    if judge_lm_condition([]):
        jump block_00003AA1

    return

label block_00003AA1:
    # Node: 00003AA1 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A96

    return

label block_00003A96:
    # Node: 00003A96 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A95

    return

label block_00003A95:
    # Node: 00003A95 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A90

    return

label block_00003A90:
    # Node: 00003A90 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A39

    return

label block_00003A39:
    # Node: 00003A39 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A31

    return

label block_00002552:
    # Node: 00002552 (慎太郎 F4后)
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_888F059A76394ED3AA6121005A67D206 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000009E0

    return

label block_00002EE7:
    # Node: 00002EE7 (三朗美髮店前)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_D0ED4462025945CB876E95E9B02C154A as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那个啊白痴呆毛～♪{w}\n有件事想让你干～……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "抱歉，现在正忙！下次好了！"

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_68F81BC3017742E799ED8AE7F25D401B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸——！……算了，等会记得回来啊。"

    window hide

    $ set_place_title(_("屋顶"))
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "C2S4 == True" }]):
        jump block_0000254F
    if judge_lm_condition([]):
        jump block_000008DA

    return

label block_000008DA:
    # Node: 000008DA (Roof)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (264, 160),"image": "images/Chapter 2/Menu/Saburo.png","hover": "images/Chapter 2/Menu/Saburo hover.png","name": "三朗"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_460
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A99
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" },{ "scope": 1, "content": "CXQSabuImechen == True" }]):
        jump block_0000252B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_00002EE7

    return

label block_0000252B:
    # Node: 0000252B (三朗美髮店2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_40479E0C330041AC8509957328C06B21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "要转换形象么？"

    window hide

    $ set_place_title(_("屋顶"))
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_0000252C

    return

label block_0000252C:
    # Node: 0000252C (選擇)
    call scb_selector("", [{"name":"はい", "content":_("换！换！我要换！")}, {"name":"いいえ", "content":_("容我三思")}]) from _call_scb_selector_46

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003A9B
    if judge_lm_condition([{ "scope": 0, "content": "C2S4 == True" },{ "scope": 1, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_0000254F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_000008DA

    return

label block_00000A12:
    # Node: 00000A12 (Roof 三朗 flag)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (264, 160),"image": "images/Chapter 2/Menu/Saburo flag.png","hover": "images/Chapter 2/Menu/Saburo hover.png","name": "三朗"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_461
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A9A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_00000A13

    return

label block_00000A13:
    # Node: 00000A13 (三朗 F4)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cat 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cat 3.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_7F497F24D349433FB39C83C619E61AB8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cat 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cat 2.ogg"

    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cat 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cat 1.ogg"

    show rs_image_AB6075791E544455A4C21B3DCBA52E1C as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀！？为什么会有这么多猫！？"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 100
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_68F81BC3017742E799ED8AE7F25D401B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦……白痴呆毛……{w}对不住，我正在午休。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "所以很抱歉，但你就别管了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、我是无所谓，但这些猫是？？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_14CD0F42E7E7472DA340494245426445 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "保护我睡觉的光荣的战士们。"

    show rs_image_8F0ABED26B9142DE9C9E509E0AE738E6 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你运气算好的，要是再前进一步，\n你……知道会有什么下场么？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呵呵！不就是一堆猫，\n怎么可能打赢我森海大人！"

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_09195950F8394809A0869961F681F32D "喵！！（猫拳）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 100
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CBFB350257CD4F1A9A0611CD76675A37 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我都警告过了。那晚安。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("屋顶"))
    pause 0.9

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_40D222D1934C4461A67407D10A843432

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003AB7

    return

label block_00003AB7:
    # Node: 00003AB7 (FLAG: CP2F4)
    call block_00003AA3 from _call_block_00003AA3

    if judge_lm_condition([]):
        jump block_00003AB9

    return

label block_00003AB9:
    # Node: 00003AB9 (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#008A45}“我是直的，现无对象”{/color}{color=#0080FF}成功结束。』{/color}"

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
        jump block_00003AA1

    return

label block_00002763:
    # Node: 00002763 (Roof 三朗 quest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (264, 160),"image": "images/Chapter 2/Menu/Saburo quest.png","hover": "images/Chapter 2/Menu/Saburo hover.png","name": "三朗"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_462
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_0000252A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A99

    return

label block_00003A84:
    # Node: 00003A84 (TO: Music room)

    if judge_lm_condition([]):
        jump block_000008D1

    return

label block_000008D1:
    # Node: 000008D1 (Music room)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S6Phase == 1" }]):
        jump block_0000251D
    if judge_lm_condition([{ "scope": 0, "content": "F6Check1 == True" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" }]):
        jump block_0000251B
    if judge_lm_condition([{ "scope": 0, "content": "F2Check1 == True" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" }]):
        jump block_00000913
    if judge_lm_condition([]):
        jump block_000008DB

    return

label block_0000251D:
    # Node: 0000251D (Music room 忍 waiting)
    $ sys_lm_menu_item = [{"pos": (496, 184),"image": "images/Chapter 2/Menu/Shinobu waiting.png","hover": "images/Chapter 2/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_463
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00002520
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A83

    return

label block_00002520:
    # Node: 00002520 (Waiting: 忍)
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#AA0055}事件{/color}{color=#0080FF}。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_0000251D

    return

label block_00003A83:
    # Node: 00003A83 (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003A3D

    return

label block_0000251B:
    # Node: 0000251B (Music room 忍 flag)
    $ sys_lm_menu_item = [{"pos": (496, 184),"image": "images/Chapter 2/Menu/Shinobu flag.png","hover": "images/Chapter 2/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_464
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_0000251E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A83

    return

label block_0000251E:
    # Node: 0000251E (忍 F6)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A43C35FAF6E4488E87E8829D5D8E84E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "今天没有社团活动，要不要一起回家？\n可以吗？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当然可以——☆\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "等等，刚才开始气氛很诡异啊，\n怎么回事？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_22306BD9E0624D81A1CFFFB486C5BAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "没事。真的没事。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_0000251F

    return

label block_0000251F:
    # Node: 0000251F (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#AA0055}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002C67

    return

label block_00002C67:
    # Node: 00002C67 (Phase ++)
    $ C2S6Phase = C2S6Phase + 1

    if judge_lm_condition([]):
        jump block_0000251D

    return

label block_00000913:
    # Node: 00000913 (Music room 翼 flag)
    $ sys_lm_menu_item = [{"pos": (496, 184),"image": "images/Chapter 2/Menu/Tsubasa flag.png","hover": "images/Chapter 2/Menu/Tsubasa hover.png","name": "つばさフラグ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_465
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A83
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさフラグ\"" }]):
        jump block_000018DE

    return

label block_000018DE:
    # Node: 000018DE (翼 F2)
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_43C2A5DA4B5D4815BEC6FE1DA10014AC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "看——♪我就知道你在——！\n我的钢琴就是叫出翼君的召唤术！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AD8CFA3B3632464BA96A924CD8D32A10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "唔……无法否定。\n因为我真的最喜欢听友君弹钢琴了……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀——！最喜欢什么的——！\n被翼君告白了——{w}！\n怎么办我该怎么办——！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9D306E6A6A55466F9DD4466BDBE612CC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "！？！？不、不是——！！！\n我不是那个意思！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2D653ACAC4114F1FA9CBB39313FD6DE6 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我其实并——！！\n不……也不是没有可是！"

    window hide

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2D653ACAC4114F1FA9CBB39313FD6DE6 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.7

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……哇！出现了！"

    window hide

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_454A1F98F91D4549A6F352AD11E26948 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    window show

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AF599E6EDE544FB39C2A38FD087F28F0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作、作哉君……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦——想干什么技安！\n我正和翼君气氛超好，不要捣乱！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E6FDC4E80B584C5E81421942D725A064 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2687EBBCBF3E4AF7A0DE1AF839CF5AF7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "……切。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EA19BEF7EE744C31BCEB11E0C0B07ABF as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "噫……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EB9D3849888641E78C28DA84B16F2AC8 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……哼。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2D653ACAC4114F1FA9CBB39313FD6DE6 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好痛！？好痛啊！{w}\n作、作哉君，不要拉我——！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    extend "为、为什么又是这样——！"

    window hide

    pause 1

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦，{color=#008080}以前也发生过{/color}呐。{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_380AC27C78834AF28FC3BC2DCB56F1C7 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那两个人怎么总是这样不合拍……{w}\n总之，还是得去看看情况。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("音乐室"))
    pause 0.3


    if judge_lm_condition([]):
        jump block_00002C65

    return

label block_00002C65:
    # Node: 00002C65 (Phase ++)
    $ C2S2Phase = C2S2Phase + 1

    if judge_lm_condition([]):
        jump block_000018DF

    return

label block_000018DF:
    # Node: 000018DF (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#0000FF}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_000008DB

    return

label block_000008DB:
    # Node: 000008DB (Music room)
    $ sys_lm_menu_item = [{"pos": (176, 288),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "ピアノ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_466
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A3D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ピアノ\"" },{ "scope": 1, "content": "C2S2Phase > 0" }]):
        jump block_00002C6F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ピアノ\"" }]):
        jump block_000008FD

    return

label block_00002C6F:
    # Node: 00002C6F (Piano F2)
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "现在不是弹琴的时候！！"

    window hide

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000008DB

    return

label block_000008FD:
    # Node: 000008FD (Piano)

    if judge_lm_condition([]):
        jump block_000008FC

    return

label block_000008FC:
    # Node: 000008FC (選擇)
    call scb_selector(_("要弹钢琴么？"), [{"name":" 演奏しない", "content":_("不想弹")}, {"name":"演奏する", "content":_("弹")}]) from _call_scb_selector_47

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"演奏する\"" },{ "scope": 1, "content": "F6Check1 == False" },{ "scope": 2, "content": "F2Check1 == False" },{ "scope": 3, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 4, "content": "C2S2 == False" },{ "scope": 4, "content": "C2S6 == False" },{ "scope": 5, "content": "C2SG1 == True" },{ "scope": 6, "content": "C2S4 == True" },{ "scope": 7, "content": "C2S5 == True" }]):
        jump block_000008FB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"演奏する\"" }]):
        jump block_00002C63
    if judge_lm_condition([{ "scope": 0, "content": "C2S6Phase == 1" },{ "scope": 1, "content": "_lm_selected_value == \" 演奏しない\"" }]):
        jump block_0000251D
    if judge_lm_condition([{ "scope": 0, "content": "F6Check1 == True" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "_lm_selected_value == \" 演奏しない\"" }]):
        jump block_0000251B
    if judge_lm_condition([{ "scope": 0, "content": "F2Check1 == True" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "_lm_selected_value == \" 演奏しない\"" }]):
        jump block_00000913
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \" 演奏しない\"" }]):
        jump block_000008DB

    return

label block_000008FB:
    # Node: 000008FB (1)
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

    if judge_lm_condition([{ "scope": 0, "content": "C2S6Phase == 1" }]):
        jump block_0000251D
    if judge_lm_condition([{ "scope": 0, "content": "C2S6 == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C2SG1 and C2S4 and C2S5 == True" }]):
        jump block_00002521
    if judge_lm_condition([{ "scope": 0, "content": "C2S2 == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" }]):
        jump block_00000914
    if judge_lm_condition([]):
        jump block_000008DB

    return

label block_00002521:
    # Node: 00002521 (忍 F6前)
    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A43C35FAF6E4488E87E8829D5D8E84E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "中午好森海。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "中午好绫濑！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00002C66

    return

label block_00002C66:
    # Node: 00002C66 (F6Check1)
    $ F6Check1 = True

    if judge_lm_condition([]):
        jump block_0000251B

    return

label block_00000914:
    # Node: 00000914 (翼 F2前)
    pause 0.5

    pause 0.5

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w=0.45}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "呼。我早就发现你在那里了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不要藏了快出来！翼酱！"

    window hide

    pause 0.35

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3FFA42ECEDF14A378835CC5A7CEED291 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "随、随叫随到。锵锵…………。"

    show rs_image_AD8CFA3B3632464BA96A924CD8D32A10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "下、下午好——我来打扰了。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("音乐室"))
    pause 0.3


    if judge_lm_condition([]):
        jump block_00002C64

    return

label block_00002C64:
    # Node: 00002C64 (F2Check1)
    $ F2Check1 = True

    if judge_lm_condition([]):
        jump block_00000913

    return

label block_00002C63:
    # Node: 00002C63 (Random)
    $ PianoRandom = Random( 4 )

    if judge_lm_condition([{ "scope": 0, "content": "PianoRandom == 0" }]):
        jump block_000008FB
    if judge_lm_condition([{ "scope": 0, "content": "PianoRandom == 1" }]):
        jump block_00000954
    if judge_lm_condition([{ "scope": 0, "content": "PianoRandom == 2" }]):
        jump block_000008FE
    if judge_lm_condition([{ "scope": 0, "content": "PianoRandom == 3" }]):
        jump block_000008FF

    return

label block_00000954:
    # Node: 00000954 (2)
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

    if judge_lm_condition([{ "scope": 0, "content": "C2S6Phase == 1" }]):
        jump block_0000251D
    if judge_lm_condition([]):
        jump block_000008DB

    return

label block_000008FE:
    # Node: 000008FE (3)
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

    if judge_lm_condition([{ "scope": 0, "content": "C2S6Phase == 1" }]):
        jump block_0000251D
    if judge_lm_condition([]):
        jump block_000008DB

    return

label block_000008FF:
    # Node: 000008FF (4)
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

    if judge_lm_condition([{ "scope": 0, "content": "C2S6Phase == 1" }]):
        jump block_0000251D
    if judge_lm_condition([]):
        jump block_000008DB

    return

label block_00003AC7:
    # Node: 00003AC7 (TO: Library)

    if judge_lm_condition([]):
        jump block_000008D2

    return

label block_000008D2:
    # Node: 000008D2 (Library)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "F6Check1 == True" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 0, "content": "C2S6Phase == 1" }]):
        jump block_0000252E
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 1, "content": "TalkShinobuF2 == 0" }]):
        jump block_00001F36
    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C2SG1 == True" }]):
        jump block_00002556
    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == True" },{ "scope": 1, "content": "C2S2Phase == 0" }]):
        jump block_000009AE
    if judge_lm_condition([]):
        jump block_000008DC

    return

label block_0000252E:
    # Node: 0000252E (Library empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_467
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003ABF

    return

label block_00003ABF:
    # Node: 00003ABF (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003ABE

    return

label block_00003ABE:
    # Node: 00003ABE (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003A9F

    return

label block_00001F36:
    # Node: 00001F36 (Library 忍 point)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 2/Menu/Shinobu point.png","hover": "images/Chapter 2/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_468
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00001F38
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003ABE

    return

label block_00001F38:
    # Node: 00001F38 (忍 F2)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_C2A28861C0A44DC6AAE17E0ABA1BE61C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怎么了？"

    pause 0.3

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_52820B68402A48B88D6C1517EC79E403 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『听取了忍的建议。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『用中二病的语言，{/color}{nw}"
    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "{color=#0080FF}{/color}{u}{color=#FF0000}大量援引漫画中的台词{/color}{/u}{color=#0080FF}。』{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00001F39

    return

label block_00001F39:
    # Node: 00001F39 (選擇)
    call scb_selector(_("这种意见可否？"), [{"name":"はい", "content":_("就是这个")}, {"name":"いいえ", "content":_("太微妙了，算了")}]) from _call_scb_selector_48

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002C73
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00001F36

    return

label block_00002C73:
    # Node: 00002C73 (TF2)
    $ TalkShinobuF2 = 1

    if judge_lm_condition([]):
        jump block_00003AC0

    return

label block_00003AC0:
    # Node: 00003AC0 (FLAG: CP2F2)
    call block_00003A0E from _call_block_00003A0E_1

    if judge_lm_condition([]):
        jump block_00003AA1

    return

label block_00002556:
    # Node: 00002556 (Library 忍 quest)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 2/Menu/Shinobu quest.png","hover": "images/Chapter 2/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_469
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00000967
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003ABE

    return

label block_00000967:
    # Node: 00000967 (小忍問題冊 1)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_22306BD9E0624D81A1CFFFB486C5BAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_E7A48E4B115D4F53A61CCC7B11022DE9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……嗯嗯。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍，在读什么呢？"

    show rs_image_C2A28861C0A44DC6AAE17E0ABA1BE61C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "问题书。正好，要不要试试？"

    show rs_image_32A6171EED0D4A9F920F16574ED46630 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "有{color=#0080FF}“简单”“一般”“困难”{/color}三种，\n这次就先从{color=#0080FF}“简单”{/color}开始好了。"

    window hide

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003AC1

    return

label block_00003AC1:
    # Node: 00003AC1 (小忍問題冊)
    call block_00003837 from _call_block_00003837_3

    if judge_lm_condition([]):
        jump block_00003AC2

    return

label block_00003AC2:
    # Node: 00003AC2 (RESET)
    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_000009AE

    return

label block_000009AE:
    # Node: 000009AE (Library answer)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 2/Menu/Shinobu.png","hover": "images/Chapter 2/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (152, 128),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "調べる"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_470
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003ABE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"調べる\"" }]):
        jump block_00003AC6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobuF6After == True" }]):
        jump block_00002603
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobu == 1" },{ "scope": 2, "content": "C2SG1 == True" },{ "scope": 3, "content": "StudyCount >= 3" }]):
        jump block_00002547
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobu == 1" },{ "scope": 2, "content": "C2SG1 == True" }]):
        jump block_00002548
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "C2SG1 == True" }]):
        jump block_000009B3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobu == 1" }]):
        jump block_00002546
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobu == 0" }]):
        jump block_00002545

    return

label block_00003AC6:
    # Node: 00003AC6 (Answer)
    call screen shinobu_question_level_selector

    if _return == 0:
        jump block_00003AC5
    elif _return == 1:
        jump block_00003AC4
    elif _return == 2:
        jump block_00003AC3
    else:
        jump block_000009AE

    return

label block_00003AC5:
    # Node: 00003AC5 (1)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    call shinobu_question_answer_sheet_show(0) from _call_shinobu_question_answer_sheet_show_9

    if judge_lm_condition([]):
        jump block_00003AC6

    return

label block_00003AC4:
    # Node: 00003AC4 (2)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    call shinobu_question_answer_sheet_show(1) from _call_shinobu_question_answer_sheet_show_10

    if judge_lm_condition([]):
        jump block_00003AC6

    return

label block_00003AC3:
    # Node: 00003AC3 (3)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    call shinobu_question_answer_sheet_show(2) from _call_shinobu_question_answer_sheet_show_11

    if judge_lm_condition([]):
        jump block_00003AC6

    return

label block_00002603:
    # Node: 00002603 (忍 F6后)
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_8FD0C8C99F91493DB85D4EB39544B538 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，还是不能接受。{w}\n星期五出发，总共三天两夜，\n按说应该周日晚上回来。"

    show rs_image_E7A48E4B115D4F53A61CCC7B11022DE9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "可是，到底为什么……\n嗯——唔～～～"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不要想那么多，会白头发的～\n无所谓了，过去的事就过去好了♪"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12E3E3C881C34AC09EF31505C89F7982 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w=0.5}{nw}"
    show rs_image_8FD0C8C99F91493DB85D4EB39544B538 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "也对。现在就先听笨蛋友的好了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00002CBC

    return

label block_00002CBC:
    # Node: 00002CBC (END: TalkF6After)
    $ TalkShinobuF6After = False

    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == True" }]):
        jump block_000009AE
    if judge_lm_condition([]):
        jump block_000008DC

    return

label block_000008DC:
    # Node: 000008DC (Library)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 2/Menu/Shinobu.png","hover": "images/Chapter 2/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_472
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003ABE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobuF6After == True" }]):
        jump block_00002603
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "C2S2Phase >= 97" },{ "scope": 2, "content": "TalkShinobuF2 == 1" }]):
        jump block_00001F37
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobu == 1" },{ "scope": 2, "content": "C2SG1 == True" },{ "scope": 3, "content": "StudyCount >= 3" }]):
        jump block_00002547
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobu == 1" },{ "scope": 2, "content": "C2SG1 == True" }]):
        jump block_00002548
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "C2SG1 == True" }]):
        jump block_000009B3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "TalkShinobu == 1" }]):
        jump block_00002546
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00002545

    return

label block_00001F37:
    # Node: 00001F37 (忍 F2選擇后)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_70861E328B2348D287F25B7F24FF54D6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "别小看漫画。\n可是有非常多打动人心的名言的。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("柔道场外"))

    if judge_lm_condition([]):
        jump block_000008DC

    return

label block_00002547:
    # Node: 00002547 (Test success)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_22306BD9E0624D81A1CFFFB486C5BAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D798B398B8514593AA6107349A76BEA1 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，期中考试成绩不错嘛。好好努力了呢。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "奖励呢！奖励呢？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12E3E3C881C34AC09EF31505C89F7982 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，你本来就该好好学习，为什么还要奖励。"

    show rs_image_073C9E8C6E964420AA676C5447C3792A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……不过，对于友来说，这已经很厉害了。{w}\n……{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    extend "乖乖。{nw}"
    show rs_image_CE498AFB1E3D4DA78B270436EF373DE6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    extend "（摸摸）"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "诶，这就是奖励？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A43C35FAF6E4488E87E8829D5D8E84E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "算是。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——好不容易这么努力的——！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8FD0C8C99F91493DB85D4EB39544B538 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说什么鬼话……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00002C72

    return

label block_00002C72:
    # Node: 00002C72 (T++)
    $ TalkShinobu = TalkShinobu + 1

    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == True" }]):
        jump block_000009AE
    if judge_lm_condition([]):
        jump block_000008DC

    return

label block_00002548:
    # Node: 00002548 (Test fail)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_22306BD9E0624D81A1CFFFB486C5BAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍～这次的期中考试又考坏了～……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12E3E3C881C34AC09EF31505C89F7982 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔……都说让你认真点了。\n"
    show rs_image_E7A48E4B115D4F53A61CCC7B11022DE9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "根据约定你要受罚。\n那么，该让友做什么呢。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不要不要好可怕——"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯——……{w}……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_A43C35FAF6E4488E87E8829D5D8E84E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "算了。考虑起来也很费劲，\n自己一个人慢慢反省去。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……感觉比受罚还难受……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00002C72

    return

label block_000009B3:
    # Node: 000009B3 (小忍問題冊 2)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D798B398B8514593AA6107349A76BEA1 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "要挑战问题吗？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide


    if judge_lm_condition([]):
        jump block_00003AC1

    return

label block_00002546:
    # Node: 00002546 (忍 F3前 2)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_18DB531342D94D37B18E5E70E8724066 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "期中考试的结果，真是期待呢。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == True" }]):
        jump block_000009AE
    if judge_lm_condition([]):
        jump block_000008DC

    return

label block_00002545:
    # Node: 00002545 (忍 F3前 1)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_8FD0C8C99F91493DB85D4EB39544B538 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说起来，友，期中考试你真的不复习？"

    show rs_image_12E3E3C881C34AC09EF31505C89F7982 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "至少试着学点东西啊。\n这次再不及格就要惩罚。\n好了就这样。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——不要嘛——！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "啊，这样说是不是考得好就有奖励呐！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6D5C4FC6CA71418A8875E35D505835E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你又……"
    show rs_image_12E3E3C881C34AC09EF31505C89F7982 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "好的时候就\n“乖乖好孩子，下次继续努力”这样好了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不要不要——！不讲理——！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8FD0C8C99F91493DB85D4EB39544B538 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……算了不想管。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00002C72

    return

label block_00003ABD:
    # Node: 00003ABD (TO: Toilet)

    if judge_lm_condition([]):
        jump block_000008D3

    return

label block_000008D3:
    # Node: 000008D3 (Toilet)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_297E564A7C1544469FB88A41AB85B6C9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 1, "content": "TalkShintaroF2 == 0" }]):
        jump block_00001F3D
    if judge_lm_condition([{ "scope": 0, "content": "C2S4 == True" }]):
        jump block_0000254E
    if judge_lm_condition([{ "scope": 0, "content": "C2S3 == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" }]):
        jump block_00000A09
    if judge_lm_condition([]):
        jump block_000008DD

    return

label block_00001F3D:
    # Node: 00001F3D (Toilet 慎太郎 point)
    $ sys_lm_menu_item = [{"pos": (368, 120),"image": "images/Chapter 2/Menu/Shintaro point.png","hover": "images/Chapter 2/Menu/Shintaro hover.png","name": "慎太郎"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_473
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00001F3C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A9F

    return

label block_00001F3C:
    # Node: 00001F3C (慎太郎 F2)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_888F059A76394ED3AA6121005A67D206 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "有事吗——？"

    pause 0.3

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_7F497F24D349433FB39C83C619E61AB8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『听取了慎太郎的建议。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『注重事实，{/color}\n{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    extend "{color=#0080FF}{/color}{u}{color=#FF0000}专注于用事实说服{/color}{/u}{color=#0080FF}。』{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("厕所"))

    if judge_lm_condition([]):
        jump block_00001F3A

    return

label block_00001F3A:
    # Node: 00001F3A (選擇)
    call scb_selector(_("这种意见可否？"), [{"name":"はい", "content":_("就是这个")}, {"name":"いいえ", "content":_("太微妙了，算了")}]) from _call_scb_selector_49

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002C71
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00001F3D

    return

label block_00002C71:
    # Node: 00002C71 (TF2)
    $ TalkShintaroF2 = True

    if judge_lm_condition([]):
        jump block_00003ABB

    return

label block_00003ABB:
    # Node: 00003ABB (FLAG: CP2F2)
    call block_00003A0E from _call_block_00003A0E_2

    if judge_lm_condition([]):
        jump block_00003AA1

    return

label block_0000254E:
    # Node: 0000254E (Toilet empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (224, 184),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "トイレ個室"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_474
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ個室\"" }]):
        jump block_000027F4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003AA0

    return

label block_000027F4:
    # Node: 000027F4 (Toilet single)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("厕所单间"))
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1C833F0E5AB54E79BCEE6017035686BE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if judge_lm_condition([]):
        jump block_000027F3

    return

label block_000027F3:
    # Node: 000027F3 (選擇)
    call scb_selector(_("要放松一下么？"), [{"name":"はい", "content":_("……忍不住了")}, {"name":"いいえ", "content":_("这不合适这不合适")}]) from _call_scb_selector_50

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_000027F2
    if judge_lm_condition([]):
        jump block_000008D3

    return

label block_000027F2:
    # Node: 000027F2 (Relax)
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
        jump block_000008D3

    return

label block_00003AA0:
    # Node: 00003AA0 (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003A9F

    return

label block_00000A09:
    # Node: 00000A09 (Toilet 慎太郎 flag)
    $ sys_lm_menu_item = [{"pos": (368, 120),"image": "images/Chapter 2/Menu/Shintaro flag.png","hover": "images/Chapter 2/Menu/Shintaro hover.png","name": "慎太郎"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_475
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A9F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_000008EA

    return

label block_000008EA:
    # Node: 000008EA (慎太郎 F3)
    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_888F059A76394ED3AA6121005A67D206 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_511A1885AB154028AF647FB028BA2458 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "奥村慎太郎！现在出动！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇！突然怎么了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BE6350EE36664764B9305ACF9E0C443E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "为了{color=#FF00FF}“御咲学园完全HOMO计划☆”{/color}\n要开始行动了。"

    show rs_image_F1B9EC1687544CF6AC26A45D3E5F4674 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "中学生！这可是决定取向的关键时期！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_48C5F16710344F4F8A8167B1D88A30CD as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{color=#800080}给这些迷路的小羊们背后猛推一把，\n让他们进入这边的世界……☆{/color}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、不好了……！\n纯洁的我肯定会被拿来祭旗的！\n要堕落到那个世界去了——！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_400D502433E44E52A9FFEAD65F622427 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_400D502433E44E52A9FFEAD65F622427 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……欸，没有兴趣？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CC8E028A316C4986B496B717E342B70C as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("厕所"))

    if judge_lm_condition([]):
        jump block_0000253C

    return

label block_0000253C:
    # Node: 0000253C (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#800080}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002C7F

    return

label block_00002C7F:
    # Node: 00002C7F (Phase ++)
    $ C2S3Phase = C2S3Phase + 1

    if judge_lm_condition([]):
        jump block_0000253B

    return

label block_0000253B:
    # Node: 0000253B (CP2 Daytime 慎太郎)
    call block_00000C25 from _call_block_00000C25_1

    if judge_lm_condition([]):
        jump block_00003AA1

    return

label block_000008DD:
    # Node: 000008DD (Toilet)
    $ sys_lm_menu_item = [{"pos": (368, 120),"image": "images/Chapter 2/Menu/Shintaro.png","hover": "images/Chapter 2/Menu/Shintaro hover.png","name": "慎太郎"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_476
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A9F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" },{ "scope": 1, "content": "TalkShintaroF2 == 1" },{ "scope": 2, "content": "C2S2Phase >= 97" }]):
        jump block_00001F3B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00002CC5

    return

label block_00001F3B:
    # Node: 00001F3B (慎太郎 F2選擇后)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F1B9EC1687544CF6AC26A45D3E5F4674 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那两个人应该能成为不错的同性恋人的。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("厕所"))

    if judge_lm_condition([]):
        jump block_000008DD

    return

label block_00002CC5:
    # Node: 00002CC5 (慎太郎筆記)
    window show

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_FD2C0CA41CDB4FD99334DB3AB5756355 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{color=#008A45}人物详细笔记{/color}，要看吗？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_place_title(_("厕所"))
    window hide


    if judge_lm_condition([]):
        jump block_00002CC6

    return

label block_00002CC6:
    # Node: 00002CC6 (選擇)
    call scb_selector("", [{"name":"はい", "content":_("看")}, {"name":"いいえ", "content":_("不想看")}]) from _call_scb_selector_51

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002CC8
    if judge_lm_condition([]):
        jump block_000008DD

    return

label block_00002CC8:
    # Node: 00002CC8 (PREPARE)
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0


    if judge_lm_condition([]):
        jump block_00002CC7

    return

label block_00002CC7:
    # Node: 00002CC7 (慎太郎筆記)
    $ renpy.block_rollback()
    call screen shintarou_notebook()

    if judge_lm_condition([]):
        jump block_00003ABC

    return

label block_00003ABC:
    # Node: 00003ABC (RESET)
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000008D3

    return

label block_00003ACC:
    # Node: 00003ACC (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A95

    return

label block_00003ACE:
    # Node: 00003ACE (Conversation F2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "找谁问建议比较好呐……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这关系到翼君和技安的将来，必须慎重选择。"

    window hide

    $ set_window("(標準)")

    return

label block_00003ACF:
    # Node: 00003ACF (Target F2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『寻找知晓“响彻心扉的的话语”的人\n并听取建议。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FBA:
    # Node: 00001FBA (Character)
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

label block_0000093A:
    # Node: 0000093A (School inside XCTA)
    if judge_lm_condition([{ "scope": 1, "content": "C2S4Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S4Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00003AD3", target_label="block_00003AD1") from _call_scb_global_map_117
    elif judge_lm_condition([{ "scope": 1, "content": "C2S4Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S2Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00003AD3", target_label="block_00003AD0") from _call_scb_global_map_118
    elif judge_lm_condition([{ "scope": 1, "content": "C2S2Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S4Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00003AD2", target_label="block_00003AD1") from _call_scb_global_map_119
    elif judge_lm_condition([{ "scope": 1, "content": "C2S2Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S2Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, True, talk_label="block_00003AD2", target_label="block_00003AD0") from _call_scb_global_map_120
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2S4Phase == 1" }]):
        jump block_00003AD3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00003A8D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00003A9E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_00003A84
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00003AC7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00003ABD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00003ACC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00003AC9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FBA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2S2Phase == 1" }]):
        jump block_00003AD2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C2S4Phase == 1" }]):
        jump block_00003AD1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C2S2Phase == 1" }]):
        jump block_00003AD0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_0000093A

    return

label block_00003AD3:
    # Node: 00003AD3 (Conversation F4)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "陆田和杉本来我们学校了。\n翼君是他们的粉丝，肯定很高兴吧——"

    window hide

    $ set_window("(標準)")

    return

label block_00003AC9:
    # Node: 00003AC9 (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_00003ACB

    return

label block_00003ACB:
    # Node: 00003ACB (RESET)
    $ C2S1Phase = 0
    $ C2S2Phase = 0
    $ C2S3Phase = 0
    $ C2S4Phase = 0
    $ C2S5Phase = 0
    $ C2S6Phase = 0

    if judge_lm_condition([]):
        jump block_000008CB

    return

label block_00003AD2:
    # Node: 00003AD2 (Conversation F2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "到底怎么做才能让翼君和技安和好呢。{w}\n总之先去看看他们的情况。"

    window hide

    $ set_window("(標準)")

    return

label block_00003AD1:
    # Node: 00003AD1 (Target F4)
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

label block_00003AD0:
    # Node: 00003AD0 (Target F2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#AA0055}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00000A03:
    # Node: 00000A03 (School inside ACTA)
    if judge_lm_condition([{ "scope": 1, "content": "C2S6Phase == 1" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, True, talk_label="block_00003AD5", target_label="block_00003AD4") from _call_scb_global_map_121
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, True, talk_label="block_00003AD6", target_label="block_00003AD4") from _call_scb_global_map_122
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2S6Phase == 1" }]):
        jump block_00003AD5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00003A8D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00003A9E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_00003A84
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00003AC7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00003ABD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00003ACC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" }]):
        jump block_00003ADC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00003AD6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00003AD4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00003AC9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FBA

    return

label block_00003AD5:
    # Node: 00003AD5 (Conversation F6)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为什么忍兴致那么好啊。有时很奇怪哦——忍。"

    window hide

    $ set_window("(標準)")

    return

label block_00003ADC:
    # Node: 00003ADC (TO: Afternoon)

    if judge_lm_condition([]):
        jump block_00003AE0

    return

label block_00003AE0:
    # Node: 00003AE0 (TO: Afternoon)

    if judge_lm_condition([]):
        jump block_00003ADF

    return

label block_00003ADF:
    # Node: 00003ADF (TO: Afternoon)

    if judge_lm_condition([]):
        jump block_000024F8

    return

label block_000024F8:
    # Node: 000024F8 (Afternoon)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    stop music fadeout 1
    $ sys_music_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
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


    if judge_lm_condition([{ "scope": 0, "content": "C2S1Phase == 1" }]):
        jump block_00000BCC
    if judge_lm_condition([]):
        jump block_00002F01

    return

label block_00000BCC:
    # Node: 00000BCC (CP2 Twilight 月空)
    call block_00000AD0 from _call_block_00000AD0

    if judge_lm_condition([]):
        jump block_00003A07

    return

label block_00002F01:
    # Node: 00002F01 (Cancel: First)
    $ FEnterMisaki = False

    if judge_lm_condition([]):
        jump block_000009D2

    return

label block_000009D2:
    # Node: 000009D2 (CP2 Twilight)
    call block_00000A21 from _call_block_00000A21

    if judge_lm_condition([]):
        jump block_00003A06

    return

label block_00003AD6:
    # Node: 00003AD6 (Conversation F1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "和阿月他们说过话后慢慢也有干劲了！{w}\n今天小钢琴部要继续活动了♪"

    window hide

    $ set_window("(標準)")

    return

label block_00003AD4:
    # Node: 00003AD4 (Target F16)
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

label block_000008CD:
    # Node: 000008CD (School inside ACTX)
    if judge_lm_condition([{ "scope": 1, "content": "C2SG1 == True" }]) and judge_lm_condition([{ "scope": 1, "content": "SYSReviewMode == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, False, talk_label="block_00003ADB", target_label="block_00003AD7") from _call_scb_global_map_123
    elif judge_lm_condition([{ "scope": 1, "content": "C2SG1 == True" }]) and judge_lm_condition([{ "scope": 1, "content": "C1S1 and C1S2 and C1S3 and C1S4 and C1S5 == True" },{ "scope": 2, "content": "CXQKaruta and C2QNewsclub and C2QYuuhi and C2QKimuraConference and C2QSakuya and C2QSora and CXQSabuImechen and CXQTsukiTest and CXQShinoQuestion  == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, False, talk_label="block_00003ADB", target_label="block_00003AD8") from _call_scb_global_map_124
    elif judge_lm_condition([{ "scope": 1, "content": "C2SG1 == True" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, False, talk_label="block_00003ADB", target_label="block_00003AD9") from _call_scb_global_map_125
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "SYSReviewMode == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, False, talk_label="block_00003ADA", target_label="block_00003AD7") from _call_scb_global_map_126
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1S1 and C1S2 and C1S3 and C1S4 and C1S5 == True" },{ "scope": 2, "content": "CXQKaruta and C2QNewsclub and C2QYuuhi and C2QKimuraConference and C2QSakuya and C2QSora and CXQSabuImechen and CXQTsukiTest and CXQShinoQuestion  == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, False, talk_label="block_00003ADA", target_label="block_00003AD8") from _call_scb_global_map_127
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", True, False, talk_label="block_00003ADA", target_label="block_00003AD9") from _call_scb_global_map_128
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "SYSReviewMode == True" }]):
        jump block_00003AD7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1S1 and C1S2 and C1S3 and C1S4 and C1S5 == True" },{ "scope": 2, "content": "CXQKaruta and C2QNewsclub and C2QYuuhi and C2QKimuraConference and C2QSakuya and C2QSora and CXQSabuImechen and CXQTsukiTest and CXQShinoQuestion  == True" }]):
        jump block_00003AD8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2SG1 == True" }]):
        jump block_00003ADB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00003A8D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00003A9E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_00003A84
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00003AC7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00003ABD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00003ACC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" }]):
        jump block_00003ADC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00003ADA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00003AD9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_000008CD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FBA

    return

label block_00003AD7:
    # Node: 00003AD7 (Target dream)
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

label block_00003AD8:
    # Node: 00003AD8 (Target 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#AA0055}下一个章节{/color}{color=#0080FF}正在等着！』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003ADB:
    # Node: 00003ADB (Conversation F3后)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈~秋天好棒~\n暖缓和和，心情真好~"

    window hide

    $ set_window("(標準)")

    return

label block_00003ADA:
    # Node: 00003ADA (Conversation F3前)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "还要穿校服，好热。"

    window hide

    $ set_window("(標準)")

    return

label block_00003AD9:
    # Node: 00003AD9 (Target 1)
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

label block_00002518:
    # Node: 00002518 (Newsclub quest)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
        jump block_00002511

    return

label block_00002C84:
    # Node: 00002C84 (Cancel: First)
    $ FNewsclub = False

    if judge_lm_condition([]):
        jump block_0000250F

    return

label block_0000250F:
    # Node: 0000250F (Newsclub 1)
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

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.2

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "打扰了！不知为何就来了。"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_8D5A9887A2D74B788AF161574F70EF1D as tag_DCBDF256A1E242E78A25910AE27C0954 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    show rs_image_E283497485C94D2C96064B6CA8800E56 as tag_CC4336DE74164173AC47C2C317367F10 at center_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哦，你是一班的森海君。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_C3A1594D73C441FA89364B17B57E8A25 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "欢迎来到{color=#00FFFF}新闻部{/color}。看看我们的杰作如何！"

    show rs_image_44EC1146BFE94EB1A8DBB6E8D8771338 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "请自由参观～"

    show rs_image_350F6A2B48EE49C8B631CE0B02F5BC2C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谢谢！{w=0.5}{nw}"
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_8DC6F44BF4644738BCD14828D87C2679 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……嗯嗯，哦哦——"
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯？所有报纸都是\n冈岛君和小岛君署名的。新闻部的其他人呐？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_A95A56566BE747DEBB035CC1B94ADE68 as tag_CC4336DE74164173AC47C2C317367F10 at center_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "嗯，因为去年刚创立，"
    show rs_image_48D2CFA5C42D4128B0F491278D44FECD as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "基本没什么传承，\n知道的人很少，新生也没人来……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9C6025197AA6408B855470BD6875E779 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "然而！总有一天我们势必会搞个大新闻，\n让所有人知道我们！！"

    show rs_image_8AAF036BA1B649CB83E37164231A6166 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "在此还要感谢刚创立就马上入部的小岛君！"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_8D5A9887A2D74B788AF161574F70EF1D as tag_DCBDF256A1E242E78A25910AE27C0954 at center_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "无需感谢。从小事开始慢慢做起即可。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……好关心部长呐。"
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_350F6A2B48EE49C8B631CE0B02F5BC2C as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，这张和床一样大的纸\n是还在写的新闻？放在地上不会被弄坏吗？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_8AAF036BA1B649CB83E37164231A6166 as tag_CC4336DE74164173AC47C2C317367F10 at left_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哈！我们怎么可能会在第二学期第一刊上犯那种低级错误！"

    show rs_image_71267AC79D7D4409849ACEE6DA4BF34E as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "森海君也记住绝对不许走过去啊！"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_6EA040B97356486ABE5FD91F92B543D2 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当然当然——！不会有问题的～"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_9C6025197AA6408B855470BD6875E779 as tag_CC4336DE74164173AC47C2C317367F10 at left_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "绝对不许过去啊！过去也要避开走啊！"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没关系！我发誓要是真的不小心，\n这辈子都娶……\n{w=0.6}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "呜，啊哇！？！？"

    show rs_image_E1E1F08446C54DCAAC86BEA1B671549E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "啊{w=0.2}\n{nw}"
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_A95A56566BE747DEBB035CC1B94ADE68 as tag_CC4336DE74164173AC47C2C317367F10 at center_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
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
    show rs_image_44EC1146BFE94EB1A8DBB6E8D8771338 as tag_DCBDF256A1E242E78A25910AE27C0954 at center_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    pause 0.3

    rs_character_53FF68C192E3494AB005C1909579AFFB "有在反省么……森海君，还有，部长。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是、是的……对不起……！"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_2FAEAC19AC5347FDA2819CA4500CD703 as tag_CC4336DE74164173AC47C2C317367F10 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "为、为何我也要……"

    show rs_image_8D5A9887A2D74B788AF161574F70EF1D as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "因为你在乱立FLAG。"

    pause 0.2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Onboard 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Onboard 1.ogg"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_CC4336DE74164173AC47C2C317367F10
    $ zorder_tag_5B6684205EA24754A986B49C70895ECD = 200
    $ zorder_tag_EB5D0582654644B7A76BB509C31DD31E = 200
    show rs_image_F90988F5C6754C53A9B5FB1BE164894B as tag_5B6684205EA24754A986B49C70895ECD at left_top zorder zorder_tag_5B6684205EA24754A986B49C70895ECD onlayer master
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_EB5D0582654644B7A76BB509C31DD31E at right_top zorder zorder_tag_EB5D0582654644B7A76BB509C31DD31E onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_53FF68C192E3494AB005C1909579AFFB "因此，森海君。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是！"

    hide tag_5B6684205EA24754A986B49C70895ECD
    hide tag_EB5D0582654644B7A76BB509C31DD31E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_8A8399081EA34489AD19EAD1C673B291 as tag_DCBDF256A1E242E78A25910AE27C0954 at center_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "为了弥补毁掉原稿的错误，{w}\n接下来你必须帮助我们，帮助新闻部收集情报。"

    show rs_image_44EC1146BFE94EB1A8DBB6E8D8771338 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "收集到什么情报时请前来汇报，到时候就拜托了。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_44EC1146BFE94EB1A8DBB6E8D8771338 as tag_DCBDF256A1E242E78A25910AE27C0954 at left_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "在、在下听令！如果这样就能原谅我的话不管什么我都会做……"

    show rs_image_9E6AF824075F4EB3B240BE13A1C54165 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
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


    if judge_lm_condition([{ "scope": 0, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase + C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase + C3S1Phase + C3S2Phase + C3S3Phase + C3S4Phase + C3S5Phase  + C3S6Phase == 0" }]):
        jump block_0000251A
    if judge_lm_condition([]):
        jump block_00002511

    return

label block_0000251A:
    # Node: 0000251A (Newsclub 岡島 quest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (112, 160),"image": "images/Chapter 2/Menu/Okajima quest.png","hover": "images/Chapter 2/Menu/Okajima hover.png","name": "岡島"}, {"pos": (392, 160),"image": "images/Chapter 2/Menu/Kojima.png","hover": "images/Chapter 2/Menu/Kojima hover.png","name": "小島"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_477
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A8F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_00002517
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" },{ "scope": 1, "content": "C2QNewsclub == False" },{ "scope": 2, "content": "C2QNewsclubPhase == 0" }]):
        jump block_00002517
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" },{ "scope": 1, "content": "TalkOkajima == 0" }]):
        jump block_0000250D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_0000250C

    return

label block_00003A8F:
    # Node: 00003A8F (TO: Aisle 2)

    if judge_lm_condition([]):
        jump block_00003A97

    return

label block_00002517:
    # Node: 00002517 (新聞部 quest)
    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_53FF68C192E3494AB005C1909579AFFB "森海同学，请处理一下这个。{w}\n内容是验证“厕所的花子君”的真伪。"

    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "据说，在厕所的单间连续三次说\n“花子君快来”就会出现……\n至少这是主流说法。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    window hide

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#3A00C4}“花子小姐”是很有名的学校怪谈，\n但是，御咲学园却出现了“花子君”的传说。\n这似乎已经发生过多次，请一定探明真相！{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_00002C85

    return

label block_00002C85:
    # Node: 00002C85 (Phase ++)
    $ C2QNewsclubPhase = C2QNewsclubPhase + 1
    $ C2QNewsclubRedirect = False

    if judge_lm_condition([]):
        jump block_00002516

    return

label block_00002516:
    # Node: 00002516 (QUEST START)
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
        jump block_00002511

    return

label block_0000250D:
    # Node: 0000250D (岡島 1)
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_6EACDBA5EB7B44D7A7699633252E6B7E as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4BF60E1CD8994FA8B74D36E307E8C354 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "任何情报请速来告知！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，说起来……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A375C883918D41239D3E5B8AE7C226B2 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哦呀！这个反应，想到什么了对不。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "其实——之前在校庭里……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C29B9703BE7C41F5840BF23219240A16 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6BEAA3D38A204EAE8EFEE059FD541711 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "唔，这种情报有点……"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_53FF68C192E3494AB005C1909579AFFB "森海君，请不要对纯洁的部长灌输邪恶思想。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
        jump block_00002509

    return

label block_00002509:
    # Node: 00002509 (T ++)
    $ TalkOkajima = TalkOkajima + 1

    if judge_lm_condition([{ "scope": 0, "content": "C2QNewsclubPhase == 0" },{ "scope": 1, "content": "C1S1Phase + C1S2Phase + C1S3Phase + C1S4Phase + C1S5Phase + C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase + C3S1Phase + C3S2Phase + C3S3Phase + C3S4Phase + C3S5Phase  + C3S6Phase == 0" },{ "scope": 2, "content": "C1QTsubasaPhase + C1QSabushinPhase + C1QMatsutaPhase == 0" },{ "scope": 3, "content": "C2QNewsclub == False" }]):
        jump block_0000251A
    if judge_lm_condition([{ "scope": 0, "content": "C2QNewsclubPhase == 1" },{ "scope": 1, "content": "C2S2Phase == 0" }]):
        jump block_00002519
    if judge_lm_condition([]):
        jump block_00002511

    return

label block_00002519:
    # Node: 00002519 (Show quest)

    if judge_lm_condition([]):
        jump block_00002511

    return

label block_0000250C:
    # Node: 0000250C (岡島 2)
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4BF60E1CD8994FA8B74D36E307E8C354 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "任何新情报请速来告知！"

    show rs_image_6BEAA3D38A204EAE8EFEE059FD541711 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "啊，记得必须是全年龄的哦。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([{ "scope": 0, "content": "C2QNewsclubPhase == 0" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C2QNewsclub == False" }]):
        jump block_0000251A
    if judge_lm_condition([{ "scope": 0, "content": "C2QNewsclubPhase == 1" },{ "scope": 1, "content": "C2S2Phase == 0" }]):
        jump block_00002519
    if judge_lm_condition([]):
        jump block_00002511

    return

label block_00002514:
    # Node: 00002514 (Newsclub)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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


    if judge_lm_condition([{ "scope": 0, "content": "C2QNewsclubPhase == 0" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C2QNewsclub == False" }]):
        jump block_0000251A
    if judge_lm_condition([]):
        jump block_00002511

    return

label block_000008F7:
    # Node: 000008F7 (Stairwell)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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


    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 1, "content": "TalkSoraF2 == 0" }]):
        jump block_00001F2A
    if judge_lm_condition([{ "scope": 0, "content": "C2S1Phase == 1" }]):
        jump block_000024FB
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase == 1" }]):
        jump block_00000A0A
    if judge_lm_condition([{ "scope": 0, "content": "C2S1 == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" }]):
        jump block_000008F8
    if judge_lm_condition([{ "scope": 0, "content": "C2S1 == True" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C2QSora == False" },{ "scope": 3, "content": "C2SG1 == False" }]):
        jump block_00002507
    if judge_lm_condition([{ "scope": 0, "content": "C2SG1 == True" },{ "scope": 1, "content": "SYSTheaterState <> 22" }]):
        jump block_000018B5
    if judge_lm_condition([{ "scope": 0, "content": "CXQTsukiTest == False" },{ "scope": 1, "content": "C2QSora == True" },{ "scope": 2, "content": "C2S2Phase < 97" }]):
        jump block_00002C60
    if judge_lm_condition([]):
        jump block_00001F2D

    return

label block_00001F2A:
    # Node: 00001F2A (Stairwell 空 point)
    $ sys_lm_menu_item = [{"pos": (272, 264),"image": "images/Chapter 2/Menu/Sora stairwell point.png","hover": "images/Chapter 2/Menu/Sora stairwell hover.png","name": "空"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_478
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A97
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_00001F2C

    return

label block_00001F2C:
    # Node: 00001F2C (空 F2)
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_EC040B7182804790B7750A3172C04105 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君有事吗？"

    pause 0.3

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_F59CF92171C0495BA4E334AC96BA8B63 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『听取了空的建议。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『尊重双方立场，使用{/color}\n{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "{color=#0080FF}{/color}{u}{color=#FF0000}中立的话语{/color}{/u}{color=#0080FF}。』{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_00001F2B

    return

label block_00001F2B:
    # Node: 00001F2B (選擇)
    call scb_selector(_("这种意见可否？"), [{"name":"はい", "content":_("就是这个")}, {"name":"いいえ", "content":_("太微妙了，算了")}]) from _call_scb_selector_52

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002C74
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00001F2A

    return

label block_00002C74:
    # Node: 00002C74 (TF2)
    $ TalkSoraF2 = 1

    if judge_lm_condition([]):
        jump block_00003A94

    return

label block_00003A94:
    # Node: 00003A94 (FLAG: CP2F2)
    call block_00003A0E from _call_block_00003A0E_3

    if judge_lm_condition([]):
        jump block_00003A96

    return

label block_000024FB:
    # Node: 000024FB (Stairwell 空 waiting)
    $ sys_lm_menu_item = [{"pos": (224, 264),"image": "images/Chapter 2/Menu/Sora stairwell waiting.png","hover": "images/Chapter 2/Menu/Sora stairwell hover.png","name": "空"}, {"pos": (440, 256),"image": "images/Chapter 2/Menu/Tsuki stairwell.png","hover": "images/Chapter 2/Menu/Tsuki stairwell hover.png","name": "月"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_479
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_000024FC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00002C5C
    if judge_lm_condition([]):
        jump block_00003A8F

    return

label block_000024FC:
    # Node: 000024FC (Waiting: 空)
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#008A45}事件{/color}{color=#0080FF}。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_000024FB

    return

label block_00002C5C:
    # Node: 00002C5C (月)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_225455F87C6D4EB5BE746486367900D8 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "森海，来得好。{w}\n现在我们在准备训练，你也一起……"

    show rs_image_9C2A4A9AB5264C8AB635A79F79E6298D as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……很想这么说不过，\n看起来现在还不是时候，抱歉。\n下次我会再来邀请你的。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_000024FB

    return

label block_00000A0A:
    # Node: 00000A0A (Stairwell 作哉 flag)
    $ sys_lm_menu_item = [{"pos": (240, 232),"image": "images/Chapter 2/Menu/Sakuya stairwell flag.png","hover": "images/Chapter 2/Menu/Sakuya stairwell hover.png","name": "作哉"}, {"pos": (456, 232),"image": "images/Chapter 2/Menu/Tsubasa stairwell.png","hover": "images/Chapter 2/Menu/Tsubasa stairwell hover.png","name": "つばさ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_480
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_00000A0C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_00000A0C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008CF

    return

label block_00000A0C:
    # Node: 00000A0C (作哉 F2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，找到了找到了。在说什么呢？"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window hide

    pause 0.6

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DFF6C096971C4020B3AD59E666124B0B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……所以，就因为你不在，\n我被强塞了班长的工作。\n"
    show rs_image_757DAFA361824FA590E148B0796C4A27 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "下次给我注意。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8DECB50317B14BD6B1D99221FBD7089C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "非、非常抱歉。真的很对不起，我会注意的……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_454A1F98F91D4549A6F352AD11E26948 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嗯……那我先走了。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_362020A2BFCD4BB1B0805CDEE692E413 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……诶。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_454A1F98F91D4549A6F352AD11E26948 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "还有事……？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3FFA42ECEDF14A378835CC5A7CEED291 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊！没、没什么！给、给你添麻烦了……！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_362020A2BFCD4BB1B0805CDEE692E413 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EB9D3849888641E78C28DA84B16F2AC8 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "好像对我有意见啊。{w}\n说，对我有什么意见？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_65886B0DDD844CEF8CB130AC05A09545 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "怎、怎么可能！！\n"
    show rs_image_362020A2BFCD4BB1B0805CDEE692E413 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "只是……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_757DAFA361824FA590E148B0796C4A27 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "只是？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A2F9611E37CC476881256D2E6C30C824 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君……\n{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "最近似乎温柔了很多的感觉……也许……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8C3DB2F9BABD40D396DB3B634865E972 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "唔……！！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_398B4081FA4A4B0AB6F12C9C027BDE6F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "呵！！我能对你温柔！？\n有点自知之明你个笨蛋！！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_95FC6FFC5BDE4EABB5152ECB6A0F08B1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "噫——！！对、对不起——！！"

    window hide

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.6

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……唔……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))
    pause 0.8

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4


    if judge_lm_condition([]):
        jump block_00003A2C

    return

label block_00003A2C:
    # Node: 00003A2C (FLAG: CP2F2)
    call block_00003A0E from _call_block_00003A0E_4

    if judge_lm_condition([]):
        jump block_00003A95

    return

label block_000008F8:
    # Node: 000008F8 (Stairwell 空 flag)
    $ sys_lm_menu_item = [{"pos": (224, 264),"image": "images/Chapter 2/Menu/Sora stairwell flag.png","hover": "images/Chapter 2/Menu/Sora stairwell hover.png","name": "空"}, {"pos": (440, 256),"image": "images/Chapter 2/Menu/Tsuki stairwell.png","hover": "images/Chapter 2/Menu/Tsuki stairwell hover.png","name": "月"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_481
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008CF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_00002FCD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00002C5F

    return

label block_00002FCD:
    # Node: 00002FCD (空 F1)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_EC040B7182804790B7750A3172C04105 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000024FA

    return

label block_000024FA:
    # Node: 000024FA (F1)
    pause 0.45

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_7838A3FA6F98494CACA2B6E04E3C82B2 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……所以下周可能会变成这样。\n"
    show rs_image_B1FC5F4C1C12446FA8B2429310BFC93F as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "虽然很辛苦，但还是拜托了。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_AE9C0A0B9876495092F4044936BA8A1A as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……嗯，我明白。\n"
    show rs_image_EC040B7182804790B7750A3172C04105 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不用担心我这边，\n哥哥专心做自己的事就好了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么什么？在说什么？"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_FF2F05BF45D647239862F7725764481C as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "关于社团的事。为了以防万一必须先安排好。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯——每天都这么辛苦呐。\n参加社团的人好厉害——"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BD6D81BDC6854CA8A673AF3932F1F2E7 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不不，不是这么回事。\n都是因为兴趣开始的，友君不也在弄小钢琴部嘛，\n都是一样的。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦原来如此！\n我也一直在为小钢琴部努力呐。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    extend "嗯嗯，我也很厉害♪"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E4A2988FBBCF49C0A1E44ED64AFE0C25 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不，其实按照空的说法，\n森海并不怎么厉害。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9812D47B81CA40BBB981222A74D455B5 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "真是的——\n这样下去可就没朋友了哦，哥哥。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_33D7E05166F54F7A900E1886FA423087 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……！！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_00002C3C

    return

label block_00002C3C:
    # Node: 00002C3C (Phase ++)
    $ C2S1Phase = C2S1Phase + 1

    if judge_lm_condition([]):
        jump block_00002500

    return

label block_00002500:
    # Node: 00002500 (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#008A45}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_000024FB

    return

label block_00002C5F:
    # Node: 00002C5F (月 F1)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_FF2F05BF45D647239862F7725764481C as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000024FA

    return

label block_00002507:
    # Node: 00002507 (Stairwell 空 quest)
    $ sys_lm_menu_item = [{"pos": (272, 264),"image": "images/Chapter 2/Menu/Sora stairwell quest.png","hover": "images/Chapter 2/Menu/Sora stairwell hover.png","name": "空"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_482
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_0000243E
    if judge_lm_condition([]):
        jump block_000008CF

    return

label block_0000243E:
    # Node: 0000243E (空 QUEST)
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_EC040B7182804790B7750A3172C04105 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_25DD39CE556B4EC69227B2977E0220CB as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "呐，友君，今天放学后有时间吗？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "我和空不同还是单身的……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AA958AA9A1FE4204BFF4DC3025EFF511 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "说、说什么呢……{w=0.4}{nw}"
    show rs_image_08054561A18A4132A09DFC953ED37EFD as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那要不要来我家一起做点心？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦哦，不错！以前还没做过，这次试试！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B971E7700CCC4821BEE883B34D9FE081 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君在家一直都是自己做饭，\n就算是第一次也肯定会很有趣的。"

    show rs_image_30DD4B1DF61D48718BE856BC8D2D0EEC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "今天没有社团活动，\n放学后我会立刻准备回家的。"

    show rs_image_EC040B7182804790B7750A3172C04105 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "能请友君去买需要的材料吗？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当然没问题——！"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))
    pause 0.8

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_914779AD760E4293ABA36667EB8385D1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg"

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 2.ogg"

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "打扰了——！材料买回来了哦～"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欢迎，谢谢你帮我去买东西。这边已经都准备好了。"

    window hide

    pause 0.5

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_6EA78EC2093A46F097116A0C2CBB397C as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_11E00DC8F6D648B99910C2CC39E0527C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好！那事不宜迟！\n"
    show rs_image_E436CC5ED79D41EABE3ADFC40CD9F8B8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "欸，说起来今天阿月去什么地方了？"

    show rs_image_4426ECB7E6A8443FB128590CB7FEBB64 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那个啊，哥哥还有其他工作，今天不在。\n"
    show rs_image_E4597D5A818F42B9819FD9D95A8EDEF9 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "所以就只有我们两个人了！"

    window hide

    pause 0.7

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_11E00DC8F6D648B99910C2CC39E0527C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.5

    if sys_music_current_file != "sound/BGM/Ailurus fulgens.ogg":
        play music "sound/BGM/Ailurus fulgens.ogg" loop
        $ sys_music_current_file = "sound/BGM/Ailurus fulgens.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "RUUUUUU……！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哦哦哦哦……！用惯了电摩，料理机还是第一次……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_999A6E34D45F4B4FBE70557FFD235916 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君，做饭时禁止讲段子。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_3960C287871D42D38C1EEBC0EEB93DF1 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对、对不起～可这个……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    extend "呜啊啊啊！要被弄脏了！飞出去了要去了——！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊——真是的……怎么弄出来这么多……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……（哭）"

    window hide

    pause 0.5

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_11E00DC8F6D648B99910C2CC39E0527C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_A6E70EA9F30F4DE4AD20434ED388ACFF as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嘿咻嘿咻嘿咻！\n"
    show rs_image_35B9BEFBF42E474DB41387E9345C36B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "空，要混合到什么程度才算混合？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_9A51889A5B884F76838CF8C5D3725812 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔，我想要更细腻的口感，所以总之搅拌到光泽亮丽为止。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_EFDC09B34577437A8D2B581A3FFFC9E4 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——光……光泽？？"

    show rs_image_999A6E34D45F4B4FBE70557FFD235916 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "快点快点，不管的话泡沫都要消失了，手快点动起来！"

    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜呜……我一直是被做的那一方，根本不明白这种工作的诀窍～"

    show rs_image_E436CC5ED79D41EABE3ADFC40CD9F8B8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "空每晚都在侍奉别人，当然更习惯了——"

    show rs_image_CCE2DFCDE5EE495CB0367ED4ED7DCA8B as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "对对，太没紧张感的话快感就都没了，\n必须要察觉对方的状态，看准时机用手……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_67270A8F682B4692B38AB9A950B04B57 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不对，这和现在没关系！"

    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦——哦——！学习了学习了。呀——不愧是现充，说话真实在。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_8AF97BE15B524E50A2E2C8FC106F60FD as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哦，说起来，友君既然是单身的话，\n为什么会说自己是“被做”的那一方呢？"

    if sys_music2_current_file != "sound/Effect Sound/Stupid 1.ogg":
        play music2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_E777A5278A874BAB891650C04B85E3D7 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫、噫！不、这个、那个、所以……说……\n我、我一直都在用电摩君……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的——空！不要突然堵我的话！！"

    show rs_image_C0725D9DCFAF4402882B4880A327CD79 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哈哈！对不诚实的友君就要施以惩罚♪"

    window hide

    pause 0.6

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_11E00DC8F6D648B99910C2CC39E0527C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_E4597D5A818F42B9819FD9D95A8EDEF9 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯！烤得不错～！"

    show rs_image_39EA77FDE17745CA860489ACA0F6FAFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "颜色真棒～！！闻起来也很香。好想就这么吃一口……"

    show rs_image_6EA78EC2093A46F097116A0C2CBB397C as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我看看……{w=0.4}{nw}"
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_C0725D9DCFAF4402882B4880A327CD79 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "嗯，最上面一层用不到，可以吃哦。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_6EA040B97356486ABE5FD91F92B543D2 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——♪{w}\n{w=0.3}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "……（吞口水）！{w=0.44}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    extend "嗯！非常好！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_A62DFA8FA08E4BD2B83B9B282B530095 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "结果好便是都好。那差不多该做一些装饰了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_CA176C5A71144199A2E3AE0C60846C57 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6EA79B30E52B4FE8B90AB55D569F24D3 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "奶油！该做这个了！我可是很擅长的，再怎么说每天每夜……"

    show rs_image_10991B4D561D4E199496DB0923CC8645 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸？"

    show rs_image_6EA040B97356486ABE5FD91F92B543D2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶？"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_A62DFA8FA08E4BD2B83B9B282B530095 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯？？"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_E777A5278A874BAB891650C04B85E3D7 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4426ECB7E6A8443FB128590CB7FEBB64 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哦？？？"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_E1E1F08446C54DCAAC86BEA1B671549E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "开、开玩笑的……我什么都没说……"

    window hide

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_11E00DC8F6D648B99910C2CC39E0527C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.5

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_A62DFA8FA08E4BD2B83B9B282B530095 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "差不多该放一些水果了！友君想放什么？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_6EA040B97356486ABE5FD91F92B543D2 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "香蕉！"

    show rs_image_D3A7495152E44A10B9BD045BA5CCCDE8 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "果然～"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶？果然？？"

    show rs_image_2D0EC305038C4AE5AB71CFDA0756ACD1 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊……{w=0.44}{nw}"
    show rs_image_7E08F07FB7E44A4682D1CA8B31E70D52 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "不、没什么……"

    window hide

    pause 0.5

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    pause 2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    pause 0.6

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 1.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 1.ogg"

    window show

    rs_character_1F1F807AA93944B08B521CE0176884C5 "{size=28}做好了～！！{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "注满爱情！{color=#FF80C0}友空CAKE☆{/color}"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯♪那这块巧克力板该写点什么呢。"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_914779AD760E4293ABA36667EB8385D1 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_FFC620A1302E417EBD9CB71C6CDE9274

    pause 0.4

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我回来了。"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_00EDE24382514EE4A0ABD3DF8E01C76D as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_11E00DC8F6D648B99910C2CC39E0527C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦，时机刚好呀，阿月！快快叫来我们三人一起吃。"

    show rs_image_2D0EC305038C4AE5AB71CFDA0756ACD1 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸！可、可是哥哥比起这个还是去吃饭比较……"

    show rs_image_350F6A2B48EE49C8B631CE0B02F5BC2C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "事到如今还害羞什么♪\n本来不就是为了给阿月做慰问品才让我过来的嘛。"

    show rs_image_D41A51E2B16F4674B1A8FB746C8F1328 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "空总是在奇怪的地方不坦率呐～"

    show rs_image_03F57FFD226C42E7AA52FB834CB4A532 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……"

    show rs_image_39EA77FDE17745CA860489ACA0F6FAFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈！友A梦就来大显身手帮助不成器的空君！{w}{w=0.2}\n{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    extend "巧克力板给我♪"

    window hide

    pause 1.4

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D7269F0DB3AF45BD8855E0CB4A5B4F64 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_1EA93E6083954B758043E518146A295A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A66B9E9678E74FA481DCD625BCC55869

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_77C99743D39944F9AD8542E6C1310363 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_6EA78EC2093A46F097116A0C2CBB397C as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欢迎回来，哥哥、现在友君也在哦。"

    show rs_image_88D1205AA473480CA2A73E26453C1F61 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "哦，这样。似乎有股香甜的气味，你们在做点心？"

    show rs_image_4426ECB7E6A8443FB128590CB7FEBB64 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔……也留着哥哥的那一块。要试试吗？"

    show rs_image_4A2DF19F343B45378225DB529BF9F33C as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯。快累坏了，稍微吃点甜食也不错。"

    window hide

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 1.4

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_24AD0B599C1D4C999833900D36849A04 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.5

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀——呀——阿月，辛苦了～！我们特别做了东西在等你哦！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "为、为什么把名字改了……不是叫做“友空CAKE”来着么？"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这是……！这是为了我做的？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对——哦——！我们为了努力认真的阿月特别做的哦。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是嘛……谢谢你们。\n我开始听说的是“也有我的那一块”，没想到会是这么大一块。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "空又在说那么绕弯子的话了～♪盘子上也好好写了感谢语哦！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那、那是友君擅自写的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "别说出来啊，没意义了！"

    # Gallery unlock: images/CG/Cake 2.png
    $ zorder_rs_image_8D8A506E039845CD89579B536CAB6E35 = -100
    show rs_image_8D8A506E039845CD89579B536CAB6E35 as rs_image_8D8A506E039845CD89579B536CAB6E35 zorder zorder_rs_image_8D8A506E039845CD89579B536CAB6E35 onlayer master
    hide rs_image_8D8A506E039845CD89579B536CAB6E35

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 0
    show rs_image_8D8A506E039845CD89579B536CAB6E35 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_6F89C24415FD428194E5571D0A2078DD as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.6

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不，你们的心意确实传达到了。\n谢谢。还没吃我就已经感觉到力量了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊啦，那这样要是真的吃过后晚上会不会睡不着觉了呐？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "真是的，最后的最后又是段子……{w}\n{size=14}…………{/size}{w=0.5}{size=14}也许吧。{/size}"

    window hide

    pause 0.9

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2


    if judge_lm_condition([]):
        jump block_00002508

    return

label block_00002508:
    # Node: 00002508 (QUEST FINISH)
    $ set_window("(標準)")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_00002C55

    return

label block_00002C55:
    # Node: 00002C55 (C2Q空)
    $ C2QSora = True

    if judge_lm_condition([]):
        jump block_00003A96

    return

label block_000018B5:
    # Node: 000018B5 (Stairwell)
    $ sys_lm_menu_item = [{"pos": (184, 400),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "一階"}, {"pos": (488, 216),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "三階"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_483
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"一階\"" }]):
        jump block_000018B6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三階\"" }]):
        jump block_000018B8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008CF

    return

label block_000018B6:
    # Node: 000018B6 (Aisle 1)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("一楼走廊"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AEF730D86D5343AF81880AC735BAFAC6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4


    if judge_lm_condition([{ "scope": 0, "content": "C2S4 == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" }]):
        jump block_000018B7
    if judge_lm_condition([]):
        jump block_000018BE

    return

label block_000018B7:
    # Node: 000018B7 (Aisle 1 flag)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (520, 253),"image": "images/Chapter 2/Menu/Poster flag.png","hover": "images/Chapter 2/Menu/Poster hover.png","name": "フラグ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_484
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008F7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグ\"" }]):
        jump block_000018BD

    return

label block_000018BD:
    # Node: 000018BD (Poster F4)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_7C42D527AA2A48348F9A478BB5F543EC as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀——！学校里怎么会有这么下流的海报！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……欸？\n{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "仔细一看，是恋爱支援海报啊。"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A0B1A1AC4435401CBBA1DCA96F7AFD50 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我第一次看到的时候\n还以为校长那家伙终于不打算隐藏了呢——"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好呀——慎酱。\n之前你也说过我们的{color=#008080}校长有那方面的兴趣{/color}呢。{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_4CD26587C69945F4BD8974AA6AAF033A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_48C5F16710344F4F8A8167B1D88A30CD as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "对呀～\n所以我们的制服才是立领服，泳装才是三角形哦。"

    show rs_image_CB49ABE40CB34BD7AA2C8B4E5739D95A as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不过，校长的司马昭之心在道德上该怎么评判并不重要，\n重要的是陆田和杉本要来演讲！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_BE6350EE36664764B9305ACF9E0C443E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀～好期待哦～♪\n绝对要和他们握手，可能的话要合影～……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_8B48851BB9F649D9A15EC7718BAB73D5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "咳咳咳……\n{w=0.5}{nw}"
    show rs_image_89F65D8BDBED4A86BE8A3B3BDE5980B7 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哦抱歉。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没事吗～？感冒？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1F71A08D20B9486AAAD89B7E17DBDA56 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "也～许吧！最近天气很冷。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_D64DA6E75BDF4404B914047221EB0B38 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我先走了～等会见～♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.4

    $ set_place_title(_("一楼走廊"))

    if judge_lm_condition([]):
        jump block_000018BC

    return

label block_000018BC:
    # Node: 000018BC (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#008040}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002C83

    return

label block_00002C83:
    # Node: 00002C83 (Phase ++)
    $ C2S4Phase = C2S4Phase + 1

    if judge_lm_condition([]):
        jump block_000018BE

    return

label block_000018BE:
    # Node: 000018BE (Aisle 1)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (520, 253),"image": "images/Chapter 2/Menu/Poster.png","hover": "images/Chapter 2/Menu/Poster hover.png","name": "フラグ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_485
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008F7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグ\"" }]):
        jump block_000018BF

    return

label block_000018BF:
    # Node: 000018BF (Poster)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_7C42D527AA2A48348F9A478BB5F543EC as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000018BE

    return

label block_000018B8:
    # Node: 000018B8 (Aisle 3)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("三楼走廊"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_3AD71FD0B91B482CBB280A8611C2741C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4


    if judge_lm_condition([]):
        jump block_000018B9

    return

label block_000018B9:
    # Node: 000018B9 (Aisle 3)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_486
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008F7

    return

label block_00002C60:
    # Node: 00002C60 (Stairwell empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_487
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([]):
        jump block_000008CF

    return

label block_00001F2D:
    # Node: 00001F2D (Stairwell 空)
    $ sys_lm_menu_item = [{"pos": (272, 264),"image": "images/Chapter 2/Menu/Sora stairwell.png","hover": "images/Chapter 2/Menu/Sora stairwell hover.png","name": "空"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_488
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A97
    if judge_lm_condition([{ "scope": 0, "content": "TalkSoraF2 == 1" },{ "scope": 1, "content": "_lm_selected_value == \"空\"" },{ "scope": 2, "content": "C2S2Phase >= 97" }]):
        jump block_00001F2F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" },{ "scope": 1, "content": "GTsukiTestSoraMode == True" },{ "scope": 2, "content": "CXQTsukiTest == True" }]):
        jump block_00002C59
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" },{ "scope": 1, "content": "CXQTsukiTest == True" }]):
        jump block_00002C61

    return

label block_00001F2F:
    # Node: 00001F2F (空 F2選擇后)
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_9C09C82BD6C4471CA272DAF35BA5D948 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "总之试着选择了中立的话语，\n至于效果如何……"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([]):
        jump block_00001F2D

    return

label block_00002C59:
    # Node: 00002C59 (阿月測眼力)
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_8013AE5050E34D619C8668AD6A90EEB7 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "想参加训练吗？"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 5" }]):
        jump block_00002C58
    if judge_lm_condition([]):
        jump block_00002C57

    return

label block_00002C58:
    # Node: 00002C58 (阿月測眼力)
    call block_0000116E from _call_block_0000116E_3

    if judge_lm_condition([]):
        jump block_00003A93

    return

label block_00003A93:
    # Node: 00003A93 (RESET)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("楼梯间"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001F2D

    return

label block_00002C57:
    # Node: 00002C57 (選擇)
    call scb_selector("", [{"name":"はい", "content":_("走，去训练了")}, {"name":"いいえ", "content":_("我很忙的")}]) from _call_scb_selector_53

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002C58
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00001F2D

    return

label block_00002C61:
    # Node: 00002C61 (SoraMode)
    $ GTsukiTestSoraMode = True

    if judge_lm_condition([]):
        jump block_00002C56

    return

label block_00002C56:
    # Node: 00002C56 (阿月測眼力)
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_9C09C82BD6C4471CA272DAF35BA5D948 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君，稍微来一下？哥哥说有想要转达给你的事。"

    show rs_image_F761F888C5034F26880B624E1477BF17 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "以前你们一起做过训练对不对？\n但哥哥现在很忙，没时间做了。"

    show rs_image_EC040B7182804790B7750A3172C04105 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不过，这段时间我可以帮你。\n和斯巴达哥哥不同，我们可以慢慢来。"

    show rs_image_8013AE5050E34D619C8668AD6A90EEB7 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，要继续吗？"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))

    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 5" }]):
        jump block_00002C58
    if judge_lm_condition([]):
        jump block_00002C57

    return

label block_0000250A:
    # Node: 0000250A (小島 Q新聞部中)
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "之前的委托，就拜托你了。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase == 0" }]):
        jump block_00002519
    if judge_lm_condition([]):
        jump block_00002511

    return

label block_0000250B:
    # Node: 0000250B (小島 1)
    window show

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_DCBDF256A1E242E78A25910AE27C0954 at center_bottom zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "照片，要来一张吗？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可以哦！YEAH☆CHEESE☆"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "拍出来的照片如果有不错的，\n可以允许我们洗出来使用吗？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？嗯，可以。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "交涉成立。{w=0.5}\n{nw}"
    show rs_image_9E7F7ED47EEE46378763123AB08C7BA3 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那么，CHEESE。"

    pause 0.2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shoot 1.ogg"

    show rs_image_9E7F7ED47EEE46378763123AB08C7BA3 as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.6

    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "感谢配合。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_00002511

    return

label block_000008E4:
    # Node: 000008E4 (Playground)
    $ sys_lm_menu_item = [{"pos": (328, 140),"image": "images/Chapter 2/Menu/Katou.png","hover": "images/Chapter 2/Menu/Katou hover.png","name": "加藤"}, {"pos": (632, 208),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "体育倉庫"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_489
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 1, "content": "_lm_selected_value == \"加藤\"" },{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 2, "content": "TalkKatouF2 == 1" }]):
        jump block_00001F48
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" },{ "scope": 1, "content": "TalkKatouStudy == False" },{ "scope": 2, "content": "C2SG1 == True" }]):
        jump block_00002525
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" },{ "scope": 1, "content": "C2SG1 == True" }]):
        jump block_00002528
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" },{ "scope": 1, "content": "TalkKatou == 0" },{ "scope": 2, "content": "TalkKatouStudy == False" }]):
        jump block_000008ED
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" },{ "scope": 1, "content": "TalkKatou == 1" }]):
        jump block_00002524
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008D4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育倉庫\"" }]):
        jump block_000008F9

    return

label block_00001F48:
    # Node: 00001F48 (加藤 F2選擇后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_62BA2B2EFFB140ECA42DC25F7DB537B4 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_81D16F74A3C44B8982DB528D7D934850 "我对别人的那些琐事\n并不怎么感兴趣呢——"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000008E4

    return

label block_00002525:
    # Node: 00002525 (加藤 F3后 1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_CF9552A127F84B139910618B1FE71819 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_5690F6AF976C4AEB8FC348FA1E25466F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "期中考试终于结束了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呐，\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    extend "加藤酱，带{color=#FF0000}成绩单{/color}了吗？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1230EA82690842C19B5D31327B9A64D9 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "当然。{w=0.45}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_142079CDA33F4DC78D096D731F4B657B as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那么……一起亮出来。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9634AD61C6DB42439EDE1028A82EA8C9 "一、二！！"

    window hide

    pause 0.7


    if judge_lm_condition([{ "scope": 0, "content": "StudyCount > 2" }]):
        jump block_00002526
    if judge_lm_condition([]):
        jump block_00002527

    return

label block_00002526:
    # Node: 00002526 (Win)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——我赢了♪"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "呜，可恶……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("校庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002C80

    return

label block_00002C80:
    # Node: 00002C80 (T ++)
    $ TalkKatou = TalkKatou + 1
    $ TalkKatouStudy = True

    if judge_lm_condition([]):
        jump block_000008E4

    return

label block_00002527:
    # Node: 00002527 (Lose)
    if sys_music2_current_file != "sound/Effect Sound/Cute 2.ogg":
        play music2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_5690F6AF976C4AEB8FC348FA1E25466F as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.3

    window show

    rs_character_81D16F74A3C44B8982DB528D7D934850 "好的我赢了～！！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎、怎么这样～……"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002C80

    return

label block_00002528:
    # Node: 00002528 (加藤 F3后 2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_5690F6AF976C4AEB8FC348FA1E25466F as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_music2_current_file != "sound/Effect Sound/As you wish 1.ogg":
        play music2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "期中考试终于结束了～♪\n这下又能优哉游哉地过日子了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "安心还太早了。"

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Onboard 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Onboard 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Onboard 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我们还有{color=#8000FF}“期末考试”{/color}\n这么个范围更大难度更高的强敌在等着……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_62BA2B2EFFB140ECA42DC25F7DB537B4 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "唔……确实……{w=0.5}{nw}"
    show rs_image_7AF8B6819D0F4889AEC03FD7D8B3FA6F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "唔哦哦……！考试什么的\n从这个世界上消失就好了！！"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000008E4

    return

label block_000008ED:
    # Node: 000008ED (加藤 F3前 1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_36E75A5BA4504559920E625E0462334C as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_81D16F74A3C44B8982DB528D7D934850 "马上就是期中考试了，\n至少这次不能是倒数第一。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_C5C9A2538FCB4FCB827FE1BBFE20727F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "啊，反正有班长没关系。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔！这我可不能当做没听到！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "那加藤酱，下次考试一决胜负！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_581796CAD76B4C929577B4C1D581EF10 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "哦、哦，可以，如你所愿。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002C80

    return

label block_00002524:
    # Node: 00002524 (加藤 F3前 2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_CF9552A127F84B139910618B1FE71819 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_bottom zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "期中考试绝对是我赢——！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_142079CDA33F4DC78D096D731F4B657B as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "我也是有骨气的！\n{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_21A5A72FBBD8459A863B99B859A0013F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……不过赌上什么东西就算了。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000008E4

    return

label block_000008DE:
    # Node: 000008DE (Shoe cupboard 滑子 point)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}, {"pos": (160, 96),"image": "images/Menu/Nameko point.png","hover": "images/Menu/Nameko hover.png","name": "滑子"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_490
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" },{ "scope": 1, "content": "C2S2Phase >= 97" }]):
        jump block_00001F1F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A31
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_000008E3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" }]):
        jump block_0000327C

    return

label block_00001F1F:
    # Node: 00001F1F (滑子 F2)
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_D7F70E4230154502BB28D6BA8AC09D91 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "森海。你有何事？"

    pause 0.3

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『听取了滑子老师的建议』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『不愧是老师！{/color}\n{nw}"
    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "{color=#0080FF}使用{/color}{u}{color=#FF0000}相对含蓄的语言{/color}{/u}{color=#0080FF}劝说。』{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))

    if judge_lm_condition([]):
        jump block_00001F20

    return

label block_00001F20:
    # Node: 00001F20 (選擇)
    call scb_selector(_("这种意见可否？"), [{"name":"はい", "content":_("就是这个")}, {"name":"いいえ", "content":_("太微妙了，算了")}]) from _call_scb_selector_54

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002C70
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_000008DE

    return

label block_00002C70:
    # Node: 00002C70 (TF2)
    $ TalkNamekoF2 = 1

    if judge_lm_condition([]):
        jump block_00003A36

    return

label block_00003A36:
    # Node: 00003A36 (FLAG: CP2F2)
    call block_00003A0E from _call_block_00003A0E_5

    if judge_lm_condition([]):
        jump block_00003A31

    return

label block_0000327C:
    # Node: 0000327C (Confirm)
    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『即将进入{/color}{color=#FF0080}下一个章节{/color}{color=#0080FF}。{/color}{w}\n{color=#0080FF}通关前回不来了，确定要继续？』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_0000327D

    return

label block_0000327D:
    # Node: 0000327D (選擇)
    call scb_selector("", [{"name":"はい", "content":_("没问题")}, {"name":"いいえ", "content":_("还有其他事情没做完")}]) from _call_scb_selector_55

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003C5E
    if judge_lm_condition([]):
        jump block_000008DE

    return

label block_00003C5E:
    # Node: 00003C5E ()
    $ del PianoRandom

    return

label block_00001F21:
    # Node: 00001F21 (Shoe cupboard)
    $ sys_lm_menu_item = [{"pos": (160, 96),"image": "images/Menu/Nameko.png","hover": "images/Menu/Nameko hover.png","name": "滑子"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_491
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" },{ "scope": 1, "content": "TalkNamekoF2 == 1" },{ "scope": 2, "content": "C2S2Phase >= 97" }]):
        jump block_00001F2E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_000008E3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A34
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" }]):
        jump block_000024F9

    return

label block_00001F2E:
    # Node: 00001F2E (滑子 F2選擇后)
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_9C78AB751CDB49FDA83251FA5B4A3825 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "或许我的言辞有些过于苦涩了。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))

    if judge_lm_condition([]):
        jump block_00001F21

    return

label block_000024F9:
    # Node: 000024F9 (滑子)
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 200
    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "有时间记得回来，我有话对你说。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))

    if judge_lm_condition([]):
        jump block_00001F21

    return

label block_00003A03:
    # Node: 00003A03 (TO: Atrium)

    if judge_lm_condition([]):
        jump block_000008D6

    return

label block_000008D6:
    # Node: 000008D6 (Atrium)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 1, "content": "TalkMatsutaF2 == 1" }]):
        jump block_00001F41
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 1, "content": "TalkMatsutaF2 == 0" }]):
        jump block_00000922
    if judge_lm_condition([{ "scope": 0, "content": "F2Check1 == True" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 0, "content": "C2S2Phase == 1" }]):
        jump block_0000252F
    if judge_lm_condition([]):
        jump block_000008E0

    return

label block_00001F41:
    # Node: 00001F41 (Atrium 松田)
    $ sys_lm_menu_item = [{"pos": (216, 168),"image": "images/Chapter 2/Menu/F2/Matsuta.png","hover": "images/Chapter 2/Menu/F2/Matsuta hover.png","name": "松田"}, {"pos": (488, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "食堂へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_492
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_00001F3F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"食堂へ\"" }]):
        jump block_000008F1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A08

    return

label block_00001F3F:
    # Node: 00001F3F (松田 F2選擇后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_21F3DA87B080401888872AA61FC24963 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "作哉虽然有时不太靠谱，\n但本质上是个好家伙。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001F41

    return

label block_000008F1:
    # Node: 000008F1 (Canteen)
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
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D138810390DC4843A14969EAD39A7E06 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2QKimuraConference == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "(TalkKimuraF3After == True) or ((TalkKimura > 0) and (TalkItou > 0))" },{ "scope": 3, "content": "(C2QNewsclubPhase == 1 ) or (FNewsclub == False)" },{ "scope": 4, "content": "TalkTsubasa > 0" },{ "scope": 4, "content": "F2Check1 == True" },{ "scope": 4, "content": "C2S2 == True" }]):
        jump block_00002539
    if judge_lm_condition([]):
        jump block_000008F2

    return

label block_00002539:
    # Node: 00002539 (Canteen 木村 quest)
    $ sys_lm_menu_item = [{"pos": (224, 171),"image": "images/Chapter 2/Menu/Itou.png","hover": "images/Chapter 2/Menu/Itou hover.png","name": "伊藤"}, {"pos": (401, 171),"image": "images/Chapter 2/Menu/Kimura quest.png","hover": "images/Chapter 2/Menu/Kimura hover.png","name": "木村"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_493
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008D6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" },{ "scope": 1, "content": "C1QKimuraConference == False" }]):
        jump block_00002533
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_00002536
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_00002543

    return

label block_00002533:
    # Node: 00002533 (木村討論 1)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_692C028CA3784566A15437BC68BB11B1 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
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
    show rs_image_EB52490B1A0A4E33BC3D00AD5EFD78E1 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
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

    $ set_place_title(_("食堂"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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


    if judge_lm_condition([]):
        jump block_00002534

    return

label block_00002534:
    # Node: 00002534 (木村討論會)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_EB8CA9E15D764183BA75236D61684ECB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}{color=#FFFF00}～木村的热血讨论室～{/color}{/size}\n{size=15}{color=#00FFFF}〈{/color}{/size}{color=#00FFFF}主持{/color}{size=15}{color=#00FFFF}〉{/color}{/size}{color=#00FFFF}木村树·伊藤圭 {/color}{size=15}{color=#00FFFF}〈{/color}{/size}{color=#00FFFF}嘉宾{/color}{size=15}{color=#00FFFF}〉{/color}{/size}{color=#00FFFF}森海友・一之濑翼・小岛正{/color}\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    extend "今日主题{color=#FF0000}『如果穿越到《大逃杀》的世界里，你会怎么做？』{/color}"

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.8

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "大、大逃杀是、那本恐怖小说？\n全班所有人残杀到最后只剩一个……"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_8A8399081EA34489AD19EAD1C673B291 as tag_DCBDF256A1E242E78A25910AE27C0954 at right_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_53FF68C192E3494AB005C1909579AFFB "在无人岛，所有人佩戴定位和处决用首环，\n使用随机配发的武器互相残杀。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_5A94C5E893564B9E8154C0AACF4B7DD1 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "好阴暗……好选不选偏偏选这个话题。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "不是很激动嘛！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "呃……你有时也真残酷。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_5A94C5E893564B9E8154C0AACF4B7DD1 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过，妄想的话怎么都好吧？我也来稍微考虑考虑。"

    show rs_image_7FBD6043466E42E3AC6ECBFECEBB3005 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "就是！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_51D4DEBA46FA459DA3B4413148F30900 as tag_0999797A178545CBA5F244F41BBA50B1 at Transform(xpos=470, yalign=0.0) zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_5A94C5E893564B9E8154C0AACF4B7DD1 as tag_2C4A74BADF6540698EF3E9A300893D1A at Transform(xpos=280, yalign=0.0) zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "怎样才好……如、如果真的发生那种事……\n我、我肯定会被第一个杀掉的……"

    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "妄想就稍微把自己加强一点啊……\n不过确实也不像是能活到最后的样子。"

    show rs_image_7FBD6043466E42E3AC6ECBFECEBB3005 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "我在想象中就要是无敌的——！\n猫山什么的一击必杀♪"

    show rs_image_D76820B84EB8486B8205116A7D46FEFC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "好像能理解，毕竟那家伙很单纯。\n在这一点上作哉过于聪明就很棘手了……"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_B97A3992A1D24282B85B44E0C876F034 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2B83F7F0083847759939BD6D74C58A5C as tag_DCBDF256A1E242E78A25910AE27C0954 at center_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_53FF68C192E3494AB005C1909579AFFB "不管是谁都不许动部长……部长肯定缩在角落里瑟瑟发抖，得尽快找出来。\n"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "……{w=0.4}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_80B4A131E4C34A6CBC5E5CB41217043C as tag_DCBDF256A1E242E78A25910AE27C0954 zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "不知能不能带相机。"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_9E6AF824075F4EB3B240BE13A1C54165 as tag_DCBDF256A1E242E78A25910AE27C0954 at left_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……你到底想拍什么……？"

    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_CF5AA529110045B9AA052BA9023E6FA3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "如果拿到的是近身武器肯定很快就被干掉了……\n不过，正因为是这种时候说不定只会给我一根叉子。"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_82BA14DF187F4770B2333382BE5C5B0C as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "那一之濑干脆和厉害的人组队不就行了。\n"
    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不巧的是我的队友一如既往是伊藤酱！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_5A94C5E893564B9E8154C0AACF4B7DD1 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "啊、啊？擅自决定什么？\n感觉你关键时候会背叛所以不要。"

    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "想多了啦——！别把我和穗海混为一谈，肯定至死都会保护伊藤的♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔……你的这种地方实在太狡猾了{size=16}。{/size}"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_328406EB66B449C99EAA3BC3E5C0EE95 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_8A8399081EA34489AD19EAD1C673B291 as tag_DCBDF256A1E242E78A25910AE27C0954 at right_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_53FF68C192E3494AB005C1909579AFFB "我会誓死保卫部长。不过，可能的话还是要脱离战场。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我、我也不想互相残杀。\n"
    show rs_image_20D50D7E2029427A96A2E0A6E34FC3DD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "要是有能一起逃走的伙伴……{w=0.4}{nw}"
    show rs_image_8791FBC16EE045C8A5316E8761B3EC61 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_5465258BCE404B519910FD1F4172107B as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔唔……班级不同插不上话。"

    show rs_image_8DC6F44BF4644738BCD14828D87C2679 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我们班的话，忍肯定会保护我。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "月和空很麻烦，有没有武器都强得要命。"

    show rs_image_C528CA6C6F534006B6F789027BE5C781 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过，这也会成为众矢之的呐。看准这个或许我还有胜算……"

    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过慎酱这样扮猪吃老虎的也不能大意。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "加藤酱、松田亲也都很强。泉君生气起来也一样。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_EFDC09B34577437A8D2B581A3FFFC9E4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜欸，感觉我死定了。忍不在完全没戏唱啊，这个。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9B9F6DFAAEB44A1FB0A65329C35C3541 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at left_top zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友、友君就由我来……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_E436CC5ED79D41EABE3ADFC40CD9F8B8 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我们不一个班。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DD2B6D134E374D149ADE7F976BF51DC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "打击——"

    window hide

    pause 0.8

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_EB8CA9E15D764183BA75236D61684ECB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.7

    window show

    rs_character_AD6884D862D5471D848B1D3473E23458 "……"

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.35

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 200
    show rs_image_8A8399081EA34489AD19EAD1C673B291 as tag_DCBDF256A1E242E78A25910AE27C0954 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "越想越觉得前途无亮了。"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "气氛都这样了你怎么负责？木村。"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_5A94C5E893564B9E8154C0AACF4B7DD1 as tag_2C4A74BADF6540698EF3E9A300893D1A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "唔……可是，本想最近看了那个电影后想让大家高兴高兴的。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哭……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7D82D2EF95ED49EA821B9751FF70275C as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你看——！翼君都感情代入过度哭起来了——！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_F82BC248415F46ACBF47A770CDE09E67 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "没、没事！本来就是假设！\n不要在意不要在意！大家都活着没关系！"

    rs_character_710A38AC94C841779DB701B5AC1010FD "这解释也太牵强了……\n"
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_98508F03C2B54E6595F99F669212CD79 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……算了，这次就到这里好了。"

    rs_character_710A38AC94C841779DB701B5AC1010FD "谢谢大家前来讨论——"

    window hide

    pause 0.9

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 2.5

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00002CB3

    return

label block_00002CB3:
    # Node: 00002CB3 (C2Q木村討論)
    $ C2QKimuraConference = True
    $ TalkKimuraQKimuraAfter = True

    if judge_lm_condition([]):
        jump block_00002535

    return

label block_00002535:
    # Node: 00002535 (QUEST FINISH)
    $ set_window("(標準)")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_00003A06

    return

label block_00002536:
    # Node: 00002536 (木村討論 2)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_692C028CA3784566A15437BC68BB11B1 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦，森海！今天放学后有空吗？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，有空哦～"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_99320781054948949BEB08A8AC3E7437 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "好像又要弄什么讨论会了。能奉陪一下吗？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "上次的很开心很热闹很好哦！我去我去！"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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


    if judge_lm_condition([]):
        jump block_00002534

    return

label block_00002543:
    # Node: 00002543 (伊藤 １)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    window show

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_99320781054948949BEB08A8AC3E7437 as tag_0999797A178545CBA5F244F41BBA50B1 at center_bottom zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "御咲某澡堂附近似乎有\n{color=#808000}祈愿就能做到想做的梦{/color}的神社，\n知道吗？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊——嗯，好像是从岔道右拐。{w}\n至于传说本身听没听过就不记得了。\n伊藤君有想祈愿的事？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E191791210724EEA9502E62AF8CDEDD5 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "我、我并没有……再说我也不住在这一带，\n传说也很可疑，才不会去呢。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "TalkItou == 0" }]):
        jump block_00002CB2
    if judge_lm_condition([{ "scope": 0, "content": "C2QKimuraConference == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "(TalkKimuraF3After == True) or ((TalkKimura > 0) and (TalkItou > 0))" },{ "scope": 3, "content": "(C2QNewsclubPhase == 1 ) or (FNewsclub == True)" },{ "scope": 4, "content": "TalkTsubasa > 0" },{ "scope": 4, "content": "F2Check1 == True" },{ "scope": 4, "content": "C2S2 == True" }]):
        jump block_00002539
    if judge_lm_condition([]):
        jump block_000008F2

    return

label block_00002CB2:
    # Node: 00002CB2 (T ++)
    $ TalkItou = TalkItou + 1

    if judge_lm_condition([{ "scope": 0, "content": "C2QKimuraConference == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "(TalkKimuraF3After == True) or ((TalkKimura > 0) and (TalkItou > 0))" },{ "scope": 3, "content": "(C2QNewsclubPhase == 1 ) or (FNewsclub == True)" },{ "scope": 4, "content": "TalkTsubasa > 0" },{ "scope": 4, "content": "F2Check1 == True" },{ "scope": 4, "content": "C2S2 == True" }]):
        jump block_00002539
    if judge_lm_condition([]):
        jump block_000008F2

    return

label block_000008F2:
    # Node: 000008F2 (Canteen)
    $ sys_lm_menu_item = [{"pos": (224, 171),"image": "images/Chapter 2/Menu/Itou.png","hover": "images/Chapter 2/Menu/Itou hover.png","name": "伊藤"}, {"pos": (401, 171),"image": "images/Chapter 2/Menu/Kimura.png","hover": "images/Chapter 2/Menu/Kimura hover.png","name": "木村"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_494
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008D6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" },{ "scope": 1, "content": "TalkKimuraQKimuraAfter == True" }]):
        jump block_00002532
    if judge_lm_condition([{ "scope": 0, "content": "C2S3 == True" },{ "scope": 1, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_000025F9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_000025FA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_00002543

    return

label block_00002532:
    # Node: 00002532 (木村討論會後)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_48D8C5CECCB84B739099EE1FBE060B20 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "以后再发现什么有趣的话题记得要再来。多多指教了♪"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F34

    return

label block_00002F34:
    # Node: 00002F34 (END: TalkQAfter)
    $ TalkKimuraQKimuraAfter = False

    if judge_lm_condition([]):
        jump block_000008F2

    return

label block_000025F9:
    # Node: 000025F9 (木村 F3后)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_692C028CA3784566A15437BC68BB11B1 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "知道吗？伊藤按摩超级好的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那种“按摩”？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1990EB79915C41699DBA3A20A151B949 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "嗯～……\n{w=0.5}{nw}"
    show rs_image_48D8C5CECCB84B739099EE1FBE060B20 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……呵呵♪不告诉你——♪"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("食堂"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F35

    return

label block_00002F35:
    # Node: 00002F35 (END: TalkF3After)
    $ TalkKimuraF3After = True

    if judge_lm_condition([{ "scope": 0, "content": "C2QKimuraConference == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "(TalkKimuraF3After == True) or ((TalkKimura > 0) and (TalkItou > 0))" },{ "scope": 3, "content": "(C2QNewsclubPhase == 1 ) or (FNewsclub == True)" },{ "scope": 4, "content": "TalkTsubasa > 0" },{ "scope": 4, "content": "F2Check1 == True" },{ "scope": 4, "content": "C2S2 == True" }]):
        jump block_00002539
    if judge_lm_condition([]):
        jump block_000008F2

    return

label block_000025FA:
    # Node: 000025FA (木村 1)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_692C028CA3784566A15437BC68BB11B1 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_bottom zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "知道吗？伊藤按摩超级好的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那种“按摩”？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AD32BE71FC11444A8598BBF482AF95D0 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊？为什么我必须要和伊藤做那种事啊？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "TalkKimura == 0" }]):
        jump block_00002CB0
    if judge_lm_condition([]):
        jump block_000008F2

    return

label block_00002CB0:
    # Node: 00002CB0 (T ++)
    $ TalkKimura = TalkKimura + 1

    if judge_lm_condition([{ "scope": 0, "content": "C2QKimuraConference == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "(TalkKimuraF3After == True) or ((TalkKimura > 0) and (TalkItou > 0))" },{ "scope": 3, "content": "(C2QNewsclubPhase == 1 ) or (FNewsclub == False)" },{ "scope": 4, "content": "TalkTsubasa > 0" },{ "scope": 4, "content": "F2Check1 == True" },{ "scope": 4, "content": "C2S2 == True" }]):
        jump block_00002539
    if judge_lm_condition([]):
        jump block_000008F2

    return

label block_00003A08:
    # Node: 00003A08 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A09

    return

label block_00000922:
    # Node: 00000922 (Atrium 松田 point)
    $ sys_lm_menu_item = [{"pos": (216, 168),"image": "images/Chapter 2/Menu/F2/Matsuta point.png","hover": "images/Chapter 2/Menu/F2/Matsuta hover.png","name": "松田"}, {"pos": (488, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "食堂へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_495
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A09
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"食堂へ\"" }]):
        jump block_000008F1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_00001F40

    return

label block_00001F40:
    # Node: 00001F40 (松田 F2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_BBE22F28F7C241C09F36BBC37FAD09EF as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "怎么了？"

    pause 0.3

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『听取了松田的建议。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『用看破一切的{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    extend "{u}{color=#FF0000}装帅言论{/color}{/u}{color=#0080FF}。』{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001F3E

    return

label block_00001F3E:
    # Node: 00001F3E (選擇)
    call scb_selector(_("这种意见可否？"), [{"name":"はい", "content":_("就是这个")}, {"name":"いいえ", "content":_("太微妙了，算了")}]) from _call_scb_selector_56

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002C6A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00000922

    return

label block_00002C6A:
    # Node: 00002C6A (TF2)
    $ TalkMatsutaF2 = 1

    if judge_lm_condition([]):
        jump block_00003A2A

    return

label block_00003A2A:
    # Node: 00003A2A (FLAG: CP2F2)
    call block_00003A0E from _call_block_00003A0E_6

    if judge_lm_condition([]):
        jump block_00003A0A

    return

label block_00003A0A:
    # Node: 00003A0A (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A07

    return

label block_0000252F:
    # Node: 0000252F (Atrium empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (488, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "食堂へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_496
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"食堂へ\"" }]):
        jump block_000008F1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A0A

    return

label block_000008E0:
    # Node: 000008E0 (Atrium)
    $ sys_lm_menu_item = [{"pos": (216, 160),"image": "images/Chapter 2/Menu/Tsubasa.png","hover": "images/Chapter 2/Menu/Tsubasa hover.png","name": "つばさ"}, {"pos": (488, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "食堂へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_497
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"食堂へ\"" }]):
        jump block_000008F1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A07
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "TalkTsubasa == 0" },{ "scope": 2, "content": "FEnterMisaki == True" }]):
        jump block_00000900
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "TalkTsubasaF6After == True" },{ "scope": 2, "content": "C2S6 == True" }]):
        jump block_000025FB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "C2S6 == True" },{ "scope": 2, "content": "FTheater == True" },{ "scope": 3, "content": "SYSTheaterState == 0" }]):
        jump block_000025FC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "C2S6 == True" },{ "scope": 2, "content": "SYSTheaterState == 0" }]):
        jump block_00002CA1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "C2SG1 == True" }]):
        jump block_00002544
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_00002523

    return

label block_00000900:
    # Node: 00000900 (翼 僅第一天)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_43C2A5DA4B5D4815BEC6FE1DA10014AC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——翼君，就算是冬装\n也穿着那件{color=#0080FF}连帽衫{/color}呐！\n我好高兴哦～"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D80600428DE9483E933DA406C9D3E860 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呃？翼、翼君？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_43C2A5DA4B5D4815BEC6FE1DA10014AC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_C1F668B282CC46B789CFCE1FCEC65D91 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    extend "那件{color=#FF0000}制服{/color}不是友君的……？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0EFDF296FEF54F7EA386A8FE035AF6F6 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    $ record_volume("music")
    $ renpy.music.set_volume(0.3, 1, "music")

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "为什么会穿着别人的制服？到底是谁的！？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好、好吓人啊翼君，怎么了？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "赶快回答。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这、这个是，很不好意思……\n今天错穿夏季制服来了，\n所以这是学校的备用品。"

    stop music2 fadeout 0.5
    $ sys_music2_current_file = ""

    $ reverse_volume("music", 1)

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_73951BCA78C0428BB2D52C4797A62C65 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊！原来是这么回事♪{w}\n只是因为闻到了不认识的人的气味\n觉得有些不可思议而已而已——"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦、哦，这样。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "话说回来，翼君好厉害，像狗一样。{w}\n要是练习练习的话说不定将来\n能干搜索取缔之类的活呐。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AD8CFA3B3632464BA96A924CD8D32A10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "才、才没有那种事，友君太夸张了，真是的。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002CB5

    return

label block_00002CB5:
    # Node: 00002CB5 (T ++)
    $ TalkTsubasa = TalkTsubasa + 1

    if judge_lm_condition([]):
        jump block_000008E0

    return

label block_000025FB:
    # Node: 000025FB (翼 F6后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_43C2A5DA4B5D4815BEC6FE1DA10014AC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_A2F9611E37CC476881256D2E6C30C824 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "上次和大家的旅行真的好开心呐。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！下次我想住迪士尼的酒店哦！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "呐——呐翼君，带我去好不好♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_65886B0DDD844CEF8CB130AC05A09545 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸！？\n"
    show rs_image_2D653ACAC4114F1FA9CBB39313FD6DE6 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_7297399DE0AD4C0CACC8C112084265D4 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "我、我明白了！我一定会努力赚钱，\n争取住到最好的房间去的！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——♪"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002CBB

    return

label block_00002CBB:
    # Node: 00002CBB (END: TalkF6After)
    $ TalkTsubasaF6After = False

    if judge_lm_condition([]):
        jump block_000008E0

    return

label block_000025FC:
    # Node: 000025FC (翼 Theater前)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5D1EEF7ED1114B3CAF82F382C1E2C4FD as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那个！\n{w=0.5}{nw}"
    show rs_image_2D653ACAC4114F1FA9CBB39313FD6DE6 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    show rs_image_3FFA42ECEDF14A378835CC5A7CEED291 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "现、现在伊丹咲的电影院\n好像在上映怀旧电影的样子……"

    show rs_image_0F5C9B2402F04E08BC3A24C710BFD9A7 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "似乎会播放以前曾流行过的电影……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_057319E958AE4B53908D6017D73C94AD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可、可以的话，下次我们两个一起去如何！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#FF0000}事件回想模式{/color}{color=#0080FF}可以使用了。\n在本章结束前只要和翼说一下话就可以前去观看。』{/color}"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F3B

    return

label block_00002F3B:
    # Node: 00002F3B (Cancel: First)
    $ FTheater = False
    $ persistent.SystemStoryCache[17] = True

    if judge_lm_condition([]):
        jump block_000008E0

    return

label block_00002CA1:
    # Node: 00002CA1 (Theater)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_1236DDA666C34A83B4ECECC6FDFC4485 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "要、要一起去看电影吗？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002CA2

    return

label block_00002CA2:
    # Node: 00002CA2 (選擇)
    call scb_selector("", [{"name":"はい", "content":_("一起去吧，翼君")}, {"name":"いいえ", "content":_("稍等现在有点事")}]) from _call_scb_selector_57

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002CA3
    if judge_lm_condition([]):
        jump block_000008E0

    return

label block_00002CA3:
    # Node: 00002CA3 (Theater)
    call block_0000213F from _call_block_0000213F_2

    if judge_lm_condition([]):
        jump block_00003A06

    return

label block_00002544:
    # Node: 00002544 (翼 F3后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_43C2A5DA4B5D4815BEC6FE1DA10014AC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼——君♪今天放学后一起去小钢琴部如何！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AF599E6EDE544FB39C2A38FD087F28F0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，对、对不起，今天有些事……\n和作哉君有些饲养上问题。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……这就只能放弃了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "果然啊，一旦开始这样的工作，\n就基本不会来小钢琴部了呢。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A0CA177675C9430E9CA86665FB37D470 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个……也许会也许不会……\n对不起，我还不清楚……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嫉妒……！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_56A9AF7A39F14E9D8BB98BE49AEEBE8D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嫉妒？"

    if sys_music2_current_file != "sound/Effect Sound/Attack 1.ogg":
        play music2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……什、什么都没有！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000008E0

    return

label block_00002523:
    # Node: 00002523 (翼 F3前)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_43C2A5DA4B5D4815BEC6FE1DA10014AC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_3FFA42ECEDF14A378835CC5A7CEED291 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "马上就是期中考试了，{w}\n友君觉得能考多少？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈。一如既往勉强过关哦～♪"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AF599E6EDE544FB39C2A38FD087F28F0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸、欸——这样啊。\n{w=0.3}{nw}"
    show rs_image_0F5C9B2402F04E08BC3A24C710BFD9A7 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "其实我也差不多……"

    show rs_image_324DBD0B16974C3883A8BF2FC87EBF3D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这次我们要一起避免犯上一学期那样的错误呢。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "上一学期？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2D653ACAC4114F1FA9CBB39313FD6DE6 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "就是{color=#008080}在我家学习，但结果考试范围完全不对，\n最后分数很低{/color}的那件事。{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_D1E91FE8CFCC41A0AABF259092C4D66F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊啊啊啊！那个黑历史！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜～不要让我想起来～！\n那件事再一次让我意识到了自己就应有多么蠢。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3FFA42ECEDF14A378835CC5A7CEED291 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哈哈……不过失败是成功之母，\n至少经验能为我们所用……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君，就算再怎么乐观\n那种大失败不是说一次都不能有，\n而是作为人就不该犯才对……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_43C2A5DA4B5D4815BEC6FE1DA10014AC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……说的也是。\n就算自己拿无可奈何当借口也没法信服。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "TalkTsubasa == 0" }]):
        jump block_00002CB5
    if judge_lm_condition([]):
        jump block_000008E0

    return

label block_00003A2D:
    # Node: 00003A2D (TO: Gym outside)

    if judge_lm_condition([]):
        jump block_000008D5

    return

label block_000008D5:
    # Node: 000008D5 (Gym outside)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000008DF

    return

label block_000008DF:
    # Node: 000008DF (Gym outside)
    $ sys_lm_menu_item = [{"pos": (168, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "体育館へ"}, {"pos": (416, 208),"image": "images/Chapter 2/Menu/Sato.png","hover": "images/Chapter 2/Menu/Sato hover.png","name": "　佐藤"}, {"pos": (664, 280),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "柔道場へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_498
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A09
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" }]):
        jump block_000008E5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"　佐藤\"" },{ "scope": 1, "content": "TalkSatou == 0" }]):
        jump block_00000905
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"　佐藤\"" },{ "scope": 1, "content": "TalkSatou == 1" }]):
        jump block_00000918
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"柔道場へ\"" }]):
        jump block_00000A04

    return

label block_000008E5:
    # Node: 000008E5 (Gym)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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


    if judge_lm_condition([{ "scope": 0, "content": "TalkIzumiF2 == 1" },{ "scope": 1, "content": "C2S2Phase >= 97" }]):
        jump block_00001F45
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" }]):
        jump block_00001F46
    if judge_lm_condition([]):
        jump block_000008E6

    return

label block_00001F45:
    # Node: 00001F45 (Gym 泉)
    $ sys_lm_menu_item = [{"pos": (296, 208),"image": "images/Chapter 2/Menu/Izumi.png","hover": "images/Chapter 2/Menu/Izumi hover.png","name": "泉"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_499
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_00001F43
    if judge_lm_condition([]):
        jump block_00003A0C

    return

label block_00001F43:
    # Node: 00001F43 (泉 F2選擇后)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_6B3637450A254E26B3FE58D8EA24C639 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "好、好像确实一直在说自己的事……抱歉。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_00001F45

    return

label block_00003A0C:
    # Node: 00003A0C (TO: Gym outside)

    if judge_lm_condition([]):
        jump block_00003A0B

    return

label block_00003A0B:
    # Node: 00003A0B (TO: Gym outside)

    if judge_lm_condition([]):
        jump block_000008D5

    return

label block_00001F46:
    # Node: 00001F46 (Gym 泉 point)
    $ sys_lm_menu_item = [{"pos": (226, 206),"image": "images/Chapter 2/Menu/Izumi point.png","hover": "images/Chapter 2/Menu/Izumi hover.png","name": "泉"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_500
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_00001F44
    if judge_lm_condition([]):
        jump block_00003A0C

    return

label block_00001F44:
    # Node: 00001F44 (泉 F2)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_4CAFD25A1F5E4405A36AFD06AA87C091 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "有什么事吗？"

    pause 0.3

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『听取了泉的建议』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『使用结合自身经验的{/color}{u}{color=#FF0000}夹杂个人意愿{/color}{/u}{color=#0080FF}的话语』{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_00001F42

    return

label block_00001F42:
    # Node: 00001F42 (選擇)
    call scb_selector(_("这种意见可否？"), [{"name":"はい", "content":_("就是这个")}, {"name":"いいえ", "content":_("太微妙了，算了")}]) from _call_scb_selector_58

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00001F46
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002C6B

    return

label block_00002C6B:
    # Node: 00002C6B (TF2)
    $ TalkIzumiF2 = 1

    if judge_lm_condition([]):
        jump block_00003A2B

    return

label block_00003A2B:
    # Node: 00003A2B (FLAG: CP2F2)
    call block_00003A0E from _call_block_00003A0E_7

    if judge_lm_condition([]):
        jump block_00003A08

    return

label block_000008E6:
    # Node: 000008E6 (Gym)
    $ sys_lm_menu_item = [{"pos": (226, 206),"image": "images/Chapter 2/Menu/Izumi.png","hover": "images/Chapter 2/Menu/Izumi hover.png","name": "泉"}, {"pos": (432, 202),"image": "images/Chapter 2/Menu/Matsuta.png","hover": "images/Chapter 2/Menu/Matsuta hover.png","name": "松田"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_501
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A0C
    if judge_lm_condition([{ "scope": 0, "content": "TalkIzumiF3After == True" },{ "scope": 1, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_000027DB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" },{ "scope": 1, "content": "TalkMatsuta == 0" }]):
        jump block_000008E8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" },{ "scope": 1, "content": "TalkMatsuta == 1" }]):
        jump block_0000091A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" },{ "scope": 1, "content": "TalkIzumi == 0" }]):
        jump block_000008E9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" },{ "scope": 1, "content": "TalkIzumi == 1" }]):
        jump block_00002541

    return

label block_000027DB:
    # Node: 000027DB (泉 F3后)
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_6B3637450A254E26B3FE58D8EA24C639 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "唔，人际关系真麻烦……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！没、没事吗？我们班怎么了？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_EA61128A65AE41848AF5DFBA1B1E3F4E as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "不不，不是这个意思。\n该说是自己的事还是别的什么。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_78EAE7781AEB4E259E9665DF655EBB18 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "抱歉让你担心了。\n我不更加成熟是不行的呐。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_000008E6

    return

label block_000008E8:
    # Node: 000008E8 (松田 1)
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_BBE22F28F7C241C09F36BBC37FAD09EF as tag_724406A84D7141298EFF0D864FAE1534 at center_bottom zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_36FA043A9D13453B8E531655A8BDDE10 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "啊——想去卡拉OK了——"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "松田亲想唱什么？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F74587AF3C5D4336B5497ADD0EDFD9BA as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "最近喜欢上外国音乐了。\n听多了那些就觉得J-POP什么的都太逊了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——什么意思——\n可是松田亲英语很烂，能听明白么？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_21F3DA87B080401888872AA61FC24963 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "不是那个问题。\n那些音乐该说是很先进，还是旋律很好……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "？？？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3D04A5D178044F04B357189727365274 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "……{w=0.4}{nw}"
    show rs_image_BBE22F28F7C241C09F36BBC37FAD09EF as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "比如说，班长在听广告背景的时候\n觉得好的也不会记住全部歌词对不对。\n能明白么？都是一样的。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦——这个意思。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F74587AF3C5D4336B5497ADD0EDFD9BA as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "再说了，现在这个时代真想翻译上网就行！"
    show rs_image_8044151835FD439999F1BE883381A5CC as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "\n确实要自己唱是很困难……"

    show rs_image_36FA043A9D13453B8E531655A8BDDE10 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "上次去唱歌除我之外全都唱的传统音乐。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那很普通哦——\n对了，当时是和谁一起去的？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D2AEEBD45B8A4EA28C01CA659F7995E6 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "上次是作哉。唱了超〇限荷〇蒙的《ぶっ生き返す!!》。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！那首嘶喊曲！？那种歌真的能唱！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "再说了，会那么唱歌的技安完全无法想象……\n明明一直都一副唯我独尊的样子。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BBE22F28F7C241C09F36BBC37FAD09EF as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "嗯～还有二班的佐藤也不错，\n他唱了南〇之星的《TSUNAMI》。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好深奥……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F74587AF3C5D4336B5497ADD0EDFD9BA as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "本来就是这种歌。\n不过还是上一首卖得更好，气氛更好。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊——说起来，\n我们班那些人好像也是这种感觉。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D2AEEBD45B8A4EA28C01CA659F7995E6 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "绫濑、奥村和赤峰兄弟，\n还有班长，下次要不要一起去？"

    if sys_music2_current_file != "sound/Effect Sound/Cute 1.ogg":
        play music2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——！要去——！"

    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_00000943

    return

label block_00000943:
    # Node: 00000943 (T ++)
    $ TalkMatsuta = TalkMatsuta + 1

    if judge_lm_condition([]):
        jump block_000008E6

    return

label block_0000091A:
    # Node: 0000091A (松田 2)
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_BBE22F28F7C241C09F36BBC37FAD09EF as tag_724406A84D7141298EFF0D864FAE1534 at center_bottom zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "社团活动时经常会听到吹奏乐部那边的练习。"

    show rs_image_F74587AF3C5D4336B5497ADD0EDFD9BA as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "最近听到的好像是一首很不错的Jazz。"

    show rs_image_36FA043A9D13453B8E531655A8BDDE10 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "下次让部员去问问曲名买CD。\n不过，吹奏乐的CD在TSURUYA有卖么……？"

    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_000008E6

    return

label block_000008E9:
    # Node: 000008E9 (泉 1)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_4CAFD25A1F5E4405A36AFD06AA87C091 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "我以前从没去过卡拉OK，\n上次被松田君和加藤君拉去了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_D668AB5BCE7641D598E5B719952F1E93 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "感觉还不错。能发散压力，心情也很好♪\n"
    show rs_image_A886E64725024E519334B46B47F7F928 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "然后，隔壁的客人好像很兴奋的样子。"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "暗中观察了一下是SUMIRE学园的学生。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_0364D19042AC45CCA8C6BF99EF5EA070 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "『这才是男人～♪』『英雄啊～♪』之类的\n{w=0.55}{nw}"
    show rs_image_D668AB5BCE7641D598E5B719952F1E93 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "唱的热火朝天。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——我以为那所学校全是有钱人家的大少爷。\n原来也有这种类型的啊——"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "而且选曲也太有趣了。\n肯定很憧憬{color=#FF00FF}英雄(H-ERO){/color}吧？"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_00002542

    return

label block_00002542:
    # Node: 00002542 (T ++)
    $ TalkIzumi = TalkIzumi + 1

    if judge_lm_condition([]):
        jump block_000008E6

    return

label block_00002541:
    # Node: 00002541 (泉 2)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_4CAFD25A1F5E4405A36AFD06AA87C091 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "商店街中段那个家庭餐馆\n真的全都是御咲的学生呢。"

    show rs_image_EA61128A65AE41848AF5DFBA1B1E3F4E as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "我有时也会和只打算喝饮料的朋友一起去不过，\n果然影响不好。不知道其他客人会怎么想。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆"))

    if judge_lm_condition([]):
        jump block_000008E6

    return

label block_00000905:
    # Node: 00000905 (佐藤 1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_2E24765C23544B69A9391DC51FE38194 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_bottom zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_F454E39E17AB417EAFAD03FC09D7C631 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "上次参加社团活动的晨练的时候\n在电车里睡过头一路到了武咲尾呢——"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊——！{color=#008080}我也有过{/color}！超难堪呐。\n那个车站在山里，下车后就有种\n“这是什么地方，我是谁！？”的感觉。{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_48B5CDA0C23A4D5AA6C1F66CBC462D3D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C9047B9706654C6F9372CB3D04713DD6 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "这种做错事的感觉真的很糟。\n"
    show rs_image_0ED56A8EA704458D9455AFBC4C60221F as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "确实，错的是我。\n可被走路十分钟就能到的家伙说教……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_F454E39E17AB417EAFAD03FC09D7C631 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "总觉得有些不服气。\n不，错肯定在我！{w}\n可不知为何就是觉得不舒服。尽管错的是我。"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000947

    return

label block_00000947:
    # Node: 00000947 (T ++)
    $ TalkSatou = TalkSatou + 1

    if judge_lm_condition([]):
        jump block_000008DF

    return

label block_00000918:
    # Node: 00000918 (佐藤２)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 300
    show rs_image_BB8AF3FC831D491CB97BFAC1E2913125 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_bottom zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "接下来的季节必须好好注意\n不要在电车里睡过头了。"

    show rs_image_1E6988844B884E2B88D92837EA789B61 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "毕竟在有暖气的车里很舒服很安心，\n一不小心就会睡过去。\n梅咲又是始发站，必定有座位。"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000008DF

    return

label block_00000A04:
    # Node: 00000A04 (Judo)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_153E9CF7193C4513869D54FA898561FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2SG1 == True" },{ "scope": 1, "content": "SYSTheaterState <> 22" }]):
        jump block_0000255B
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 1, "content": "TalkTsukiF2 == 0" }]):
        jump block_00001F30
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 1, "content": "TalkTsukiF2 == 1" },{ "scope": 0, "content": "C2S1 == True" }]):
        jump block_00000ACA
    if judge_lm_condition([]):
        jump block_00000A05

    return

label block_0000255B:
    # Node: 0000255B (Judo)
    $ sys_lm_menu_item = [{"pos": (320, 232),"image": "images/Chapter 2/Menu/Tsuki.png","hover": "images/Chapter 2/Menu/Tsuki hover.png","name": "月"}, {"pos": (497, 230),"image": "images/Chapter 2/Menu/Sora.png","hover": "images/Chapter 2/Menu/Sora hover.png","name": "空"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_502
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A0C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" },{ "scope": 1, "content": "TalkSoraF6After == True" }]):
        jump block_00002602
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" },{ "scope": 1, "content": "TalkTsukiF6After == True" }]):
        jump block_00002601
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" },{ "scope": 1, "content": "GTsukiTestSoraMode == True" },{ "scope": 2, "content": "CXQTsukiTest == True" },{ "scope": 3, "content": "TalkTsukiSora == True" },{ "scope": 3, "content": "C2S6 == True" },{ "scope": 4, "content": "TalkSoraF6After == False" }]):
        jump block_00002FBF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00000ACB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_00000ACC

    return

label block_00002602:
    # Node: 00002602 (空 F6后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_EC040B7182804790B7750A3172C04105 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_25DD39CE556B4EC69227B2977E0220CB as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "去旅行住的酒店当然不错，但果然还是自己家最舒服——"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那当然，你们家可是比那酒店还豪华呐。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AA958AA9A1FE4204BFF4DC3025EFF511 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "没、没这回事哦。\n"
    show rs_image_F761F888C5034F26880B624E1477BF17 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "友君回家的时候没有这种感觉吗？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "酒店那边更大更舒服，好想一直住在那里呐～"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestSoraMode == True" }]):
        jump block_00002FC1
    if judge_lm_condition([]):
        jump block_0000255B

    return

label block_00002FC1:
    # Node: 00002FC1 (END: TalkF6After)
    $ TalkSoraF6After = False

    if judge_lm_condition([]):
        jump block_0000255B

    return

label block_00002601:
    # Node: 00002601 (月 F6后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_FF2F05BF45D647239862F7725764481C as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "之前大家一起来了次盛大的迟到呐。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "有何感想？一只脚踏入不良泥潭的优等生！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E4A2988FBBCF49C0A1E44ED64AFE0C25 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "在本该上学的时候做别的……\n有股不明所以的优越感呢。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_722CB01DCAFC49349A68F58FFBF69D05 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……很赞！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸欸欸欸！不行的阿月——！\n那么做空会很伤心的！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C55DDE5781304E9BBC5E1E1C55EB2DEB as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "开玩笑。\n不过，大家一起慌慌张张往回赶，\n也算是不错的经历了。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_0000255B

    return

label block_00002FBF:
    # Node: 00002FBF (阿月測眼力)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_8013AE5050E34D619C8668AD6A90EEB7 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "想参加训练吗？"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 5" }]):
        jump block_00003A2F
    if judge_lm_condition([]):
        jump block_00003A2E

    return

label block_00003A2F:
    # Node: 00003A2F (阿月測眼力)
    call block_0000116E from _call_block_0000116E_4

    if judge_lm_condition([]):
        jump block_00003A30

    return

label block_00003A30:
    # Node: 00003A30 (RESET)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("柔道场外"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_153E9CF7193C4513869D54FA898561FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_0000255B

    return

label block_00003A2E:
    # Node: 00003A2E (選擇)
    call scb_selector("", [{"name":"はい", "content":_("走，去训练了")}, {"name":"いいえ", "content":_("我很忙的")}]) from _call_scb_selector_59

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003A2F
    if judge_lm_condition([]):
        jump block_0000255B

    return

label block_00000ACB:
    # Node: 00000ACB (月 F3后)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_FF2F05BF45D647239862F7725764481C as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000254C

    return

label block_0000254C:
    # Node: 0000254C (F3后)
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_B971E7700CCC4821BEE883B34D9FE081 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "之前和作……{w=0.4}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_AA958AA9A1FE4204BFF4DC3025EFF511 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不对，{w=0.4}{nw}"
    show rs_image_30DD4B1DF61D48718BE856BC8D2D0EEC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "和朋友一起去的\n新开的咖啡店也想和哥哥去呢。\n戚风蛋糕真的很棒♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B971E7700CCC4821BEE883B34D9FE081 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "一想起来就又想去了。\n哥哥，下个周末我们一起去好不好♪"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_8F17CE9B9953435FA745F57FC7AB45AC as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……吃太多会发胖的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_28C590FF58F046C8B1B5CB446BE7DBC7 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "才不会——这部分靠训练就能减掉——"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_9CD666B82870491B8A8E86DEB16BE5D2 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "总、总之还是别摄入太多糖分为好。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_33D7E05166F54F7A900E1886FA423087 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……我不行。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦——阿月本来就不是甜食党呐。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4F3E2E3628734329904C89EF6859F2DC as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我很高兴，但，也很难受。现实果然无比艰辛……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不就是吃个点心么！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("楼梯间"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestSoraMode == True" }]):
        jump block_00002FC0
    if judge_lm_condition([]):
        jump block_0000255B

    return

label block_00002FC0:
    # Node: 00002FC0 (T ++)
    $ TalkTsukiSora = True

    if judge_lm_condition([]):
        jump block_0000255B

    return

label block_00000ACC:
    # Node: 00000ACC (空 F3后)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_EC040B7182804790B7750A3172C04105 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000254C

    return

label block_00001F30:
    # Node: 00001F30 (Judo 月 point)
    $ sys_lm_menu_item = [{"pos": (320, 232),"image": "images/Chapter 2/Menu/Tsuki point.png","hover": "images/Chapter 2/Menu/Tsuki hover.png","name": "月"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_503
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00001F34
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A0C

    return

label block_00001F34:
    # Node: 00001F34 (月 F2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_FF2F05BF45D647239862F7725764481C as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "何事？"

    pause 0.3

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_F59CF92171C0495BA4E334AC96BA8B63 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『听取了月的建议』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『直白叫出作哉的名字，{/color}\n{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    extend "{color=#0080FF}用{/color}{u}{color=#FF0000}有些带刺的话语{/color}{/u}{color=#0080FF}。』{/color}"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("柔道场外"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001F32

    return

label block_00001F32:
    # Node: 00001F32 (選擇)
    call scb_selector(_("这种意见可否？"), [{"name":"はい", "content":_("就是这个")}, {"name":"いいえ", "content":_("太微妙了，算了")}]) from _call_scb_selector_60

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00001F30
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002C6C

    return

label block_00002C6C:
    # Node: 00002C6C (TF2)
    $ TalkTsukiF2 = 1

    if judge_lm_condition([]):
        jump block_00003A2B

    return

label block_00000ACA:
    # Node: 00000ACA (Judo 月)
    $ sys_lm_menu_item = [{"pos": (320, 232),"image": "images/Chapter 2/Menu/Tsuki.png","hover": "images/Chapter 2/Menu/Tsuki hover.png","name": "月"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_504
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A0C
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase >= 97" },{ "scope": 1, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00001F33
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_000024FD

    return

label block_00001F33:
    # Node: 00001F33 (月 F2選擇后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_C55DDE5781304E9BBC5E1E1C55EB2DEB as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "去找那个不良好好教训他一顿。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("柔道场外"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000ACA

    return

label block_000024FD:
    # Node: 000024FD (月 F1后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_FF2F05BF45D647239862F7725764481C as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？阿月一个人在这里做什么呢？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B1FC5F4C1C12446FA8B2429310BFC93F as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "自主练习。……再不努力不行了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦、哦～……我觉得现在已经很强了哦？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E4A2988FBBCF49C0A1E44ED64AFE0C25 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "并不是。\n最近空越来越擅长社交了。\n在旁边看着觉得自己也要加油了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，说的不是社团是这个？"

    show rs_image_F63E385A95E44F529E8174DDE5CC8B81 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……嗯。这件事本身是非常好的不过，\n要是空的魅力继续这么……"

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2A145ED2838E49ADA8A590DDDE9D39FB as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "太耀眼了。这么下去哥哥就无法直视了！"

    show rs_image_9CD666B82870491B8A8E86DEB16BE5D2 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "然后，心里也很难受……\n……要是空不会被坏人缠上就好了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "阿月还是老样子呐。{w}\n在我看来两人同样都很帅很有魅力哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_48D6C50D52C74DB0A8DE2E2202963AE7 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是、是么？听起来挺好的。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯嗯！所以阿月也不要只关心小空。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "要注意自己有没有被坏人缠上！\n"
    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "帅气的阿月还是有很多粉丝的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_78B8B030A797438793EB50C49503E6F0 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不可能。我时常在空身边，\n绝不可能注意到空之外的人。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_722CB01DCAFC49349A68F58FFBF69D05 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空就是如此有魅力。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（没、没救了，这个脑残大哥……）"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("柔道场外"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000ACA

    return

label block_00000A05:
    # Node: 00000A05 (Judo empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_505
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A0C

    return

label block_00003A3B:
    # Node: 00003A3B (TO: Schoolhouse)

    if judge_lm_condition([]):
        jump block_000008D7

    return

label block_000008D7:
    # Node: 000008D7 (Schoolhouse)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase == 1" },{ "scope": 0, "content": "C2S2Phase >= 97" }]):
        jump block_00002F52
    if judge_lm_condition([{ "scope": 0, "content": "C2QSakuya == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C1S4 == True" },{ "scope": 3, "content": "C2S2 == True" }]):
        jump block_0000254A
    if judge_lm_condition([]):
        jump block_000008E1

    return

label block_00002F52:
    # Node: 00002F52 (Schoolhouse empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_506
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A39

    return

label block_0000254A:
    # Node: 0000254A (Schoolhouse 作哉 quest)
    $ sys_lm_menu_item = [{"pos": (360, 160),"image": "images/Chapter 2/Menu/Sakuya quest.png","hover": "images/Chapter 2/Menu/Sakuya hover.png","name": "作哉"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_507
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A39
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_00002558

    return

label block_00002558:
    # Node: 00002558 (作哉)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_E6FDC4E80B584C5E81421942D725A064 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "好了，差不多到散步的时间了。"

    pause 0.2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_45DAF0F8DEAA4C16818A7935B79E801D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "出来——！小翼——！"

    window hide

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
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
    show rs_image_4C9460B4582D4F9BB227C7D10D9F0CA0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "乖乖♪到散步的时间了哦——{w}\n今天也要元气满满地散步哦♪"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide


    if judge_lm_condition([]):
        jump block_0000255A

    return

label block_0000255A:
    # Node: 0000255A (QUEST START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托已经开始，请达成目标。』{/color}"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1


    if judge_lm_condition([]):
        jump block_00002559

    return

label block_00002559:
    # Node: 00002559 (CP2 作哉散歩)
    call block_00000A75 from _call_block_00000A75

    if judge_lm_condition([]):
        jump block_00003A39

    return

label block_000008E1:
    # Node: 000008E1 (Schoolhouse)
    $ sys_lm_menu_item = [{"pos": (360, 160),"image": "images/Chapter 2/Menu/Sakuya.png","hover": "images/Chapter 2/Menu/Sakuya hover.png","name": "作哉"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_508
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A3A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" },{ "scope": 1, "content": "C2S6 == True" }]):
        jump block_000025FD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" },{ "scope": 1, "content": "C2SG1 == True" }]):
        jump block_00000A0F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_00000908

    return

label block_00003A3A:
    # Node: 00003A3A (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003A39

    return

label block_000025FD:
    # Node: 000025FD (作哉 F6后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_5FFD58FCBF734135AA883B505D03EB3E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_757DAFA361824FA590E148B0796C4A27 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小翼好像在闹情绪，也不听我的话。"

    show rs_image_A4CF621C3DEB4E9384E96660488F1436 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "肯定是旅行的时候把它放置在一边生气了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是吗？动物好有意思呐。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说起来，旅行期间小翼是谁照顾的？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DFF6C096971C4020B3AD59E666124B0B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "滑子老师找人照顾的。那人一副自大的样子。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯嗯！技安也是这种感觉正好！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2687EBBCBF3E4AF7A0DE1AF839CF5AF7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊？话说你怎么还在这，快滚。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀——！\n难得一开始对话这么顺利最后还是这样了——！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校舍内"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000008E1

    return

label block_00000A0F:
    # Node: 00000A0F (作哉 F3后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_5FFD58FCBF734135AA883B505D03EB3E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_DFF6C096971C4020B3AD59E666124B0B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "该怎么做呢，今天社团活动前还是想去散散步的。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，那把我也带上！我有很多要问的事情哦♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1A5E3A7F00B546FE8A7423BB9C2B93DB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……哈？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "动物园约会的经过，还有现在和翼君的关系之类的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "作为两人的丘比特我有权知道——！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8C3DB2F9BABD40D396DB3B634865E972 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_2687EBBCBF3E4AF7A0DE1AF839CF5AF7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "切，管你。\n我又没找你帮忙，全是你自作多情。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊！？怎么可以这么对恩人说话！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_398B4081FA4A4B0AB6F12C9C027BDE6F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "就你这样连定丁点恩人都算不上，何来感谢！\n笨蛋笨蛋一边去！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔唔唔唔唔！！！！我生气了！！\n本想让翼君和你搞好关系的我不管了！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "才不会把我家的翼君交给技安这种人——！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_757DAFA361824FA590E148B0796C4A27 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈，我听不见——\n再说了，一之濑已经是饲育系的了。\n真是抱歉呐——"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不对不对！翼君是小钢琴部的所有物！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EB9D3849888641E78C28DA84B16F2AC8 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "饲育系！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "小钢琴部！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_2687EBBCBF3E4AF7A0DE1AF839CF5AF7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EC0D4FD5EFFE482182DE336BAE27C2C3 "哼！！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校舍内"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000008E1

    return

label block_00000908:
    # Node: 00000908 (作哉)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_5FFD58FCBF734135AA883B505D03EB3E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_A4CF621C3DEB4E9384E96660488F1436 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊——期中考试好烦人——{w}\n不想考——真是的。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_70791C94500A466286BAA986A9A35B33 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……呼～\n想和狗一样悠闲度日。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那就为了变成狗后能更可爱而努力好了！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_155F4A0E12344ED0A4C06D837688FA79 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "是啊——现在这样……\n{w=0.4}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FD53CD2278134B3E8C2280BAD0FFB730 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "噫，你怎么在这！！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_398B4081FA4A4B0AB6F12C9C027BDE6F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "去去！滚一边去！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校舍内"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000008E1

    return

label block_00003A04:
    # Node: 00003A04 (TO: Schooldoor)

    if judge_lm_condition([]):
        jump block_000008D8

    return

label block_000008D8:
    # Node: 000008D8 (School door)
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
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000008E2

    return

label block_000008E2:
    # Node: 000008E2 (School door)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (96, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "屋外トイレへ"}, {"pos": (456, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "学校看板"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_509
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003A06
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外トイレへ\"" }]):
        jump block_000008F5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学校看板\"" }]):
        jump block_00000931

    return

label block_000008F5:
    # Node: 000008F5 (Outside toilet)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("室外厕所"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D5370D554F61451C806A39C7BC540968 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002C8E

    return

label block_00002C8E:
    # Node: 00002C8E (Outside toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (472, 192),"image": "images/Menu/Tokiwa.png","hover": "images/Menu/Tokiwa hover.png","name": "常磐"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_510
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000008D8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" },{ "scope": 1, "content": "FTokiwaHelp == True" }]):
        jump block_00002C8D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase > 0" },{ "scope": 1, "content": "C2QYuuhiPhase > 0" }]):
        jump block_00002C92
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" }]):
        jump block_00002C8F

    return

label block_00002C8D:
    # Node: 00002C8D (常磐 First)
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

    rs_character_C223850065F6443080205D1F61C04C98 "呀，你好。看鞋子的颜色，你是二年级学生吧。{w}\n我是三年级的{color=#008A45}常磐进{/color}。"

    show rs_image_2917E94D246C4B5DBB7438FB372D005B as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C223850065F6443080205D1F61C04C98 "我喜欢打听一些各种各样的有趣的事情。{w}\n所以，如果你在寻找{color=#008080}事件{/color}或{color=#FF8000}委托{/color}时遇到了困难，\n来找我，我会给你一些{color=#FF0000}提示{/color}的。"

    show rs_image_C792083E91604DFD9FEB035D608ACFF9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C223850065F6443080205D1F61C04C98 "能帮上你的忙我也会很高兴的。待会见。"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外厕所"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002C8C

    return

label block_00002C8C:
    # Node: 00002C8C (Cancel: First)
    $ FTokiwaHelp = False

    if judge_lm_condition([]):
        jump block_00002C8E

    return

label block_00002C92:
    # Node: 00002C92 (常磐 Helpless)
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
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002C8E

    return

label block_00002C8F:
    # Node: 00002C8F (常磐)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 200
    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 at center_bottom zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_C223850065F6443080205D1F61C04C98 "怎么了？有什么在意的事情吗？"


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C90:
    # Node: 00002C90 (常磐 Help)
    call scb_selector("", [{"name":"フラグについて", "content":_("关于事件……")},{"name":"クエストについて", "content":_("关于委托……")},{"name":"なんでもない", "content":_("其实木有事")}]) from _call_scb_selector_61

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"なんでもない\"" }]):
        jump block_00002C91
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C2S1 == False" }]):
        jump block_00002C94
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C2S2 == False" }]):
        jump block_00002C95
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C2S3 == False" }]):
        jump block_00002C96
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C2S4 == False" }]):
        jump block_00002C93
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C2S5 == False" }]):
        jump block_00002C97
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"フラグについて\"" },{ "scope": 1, "content": "C2S6 == False" }]):
        jump block_00002F37
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "CXQKaruta == False" }]):
        jump block_00002C99
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "C2QYuuhi == False" }]):
        jump block_00002F38
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "C2QKimuraConference == False" }]):
        jump block_00002C98
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "CXQSabuImechen == False" }]):
        jump block_00002C9B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "CXQTsukiTest == False" }]):
        jump block_00002C9C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "CXQShinoQuestion == False" },{ "scope": 2, "content": "C2SG1 == True" }]):
        jump block_00002C9D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "C2S1 == True" },{ "scope": 2, "content": "C2QSora == False" },{ "scope": 3, "content": "C2SG1 == False" }]):
        jump block_00002C9E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "C2QSakuya == False" },{ "scope": 2, "content": "C1S4 == True" },{ "scope": 3, "content": "C2S2 == True" }]):
        jump block_00002CA0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クエストについて\"" },{ "scope": 1, "content": "C2QNewsclub == False" }]):
        jump block_00002C9A
    if judge_lm_condition([]):
        jump block_00002C9F

    return

label block_00002C91:
    # Node: 00002C91 (Back)
    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("室外厕所"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002C8E

    return

label block_00002C94:
    # Node: 00002C94 (Flag 1)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "去找楼梯间的{color=#008A45}赤峰空君{/color}和{color=#008A45}赤峰月君{/color}\n说点什么如何？"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C95:
    # Node: 00002C95 (Flag 2)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "去音乐室{color=#3A00C4}弹一下钢琴{/color}，\n他会再去拜访你。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C96:
    # Node: 00002C96 (Flag 3)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "厕所里的{color=#AA0055}奥村慎太郎君{/color}\n想做什么有意思的事。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C93:
    # Node: 00002C93 (Flag 4)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "一楼走廊贴了张{color=#008A45}海报{/color}，\n请务必去看看。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C97:
    # Node: 00002C97 (Flag 5)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "放学后回家前，\n记得和校门口的{color=#3A00C4}榊雪绪君{/color}和{color=#3A00C4}猫山四朗君{/color}\n打声招呼。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002F37:
    # Node: 00002F37 (Flag 6)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "继续到音乐室{color=#AA0055}弹钢琴{/color}，\n你的熟人还会去。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C99:
    # Node: 00002C99 (小林翻歌牌)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "放学后的公园里\n{color=#FF8000}小林君{/color}正等着和你玩传统游戏。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002F38:
    # Node: 00002F38 (QUEST 夕阳)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "放学后进家门前，\n记得{color=#FF8000}夕阳君{/color}在宝咲站口等你。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C98:
    # Node: 00002C98 (木村討論會)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "首先先和{color=#FF8000}木村树君{/color}、{color=#FF8000}伊藤圭君{/color}、{color=#FF8000}一之濑翼君{/color}、{color=#FF8000}小岛正君{/color}\n都谈一次话。"

    rs_character_C223850065F6443080205D1F61C04C98 "之后再和{color=#FF8000}木村君{/color}谈一次的话，\n你们就可以去开讨论会了。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C9B:
    # Node: 00002C9B (三朗美髮店)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "屋顶上的{color=#FF8000}猫山三朗{/color}好像有事情想要拜托你呐。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C9C:
    # Node: 00002C9C (阿月測眼力)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "去和楼梯间的{color=#FF8000}赤峰月君{/color}谈一下的话\n好像能进行什么测试的样子。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C9D:
    # Node: 00002C9D (小忍問題冊)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "去和图书馆里的{color=#FF8000}绫濑忍{/color}谈一下。\n他好像给你准备了有趣的游戏。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C9E:
    # Node: 00002C9E (QUEST 空)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "楼梯间的{color=#FF8000}赤峰空君{/color}想要和你“共同作业”，\n请去找找他。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002CA0:
    # Node: 00002CA0 (QUEST 作哉)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "校舍内的{color=#FF8000}穗海作哉{/color}继续有事找你。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C9A:
    # Node: 00002C9A (新聞部任務)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Notice 1.ogg"

    rs_character_C223850065F6443080205D1F61C04C98 "{color=#FF8000}新闻部活动室{/color}又发生有趣的事情了哦。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00002C9F:
    # Node: 00002C9F (No Help)
    show rs_image_1D81F7CC53CF4EF697CE06D9359105F3 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C223850065F6443080205D1F61C04C98 "现在已经没有什么其他有趣的事情了。"

    show rs_image_BFA650AC179546C0BB0783630BBB10C9 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "还有什么想要问的事情吗？"

    window hide


    if judge_lm_condition([]):
        jump block_00002C90

    return

label block_00000931:
    # Node: 00000931 (Board)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_3BE9AC227F0142FBAABEEB7605D6A3F9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}私立御咲学园是某县（省）的宝咲市所拥有的\n一所初高中男子校。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『……。\n……。\n重点是，{/color}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    extend "{color=#0080FF}校内恋爱非常繁荣，赫赫有名。』{/color}"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide


    if judge_lm_condition([]):
        jump block_000008E2

    return

label block_00003A3C:
    # Node: 00003A3C (TO: School inside)

    if judge_lm_condition([]):
        jump block_00003A3D

    return

label block_000018CF:
    # Node: 000018CF (Conversation F2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "找谁问建议比较好呐……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这关系到翼君和技安的将来，必须慎重选择。"

    window hide

    $ set_window("(標準)")

    return

label block_000018CE:
    # Node: 000018CE (Target F2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『寻找知晓“响彻心扉的的话语”的人\n并听取建议。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FB9:
    # Node: 00001FB9 (Character)
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

label block_0000093B:
    # Node: 0000093B (School outside XCTA)
    if judge_lm_condition([{ "scope": 1, "content": "C2S4Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S4Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_00002567", target_label="block_00002564") from _call_scb_global_map_129
    elif judge_lm_condition([{ "scope": 1, "content": "C2S4Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S2Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_00002567", target_label="block_00002EE4") from _call_scb_global_map_130
    elif judge_lm_condition([{ "scope": 1, "content": "C2S2Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S4Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_00002563", target_label="block_00002564") from _call_scb_global_map_131
    elif judge_lm_condition([{ "scope": 1, "content": "C2S2Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S2Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, True, talk_label="block_00002563", target_label="block_00002EE4") from _call_scb_global_map_132
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2S4Phase == 1" }]):
        jump block_00002567
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00003A38
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_00003A03
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00003A2D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00003A3B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00003A04
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00003A3C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00000956
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FB9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2S2Phase == 1" }]):
        jump block_00002563
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C2S4Phase == 1" }]):
        jump block_00002564
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C2S2Phase == 1" }]):
        jump block_00002EE4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_0000093B

    return

label block_00002567:
    # Node: 00002567 (Conversation F4)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "陆田和杉本来我们学校了。\n翼君是他们的粉丝，肯定很高兴吧——"

    window hide

    $ set_window("(標準)")

    return

label block_00000956:
    # Node: 00000956 (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_0000095F

    return

label block_0000095F:
    # Node: 0000095F (RESET)
    $ C2S1Phase = 0
    $ C2S2Phase = 0
    $ C2S3Phase = 0
    $ C2S4Phase = 0
    $ C2S5Phase = 0
    $ C2S6Phase = 0

    if judge_lm_condition([]):
        jump block_000008CC

    return

label block_00002563:
    # Node: 00002563 (Conversation F2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "到底怎么做才能让翼君和技安和好呐。{w}\n总之先去看看他们的情况。"

    window hide

    $ set_window("(標準)")

    return

label block_00002564:
    # Node: 00002564 (Target F4)
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

label block_00002EE4:
    # Node: 00002EE4 (Target F2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#AA0055}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00000A02:
    # Node: 00000A02 (School outside ACTA)
    if judge_lm_condition([{ "scope": 1, "content": "C2S6Phase == 1" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, True, talk_label="block_00002569", target_label="block_0000255C") from _call_scb_global_map_133
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, True, talk_label="block_00002561", target_label="block_0000255C") from _call_scb_global_map_134
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2S6Phase == 1" }]):
        jump block_00002569
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00003A38
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_00003A03
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00003A2D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00003A3B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00003A04
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00003A3C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" }]):
        jump block_000024F8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00002561
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_0000255C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00000956
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FB9

    return

label block_00002569:
    # Node: 00002569 (Conversation F6)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为什么忍兴致那么好啊。有时很奇怪哦——忍。"

    window hide

    $ set_window("(標準)")

    return

label block_00002561:
    # Node: 00002561 (Conversation F1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "和阿月他们说过话后慢慢也有干劲了！{w}\n今天小钢琴部要继续活动了♪"

    window hide

    $ set_window("(標準)")

    return

label block_0000255C:
    # Node: 0000255C (Target F16)
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

label block_000008CE:
    # Node: 000008CE (School outside ACTX)
    if judge_lm_condition([{ "scope": 1, "content": "C2SG1 == True" }]) and judge_lm_condition([{ "scope": 1, "content": "SYSReviewMode == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, False, talk_label="block_0000256B", target_label="block_000031C3") from _call_scb_global_map_135
    elif judge_lm_condition([{ "scope": 1, "content": "C2SG1 == True" }]) and judge_lm_condition([{ "scope": 1, "content": "C1S1 and C1S2 and C1S3 and C1S4 and C1S5 == True" },{ "scope": 2, "content": "CXQKaruta and C2QNewsclub and C2QYuuhi and C2QKimuraConference and C2QSakuya and C2QSora and CXQSabuImechen and CXQTsukiTest and CXQShinoQuestion == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, False, talk_label="block_0000256B", target_label="block_00002F47") from _call_scb_global_map_136
    elif judge_lm_condition([{ "scope": 1, "content": "C2SG1 == True" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, False, talk_label="block_0000256B", target_label="block_000009BE") from _call_scb_global_map_137
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "SYSReviewMode == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, False, talk_label="block_000009BD", target_label="block_000031C3") from _call_scb_global_map_138
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C1S1 and C1S2 and C1S3 and C1S4 and C1S5 == True" },{ "scope": 2, "content": "CXQKaruta and C2QNewsclub and C2QYuuhi and C2QKimuraConference and C2QSakuya and C2QSora and CXQSabuImechen and CXQTsukiTest and CXQShinoQuestion == True" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, False, talk_label="block_000009BD", target_label="block_00002F47") from _call_scb_global_map_139
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", True, False, talk_label="block_000009BD", target_label="block_000009BE") from _call_scb_global_map_140
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "SYSReviewMode == True" }]):
        jump block_000031C3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C1S1 and C1S2 and C1S3 and C1S4 and C1S5 == True" },{ "scope": 2, "content": "CXQKaruta and C2QNewsclub and C2QYuuhi and C2QKimuraConference and C2QSakuya and C2QSora and CXQSabuImechen and CXQTsukiTest and CXQShinoQuestion == True" }]):
        jump block_00002F47
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2SG1 == True" }]):
        jump block_0000256B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00003A38
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_00003A03
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00003A2D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00003A3B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00003A04
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00003A3C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後\"" }]):
        jump block_000024F8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000009BD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_000009BE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_000008CE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FB9

    return

label block_000031C3:
    # Node: 000031C3 (Target dream)
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

label block_00002F47:
    # Node: 00002F47 (Target 2)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#AA0055}下一个章节{/color}{color=#0080FF}正在等着！』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_0000256B:
    # Node: 0000256B (Conversation F3后)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼～期中考试终于考完了～"

    window hide

    $ set_window("(標準)")

    return

label block_000009BD:
    # Node: 000009BD (Conversation F3前)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "快要期中考试了……啊，真讨厌。"

    window hide

    $ set_window("(標準)")

    return

label block_000009BE:
    # Node: 000009BE (Target 1)
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

label block_000018C6:
    # Node: 000018C6 (BGM 1)
    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_000018C2

    return

