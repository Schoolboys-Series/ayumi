# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000020C1 (小林翻歌牌)

define karuta_sentence_list = [
    _("『{color=#FF0000}滑{/color}子老师是 直的不能再直的 家庭顶梁柱』"),
    _("『{color=#FF0000}半{/color}夜昏暗暗 却从未知少年处 收到了问询』"),
    _("『{color=#FF0000}坐{/color}立难安时 就一定要这么做 拿起电摩君』"),
    _("『{color=#FF0000}期{/color}待写头条 追寻梦幻与真实 寻找大新闻』"),
    _("『{color=#FF0000}小{/color}心这么做 一个不好就会被 其他人撞到』"),
    _("『{color=#FF0000}什{/color}么是道路 无视就好来散步 小翼不迷路』"),
    _("『{color=#FF0000}想{/color}不想知晓 让我来教你就好 姿势要提高』"),
    _("『{color=#FF0000}一{/color}之濑翼君 有时突然变病娇 恋爱的烦恼』"),
    _("『{color=#FF0000}据{/color}传花乃汤 一周里的某一天 非常之热闹』"),
    _("『{color=#FF0000}猫{/color}山两兄弟 如果闻了木天蓼 倒地起不了』"),
    _("『{color=#FF0000}觉{/color}得是不良 其实只是在装样 反正也不小』"),
    _("『{color=#FF0000}做{/color}饭小能手 锅碗瓢盆加汤勺 爆炸威力高』"),
    _("『{color=#FF0000}总{/color}共两根毛 再看今天的表情 变换不安宁』"),
    _("『{color=#FF0000}魔{/color}法师夕阳 一直都和触手斗 总是被吃透』"),
    _("『{color=#FF0000}早{/color}被迷住的 社团训练的经理 今天也亲密』"),
    _("『{color=#FF0000}就{/color}算是英雄 男人全都受不了 快乐也没跑』"),
    _("『{color=#FF0000}动{/color}不动斗嘴 一边疑似是不良 一边优等生』"),
    _("『{color=#FF0000}加{/color}藤酱所曰 喜欢的人的年龄 或许非常高』"),
    _("『{color=#FF0000}居{/color}然要迟到 快快叫九尾帮忙 瞬间到学校』"),
    _("『{color=#FF0000}于{/color}远处等待 只要他一直幸福 那便都安好』"),
    _("『{color=#FF0000}铁{/color}拳的制裁 单纯理由当然有 仅仅为朋友』"),
    _("『{color=#FF0000}所{/color}谓的变态 稍微给尝点甜头 马上服帖帖』"),
    _("『{color=#FF0000}逐{/color}渐变温暖 正因为如此感觉 一把揽入怀』"),
    _("『{color=#FF0000}学{/color}校音乐室 放学后只想和你 两个人一起』"),
    _("『{color=#FF0000}看{/color}似是糖球 吃下去就能抵达 梦想的世界』"),
    _("『{color=#FF0000}痛{/color}苦不安时 陪在身边的就是 最好的朋友』"),
    _("『{color=#FF0000}憧{/color}憬着前辈 清廉正直的目光 星星般闪耀』"),
    _("『{color=#FF0000}只{/color}有这个呐 观察少年的日常 每天都见涨』"),
    _("『{color=#FF0000}本{/color}来是敌人 何时才能得实现 这股恋爱心』"),
    _("『{color=#FF0000}机{/color}智如光君 煽动前辈的好手 效果还真有』"),
    _("『{color=#FF0000}得{/color}道终成仙 超越一切的快感 终成大贤者』"),
    _("『{color=#FF0000}又{/color}叕要拌嘴 传达一切想法的 超发球攻击』"),
    _("『{color=#FF0000}按{/color}摩超拿手 不过特别菜单是 某个人独有』"),
    _("『{color=#FF0000}可{/color}爱小熊猫 作者两人立字据 大家要去吸』"),
    _("『{color=#FF0000}自{/color}从那天起 学院生活成为了 仅有的一切』"),
    _("『{color=#FF0000}背{/color}着双肩包 还被画到漫画里 工口意义上』"),
    _("『{color=#FF0000}九{/color}尾大人呀 为何喜欢类型是 肌肉型的呐』"),
    _("『{color=#FF0000}变{/color}成露出狂 即便如此也要做 上啊野球拳』"),
    _("『{color=#FF0000}黑{/color}色比基尼 魅惑人心小三角 来吧来裸聊』"),
    _("『{color=#FF0000}不{/color}分攻和受 不用多说交出来 全交给慎酱』"),
    _("『{color=#FF0000}传{/color}统兜裆布 身体心灵都看来 威风加帅气』"),
    _("『{color=#FF0000}大{/color}量下流梗 如同潮水一般来 这是直播哟』"),
    _("『{color=#FF0000}喝{/color}酒到天亮 本来醉酒这件事 仅大人才好』"),
    _("『{color=#FF0000}那{/color}个组织的 威风凛凛美男子 原来是兄弟』"),
]

