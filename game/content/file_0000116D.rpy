# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 0000116D (阿月測眼力)

label block_0000116E:
    # Node: 0000116E (開始)
    python:
        CorrectCount = 0
        CurrentIndex = 0
        TotalCount = 0
        TimeState = 0
        record_volume("music")
        renpy.music.set_volume(0, 1, "music")

    play effect "sound/Effect Sound/Drum 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ set_place_title(False)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 1.5

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_69E470D45F2C464CA4A1DAED028068FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    if sys_music2_current_file != "sound/BGM/Series - Akamine brothers.ogg":
        play music2 "sound/BGM/Series - Akamine brothers.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Series - Akamine brothers.ogg"

    pause 0.4

    play effect "sound/Effect Sound/Break 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_ED4EBC53C3F040A5B5A519ACC94246AA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_C29BFF9F2C814823B4B63C9D37A39E79

    pause 0.4

    if Chapter > 2 and (GTsukiTestSoraMode == False):
        $ TimeState = 2
    elif GTsukiTestSoraMode == True:
        $ TimeState = 1
    else:
        $ TimeState = 0

    call screen tsuki_test_level_selector

    $ zorder_tag_348CF07D60744BC79223A712FCFA9BD9 = 400

    if _return == "Return":
        jump tsuki_test_end
    if _return == "Find1":
        jump tsuki_test_find_1
    if _return == "Number1":
        jump tsuki_test_number_1
    if _return == "Find2":
        jump tsuki_test_find_2
    if _return == "Number2":
        jump tsuki_test_number_2
    if _return == "Find3":
        jump tsuki_test_find_3

    return

screen tsuki_test_level_selector:
    fixed at tsuki_test_level_selector_screen:
        add "images/Games/Tsukis-concentration-test/Blackboard.png" xalign 0.5 yalign 0.5 zoom 0.4
        textbutton _("寻找文字\n简单"):
            style "tsuki_test_level_selector_button"
            xpos 400
            ypos 175
            action Return("Find1")
        if GTsukiTestStage > 1:
            textbutton _("寻找文字\n中等"):
                style "tsuki_test_level_selector_button"
                xpos 226
                ypos 265
                action Return("Find2")
        else:
            text _("寻找文字\n中等"):
                style "tsuki_test_level_selector_muted_text"
                xpos 226
                ypos 275
        if GTsukiTestStage > 3:
            textbutton _("寻找文字\n困难"):
                style "tsuki_test_level_selector_button"
                xpos 570
                ypos 270
                action Return("Find3")
        else:
            text _("寻找文字\n困难"):
                style "tsuki_test_level_selector_muted_text"
                xpos 570
                ypos 280
        if GTsukiTestStage > 0:
            textbutton _("寻找数字\n简单"):
                style "tsuki_test_level_selector_button"
                xpos 260
                ypos 395
                action Return("Number1")
        else:
            text _("寻找数字\n简单"):
                style "tsuki_test_level_selector_muted_text"
                xpos 260
                ypos 405
        if GTsukiTestStage > 2:
            textbutton _("寻找数字\n困难"):
                style "tsuki_test_level_selector_button"
                xpos 460
                ypos 382
                action Return("Number2")
        else:
            text _("寻找数字\n困难"):
                style "tsuki_test_level_selector_muted_text"
                xpos 460
                ypos 392
        textbutton _("离开"):
            style "tsuki_test_level_selector_button"
            xpos 399
            ypos 280
            action Return("Return")

transform tsuki_test_level_selector_screen:
    xanchor 0.5
    xpos 400
    ypos -500
    on show:
        easein 0.5 ypos 0
    on hide:
        easeout_back 0.7 ypos -800
transform tsuki_test_level_selector_timeline(timeline):
    xpos 0
    ypos 0
    xzoom 1
    linear timeline xzoom 0

style tsuki_test_level_selector_button:
    xanchor 0.5
