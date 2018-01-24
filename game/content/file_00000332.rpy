# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00000332 (體育祭)

label block_00000333:
    # Node: 00000333 ()
    $ Status = 0
    $ SelectedPerson = 0
    $ SelectedPhase = 0
    $ StatusX = 0
    $ StatusY = 0
    $ Phase1Count = 0
    $ Phase2Count = 0
    $ Phase3Count = 0
    $ Phase4Count = 0
    $ Phase1Result = _("失败")
    $ Phase2Result = _("失败")
    $ Phase3Result = _("失败")
    $ Phase4Result = _("失败")
    $ WinCount = 0

    if judge_lm_condition([]):
        jump block_000007DF

    return

label block_000007DF:
    # Node: 000007DF (Class 2-1)
    $ set_window("(標準)")
    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    $ set_place_title(_("二年一班教室"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F3D233F763D6421EBDC0A1616D4F0D6F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000007E0

    return

label block_000007E0:
    # Node: 000007E0 (Class 2-1)
    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 100
    show rs_image_01DDEE0986E344EC8A1E7E8649473915 as tag_521EB228B90943B3A2B33F87C47D3A0E at center_bottom zorder zorder_tag_521EB228B90943B3A2B33F87C47D3A0E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_lm_menu_item = [{"pos": (96, 200),"image": "images/Celemony/Menu/Sports Celemony/Shintaro.png","hover": "images/Celemony/Menu/Sports Celemony/Shintaro hover.png","name": "慎太郎"}, {"pos": (216, 200),"image": "images/Celemony/Menu/Sports Celemony/Matsuta.png","hover": "images/Celemony/Menu/Sports Celemony/Matsuta hover.png","name": "松田"}, {"pos": (304, 205),"image": "images/Celemony/Menu/Sports Celemony/Shinobu.png","hover": "images/Celemony/Menu/Sports Celemony/Shinobu hover.png","name": "しのぶ"}, {"pos": (384, 208),"image": "images/Celemony/Menu/Sports Celemony/Tsuki.png","hover": "images/Celemony/Menu/Sports Celemony/Tsuki hover.png","name": "月"}, {"pos": (497, 205),"image": "images/Celemony/Menu/Sports Celemony/Izumi.png","hover": "images/Celemony/Menu/Sports Celemony/Izumi hover.png","name": "泉"}, {"pos": (560, 215),"image": "images/Celemony/Menu/Sports Celemony/Sora.png","hover": "images/Celemony/Menu/Sports Celemony/Sora hover.png","name": "空"}, {"pos": (685, 210),"image": "images/Celemony/Menu/Sports Celemony/Katou.png","hover": "images/Celemony/Menu/Sports Celemony/Katou hover.png","name": "加藤"}, {"pos": (724, 55),"type":"textbutton","text":_("继续"),"name": "確認終了"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, -0.001) from _call_lm_menu_5
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"確認終了\"" }]):
        jump block_000007E2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000024C5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_000024E4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_000024E6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_000024E9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" }]):
        jump block_000024E8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_000024E7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_000024EA

    return

label block_000007E2:
    # Node: 000007E2 (Class 2-2)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    $ set_place_title(_("二年二班教室"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_74FFA1FC7D7C4EDEB7565F683C1767BE as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F3D233F763D6421EBDC0A1616D4F0D6F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000007E1

    return

label block_000007E1:
    # Node: 000007E1 (Class 2-2)
    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 100
    show rs_image_D7C840B2AB1547AB95032FAD306EB9E1 as tag_521EB228B90943B3A2B33F87C47D3A0E at center_bottom zorder zorder_tag_521EB228B90943B3A2B33F87C47D3A0E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    
    $ sys_lm_menu_item = [{"pos": (104, 200),"image": "images/Celemony/Menu/Sports Celemony/Sakuya.png","hover": "images/Celemony/Menu/Sports Celemony/Sakuya hover.png","name": "作哉"}, {"pos": (224, 200),"image": "images/Celemony/Menu/Sports Celemony/Sato.png","hover": "images/Celemony/Menu/Sports Celemony/Sato hover.png","name": "佐藤"}, {"pos": (298, 200),"image": "images/Celemony/Menu/Sports Celemony/Kimura.png","hover": "images/Celemony/Menu/Sports Celemony/Kimura hover.png","name": "木村"}, {"pos": (416, 208),"image": "images/Celemony/Menu/Sports Celemony/Okajima.png","hover": "images/Celemony/Menu/Sports Celemony/Okajima hover.png","name": "岡島"}, {"pos": (496, 220),"image": "images/Celemony/Menu/Sports Celemony/Kojima.png","hover": "images/Celemony/Menu/Sports Celemony/Kojima hover.png","name": "小島"}, {"pos": (560, 216),"image": "images/Celemony/Menu/Sports Celemony/Itou.png","hover": "images/Celemony/Menu/Sports Celemony/Itou hover.png","name": "伊藤"}, {"pos": (672, 209),"image": "images/Celemony/Menu/Sports Celemony/Saburo.png","hover": "images/Celemony/Menu/Sports Celemony/Saburo hover.png","name": "三朗"}, {"pos": (724, 55),"type":"textbutton","text":_("继续"),"name": "確認終了"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, -0.001) from _call_lm_menu_6
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"確認終了\"" }]):
        jump block_00003933
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_000024F1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_000024F0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_000024EF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_000024EE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"佐藤\"" }]):
        jump block_000024ED
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_000024EC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_000024EB

    return