label block_000020C2:
    # Node: 000020C2 (開始)
    python:
        FailCount = 0
        WinCount = 0
        LoseCount = 0
        if not "GKarutaStage" in globals() or not isinstance(GKarutaStage, list):
            GKarutaStage = [False] * 44

    $ set_place_title(False)

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    image karuta_counter = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#FFFFFFAA",
        size=50)

    if GKarutaViewMode == True:
        jump karuta_viewmode
    else:
        jump karuta_start

    return

label karuta_viewmode:
    # Node: 00002259 (View mode)    
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    play effect "sound/Effect Sound/Paper 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 400
    hide tag_ECFB5B509A334A868686B3435242BF90
    show rs_image_CE6D20694D9B4549B61DEB04A06351CF as tag_063DF7E916A1424E84C7F9FED562D399 at center_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_4AFEA28C2CEB4651BB0258C8206CD0EB

    call screen karuta_view_screen

    jump karuta_view_end

    return

screen karuta_view_screen:
    default view_title = _("可以看拿到的歌牌哦")
    default karuta_showing_id = -1
    vpgrid:
        style "karuta_view_screen_viewport"
        cols 4
        spacing 10
        draggable True
        mousewheel True
        scrollbars None
        for index, card in enumerate(karuta_sentence_list):
            if GKarutaStage[index] == True:
                imagebutton at karuta_view_screen_image(0.2):
                    idle "images/Games/Karuta-game-from-Kobayashi/Card/" + str(index + 1) + ".png"
                    action [
                        Play("effect", "sound/Effect Sound/Paper 1.ogg"),
                        SetScreenVariable("karuta_showing_id", index),
                        SetScreenVariable("view_title", karuta_sentence_list[index])
                    ]
            else:
                add "images/Games/Karuta-game-from-Kobayashi/Cover.png" at karuta_view_screen_image(0.5962)
    add "images/Games/Karuta-game-from-Kobayashi/Avatar/Minami Smile.png"
    use karuta_minami_word(view_title)
    textbutton "×":
        style "karuta_view_exit_button"
        action Return()
    if karuta_showing_id > -1:
        add "images/Games/Karuta-game-from-Kobayashi/Card/" + str(karuta_showing_id + 1) + ".png" xpos 399 ypos 167

screen karuta_minami_word(title):
    text title at karuta_minami_word_transform style "karuta_minami_word"

screen karuta_selector(card_selected_state, time_limitation):
    $ x_pos = 170
    $ y_pos = 151
    for i in range(12):
        if card_selected_state[i] == True:
            imagebutton:
                xpos x_pos
                ypos y_pos
                idle "images/Games/Karuta-game-from-Kobayashi/Placeholder.png"
                hover "images/Games/Karuta-game-from-Kobayashi/Placeholder hover.png"
                action Return(i)
        $ x_pos += 119
        if (i == 3) or (i == 7):
            $ x_pos = 170
            $ y_pos += 149
    timer time_limitation action Return(-1)

transform karuta_minami_word_transform:
    on show:
        alpha 0
        linear 0.15 alpha 1
    on hide:
        linear 0.15 alpha 0
transform karuta_view_screen_image(zoom_level):
    zoom zoom_level
style karuta_view_screen_viewport is vpgrid:
    ypos 126
    ysize 474
    xpos 60
style karuta_minami_word:
    xpos 40
    ypos 19
    font "font/zcool-happy-ayumi-extended.ttf"
    color "#000000"
    size 30
style karuta_view_exit_button:
    xanchor 1.0
    yanchor 1.0
    xpos 790
    ypos 590
style karuta_view_exit_button_text:
    font "font/source-hans-sans-heavy.ttc"
    size 40
    color "#FFFFFF"
    hover_color "#A0A0A0"
    outlines [(absolute(2), "#222222", absolute(0), absolute(0))]