style tsuki_test_level_selector_button_text:
    color "#FAFAFA"
    hover_color "#BCAAA4"
    text_align 0.5
    font "font/zcool-happy-ayumi-extended.ttf"
style tsuki_test_level_selector_muted_text is tsuki_test_level_selector_button_text:
    xanchor 0.5
    color "#BCAAA4"

screen tsuki_test_selector(question):
    python:
        random.shuffle(question["item"])
    text question["title"] style "tsuki_test_selector_title"
    if question["type"] == "number":
        grid 4 2:
            xalign 0.5
            yalign 0.5
            for item in question["item"]:
                textbutton item:
                    style "tsuki_test_selector_number_item"
                    action Return(item)
    else:
        vbox:
            xalign 0.5
            yalign 0.6
            for item in question["item"]:
                textbutton item:
                    style "tsuki_test_selector_find_item"
                    action Return(item)
    if "time" in question:
        timer question["time"] action Return("")
        add "images/Games/Tsukis-concentration-test/Time.png" at tsuki_test_level_selector_timeline(question["time"])

style tsuki_test_selector_title:
    color "#FAFAFA"
    size 50
    xalign 0.5
    ypos 20
    font "font/source-hans-sans-heavy.ttc"
style tsuki_test_selector_find_item:
    ymargin 5
    xalign 0.5
    xsize 400
    background "images/Games/Tsukis-concentration-test/Item.png"
style tsuki_test_selector_find_item_text:
    font "font/source-hans-sans-medium.ttc"
    size 30
    xalign 0.5
    color "#FFFFFF"
    hover_color "#E0E0E0"
style tsuki_test_selector_number_item:
    xsize 177
    ysize 156
    xmargin 10
    ymargin 10
    background "images/Games/Tsukis-concentration-test/Number button.png"
style tsuki_test_selector_number_item_text:
    font "font/source-hans-sans-medium.ttc"
    size 80
    xalign 0.5
    yalign 0.5
    color "#FFFFFF"
    hover_color "#808080"

label tsuki_test_end:
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    $ del CorrectCount
    $ del CurrentIndex
    $ del TotalCount
    $ del TimeState

    stop music2 fadeout 0.5
    $ sys_music_current_file = ""

    $ reverse_volume("music", 0.7)

    return

label tsuki_test_find_1:
    play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"
    $ set_window("イベントモード")

    if TimeState == 2:
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "就看你能多快找到正确答案了。{w}\n来，开始了。"
        window hide
    elif TimeState == 1:
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，头脑训练要开始了哦。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这次的训练是“{color=#0080FF}寻找正确选项{/color}”。\n不过，一定要小心{color=#FF0000}时间限制{/color}哦。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "速速找到正确答案就好了呐。{w}\n来，开始了。"
        window hide
    else:
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "就看你能多快找到正确答案了。{w}\n来，开始了。"
        window hide

    jump tsuki_test_find_1_content

    return

label tsuki_test_find_1_content:
    $ TotalCount = 10
    $ tsuki_test_question_set = [
        {
            "type": "find",
            "title": _("找到 {color=#2196F3}TALPIDAE{/color}"),
            "item": ["TALPIDAE", "TALPIDEA", "TALPIDOE", "PANTS"],
            "time": 3,
            "result": "TALPIDAE"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}TALPIDAE{/color}"),
            "item": ["BIKINI", "TALPIDAE", "TALPIDEA", "TALPIDOE"],
            "time": 3,
            "result": "TALPIDAE"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}TALPIDAE{/color}"),
            "item": ["TOLPIDAE", "TALPIDAE", "TOLPIDIE", "PANTS", "AILURUS FULGENS", "TALPIDEE"],
            "time": 3,
            "result": "TALPIDAE"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}TALPIDAE{/color}"),
            "item": ["TOLPIDAE", "TOLPLDAE", "TALPIDAE", "TOLPODOE", "PANTS", "TSUBASA", "AUTUMN FOLIAGE", "TALPTALP"],
            "time": 3,
            "result": "TALPIDAE"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}TSUBASA{/color}"),
            "item": ["TSUMIKI", "TSUBOMI", "TSUBAME", "TSUBASA"],
            "time": 3,
            "result": "TSUBASA"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}TSUBASA{/color}"),
            "item": ["TSUBASE", "TSUBASO", "TSUBASA", "TSUPASA"],
            "time": 3,
            "result": "TSUBASA"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}TSUBASA{/color}"),
            "item": ["SHIPASA", "SHIBASA", "TSUPAZA", "TSUBAZA", "TSUBASA", "TSUPASA"],
            "time": 3,
            "result": "TSUBASA"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}TSUBASA{/color}"),
            "item": ["TSUPASA", "ZUBASA", "TSBASA", "ZUBAZA", "TSUBAZA", "TSUHAZA", "TSUPAZA", "TSUBASA"],
            "time": 3,
            "result": "TSUBASA"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}VIBRATOR{/color}"),
            "item": ["VIBRETAR", "VIBRETOR", "VIBRATER", "VIBRETER", "VIBROTAR", "VIBROTER", "VIBRATOR", "VINROTOR"],
            "time": 3.5,
            "result": "VIBRATOR"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}VIBRATOR{/color}"),
            "item": ["VIBRETAR", "VIBROTAR", "VIBROTER", "VIBROTOR", "VIBRATOR", "VIBRATER", "VIBRATAR", "VIBRETER"],
            "time": 3.5,
            "result": "VIBRATOR"
        }
    ]

    jump tsuki_test_run_question

    return

