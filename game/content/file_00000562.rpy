# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00000562 (音楽祭)

label block_00000563:
    # Node: 00000563 (開始)

    jump block_0000261E

    return

label block_0000261E:
    # Node: 0000261E (Classroom 1-1)
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

    jump block_0000261D

    return

label block_0000261D:
    # Node: 0000261D (Classroom 1-1)
    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 100
    show rs_image_36DCE6288A1B4B4BB4F472650542F4CB as tag_521EB228B90943B3A2B33F87C47D3A0E at center_bottom zorder zorder_tag_521EB228B90943B3A2B33F87C47D3A0E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_lm_menu_item = [{"pos": (96, 200),"image": "images/Celemony/Menu/Music Festival/Shintaro.png","hover": "images/Celemony/Menu/Music Festival/Shintaro hover.png","name": "慎太郎"}, {"pos": (216, 200),"image": "images/Celemony/Menu/Music Festival/Matsuta.png","hover": "images/Celemony/Menu/Music Festival/Matsuta hover.png","name": "松田"}, {"pos": (304, 205),"image": "images/Celemony/Menu/Music Festival/Shinobu.png","hover": "images/Celemony/Menu/Music Festival/Shinobu hover.png","name": "しのぶ"}, {"pos": (384, 208),"image": "images/Celemony/Menu/Music Festival/Tsuki.png","hover": "images/Celemony/Menu/Music Festival/Tsuki hover.png","name": "月"}, {"pos": (497, 205),"image": "images/Celemony/Menu/Music Festival/Izumi.png","hover": "images/Celemony/Menu/Music Festival/Izumi hover.png","name": "泉"}, {"pos": (560, 215),"image": "images/Celemony/Menu/Music Festival/Sora.png","hover": "images/Celemony/Menu/Music Festival/Sora hover.png","name": "空"}, {"pos": (685, 210),"image": "images/Celemony/Menu/Music Festival/Katou.png","hover": "images/Celemony/Menu/Music Festival/Katou hover.png","name": "加藤"}, {"pos": (720, 60),"type":"textbutton","text":_("继续"),"name": "確認終了"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, -0.001) from _call_lm_menu_439
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"確認終了\"" }]):
        jump block_00002610
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_0000261C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_0000261B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_00002619
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00002617
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" }]):
        jump block_00002611
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_0000260E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_0000260D

    return

label block_00002610:
    # Node: 00002610 (Classroom 1-2)
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

    jump block_0000260F

    return

label block_0000260F:
    # Node: 0000260F (Classroom 1-2)
    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 100
    show rs_image_0C713C75424547F8B475126078350741 as tag_521EB228B90943B3A2B33F87C47D3A0E at center_bottom zorder zorder_tag_521EB228B90943B3A2B33F87C47D3A0E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_lm_menu_item = [{"pos": (104, 200),"image": "images/Celemony/Menu/Music Festival/Sakuya.png","hover": "images/Celemony/Menu/Music Festival/Sakuya hover.png","name": "作哉"}, {"pos": (224, 200),"image": "images/Celemony/Menu/Music Festival/Sato.png","hover": "images/Celemony/Menu/Music Festival/Sato hover.png","name": "佐藤"}, {"pos": (298, 200),"image": "images/Celemony/Menu/Music Festival/Kimura.png","hover": "images/Celemony/Menu/Music Festival/Kimura hover.png","name": "木村"}, {"pos": (416, 208),"image": "images/Celemony/Menu/Music Festival/Okajima.png","hover": "images/Celemony/Menu/Music Festival/Okajima hover.png","name": "岡島"}, {"pos": (496, 220),"image": "images/Celemony/Menu/Music Festival/Kojima.png","hover": "images/Celemony/Menu/Music Festival/Kojima hover.png","name": "小島"}, {"pos": (560, 216),"image": "images/Celemony/Menu/Music Festival/Itou.png","hover": "images/Celemony/Menu/Music Festival/Itou hover.png","name": "伊藤"}, {"pos": (672, 209),"image": "images/Celemony/Menu/Music Festival/Saburo.png","hover": "images/Celemony/Menu/Music Festival/Saburo hover.png","name": "三朗"}, {"pos": (720, 60),"type":"textbutton","text":_("继续"),"name": "確認終了"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, -0.001) from _call_lm_menu_440
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"確認終了\"" }]):
        jump block_00003C0C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_0000261A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_00002618
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_00002616
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_00002615
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"佐藤\"" }]):
        jump block_00002614
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_00002613
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_00002612

    return