label block_00003933:
    # Node: 00003933 (Start)
    pause 0.4

    $ set_place_title(False)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2

    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.6

    if sys_effect3_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_4150D18D984E4FA891D9F6C8921DCD50 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_4CBC3D399C6A4D2DAC7D06010FCCC122

    pause 0.3

    if sys_music2_current_file != "sound/BGM/Celemony.ogg":
        play music2 "sound/BGM/Celemony.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Celemony.ogg"

    $ set_window("体育祭、音楽祭")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "『接下来安排出赛选手。』"

    window hide


    if judge_lm_condition([]):
        jump block_00003932

    return

label block_00003932:
    # Node: 00003932 (PREPARE)
    $ Status = [0] * 16
    show expression "images/Celemony/AVATAR/Tomo.png" as Avatar_1 at Transform(xpos=77,ypos=27) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Shinobu.png" as Avatar_2 at Transform(xpos=77,ypos=130) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Tsuki.png" as Avatar_3 at Transform(xpos=225,ypos=27) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Sora.png" as Avatar_4 at Transform(xpos=225, ypos=130) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Shintaro.png" as Avatar_5 at Transform(xpos=373, ypos=27) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Katou.png" as Avatar_6 at Transform(xpos=373, ypos=130) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Izumi.png" as Avatar_7 at Transform(xpos=521, ypos=27) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Matsuta.png" as Avatar_8 at Transform(xpos=521, ypos=130) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Tsubasa.png" as Avatar_9 at Transform(xpos=107, ypos=395) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Sakuya.png" as Avatar_10 at Transform(xpos=107, ypos=498) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Saburo.png" as Avatar_11 at Transform(xpos=255, ypos=395) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Itou.png" as Avatar_12 at Transform(xpos=255, ypos=498) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Kimura.png" as Avatar_13 at Transform(xpos=403, ypos=395) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Sato.png" as Avatar_14 at Transform(xpos=403, ypos=498) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Okajima.png" as Avatar_15 at Transform(xpos=551, ypos=395) zorder 100 onlayer master
    show expression "images/Celemony/AVATAR/Kojima.png" as Avatar_16 at Transform(xpos=551, ypos=498) zorder 100 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    image sprots_celemony_number = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#FFFFFF",
        size=30,
        text_align=0.5)
    image sprots_celemony_event = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#FFFFFF",
        size=16,
        text_align=0.5)

    show sprots_celemony_event (_("百米田径")) as Title_1 at Transform(xpos=119, ypos=264) zorder 400 onlayer master
    show sprots_celemony_event (_("骑马战")) as Title_2 at Transform(xpos=274, ypos=264) zorder 400 onlayer master
    show sprots_celemony_event (_("借物竞走")) as Title_3 at Transform(xpos=431, ypos=264) zorder 400 onlayer master
    show sprots_celemony_event (_("投球入篮")) as Title_4 at Transform(xpos=586, ypos=264) zorder 400 onlayer master
    show sprots_celemony_number "4" as Number_1 at Transform(xpos=139, ypos=290) zorder 400 onlayer master
    show sprots_celemony_number "4" as Number_2 at Transform(xpos=284, ypos=290) zorder 400 onlayer master
    show sprots_celemony_number "4" as Number_3 at Transform(xpos=451, ypos=290) zorder 400 onlayer master
    show sprots_celemony_number "4" as Number_4 at Transform(xpos=606, ypos=290) zorder 400 onlayer master

    if judge_lm_condition([]):
        jump block_00003935

    return