label tsuki_test_run_question:
    while CurrentIndex < TotalCount:
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        if tsuki_test_question_set[CurrentIndex]["type"] == "number":
            call tsuki_test_show_number(tsuki_test_question_set[CurrentIndex]["numbers"])
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"
        call screen tsuki_test_selector(tsuki_test_question_set[CurrentIndex])
        stop effect2 fadeout 0.2
        $ sys_effect2_current_file = ""
        if _return == tsuki_test_question_set[CurrentIndex]["result"]:
            call tsuki_test_correct
        else:
            call tsuki_test_wrong
        $ CurrentIndex += 1

    jump tsuki_test_judge_result

    return

label tsuki_test_correct:
    play effect "sound/Effect Sound/Correct 1.ogg" noloop

    show rs_image_0C55A05D870D4AFD8FA6561C542AEB06 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_2594659CB59F456896B2EF27AD70323C as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"
        show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    elif TimeState == 1:
        show rs_image_7E2778FA3D624F319D303738D4143BE5 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        window show
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "非常好哦！"
        show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    else:
        show rs_image_CA7FB6339967475B8EDC72EB94052C60 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"
        show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    
    window hide

    hide tag_348CF07D60744BC79223A712FCFA9BD9
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    $ CorrectCount += 1

    return

label tsuki_test_wrong:
    play effect "sound/Effect Sound/Wrong 1.ogg" noloop

    show rs_image_4C358D6358994092B67D2FE620F9E858 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_89E17548BB5E44C3928F3166B177C150 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"
        show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    elif TimeState == 1:
        show rs_image_B63B525194554F0BBF36CCFF8577D5AC as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        window show
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好可惜。"
        show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    else:
        show rs_image_5CE8CAA349B8484888F68CD67D37CBFD as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"
        show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    
    window hide

    hide tag_348CF07D60744BC79223A712FCFA9BD9
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    return

label tsuki_test_judge_result:
    if GTsukiTestStage == 5:
        jump tsuki_test_final_question
    elif (CorrectCount / float(TotalCount)) >= 0.7:
        jump tsuki_test_next_question
    else:
        jump block_000037B7

    return