label block_00003C0C:
    # Node: 00003C0C (Start)
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

    hide tag_9250047CA6624153B022ECE456CDD7CB
    hide tag_FD703D9AE62B4308878305DF2E3E8C22
    hide tag_1883146FD3304D849EFF705A9AB4395F
    hide tag_2CC7E9871AA7494D909E38877A131DD2
    hide tag_82ACCE894BBB4B2FA8DBE2D94331EE6C
    hide tag_8A5DFBC2EFC943EFAF0F878D5477FA0A
    hide tag_1D9AFF28F2B0414ABA7DC5D1FF98F8EB
    hide tag_39E017DE8747437EB5A6F311C1106EAA
    hide tag_D419A79FBA734761B6AEE489D19D60BB
    hide tag_E4AD2080E1DF4712BF324F1B123305D4
    hide tag_F7FA86CC15A84129AD8823E67B40BF5D
    hide tag_CBBC42DB06344BEAA6FE93B55E0869D1
    hide tag_480ECA2736744B7991D7FFE6300A852A
    hide tag_8C8203DEE2C94C79AFD5C207DF6F61B5
    hide tag_D2DB8322086A4598A5A7A97B184131ED
    hide tag_63442126DDDF434D96A3E9656ACD2763
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.6

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_4C48D9E5007446F8B852C5E8EE39604F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_4CBC3D399C6A4D2DAC7D06010FCCC122

    show rs_image_50574D67D9E1480190A94440CC260636 _("选择出赛人员") as hint_1:
        xpos 800
        ypos 375
        parallel:
            linear 20 xpos -200
            xpos 800
            repeat
    show rs_image_50574D67D9E1480190A94440CC260636 _("选择出赛人员") as hint_2:
        xpos 800
        ypos 375
        pause 5
        parallel:
            linear 20 xpos -200
            xpos 800
            repeat
    show rs_image_50574D67D9E1480190A94440CC260636 _("选择出赛人员") as hint_3:
        xpos 800
        ypos 375
        pause 10
        parallel:
            linear 20 xpos -200
            xpos 800
            repeat
    show rs_image_50574D67D9E1480190A94440CC260636 _("选择出赛人员") as hint_4:
        xpos 800
        ypos 375
        pause 15
        parallel:
            linear 20 xpos -200
            xpos 800
            repeat

    pause 0.3

    if sys_music2_current_file != "sound/BGM/Celemony.ogg":
        play music2 "sound/BGM/Celemony.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Celemony.ogg"

    $ set_window("体育祭、音楽祭")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "『接下来安排出赛选手。』"

    window hide

    call celemony([
        {"x": 52, "y": 10, "id": 0, "image": "images/Celemony/Event/Soprano.png"},
        {"x": 237, "y": 10, "id": 1, "image": "images/Celemony/Event/Alto.png"},
        {"x": 422, "y": 10, "id": 2, "image": "images/Celemony/Event/Tenor.png"},
        {"x": 607, "y": 10, "id": 0, "image": "images/Celemony/Event/Soprano.png"},
        {"x": 52, "y": 97, "id": 2, "image": "images/Celemony/Event/Tenor.png"},
        {"x": 237, "y": 97, "id": 3, "image": "images/Celemony/Event/Bass.png"},
        {"x": 422, "y": 97, "id": 3, "image": "images/Celemony/Event/Bass.png"},
        {"x": 607, "y": 97, "id": 2, "image": "images/Celemony/Event/Tenor.png"},
        {"x": 52, "y": 184, "id": 1, "image": "images/Celemony/Event/Alto.png"},
        {"x": 237, "y": 184, "id": 1, "image": "images/Celemony/Event/Alto.png"},
        {"x": 422, "y": 184, "id": 2, "image": "images/Celemony/Event/Tenor.png"},
        {"x": 607, "y": 184, "id": 3, "image": "images/Celemony/Event/Bass.png"},
        {"x": 52, "y": 271, "id": 1, "image": "images/Celemony/Event/Alto.png"},
        {"x": 237, "y": 271, "id": 2, "image": "images/Celemony/Event/Tenor.png"},
        {"x": 422, "y": 271, "id": 3, "image": "images/Celemony/Event/Bass.png"},
        {"x": 607, "y": 271, "id": 1, "image": "images/Celemony/Event/Alto.png"},
    ], {
        "base": {
            "Itou":      [3,   4,   1,  2],
            "Izumi":     [3,   4,   2,  0],
            "Katou":     [0,   2,   2,  3],
            "Kimura":    [-12, -12,  3,  4],
            "Kojima":    [4,   4,   1,  0],
            "Matsuda":   [-2,  -2,   3,  4],
            "Okajima":   [0,   3,   3,  2],
            "Saburou":   [-2,   1,   3,  2],
            "Sakuya":    [1,   3,   3,  2],
            "Satou":     [4,   4,   4,  4],
            "Shinobu":   [-3,   3,  -2, -2],
            "Shintarou": [1,   3,   3,  3],
            "Sora":      [2,   4,   3,  1],
            "Tomo":      [2,   4,   1,  0],
            "Tsubasa":   [10,  10,  2,  0],
            "Tsuki":     [-13, -13, -2,  4],
        },
        "extra": [
            {
                "condition": [[], ["Izumi", "Matsuda"]], # 卡拉OK训练
                "range": [
                    {"rate": [0, 0.5], "value": 2, "description": _("泉酱好像在唱卡拉OK一样")},
                    {"rate": [0.5, 1], "value": 0}
                ]
            }, {
                "condition": [[], ["Itou", "Kimura"]], # 五音不全
                "range": [
                    {"rate": [0, 0.5], "value": -3, "description": _("不想描述木村亲唱了什么")},
                    {"rate": [0.5, 1], "value": 0}
                ]
            }, {
                "condition": [[0], ["Kojima", "Okajima"]], # 受到惊吓
                "range": [
                    {"rate": [0, 1], "value": -1, "description": _("小岛君的歌声吓到部长了")}
                ]
            }, {
                "condition": [[0, 1], ["Matsusa", "Sakuya"]], # 超极限荷尔蒙
                "range": [
                    {"rate": [0, 0.4], "value": 3, "description": _("傲娇君肯定专门练习过")},
                    {"rate": [0.4, 0.8], "value": -3, "description": _("傲娇君声音飚太高了")},
                    {"rate": [0.8, 1], "value": 1, "description": _("傲娇君意外唱的不错")}
                ]
            }, {
                "condition": [[0, 1], ["Tomo", "Tsubasa"]], # 小钢琴部
                "range": [
                    {"rate": [0, 1], "value": 2, "description": _("不愧是小钢琴部")}
                ]
            }, {
                "condition": [[], ["Tomo", "Sakuya", "Tsubasa"]], # 嫉妒心
                "range": [
                    {"rate": [0, 0.6], "value": 4, "description": _("傲娇君对友亲的对抗心产生了不错的效果")},
                    {"rate": [0.6, 0.8], "value": -3, "description": _("傲娇君对友亲的对抗心强过头了")},
                    {"rate": [0.8, 1], "value": 0}
                ]
            }, {
                "condition": [[], ["Sakuya", "Tsubasa"]], # 天籁之音
                "range": [
                    {"rate": [0, 0.8], "value": 6, "description": _("翼亲的声音好好听~")},
                    {"rate": [0.8, 1], "value": 0}
                ]
            }, {
                "condition": [[], ["Tomo", "Shinobu"]], # 天才音乐家
                "range": [
                    {"rate": [0, 0.5], "value": 2, "description": _("哟，天才音乐家！")},
                    {"rate": [0.5, 0.7], "value": 1, "description": _("友亲真的很有音乐天分呢")},
                    {"rate": [0.7, 1], "value": 0}
                ]
            }, {
                "condition": [[], ["Tomo", "Satou"]], # 迟早发生的事
                "range": [
                    {"rate": [0, 0.2], "value": 1, "description": _("佐藤君的样子有些奇怪")},
                    {"rate": [0.2, 1], "value": 0}
                ]
            }, {
                "condition": [[], ["Matsuda", "Sakuya", "Izumi"]], # 继续卡拉OK？
                "range": [
                    {"rate": [0, 0.2], "value": 1, "description": _("松田亲像在唱卡拉OK")},
                    {"rate": [0.2, 0.4], "value": 2, "description": _("松田亲好起劲")},
                    {"rate": [0.4, 0.6], "value": -2, "description": _("松田亲居然会唱错词")},
                    {"rate": [0.6, 0.8], "value": -1, "description": _("松田亲看起来累坏了")},
                    {"rate": [0.8, 1], "value": 0}
                ]
            }, {
                "condition": [[0], ["Tomo", "Sakuya"]], # 听天由命
                "range": [
                    {"rate": [0, 0.5], "value": 5, "description": _("在女高音上听天由命的友亲和傲娇君")},
                    {"rate": [0, 0.5], "value": -5, "description": _("在女高音上听天由命的友亲和傲娇君")}
                ]
            }, {
                "condition": [[2, 3], ["Tsuki", "Sora"]], # 意外还不错
                "range": [
                    {"rate": [0, 0.65], "value": 2, "description": _("阿月和小空的互相激励效果看来随时都有")},
                    {"rate": [0.65, 1], "value": 0}
                ]
            }, {
                "condition": [[2, 3], ["Saburou", "Shintarou"]], # 猫咪催眠曲
                "range": [
                    {"rate": [0, 0.4], "value": -2, "description": _("差点因为三酱的声音睡着了")},
                    {"rate": [0.4, 1], "value": 0}
                ]
            }, {
                "condition": [[0, 1], ["Saburou", "Shintarou"]], # 猫咪狂躁曲
                "range": [
                    {"rate": [0, 0.4], "value": 2, "description": _("三酱好棒！")},
                    {"rate": [0.4, 1], "value": 0}
                ]
            }, {
                "condition": [[], ["Sakuya", "Shintarou"]], # 傲娇君的歌声
                "range": [
                    {"rate": [0, 0.2], "value": 2, "description": _("傲娇君为什么要看着我唱歌……")},
                    {"rate": [0.2, 1], "value": 0}
                ]
            }
        ]
    }) from _call_celemony_1

    jump block_00003C06

    return

