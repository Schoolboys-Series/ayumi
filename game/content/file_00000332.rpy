# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00000332 (體育祭)

label block_00000333:
    # Node: 00000333 ()

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

    jump block_000007E0

    return

label block_000007E0:
    # Node: 000007E0 (Class 2-1)
    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 100
    show rs_image_01DDEE0986E344EC8A1E7E8649473915 as tag_521EB228B90943B3A2B33F87C47D3A0E at center_bottom zorder zorder_tag_521EB228B90943B3A2B33F87C47D3A0E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_lm_menu_item = [{"pos": (96, 200),"image": "images/Celemony/Menu/Sports Celemony/Shintaro.png","hover": "images/Celemony/Menu/Sports Celemony/Shintaro hover.png","name": "慎太郎"}, {"pos": (216, 200),"image": "images/Celemony/Menu/Sports Celemony/Matsuta.png","hover": "images/Celemony/Menu/Sports Celemony/Matsuta hover.png","name": "松田"}, {"pos": (304, 205),"image": "images/Celemony/Menu/Sports Celemony/Shinobu.png","hover": "images/Celemony/Menu/Sports Celemony/Shinobu hover.png","name": "しのぶ"}, {"pos": (384, 208),"image": "images/Celemony/Menu/Sports Celemony/Tsuki.png","hover": "images/Celemony/Menu/Sports Celemony/Tsuki hover.png","name": "月"}, {"pos": (497, 205),"image": "images/Celemony/Menu/Sports Celemony/Izumi.png","hover": "images/Celemony/Menu/Sports Celemony/Izumi hover.png","name": "泉"}, {"pos": (560, 215),"image": "images/Celemony/Menu/Sports Celemony/Sora.png","hover": "images/Celemony/Menu/Sports Celemony/Sora hover.png","name": "空"}, {"pos": (685, 210),"image": "images/Celemony/Menu/Sports Celemony/Katou.png","hover": "images/Celemony/Menu/Sports Celemony/Katou hover.png","name": "加藤"}, {"pos": (720, 60),"type":"textbutton","text":_("继续"),"name": "確認終了"}]
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

    jump block_000007E1

    return