label tsuki_test_final_question:
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    if TimeState == 1:
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "[TotalCount]问中[CorrectCount]问正确！{w}很不错哦。\n什么时候想再次挑战请随时来找我。{w=0.7}{nw}"
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"
        extend "{i}以上、解散♪{/i}"
    else:
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "[TotalCount]问中[CorrectCount]问正确！{w}做的不错。\n什么时候想再次挑战随时来找我。{w=0.7}{nw}"
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"
        extend "{i}以上、解散！{/i}"

    window hide

    pause 0.6

    play effect "sound/Effect Sound/Drum 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_31FEF114566B4AB483D935C987B9E096
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.7

    $ set_window("(標準)")

    jump tsuki_test_end

    return

label tsuki_test_next_question:
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if TimeState == 1:
        show rs_image_7E2778FA3D624F319D303738D4143BE5 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    elif TimeState == 2:
        show rs_image_2594659CB59F456896B2EF27AD70323C as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    else:
        show rs_image_CA7FB6339967475B8EDC72EB94052C60 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    
    window show

    if TimeState == 1:
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "[TotalCount]问中[CorrectCount]问正确！{w}真的很努力了。\n看样子可以挑战{nw}"
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"
        extend "{color=#FF00FF}下个问题{/color}了呐。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "下次会换更难的问题。\n准备好了请随时来找我哦。{w=0.7}{nw}"
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"
        extend "{i}以上、解散♪{/i}"
    else:
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "[TotalCount]问中[CorrectCount]问正确！{w}做的不错。\n看样子可以挑战{nw}"
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"
        extend "{color=#FF00FF}下个问题{/color}了。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "下次会换个更难的问题。\n准备好了随时来找我。{w=0.7}{nw}"
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"
        extend "{i}以上、解散！{/i}"

    window hide

    pause 0.6

    play effect "sound/Effect Sound/Drum 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_31FEF114566B4AB483D935C987B9E096
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.7

    $ set_window("(標準)")

    $ GTsukiTestStage = GTsukiTestStage + 1

    if judge_lm_condition([{ "scope": 0, "content": "CXQTsukiTest == False" }]):
        jump tsuki_test_quest_finished
    if judge_lm_condition([]):
        jump tsuki_test_end

    return

label tsuki_test_quest_finished:
    $ set_window("(標準)")
    play effect2 "sound/BGM/Quest Finished.ogg" noloop
    $ sys_effect2_current_file = "sound/BGM/Quest Finished.ogg"

    window show
    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"
    window hide

    pause 0.8

    $ CXQTsukiTest = True

    jump tsuki_test_end

    return

label tsuki_test_retry_question:
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if TimeState == 1:
        show rs_image_B63B525194554F0BBF36CCFF8577D5AC as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    elif TimeState == 2:
        show rs_image_89E17548BB5E44C3928F3166B177C150 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
    else:
        show rs_image_5CE8CAA349B8484888F68CD67D37CBFD as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    if TimeState == 1:
        s_character_4CFD8855F77C4A9085B6B9BFABDD845A "[TotalCount]问中[CorrectCount]问正确！{w}很不错哦。\n不过，这样还不足以挑战{nw}"
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"
        extend "{color=#FF00FF}下个问题{/color}呐。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "等准备好了来找我，\n我们再试一次。{w=0.7}{nw}"
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"
        extend "{i}以上、解散♪{/i}"
    else:
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "[TotalCount]问中[CorrectCount]问正确！{w}你很努力了。\n不过，这个水平还不足以挑战{nw}"
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"
        extend "{color=#FF00FF}下个问题{/color}。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "下次我们再试一次。\n准备好了随时来找我。{w=0.7}{nw}"
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"
        extend "{i}以上、解散！{/i}"

    window hide

    pause 0.6

    play effect "sound/Effect Sound/Drum 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_31FEF114566B4AB483D935C987B9E096
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.7

    $ set_window("(標準)")

    jump tsuki_test_end

    return