label block_00003C06:
    # Node: 00003C05 (Calculate)
    $ set_window("イベントモード")
    hide hint_1
    hide hint_2
    hide hint_3
    hide hint_4
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "就这样大家决定好分工，开始各自练习。{w}\n不过慎酱推荐的衣服最后还是没能采用……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "音乐祭当天，一班和二班的成绩是——"

    window hide

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 2


    if sum(1 if x > 12 else 0 for x in _return["score"]) > 2:
        jump block_00003C08
    else:
        jump block_00003BF4

    return

label block_00003C08:
    # Node: 00003C08 (Win)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    # Gallery unlock: images/CG/Music festival win.png
    $ zorder_rs_image_7AFFBEE2AA274C4C836D31E63DA4932A = -100
    show rs_image_7AFFBEE2AA274C4C836D31E63DA4932A as rs_image_7AFFBEE2AA274C4C836D31E63DA4932A zorder zorder_rs_image_7AFFBEE2AA274C4C836D31E63DA4932A onlayer master
    hide rs_image_7AFFBEE2AA274C4C836D31E63DA4932A

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_061B0CC8862A4FF8B54E6E627F1B88DB as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clap 1.ogg"

    pause 2

    # Gallery unlock: images/CG/Music festival win.png
    $ zorder_rs_image_7AFFBEE2AA274C4C836D31E63DA4932A = -100
    show rs_image_7AFFBEE2AA274C4C836D31E63DA4932A as rs_image_7AFFBEE2AA274C4C836D31E63DA4932A zorder zorder_rs_image_7AFFBEE2AA274C4C836D31E63DA4932A onlayer master
    hide rs_image_7AFFBEE2AA274C4C836D31E63DA4932A

    show rs_image_7AFFBEE2AA274C4C836D31E63DA4932A as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003C04

    return