label block_000007E1:
    # Node: 000007E1 (Class 2-2)
    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 100
    show rs_image_D7C840B2AB1547AB95032FAD306EB9E1 as tag_521EB228B90943B3A2B33F87C47D3A0E at center_bottom zorder zorder_tag_521EB228B90943B3A2B33F87C47D3A0E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    
    $ sys_lm_menu_item = [{"pos": (104, 200),"image": "images/Celemony/Menu/Sports Celemony/Sakuya.png","hover": "images/Celemony/Menu/Sports Celemony/Sakuya hover.png","name": "作哉"}, {"pos": (224, 200),"image": "images/Celemony/Menu/Sports Celemony/Sato.png","hover": "images/Celemony/Menu/Sports Celemony/Sato hover.png","name": "佐藤"}, {"pos": (298, 200),"image": "images/Celemony/Menu/Sports Celemony/Kimura.png","hover": "images/Celemony/Menu/Sports Celemony/Kimura hover.png","name": "木村"}, {"pos": (416, 208),"image": "images/Celemony/Menu/Sports Celemony/Okajima.png","hover": "images/Celemony/Menu/Sports Celemony/Okajima hover.png","name": "岡島"}, {"pos": (496, 220),"image": "images/Celemony/Menu/Sports Celemony/Kojima.png","hover": "images/Celemony/Menu/Sports Celemony/Kojima hover.png","name": "小島"}, {"pos": (560, 216),"image": "images/Celemony/Menu/Sports Celemony/Itou.png","hover": "images/Celemony/Menu/Sports Celemony/Itou hover.png","name": "伊藤"}, {"pos": (672, 209),"image": "images/Celemony/Menu/Sports Celemony/Saburo.png","hover": "images/Celemony/Menu/Sports Celemony/Saburo hover.png","name": "三朗"}, {"pos": (720, 60),"type":"textbutton","text":_("继续"),"name": "確認終了"}]
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

    play effect3 "sound/Effect Sound/Break 1.ogg" noloop
    $ sys_effect3_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_4150D18D984E4FA891D9F6C8921DCD50 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_4CBC3D399C6A4D2DAC7D06010FCCC122

    show rs_image_50574D67D9E1480190A94440CC260636 _("选择出赛选手") as hint_1:
        xpos 800
        ypos 375
        parallel:
            linear 20 xpos -200
            xpos 800
            repeat
    show rs_image_50574D67D9E1480190A94440CC260636 _("选择出赛选手") as hint_2:
        xpos 800
        ypos 375
        pause 5
        parallel:
            linear 20 xpos -200
            xpos 800
            repeat
    show rs_image_50574D67D9E1480190A94440CC260636 _("选择出赛选手") as hint_3:
        xpos 800
        ypos 375
        pause 10
        parallel:
            linear 20 xpos -200
            xpos 800
            repeat
    show rs_image_50574D67D9E1480190A94440CC260636 _("选择出赛选手") as hint_4:
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
        {"x": 52, "y": 10, "id": 0, "image": "images/Celemony/Event/Running.png"},
        {"x": 237, "y": 10, "id": 3, "image": "images/Celemony/Event/Ball shooting.png"},
        {"x": 422, "y": 10, "id": 2, "image": "images/Celemony/Event/Race walking.png"},
        {"x": 607, "y": 10, "id": 0, "image": "images/Celemony/Event/Running.png"},
        {"x": 52, "y": 97, "id": 3, "image": "images/Celemony/Event/Ball shooting.png"},
        {"x": 237, "y": 97, "id": 1, "image": "images/Celemony/Event/Riding battle.png"},
        {"x": 422, "y": 97, "id": 3, "image": "images/Celemony/Event/Ball shooting.png"},
        {"x": 607, "y": 97, "id": 2, "image": "images/Celemony/Event/Race walking.png"},
        {"x": 52, "y": 184, "id": 1, "image": "images/Celemony/Event/Riding battle.png"},
        {"x": 237, "y": 184, "id": 0, "image": "images/Celemony/Event/Running.png"},
        {"x": 422, "y": 184, "id": 3, "image": "images/Celemony/Event/Ball shooting.png"},
        {"x": 607, "y": 184, "id": 1, "image": "images/Celemony/Event/Riding battle.png"},
        {"x": 52, "y": 271, "id": 2, "image": "images/Celemony/Event/Race walking.png"},
        {"x": 237, "y": 271, "id": 1, "image": "images/Celemony/Event/Riding battle.png"},
        {"x": 422, "y": 271, "id": 2, "image": "images/Celemony/Event/Race walking.png"},
        {"x": 607, "y": 271, "id": 0, "image": "images/Celemony/Event/Running.png"},
    ], {
        "base": {
            "Itou": [1, -2,  1,  1],
            "Izumi": [2,  1,  1,  3],
            "Katou": [3,  3,  3,  3],
            "Kimura": [4,  4,  3, -2],
            "Kojima": [2, -2,  2,  2],
            "Matsuda": [3,  4,  1,  4],
            "Okajima": [1,  0,  2,  2],
            "Saburou": [4,  1,  4,  4],
            "Sakuya": [3,  2,  1,  4],
            "Satou": [1,  1,  1,  1],
            "Shinobu": [3,  4,  3,  0],
            "Shintarou": [1,  1,  4,  2],
            "Sora": [4,  2,  2,  3],
            "Tomo": [0, -12, 3,  0],
            "Tsubasa": [-2, -12, 2, -1],
            "Tsuki": [3,  4, -2,  2],
        },
        "extra": [
            {
                "condition": [[], ["Itou", "Kimura"]], # RUN RUN LOVERS
                "range": [
                    {"rate": [0, 0.5], "value": 2, "description": _("因为和木村亲在一起，伊藤酱变得很努力")},
                    {"rate": [0.5, 0.6], "value": -2, "description": _("因为太过在意木村亲，伊藤酱犯了不少小失误")},
                    {"rate": [0.6, 1], "value": 0}
                ]
            },
            {
                "condition": [[], ["Itou", "Kimura", "Sakuya", "Saburou"]], # 双低集团
                "range": [
                    {"rate": [0, 1], "value": -2, "description": _("双低集团混在一起不会有好事的……")}
                ]
            },
            {
                "condition": [[], ["Katou", "Matsuda"]], # 找不到对象同盟
                "range": [
                    {"rate": [0, 1], "value": 2, "description": _("加藤酱和松田亲达成了奇妙的共识")}
                ]
            },
            {
                "condition": [[], ["Okajima", "Kojima"]], # “搞个大新闻”
                "range": [
                    {"rate": [0, 0.5], "value": 3, "description": _("小岛君在部长面前特别努力")},
                    {"rate": [0.5, 1], "value": -3, "description": _("新闻部的两人又把比赛放到一边取材去了")}
                ]
            },
            {
                "condition": [[], ["Kojima", "Tsubasa"]], # 白色***同志
                "range": [
                    {"rate": [0, 0.5], "value": 3, "description": _("小岛君在帮翼亲，他们的关系有这么好吗")},
                    {"rate": [0.5, 1], "value": -3, "description": _("小岛君在帮翼亲，但好像起了反效果")}
                ]
            },
            {
                "condition": [[], ["Matsuda", "Sakuya"]], # 远观而不亵玩
                "range": [
                    {"rate": [0, 0.5], "value": 4, "description": _("松田亲真的很想在傲娇君面前好好表现呢")},
                    {"rate": [0.5, 0.6], "value": 2, "description": _("松田亲很卖力，是因为傲娇君吗")},
                    {"rate": [0.6, 0.8], "value": -4, "description": _("因为傲娇君的存在松田亲彻底慌乱了")},
                    {"rate": [0.8, 1], "value": 0}
                ]
            },
            {
                "condition": [[1], ["Saburou", "Shintarou"]], # 肌肤相亲
                "range": [
                    {"rate": [0, 0.2], "value": 10, "description": _("和三酱的肌肤相亲，嘿嘿")},
                    {"rate": [0.2, 0.4], "value": -10, "description": _("比赛算什么，三酱最重要！")},
                    {"rate": [0.4, 1], "value": 0}
                ]
            },
            {
                "condition": [[], ["Saburou", "Tomo"]], # 猫的本性
                "range": [
                    {"rate": [0, 0.35], "value": 1, "description": _("三酱总是盯着友亲看，呜呜")},
                    {"rate": [0.35, 0.5], "value": -1, "description": _("三酱居然会袭击友亲，真是的")},
                    {"rate": [0.5, 1], "value": 0}
                ]
            },
            {
                "condition": [[], ["Tsubasa", "Tomo", "Sakuya"]], # 三角恋？
                "range": [
                    {"rate": [0, 0.2], "value": 1, "description": _("傲娇君和翼亲关系真好")},
                    {"rate": [0.2, 0.5], "value": -1, "description": _("果然傲娇君翼亲和友亲的三角恋会出问题")},
                    {"rate": [0.5, 1], "value": 0}
                ]
            },
            {
                "condition": [[], ["Tsubasa", "Matsuda", "Sakuya"]], # 三角恋
                "range": [
                    {"rate": [0, 0.25], "value": 1, "description": _("翼亲和松田亲是竞争对手呢")},
                    {"rate": [0.25, 1], "value": 0}
                ]
            },
            {
                "condition": [[0, 2, 3], ["Saburou", "Shintarou"]], # 我是直(wan)的
                "range": [
                    {"rate": [0, 0.4], "value": 1, "description": _("和三酱同一个项目真好")},
                    {"rate": [0.4, 0.5], "value": 2, "description": _("必须给三酱展现出我的毅力！")},
                    {"rate": [0.5, 0.6], "value": -2, "description": _("太过在意三酱了……大家对不起")},
                    {"rate": [0.6, 1], "value": 0}
                ]
            },
            {
                "condition": [[], ["Sakuya", "Tsubasa"]], # 并不讨厌
                "range": [
                    {"rate": [0, 0.2], "value": 1, "description": _("傲娇君很卖力呢，是因为翼亲吧")},
                    {"rate": [0.2, 0.4], "value": -1, "description": _("翼亲总是心神不宁")},
                    {"rate": [0.4, 0.5], "value": -5, "description": _("啊，早知道不把傲娇君和翼亲分在同一个组就好了")},
                    {"rate": [0.5, 0.6], "value": 4, "description": _("哇，傲娇君的大活跃！")},
                    {"rate": [0.6, 1], "value": 0}
                ]
            },
            {
                "condition": [[], ["Sora", "Tsuki"]], # 赤峰双子
                "range": [
                    {"rate": [0, 0.65], "value": 4, "description": _("赤峰兄弟真的好厉害")},
                    {"rate": [0.65, 1], "value": -1, "description": _("阿月在赛场上也这么开放，我也想和三酱……")}
                ]
            },
            {
                "condition": [[], ["Sora", "Tomo"]], # 甜食党
                "range": [
                    {"rate": [0, 1], "value": 1, "description": _("小空和友亲都喜欢料理吧，难怪他们这么默契")}
                ]
            },
            {
                "condition": [[], ["Tsubasa", "Tomo"]], # 第一次的温柔
                "range": [
                    {"rate": [0, 0.5], "value": 1, "description": _("总觉得友亲和翼亲有一腿")},
                    {"rate": [0.5, 0.6], "value": 2, "description": _("翼亲的超常发挥！")},
                    {"rate": [0.6, 0.7], "value": -1, "description": _("以后绝对不允许友亲和翼亲不分场合秀恩爱了")},
                    {"rate": [0.7, 0.95], "value": 0},
                    {"rate": [0.95, 1], "value": 5, "description": _("友亲和翼亲又在约会")}
                ]
            },
            {
                "condition": [[], ["Shintarou", "Tomo"]], # 变态同志
                "range": [
                    {"rate": [0, 0.5], "value": 3, "description": _("和友亲达成了共识")},
                    {"rate": [0.5, 1], "value": -3, "description": _("唔，友亲的作战好像问题很大……")}
                ]
            },
            {
                "condition": [[1], ["Tomo", "Shinobu"]], # 青梅竹马 高级版
                "range": [
                    {"rate": [0, 0.5], "value": 10, "description": _("哇，友亲居然差点活到最后，佩服")},
                    {"rate": [0.5, 0.9], "value": -2, "description": _("连小忍都被友亲打乱步调了")},
                    {"rate": [0.9, 1], "value": 0}
                ]
            },
            {
                "condition": [[0, 2, 3], ["Tomo", "Shinobu"]], # 青梅竹马
                "range": [
                    {"rate": [0, 0.5], "value": 2, "description": _("小忍在帮友亲呢")},
                    {"rate": [0.5, 0.9], "value": -2, "description": _("友亲真是总在给小忍帮倒忙呢")},
                    {"rate": [0.9, 1], "value": 0}
                ]
            }
        ]
    }) from _call_celemony

    jump block_0000395F

    return

label block_0000395F:
    # Node: 0000395F (Calculate)
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

    if sum(1 if x > 8 else 0 for x in _return["score"]) > 2:
        jump block_000024C9
    else:
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

    jump block_0000147F

    return

label block_000024CB:
    # Node: 000024CB (Lose)
    play effect "sound/Effect Sound/Sorry 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Sorry 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_D123F79A6B5940889E3CF0422ABE8095 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_7C9AB5ABEE5E487EAB75A4EA474E500B

    pause 2

    jump block_0000147F

    return

label block_0000147F:
    # Node: 0000147F (Result)
    call convert_celemony_detail(_return, [_("百米田径"), _("骑马战"), _("借物竞走"), _("投球入篮")])

    python:
        set_window("イベントモード")
        for index, event in enumerate(_return):
            _return[index]["succeed"] = _return[index]["score"] > 8

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
        jump block_00003989

    return

label block_00003989:
    # Node: 00003989 ()

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

    jump block_000007E0

    return