label tsuki_test_show_number(numbers):
    show rs_image_CAF438FA09DC41CCB7C54CB078F6541F as tsuki_test_number_background at Transform(xpos=273, ypos=174)
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ tsuki_test_show_number_count = len(numbers)
    $ tsuki_test_show_number_pointer = 0
    while tsuki_test_show_number_pointer < tsuki_test_show_number_count:
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        show rs_image_DAF60EB1E6554D8E9D9F69C2498A1C6D numbers[tsuki_test_show_number_pointer] as tsuki_test_number_pointer:
            alpha 0
            xanchor 0.5
            yanchor 0.5
            xpos 425
            ypos 290
            parallel:
                easein 0.2 alpha 1 xpos 400
                pause 0.6
                easein 0.2 alpha 0 xpos 375
        $ renpy.pause(0.8, hard=True)
        hide tsuki_test_number_pointer
        $ tsuki_test_show_number_pointer += 1

    hide tsuki_test_number_background
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ del tsuki_test_show_number_count
    $ del tsuki_test_show_number_pointer

    return

label tsuki_test_number_1:
    play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"
    $ set_window("イベントモード")

    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 2" }]):
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，尝试记住他们。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，开始。"
        window hide
    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 1" }]):
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，头脑训练要开始了哦。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，请试着记住他们。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，准备——{w}开始！"
        window hide
    if judge_lm_condition([]):
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，尝试记住他们。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，开始。"
        window hide

    jump tsuki_test_number_1_content

    return

label tsuki_test_number_1_content:
    $ TotalCount = 9
    $ tsuki_test_question_set = [
        {
            "type": "number",
            "title": _("0-9没有出现的数字是"),
            "numbers": ["9", "5", "8", "4", "0", "3", "6", "2", "1"],
            "item": ["0", "7", "2", "1", "4", "6", "5", "8"],
            "result": "7"
        }, {
            "type": "number",
            "title": _("0-9没有出现的数字是"),
            "numbers": ["5", "3", "1", "9", "7", "4", "0", "6", "8"],
            "item": ["2", "8", "0", "1", "4", "7", "6", "5"],
            "result": "2"
        }, {
            "type": "number",
            "title": _("0-9没有出现的数字是"),
            "numbers": ["1", "7", "3", "5", "0", "9", "8", "2", "6"],
            "item": ["5", "4", "7", "8", "1", "2", "3", "6"],
            "result": "4"
        }, {
            "type": "number",
            "title": _("3出现了多少次"),
            "numbers": ["3", "2", "1", "1", "1", "2", "1", "3", "3"],
            "item": ["0", "1", "2", "3", "4", "5", "6", "7"],
            "result": "3"
        }, {
            "type": "number",
            "title": _("1出现了多少次"),
            "numbers": ["1", "4", "1", "2", "3", "4", "3", "4"],
            "item": ["0", "1", "2", "3", "4", "5", "6", "7"],
            "result": "2"
        }, {
            "type": "number",
            "title": _("2出现了多少次"),
            "numbers": ["1", "1", "2", "3", "1", "3", "3", "2"],
            "item": ["0", "1", "2", "3", "4", "5", "6", "7"],
            "result": "2"
        }, {
            "type": "number",
            "title": _("2的颜色是"),
            "numbers": [
                "{color=#FF0000}1{/color}",
                "{color=#008000}3{/color}",
                "{color=#FF00FF}2{/color}",
                "{color=#FF00FF}2{/color}",
                "{color=#0000FF}4{/color}",
                "{color=#0000FF}4{/color}",
                "{color=#FF0000}1{/color}"
            ],
            "item": [_("绿"), _("黄"), _("红"), _("粉"), _("白"), _("黑"), _("紫"), _("蓝")],
            "result": _("粉")
        }, {
            "type": "number",
            "title": _("3的颜色是"),
            "numbers": [
                "{color=#0000FF}1{/color}",
                "{color=#FF0000}2{/color}",
                "{color=#0000FF}3{/color}",
                "{color=#0000FF}4{/color}",
                "{color=#FF0000}5{/color}",
                "{color=#FF0000}6{/color}",
                "{color=#0000FF}7{/color}"
            ],
            "item": [_("绿"), _("黄"), _("红"), _("粉"), _("白"), _("黑"), _("紫"), _("蓝")],
            "result": _("蓝")
        }, {
            "type": "number",
            "title": _("1的颜色是"),
            "numbers": [
                "{color=#008000}1{/color}",
                "{color=#800080}2{/color}",
                "{color=#FF0000}3{/color}",
                "{color=#FFFF00}4{/color}",
                "{color=#FF00FF}5{/color}",
                "{color=#0000FF}6{/color}"
            ],
            "item": [_("绿"), _("黄"), _("红"), _("粉"), _("白"), _("黑"), _("紫"), _("蓝")],
            "result": _("绿")
        }
    ]

    jump tsuki_test_run_question

    return