label block_00003BF4:
    # Node: 00003BF4 (Lose)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Sorry 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Sorry 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_D123F79A6B5940889E3CF0422ABE8095 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_7C9AB5ABEE5E487EAB75A4EA474E500B

    pause 2


    if judge_lm_condition([]):
        jump block_00003C04

    return

label block_00003C04:
    # Node: 00003C04 (Result)
    $ set_window("イベントモード")

    call convert_celemony_detail(_return, [_("女高音"), _("女低音"), _("男高音"), _("男低音")]) from _call_convert_celemony_detail_1

    python:
        set_window("イベントモード")
        for index, event in enumerate(_return):
            _return[index]["succeed"] = _return[index]["score"] > 12

    pause

    $ renpy.block_rollback()

    call screen celemony_detail(_return)

    pause 1

    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_367D6887C01741AFA0312C70A109F138

    pause 3


    if judge_lm_condition([]):
        jump block_00003C07

    return

label block_00003C07:
    # Node: 00003C07 (終了)

    return

label block_0000261A:
    # Node: 0000261A (作哉)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_DFF6C096971C4020B3AD59E666124B0B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "什么都行，你来决定。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000260F

    return

label block_00002618:
    # Node: 00002618 (三朗)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_48F9BE60F5244821B20C0F50155C0114 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我卡拉OK很棒的！\n{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_2F053DD5EF4C49B388E430ED01FE5A69 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "{color=#804000}“{/color}{color=#800080}数码～小熊猫{/color}{color=#804000}～♪”{/color}"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000260F

    return