label karuta_view_end:
    play effect "sound/Effect Sound/Impact 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_7ACA96681ED8438984D635078E9C20A5

    python:
        reverse_volume("music", 1)
        del FailCount
        del WinCount
        del LoseCount

    return

label karuta_start:
    pause 1

    play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
    $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_84D7210FBBF34E428243573CCC75C981

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B97613BF336C43ECB48087EFE630E56D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 500
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 500
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 500
    show rs_image_2D66580B8E7D43CD9D46BD73F15B291B as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3F0E353CFDB748D89954EDA3CA501941 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_0013370D932E48D7BA71F9ABB90D97FE as tag_063DF7E916A1424E84C7F9FED562D399 at center_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    pause 0.7

    show screen karuta_minami_word(_("准备开始读牌了。"))
    pause
    hide screen karuta_minami_word
    pause 0.2
    show screen karuta_minami_word(_("根据我的话的第一个字选牌，多者即赢。"))
    pause
    hide screen karuta_minami_word
    pause 0.2
    show screen karuta_minami_word(_("那么，准备……"))

    python:
        karuta_card_list = [0] * 12
        karuta_random_limitation = 44
        if (Chapter == 2) and (C2SG1 == False):
            karuta_random_limitation = 12
        elif ((Chapter == 2) and (C2SG1 == True)) or ((Chapter > 2) and (C3SG1 == False)):
            karuta_random_limitation = 21
        elif  (Chapter > 2) and (C3SG1 == True) and (C3SG2 == False):
            karuta_random_limitation = 32
        for i in range(12):
            karuta_card_already_picked = True
            while karuta_card_already_picked == True:
                karuta_target_card_index = renpy.random.randint(0, karuta_random_limitation - 1)
                karuta_card_already_picked = False
                for j in range(i):
                    if karuta_card_list[j] == karuta_target_card_index:
                        karuta_card_already_picked = True
                        break
            karuta_card_list[i] = karuta_target_card_index
        del karuta_card_already_picked
        del karuta_target_card_index
        del karuta_random_limitation
        CardX = 170
        CardY = 151
        for i in range(12):
            renpy.show(
                "images/Games/Karuta-game-from-Kobayashi/Card/" + str(karuta_card_list[i] + 1) + ".png",
                at_list=[Transform(xpos=CardX, ypos=CardY, zoom=0.3355)],
                what=renpy.easy.displayable("images/Games/Karuta-game-from-Kobayashi/Card/" + str(karuta_card_list[i] + 1) + ".png"),
                tag="Card" + str(i), zorder=100
            )
            CardX = CardX + 119
            if (i == 3) or (i == 7):
                CardX = 170
                CardY = CardY + 149
        del CardX
        del CardY

    if sys_music2_current_file != "sound/BGM/Drum.ogg":
        play music2 "sound/BGM/Drum.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Drum.ogg"

    pause
    hide screen karuta_minami_word
    pause 0.2
    show screen karuta_minami_word(_("开始！"))
    pause
    hide screen karuta_minami_word

    $ karuta_current_index = -1
    $ karuta_card_available = [True] * 12
    while (WinCount + FailCount + LoseCount) < 12:
        python:
            if karuta_current_index > -1: # 放置遮罩层
                CoverX = 0
                CoverY = 0
                if karuta_current_index < 4:
                    CoverY = 151
                elif karuta_current_index < 8:
                    CoverY = 300
                else:
                    CoverY = 449
                if karuta_current_index % 4 == 0:
                    CoverX = 170
                elif karuta_current_index % 4 == 1:
                    CoverX = 289
                elif karuta_current_index % 4 == 2:
                    CoverX = 408
                else:
                    CoverX = 527
                renpy.show(
                    "images/Games/Karuta-game-from-Kobayashi/Cover.png",
                    at_list=[Transform(xpos=CoverX, ypos=CoverY)],
                    what=renpy.easy.displayable("images/Games/Karuta-game-from-Kobayashi/Cover.png"),
                    tag="Cover" + str(karuta_current_index),
                    zorder=200
                )
                del CoverX
                del CoverY
            while True: # 选取下一张卡片
                karuta_current_index = Random(12)
                if karuta_card_available[karuta_current_index] == True:
                    break
        hide screen karuta_minami_word
        show screen karuta_minami_word(karuta_sentence_list[karuta_card_list[karuta_current_index]])
        call screen karuta_selector(karuta_card_available, (Random(3626) + 1375) / float(1000))
        if _return == -1: # 没有选择（超时）
            $ LoseCount += 1
            play effect2 "sound/Effect Sound/Eye shine 1.ogg" noloop
            $ sys_effect2_current_file = "sound/Effect Sound/Eye shine 1.ogg"
            $ zorder_tag_AC2A781923074987B89EFF82C1C606E7 = 500
            show rs_image_A91E74B6874A4367AFACA7A60A9659EC as tag_AC2A781923074987B89EFF82C1C606E7 zorder zorder_tag_AC2A781923074987B89EFF82C1C606E7 onlayer master
            show rs_image_CB9A3B7C3FB14F81B2F472B12826B614 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
            show rs_image_0013370D932E48D7BA71F9ABB90D97FE as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
            show rs_image_3F0E353CFDB748D89954EDA3CA501941 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
            with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7
            hide screen karuta_minami_word
            show screen karuta_minami_word(_("漂亮！"))
            pause
        elif _return == karuta_current_index: # 选择正确
            $ print "Get card " + str(karuta_card_list[karuta_current_index])
            $ GKarutaStage[karuta_card_list[karuta_current_index]] = True
            $ WinCount += 1
            play effect2 "sound/Effect Sound/Eye shine 1.ogg" noloop
            $ sys_effect2_current_file = "sound/Effect Sound/Eye shine 1.ogg"
            $ zorder_tag_AC2A781923074987B89EFF82C1C606E7 = 500
            show rs_image_3C7EEE2FD7C44450926F5BF4222D3790 as tag_AC2A781923074987B89EFF82C1C606E7 zorder zorder_tag_AC2A781923074987B89EFF82C1C606E7 onlayer master
            show rs_image_2D66580B8E7D43CD9D46BD73F15B291B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
            show rs_image_0013370D932E48D7BA71F9ABB90D97FE as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
            show rs_image_27A9CE608540480586E95E611EE27408 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
            with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7
            hide screen karuta_minami_word
            show screen karuta_minami_word(_("哦！"))
            pause
        else: # 选择错误
            $ FailCount += 1
            play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
            $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"
            $ zorder_tag_AC2A781923074987B89EFF82C1C606E7 = 500
            show rs_image_601DB506811341439D5AD034B152D4B1 as tag_AC2A781923074987B89EFF82C1C606E7 zorder zorder_tag_AC2A781923074987B89EFF82C1C606E7 onlayer master
            show rs_image_CB9A3B7C3FB14F81B2F472B12826B614 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
            show rs_image_01044D5E34704EB59BE69F0E074703D2 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
            show rs_image_345982F54C7E4D819B8EFD9BB1463E34 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
            with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7
            hide screen karuta_minami_word
            show screen karuta_minami_word(_("只有三次选错机会哦。"))
            pause
        hide tag_AC2A781923074987B89EFF82C1C606E7
        with rs_effect_F1D853AA1431437BBF572B63AF1E4944
        $ karuta_card_available[karuta_current_index] = False
        # 更新指数
        hide tomo_counter
        hide kobayashi_counter
        show karuta_counter str(WinCount) as tomo_counter at Transform(xpos=24, ypos=235)
        show karuta_counter str(LoseCount) as kobayashi_counter at Transform(xpos=696, ypos=235)
        # 判断试错上限
        if FailCount == 3:
            jump karuta_game_finished

    jump karuta_game_finished

    return

label karuta_game_finished:
    # Node: 000039CE (CLEAR)
    show screen karuta_minami_word(_("到此为止！"))

    hide tomo_counter
    hide kobayashi_counter
    hide Card0
    hide Card1
    hide Card2
    hide Card3
    hide Card4
    hide Card5
    hide Card6
    hide Card7
    hide Card8
    hide Card9
    hide Card10
    hide Card11
    hide Cover0
    hide Cover1
    hide Cover2
    hide Cover3
    hide Cover4
    hide Cover5
    hide Cover6
    hide Cover7
    hide Cover8
    hide Cover9
    hide Cover10
    hide Cover11
    with rs_effect_EF2A46F3AC1640F184034E18DCB12407

    play effect "sound/Effect Sound/Yoo 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Yoo 1.ogg"

    pause 2

    play effect "sound/Effect Sound/Impact 1.ogg" noloop
    $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide screen karuta_minami_word
    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_EF2A46F3AC1640F184034E18DCB12407

    pause 2

    python:
        reverse_volume("music", 1)
        del FailCount
        del WinCount
        del LoseCount
        del karuta_card_available
        del karuta_current_index
        del karuta_card_list

    return