label tsuki_test_find_2:
    play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    if TimeState == 2:
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练也是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "比上次要难得多，做好觉悟比较好。{w}\n那么，开始。"
    elif TimeState == 1:
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，头脑训练要开始了哦。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这次的训练是“{color=#0080FF}寻找正确选项{/color}”。\n不过，也要小心{color=#FF0000}时间限制{/color}哦。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "比上次要难很多，一定小心哦。{w}\n加油，准备——{w}开始！"
    else:
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练也是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "比上次要难得多，做好觉悟比较好。{w}\n那么，开始。"
    
    window hide

    jump tsuki_test_find_2_content

    return

label tsuki_test_find_2_content:
    $ TotalCount = 10
    $ tsuki_test_question_set = [
        {
            "type": "find",
            "title": _("找到 {color=#2196F3}SCHOOLBOYS{/color}"),
            "item": ["SCHOOLBOYZ", "SCHOLOBOYS", "SCHOLLBOYS", "SCHOOLBOYS", "SCHOOLBOLS"],
            "time": 3,
            "result": "SCHOOLBOYS"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}SCHOOLBOYS{/color}"),
            "item": ["SCHOLOBOYS", "SCHOOLBOYZ", "SCHOLBOOYS", "SCHOOLBOYS", "SCHOOLBLOS"],
            "time": 3,
            "result": "SCHOOLBOYS"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}SCHOOLBOYS{/color}"),
            "item": ["SCHLOOBOYZ", "SCHOLOBOYZ", "SCHLOOBOYS", "SCHOOLBOYZ", "SCHOULBOYS", "SCHLOLBOYS", "SCHOLOBOYS", "SCHOOLBOYS"],
            "time": 3,
            "result": "SCHOOLBOYS"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}AYUMI{/color}"),
            "item": ["AYUMU", "AYOMU", "AYOMI", "AYUMI", "AYAMI"],
            "time": 3,
            "result": "AYUMI"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}AYUMI{/color}"),
            "item": ["AYUMA", "AYOMI", "AYOMO", "AYAMI", "AYAMA", "AYUMI", "AYUMU"],
            "time": 3,
            "result": "AYUMI"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}AYUMI{/color}"),
            "item": ["AYIMI", "AYIMU", "AYAMA", "AYAMI", "AYOMI", "AYUMU", "AYUMI", "AYUMA"],
            "time": 3,
            "result": "AYUMI"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}WOLFS{/color}"),
            "item": ["WALFS", "WOLPZ", "WOLPUS", "FOLFS", "WOLFZ", "WOLWZ", "WOLFS", "WOLWS"],
            "time": 3,
            "result": "WOLFS"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}WOLFS{/color}"),
            "item": ["WOPOS", "WALFZ", "WOLAS", "WOPLS", "WALFS", "WOLFZ", "WOLFS", "WOLPS"],
            "time": 3,
            "result": "WOLFS"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}PRAECANTATOR{/color}"),
            "item": ["PRAECAHTATER", "PRAECAHTATOR", "PRAECANTATOR", "PRAECANTETOR", "PRAECENTATOR"],
            "time": 3.5,
            "result": "PRAECANTATOR"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}PRAECANTATOR{/color}"),
            "item": ["PRAECAHTATOR", "PRAECANTATOR", "PRAECENTATOR", "PREACANTATOR", "PRAECANTATER", "PRAECANTETER", "PRAEHANTATOR", "PRAECAHTOTER"],
            "time": 3.5,
            "result": "PRAECANTATOR"
        }
    ]

    jump tsuki_test_run_question

    return