label block_00002616:
    # Node: 00002616 (伊藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_99320781054948949BEB08A8AC3E7437 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "啊——啊——……♪\n{w=0.5}{nw}"
    show rs_image_4D6C0781022E46CA9AF15C613D7158EB as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "嗯，果然低音不行。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000260F

    return

label block_00002615:
    # Node: 00002615 (木村)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_AD32BE71FC11444A8598BBF482AF95D0 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊——♪啊——♪啊゛～\n{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_952F244A7CFB4533820FFCEB6B3D761A as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……咳咳！\n不行，高音根本发不出……"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000260F

    return

label block_00002614:
    # Node: 00002614 (佐藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_DDF3DD19A6EF49059D534A21C414D18B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "呵呵呵♪总算是我的出场时间了！\n旋律和乐感全交给我。\n《The Moldau》我也是演奏过的哦。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000260F

    return

label block_00002613:
    # Node: 00002613 (岡島)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_A375C883918D41239D3E5B8AE7C226B2 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "就等着大家的大新闻了！\n为了我们新闻部的知名度，\n大家要好好展现自己的勇姿！"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000260F

    return

label block_00002612:
    # Node: 00002612 (小島)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_53FF68C192E3494AB005C1909579AFFB "请选男低音之外的。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000260F

    return

label block_0000261C:
    # Node: 0000261C (忍)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_9133C483CCA9460C804D7FCD561DE619 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不是很擅长唱歌……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是吗？不是在卡拉OK里\n{color=#FF00FF}“啊～有你真好～♪”{/color}唱的很开心嘛。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000261D

    return

label block_0000261B:
    # Node: 0000261B (月)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_8F17CE9B9953435FA745F57FC7AB45AC as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我不擅长唱歌。\n希望不要给大家添麻烦……"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000261D

    return

label block_00002619:
    # Node: 00002619 (空)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_AE9C0A0B9876495092F4044936BA8A1A as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这个我有比哥哥做得更好的自信！\n{w=0.5}{nw}"
    show rs_image_9C09C82BD6C4471CA272DAF35BA5D948 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……诶，说起来男高音和女低音中更低的是……？"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000261D

    return

label block_00002617:
    # Node: 00002617 (慎太郎)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_FD2C0CA41CDB4FD99334DB3AB5756355 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我的声线不高也不低，到底该选什么呢——"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000261D

    return

label block_00002611:
    # Node: 00002611 (加藤)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_581796CAD76B4C929577B4C1D581EF10 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_81D16F74A3C44B8982DB528D7D934850 "听歌不错，唱歌太羞耻。\n帮我选个有趣的声部就好。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000261D

    return

label block_0000260E:
    # Node: 0000260E (泉)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_9AF02379E9534E1FB204413A9C8F2675 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "我还没有变声，所以很低的部分唱不出来。\n比如女低音就不错。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000261D

    return

label block_0000260D:
    # Node: 0000260D (松田)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_3D04A5D178044F04B357189727365274 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "听歌不错，合唱就……\n{w=0.5}{nw}"
    show rs_image_ED1123A4A4404155ABBDBFA9983E6A38 as tag_F12981B3CF794DEA86CFB94275B48CFB zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "可别弄错把我分到女高音。会被笑话的。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("二年一班教室"))

    if judge_lm_condition([]):
        jump block_0000261D

    return