style sports_celemony_apply_button:
    color "#F2BB7E"
    size 36
    outlines [(absolute(4), "#FF6800", absolute(0), absolute(0))]
    hover_color "#FF6800"
    hover_outlines [(absolute(4), "#F2BB7E", absolute(0), absolute(0))]

label block_00003935:
    # Node: 00003935 (Selection)
    $ sys_lm_menu_item = [
        {"pos": (77, 27),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Tomo hover.png","name": "友"},
        {"pos": (77, 130),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Shinobu hover.png","name": "しのぶ"},
        {"pos": (225, 27),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Tsuki hover.png","name": "月"},
        {"pos": (225, 130),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Sora hover.png","name": "空"},
        {"pos": (373, 27),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Shintaro hover.png","name": "慎太郎"},
        {"pos": (373, 130),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Katou hover.png","name": "加藤"},
        {"pos": (521, 27),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Izumi hover.png","name": "泉"},
        {"pos": (521, 130),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Matsuta hover.png","name": "松田"},
        {"pos": (107, 395),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Tsubasa hover.png","name": "つばさ"},
        {"pos": (107, 498),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Sakuya hover.png","name": "作哉"},
        {"pos": (255, 395),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Saburo hover.png","name": "三朗"},
        {"pos": (255, 498),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Itou hover.png","name": "伊藤"},
        {"pos": (403, 395),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Kimura hover.png","name": "木村"},
        {"pos": (403, 498),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Sato hover.png","name": "佐藤"},
        {"pos": (551, 395),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Okajima hover.png","name": "岡島"},
        {"pos": (551, 498),"image": "images/Celemony/AVATAR/Placeholder.png","hover": "images/Celemony/AVATAR/Kojima hover.png","name": "小島"},
        {"pos": (346, 264),"type":"textbutton","text":"出赛！","style":"sports_celemony_apply_button","condition":[{"scope":0,"content":"Phase1Count == 4 and Phase2Count == 4 and Phase3Count == 4 and Phase4Count == 4"}],"name": "Start"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_7
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友\"" }]):
        jump block_00003945
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00003944
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00003943
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_00003942
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00003940
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" }]):
        jump block_00003941
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_0000393F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_0000393E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_0000393D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_0000393A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_0000393B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_0000393C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_00003937
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"佐藤\"" }]):
        jump block_00003938
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_00003939
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_00003936
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Start\"" }]):
        jump block_0000395F

    return

label block_0000395B:
    # Node: 0000395B (Select Phase)
    $ sys_lm_choice_item = ["暂不决定"]
    if Phase1Count < 4:
        $ sys_lm_choice_item += ["百米田径"]
    if Phase2Count < 4:
        $ sys_lm_choice_item += ["骑马战"]
    if Phase3Count < 4:
        $ sys_lm_choice_item += ["借物竞走"]
    if Phase4Count < 4:
        $ sys_lm_choice_item += ["投球入篮"]
    $ sys_lm_choice_sound = { "click": "sound/Effect Sound/System - choose.ogg" }
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound
    if _lm_selected_value == "百米田径":
        $ SelectedPhase = 1
    elif _lm_selected_value == "骑马战":
        $ SelectedPhase = 2
    elif _lm_selected_value == "借物竞走":
        $ SelectedPhase = 3
    elif _lm_selected_value == "投球入篮":
        $ SelectedPhase = 4
    else:
        $ SelectedPhase = 0

    if judge_lm_condition([]):
        jump block_00003934

    return

label block_00003934:
    # Node: 00003934 (Update)
    $ renpy.hide("Status_" |str_combine| SelectedPerson)
    if Status[SelectedPerson - 1] == 1:
        $ Phase1Count -= 1
    elif Status[SelectedPerson - 1] == 2:
        $ Phase2Count -= 1
    elif Status[SelectedPerson - 1] == 3:
        $ Phase3Count -= 1
    elif Status[SelectedPerson - 1] == 4:
        $ Phase4Count -= 1
    if SelectedPerson < 5:
        $ StatusX = 102 + (SelectedPerson - 1) * 148
        $ StatusY = 16
    elif SelectedPerson < 9:
        $ StatusX = 102 + (SelectedPerson - 5) * 148
        $ StatusY = 119
    elif SelectedPerson < 13:
        $ StatusX = 132 + (SelectedPerson - 9) * 148
        $ StatusY = 384
    else:
        $ StatusX = 132 + (SelectedPerson - 13) * 148
        $ StatusY = 487
    if SelectedPhase == 1:
        $ Phase1Count = Phase1Count + 1
        $ renpy.show("images/Celemony/Event/Running.png", at_list=[Transform(xpos=StatusX, ypos=StatusY)], what=renpy.easy.displayable("images/Celemony/Event/Running.png"), tag="Status_" |str_combine| SelectedPerson, zorder=50)
    elif SelectedPhase == 2:
        $ Phase2Count = Phase2Count + 1
        $ renpy.show("images/Celemony/Event/Riding battle.png", at_list=[Transform(xpos=StatusX, ypos=StatusY)], what=renpy.easy.displayable("images/Celemony/Event/Riding battle.png"), tag="Status_" |str_combine| SelectedPerson, zorder=50)
    elif SelectedPhase == 3:
        $ Phase3Count = Phase3Count + 1
        $ renpy.show("images/Celemony/Event/Race walking.png", at_list=[Transform(xpos=StatusX, ypos=StatusY)], what=renpy.easy.displayable("images/Celemony/Event/Race walking.png"), tag="Status_" |str_combine| SelectedPerson, zorder=50)
    elif SelectedPhase == 4:
        $ Phase4Count = Phase4Count + 1
        $ renpy.show("images/Celemony/Event/Ball shooting.png", at_list=[Transform(xpos=StatusX, ypos=StatusY)], what=renpy.easy.displayable("images/Celemony/Event/Ball shooting.png"), tag="Status_" |str_combine| SelectedPerson, zorder=50)
    $ Status[SelectedPerson - 1] = SelectedPhase
    hide Number_1
    hide Number_2
    hide Number_3
    hide Number_4
    hide Title_1
    hide Title_2
    hide Title_3
    hide Title_4
    if Phase1Count < 4 or Phase2Count < 4 or Phase3Count < 4 or Phase4Count < 4:
        show sprots_celemony_event (_("百米田径")) as Title_1 at Transform(xpos=119, ypos=264) zorder 400 onlayer master
        show sprots_celemony_event (_("骑马战")) as Title_2 at Transform(xpos=274, ypos=264) zorder 400 onlayer master
        show sprots_celemony_event (_("借物竞走")) as Title_3 at Transform(xpos=431, ypos=264) zorder 400 onlayer master
        show sprots_celemony_event (_("投球入篮")) as Title_4 at Transform(xpos=586, ypos=264) zorder 400 onlayer master
        show sprots_celemony_number (str(4 - Phase1Count)) as Number_1 at Transform(xpos=139, ypos=290) zorder 400 onlayer master
        show sprots_celemony_number (str(4 - Phase2Count)) as Number_2 at Transform(xpos=284, ypos=290) zorder 400 onlayer master
        show sprots_celemony_number (str(4 - Phase3Count)) as Number_3 at Transform(xpos=451, ypos=290) zorder 400 onlayer master
        show sprots_celemony_number (str(4 - Phase4Count)) as Number_4 at Transform(xpos=606, ypos=290) zorder 400 onlayer master

    if judge_lm_condition([]):
        jump block_0000395D

    return

label block_0000395D:
    # Node: 0000395D (To: Selection)

    if judge_lm_condition([]):
        jump block_00003935

    return

label block_00003945:
    # Node: 00003945 (友)
    $ SelectedPerson = 1

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_00003944:
    # Node: 00003944 (忍)
    $ SelectedPerson = 5

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_00003943:
    # Node: 00003943 (月)
    $ SelectedPerson = 2

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_00003942:
    # Node: 00003942 (空)
    $ SelectedPerson = 6

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_00003940:
    # Node: 00003940 (慎太郎)
    $ SelectedPerson = 3

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_00003941:
    # Node: 00003941 (加藤)
    $ SelectedPerson = 7

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_0000393F:
    # Node: 0000393F (泉)
    $ SelectedPerson = 4

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_0000393E:
    # Node: 0000393E (松田)
    $ SelectedPerson = 8

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_0000393D:
    # Node: 0000393D (翼)
    $ SelectedPerson = 9

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_0000393A:
    # Node: 0000393A (作哉)
    $ SelectedPerson = 13

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_0000393B:
    # Node: 0000393B (三朗)
    $ SelectedPerson = 10

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_0000393C:
    # Node: 0000393C (伊藤)
    $ SelectedPerson = 14

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_00003937:
    # Node: 00003937 (木村)
    $ SelectedPerson = 11

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_00003938:
    # Node: 00003938 (佐藤)
    $ SelectedPerson = 15

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_00003939:
    # Node: 00003939 (岡島)
    $ SelectedPerson = 12

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_00003936:
    # Node: 00003936 (小島)
    $ SelectedPerson = 16

    if judge_lm_condition([]):
        jump block_0000395B

    return

label block_0000395F:
    # Node: 0000395F (Calculate)
    $ set_window("イベントモード")
    hide Status_1
    hide Status_2
    hide Status_3
    hide Status_4
    hide Status_5
    hide Status_6
    hide Status_7
    hide Status_8
    hide Status_9
    hide Status_10
    hide Status_11
    hide Status_12
    hide Status_13
    hide Status_14
    hide Status_15
    hide Status_16
    hide Number_1
    hide Number_2
    hide Number_3
    hide Number_4
    hide Avatar_1
    hide Avatar_2
    hide Avatar_3
    hide Avatar_4
    hide Avatar_5
    hide Avatar_6
    hide Avatar_7
    hide Avatar_8
    hide Avatar_9
    hide Avatar_10
    hide Avatar_11
    hide Avatar_12
    hide Avatar_13
    hide Avatar_14
    hide Avatar_15
    hide Avatar_16
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "就这样，每人了解自己的职责后\n不断练习，不断努力……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "最后，红队的成绩是——"

    window hide

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 2


    if judge_lm_condition([]):
        jump block_00003960

    return

label block_00003960:
    # Node: 00003960 (Calculate)
    $ Score = [0] * 4
    $ scoreTable = [
        [ 0, -12, 3,  0],
        [ 3,  4, -2,  2],
        [ 1,  1,  4,  2],
        [ 2,  1,  1,  3],
        [ 3,  4,  3,  0],
        [ 4,  2,  2,  3],
        [ 3,  3,  3,  3],
        [ 3,  4,  1,  4],
        [-2, -12, 2, -1],
        [ 4,  1,  4,  4],
        [ 4,  4,  3, -2],
        [ 1,  0,  2,  2],
        [ 3,  2,  1,  4],
        [ 1, -2,  1,  1],
        [ 1,  1,  1,  1],
        [ 2, -2,  2,  2]
    ]
    $ i = 0
    while i < 16:
        $ Score[Status[i] - 1] += scoreTable[i][Status[i] - 1]
        $ i += 1
    if Score[0] > 5:
        $ Phase1Result = _("胜利")
        $ WinCount += 1
    if Score[1] > 5:
        $ Phase2Result = _("胜利")
        $ WinCount += 1
    if Score[2] > 5:
        $ Phase3Result = _("胜利")
        $ WinCount += 1
    if Score[3] > 5:
        $ Phase4Result = _("胜利")
        $ WinCount += 1
    $ del scoreTable
    $ del Score
    $ del i

    if judge_lm_condition([{ "scope": 0, "content": "WinCount > 2" }]):
        jump block_000024C9
    if judge_lm_condition([]):
        jump block_000024CB

    return

label block_000024C9:
    # Node: 000024C9 (Win)
    if sys_effect_current_file != "sound/Effect Sound/Trumpet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    # Gallery unlock: images/CG/Sports celemony win.png
    $ zorder_rs_image_85BB53EF8F764B8998C0F67FF475E7E5 = -100
    show rs_image_85BB53EF8F764B8998C0F67FF475E7E5 as rs_image_85BB53EF8F764B8998C0F67FF475E7E5 zorder zorder_rs_image_85BB53EF8F764B8998C0F67FF475E7E5 onlayer master
    hide rs_image_85BB53EF8F764B8998C0F67FF475E7E5

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_5BACA245EF584E56B6D17425B501514A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    if sys_effect2_current_file != "sound/Effect Sound/Clap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clap 1.ogg"

    pause 2

    # Gallery unlock: images/CG/Sports celemony win.png
    $ zorder_rs_image_85BB53EF8F764B8998C0F67FF475E7E5 = -100
    show rs_image_85BB53EF8F764B8998C0F67FF475E7E5 as rs_image_85BB53EF8F764B8998C0F67FF475E7E5 zorder zorder_rs_image_85BB53EF8F764B8998C0F67FF475E7E5 onlayer master
    hide rs_image_85BB53EF8F764B8998C0F67FF475E7E5

    show rs_image_85BB53EF8F764B8998C0F67FF475E7E5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000147F

    return

label block_0000147F:
    # Node: 0000147F (Result)
    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FF8000}详情：{/color}\n百米田径: [Phase1Result] 骑马战: [Phase2Result]\n借物竞走: [Phase3Result] 投球入篮: [Phase4Result]"

    window hide

    pause 1

    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_367D6887C01741AFA0312C70A109F138

    pause 3


    if judge_lm_condition([]):
        jump block_00003989

    return

label block_00003989:
    # Node: 00003989 ()
    $ del Status
    $ del SelectedPerson
    $ del SelectedPhase
    $ del StatusX
    $ del StatusY
    $ del Phase1Count
    $ del Phase2Count
    $ del Phase3Count
    $ del Phase4Count
    $ del Phase1Result
    $ del Phase2Result
    $ del Phase3Result
    $ del Phase4Result
    $ del WinCount

    return

label block_000024CB:
    # Node: 000024CB (Lose)
    if sys_effect_current_file != "sound/Effect Sound/Sorry 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Sorry 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Sorry 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_D123F79A6B5940889E3CF0422ABE8095 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_7C9AB5ABEE5E487EAB75A4EA474E500B

    pause 2


    if judge_lm_condition([]):
        jump block_0000147F

    return

label block_000024F1:
    # Node: 000024F1 (作哉)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_F0988CA2235149BBB7560C242B59EA69 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "随意，我不会反对。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E1

    return

label block_000024F0:
    # Node: 000024F0 (三朗)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_104E19984CF747D19D3CC74E9452E4A0 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我——我——！我要田径！\n最帅最受欢迎的那个♪"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E1

    return

label block_000024EF:
    # Node: 000024EF (伊藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_E0D6A617AD044B16B42360567510F7DD as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "虽说是田径部，我不过是个经理……\n似乎并没什么用。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E1

    return

label block_000024EE:
    # Node: 000024EE (木村)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_67E4971422B24DE799679E73FB92C9E9 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "我很想参加借物竞走，但我是田径部的……"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E1

    return

label block_000024ED:
    # Node: 000024ED (佐藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_C8A74E1418F4431CAD466A4648F12769 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "不要小看文化部里的运动部——吹奏乐部啊！\n田径、骑马战、什么都行！\n{w=0.5}{nw}"
    show rs_image_52DA2DC477DA4AA6B9083C9822781AEE as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E1

    return

label block_000024EC:
    # Node: 000024EC (岡島)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_80DDCB83351245C2B44A943AC22567CC as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "期待大家的活跃哦！\n到时候大家的勇姿我们新闻部会全部记下的！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E1

    return

label block_000024EB:
    # Node: 000024EB (小島)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_BADBAA4F0A4C41C38EF36F3121398C07 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_53FF68C192E3494AB005C1909579AFFB "骑马战之外的，拜托了。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E1

    return

label block_000024C5:
    # Node: 000024C5 (忍)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_498B24D29055445D92291B73D348191E as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "感觉又要被当做骑马战的受保护对象了。\n偶尔也想试点别的啊。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E0

    return

label block_000024E4:
    # Node: 000024E4 (月)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_9C6FBD9DB462411BAFEABE7C5B5F94E9 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我对运动很有自信。\n不过，还是球类之外比较好。\n田径类的话，空要更强。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E0

    return

label block_000024E6:
    # Node: 000024E6 (空)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_B9C05B244A1F41E7AFDE876574238D4A as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我不管什么都可以哦，只要能快乐竞赛就好！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E0

    return

label block_000024E9:
    # Node: 000024E9 (慎太郎)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_E7D86BC45AC5484380764CF9B109D0DA as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "给你们看看归宅部的力量～！！\n{w=0.55}{nw}"
    show rs_image_09451D7B22D74AB5A1A4927086141825 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……要是能选晚上的运动就好了。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E0

    return

label block_000024E8:
    # Node: 000024E8 (加藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_B12DC311D86A491398AB2D191F6D3C8E as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_81D16F74A3C44B8982DB528D7D934850 "什么都行，随便你了。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E0

    return

label block_000024E7:
    # Node: 000024E7 (泉)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_58FAE766750B4FF09356905A1635623E as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "我虽然什么都行……\n但要是有能活用排球部训练的项目就好了。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E0

    return

label block_000024EA:
    # Node: 000024EA (松田)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_74683F1B7537443795430EB9D51FB743 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "不是投球就行，太幼稚了。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_000007E0

    return