label tsuki_test_number_2:
    play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    if TimeState == 2:
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，尝试记住他们。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不用多说，难度肯定比上次高。{w}那么，开始。"
    elif TimeState == 1:
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，头脑训练要开始了哦。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，请试着记住他们。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "请注意比上次要难了一些哦。准备——{w}开始！"
    else:
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，尝试记住他们。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不用多说，难度肯定比上次高。{w}那么，开始。"
    
    window hide

    jump tsuki_test_number_2_content

    return

label tsuki_test_number_2_content:
    $ TotalCount = 9
    $ tsuki_test_question_set = [
        {
            "type": "number",
            "title": _("0-9没有出现的数字是"),
            "numbers": ["4", "0", "9", "3", "8", "7", "5", "2", "6"],
            "item": ["0", "7", "2", "1", "4", "6", "5", "8"],
            "result": "1"
        }, {
            "type": "number",
            "title": _("0-9没有出现的数字是"),
            "numbers": ["4", "1", "3", "0", "5", "8", "9", "7", "2"],
            "item": ["3", "6", "7", "9", "4", "2", "5", "8"],
            "result": "6"
        }, {
            "type": "number",
            "title": _("0-9没有出现的数字是"),
            "numbers": ["9", "3", "0", "5", "2", "4", "7", "5", "6"],
            "item": ["4", "1", "2", "3", "0", "9", "6", "5"],
            "result": "1"
        }, {
            "type": "number",
            "title": _("5出现了多少次"),
            "numbers": ["5", "9", "9", "4", "4", "5", "4", "9"],
            "item": ["0", "1", "2", "3", "4", "5", "6", "7"],
            "result": "2"
        }, {
            "type": "number",
            "title": _("4出现了多少次"),
            "numbers": ["8", "6", "2", "4", "6", "2", "7", "8", "2"],
            "item": ["0", "1", "2", "3", "4", "5", "6", "7"],
            "result": "1"
        }, {
            "type": "number",
            "title": _("9出现了多少次"),
            "numbers": ["5", "2", "9", "5", "2", "9", "5", "1", "9"],
            "item": ["0", "1", "2", "3", "4", "5", "6", "7"],
            "result": "3"
        }, {
            "type": "number",
            "title": _("0的颜色是"),
            "numbers": [
                "{color=#FF0000}9{/color}",
                "{color=#FF0000}8{/color}",
                "{color=#0000FF}7{/color}",
                "{color=#0000FF}6{/color}",
                "{color=#008000}5{/color}",
                "{color=#008000}4{/color}",
                "{color=#FFFF00}3{/color}",
                "{color=#FFFF00}2{/color}",
                "{color=#FF8040}1{/color}",
                "{color=#FF8040}0{/color}"
            ],
            "item": [_("绿"), _("黄"), _("红"), _("粉"), _("白"), _("黑"), _("紫"), _("蓝")],
            "result": _("橘")
        }, {
            "type": "number",
            "title": _("7的颜色是"),
            "numbers": [
                "{color=#008000}0{/color}",
                "{color=#0000FF}1{/color}",
                "{color=#008000}2{/color}",
                "{color=#0000FF}3{/color}",
                "{color=#FFFF00}4{/color}",
                "{color=#FF0000}5{/color}",
                "{color=#FFFF00}6{/color}",
                "{color=#FF0000}7{/color}",
                "{color=#FF8000}8{/color}",
                "{color=#FF8000}9{/color}",
            ],
            "item": [_("绿"), _("黄"), _("红"), _("粉"), _("白"), _("黑"), _("紫"), _("蓝")],
            "result": _("红")
        }, {
            "type": "number",
            "title": _("8的颜色是"),
            "numbers": [
                "{color=#FFFF00}0{/color}",
                "{color=#C0C0C0}7{/color}",
                "{color=#FF0000}2{/color}",
                "{color=#800080}1{/color}",
                "{color=#B71C1C}8{/color}",
                "{color=#008000}0{/color}",
                "{color=#FF8000}1{/color}",
                "{color=#FF8000}4{/color}",
                "{color=#0000FF}5{/color}"
            ],
            "item": [_("绿"), _("黄"), _("红"), _("粉"), _("白"), _("黑"), _("紫"), _("蓝")],
            "result": _("红")
        }
    ]

    jump tsuki_test_run_question

    return

label tsuki_test_find_3:
    play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    if judge_lm_condition([{ "scope": 0, "content": "TimeState== 2" }]):
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练仍然是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的非常困难，一定要好好努力。{w}\n那么，开始。"
    if judge_lm_condition([{ "scope": 0, "content": "TimeState== 1" }]):
        $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
        show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，头脑训练要开始了哦。"
        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这次的训练是“{color=#0080FF}寻找正确选项{/color}”。\n不过，也要小心{color=#FF0000}时间限制{/color}哦。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的非常困难，请一定要注意。{w}\n加油，准备——{w}开始！"
    if judge_lm_condition([]):
        show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        window show
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练仍然是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"
        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的非常困难，一定要好好努力。{w}\n那么，开始。"

    window hide

    jump tsuki_test_find_3_content

    return

label tsuki_test_find_3_content:
    $ TotalCount = 10
    $ tsuki_test_question_set = [
        {
            "type": "find",
            "title": _("找到 {color=#2196F3}ユウヒ{/color}"),
            "item": ["ユフヒ", "ユウピ", "ユウヒ", "ヱウヒ"],
            "time": 3,
            "result": "ユウヒ"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}朔{/color}"),
            "item": ["胡", "朝", "期", "朔"],
            "time": 3,
            "result": "朔"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}滑子老师{/color}"),
            "item": ["滑子老师", "骨子老师", "滑了老师", "滑子老帅"],
            "time": 3,
            "result": "滑子老师"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}森海友{/color}"),
            "item": ["林森友", "森梅友", "森海反", "森海友"],
            "time": 3,
            "result": "森海友"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}绫濑しのぶ{/color}"),
            "item": ["绫頼しのぶ", "绫濑しのぶ", "绫濑しのぷ", "绫濑じのぶ", "绫濑しのふ"],
            "time": 3,
            "result": "绫濑しのぶ"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}一之濑つばさ{/color}"),
            "item": ["二之濑つばさ", "一之濑つはさ", "一之頼つばさ", "一之濑つばさ", "三之濑つばさ", "一之濑つぱさ"],
            "time": 3,
            "result": "一之濑つばさ"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}奥村慎太郎{/color}"),
            "item": ["奥村真太郎", "奥材慎太郎", "奥村慎大朗", "奥村慎太朗", "奥村慎犬郎", "奥村慎太郎", "奥村清太郎"],
            "time": 3,
            "result": "奥村慎太郎"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}穂海作哉{/color}"),
            "item": ["穂梅作哉", "补海作哉", "穂海昨哉", "穂海作哉", "穂海乍哉", "穂悔作哉", "穂侮作哉"],
            "time": 3,
            "result": "穂海作哉"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}猫山三朗{/color}"),
            "item": ["猫山三郎", "猫山三朗", "猫川三朗", "猫山二朗", "猫山三郞", "描山三朗", "苗山三朗"],
            "time": 3,
            "result": "猫山三朗"
        }, {
            "type": "find",
            "title": _("找到 {color=#2196F3}赤峰空{/color}"),
            "item": ["赤峰空", "赤蜂空", "赤峰究", "赤峰月", "赤锋空", "赤烽空", "亦峰空", "赤峰突"],
            "time": 3,
            "result": "赤峰空"
        }
    ]

    jump tsuki_test_run_question

    return
