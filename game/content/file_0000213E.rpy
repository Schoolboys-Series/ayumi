# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 0000213E (Theater)

label theater_prepare:
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show black zorder -100
    with Dissolve(0.5)

    jump block_0000213F

    return

label block_0000213F:
    # Node: 0000213F (開始)
    jump block_00003927

    return

label block_00003927:
    # Node: 00003927 (Background)
    if "SYSTempChapterValue" in globals():
        $ Chapter = SYSTempChapterValue
        $ del SYSTempChapterValue

    $ set_place_title(False)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_C92191ED858E430FAE8AD5B3F68FC7E6
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_747C986A971D4B81833D573429A46067
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    stop music fadeout 2
    $ sys_music_current_file = ""

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 1.5

    play effect "sound/Effect Sound/Clamorous 1.ogg" loop
    $ sys_effect_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_73CFE9C4EA8A49C2AB09B7E6AF362B42 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1

    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 100
    show rs_image_9D34FD7A4503452C9396AB46BFE8DC70 as tag_521EB228B90943B3A2B33F87C47D3A0E at center_bottom zorder zorder_tag_521EB228B90943B3A2B33F87C47D3A0E onlayer master
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ theater_current_chapter = 1
    jump theater_content

    return

label theater_content:
    hide tag_C92191ED858E430FAE8AD5B3F68FC7E6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C92191ED858E430FAE8AD5B3F68FC7E6 = 200
    $ story_list = []

    if theater_current_chapter == 1:
        show rs_image_ED2F27CEEF274CE19761245BE36E9987 as tag_C92191ED858E430FAE8AD5B3F68FC7E6 at center_bottom zorder zorder_tag_C92191ED858E430FAE8AD5B3F68FC7E6 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        $ story_list = [
            { "name": _("大家来相扑"), "description": _("在准太的提案下决定参加\n相扑大会的一班。\n然而、其中却有一些烦恼…"), "available": C1S1 or (Chapter == 0 and persistent.SystemStoryCache[0]) },
            { "name": _("翼的流转音符"), "description": _("小钢琴部的初次任务！\n在练习中、翼担任了\n合唱部分……"), "available": C1S2 or (Chapter == 0 and persistent.SystemStoryCache[1]) },
            { "name": _("寻求刺激·解"), "description": _("在可疑的书店相遇的\n友和三朗。机缘巧合之下、\n友成为了三朗的师父……"), "available": C1S3 or (Chapter == 0 and persistent.SystemStoryCache[2]) },
            { "name": _("不可思议！猫狗物语"), "description": _("一如既往待在校舍\n后方等待主人的小翼。\n某一天、一个谜之生物\n拜访了此处…？"), "available": C1S4 or (Chapter == 0 and persistent.SystemStoryCache[3]) },
            { "name": _("久远回忆"), "description": _("这是发生在不太遥远的过去、\n友和忍的回忆……"), "available": C1S5 or (Chapter == 0 and persistent.SystemStoryCache[4]) }]
    elif theater_current_chapter == 2:
        show rs_image_3AF53F7033944613A137682A2375B9CF as tag_C92191ED858E430FAE8AD5B3F68FC7E6 at center_bottom zorder zorder_tag_C92191ED858E430FAE8AD5B3F68FC7E6 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        $ story_list = [
            { "name": _("并驶之舟"), "description": _("将来决定走上\n不同道路的月和空。\n两人逐渐产生了\n些许变化……"), "available": C2S1 or (Chapter == 0 and persistent.SystemStoryCache[5]) },
            { "name": _("傲娇男孩子的治疗法"), "description": _("为了帮助翼和作哉\n改善关系、\n在友的计划下两人要去\n动物园约会…？"), "available": C2S2 or (Chapter == 0 and persistent.SystemStoryCache[6]) },
            { "name": _("RUN☆RUN☆LOVERS"), "description": _("树被恋人甩了、\n这个情报传入了圭的耳中…"), "available": C2S3 or (Chapter == 0 and persistent.SystemStoryCache[7]) },
            { "name": _("我是直的，现无对象"), "description": _("因为某个理由心情\n烦躁的三朗。\n偶然地、遇到了准备\n进行演讲的志…"), "available": C2S4 or (Chapter == 0 and persistent.SystemStoryCache[8]) },
            { "name": _("狐的报恩"), "description": _("暑假结束后、时不时会丧失\n自我意识的雪绪、\n为了寻找原因前往了\n银纲山…？"), "available": C2S5 or (Chapter == 0 and persistent.SystemStoryCache[9]) },
            { "name": _("欢迎来到食人狼之馆"), "description": _("友和夕阳奇迹般地抽中了\n孤岛旅行、邀请了朋友们\n一起参加、然而、\n等待他们的却是在暴风雨中\n发生的事件……"), "available": C2S6 or (Chapter == 0 and persistent.SystemStoryCache[10]) }]
    elif theater_current_chapter == 3:
        show rs_image_45ACA217F785495E913FDA91D78465B3 as tag_C92191ED858E430FAE8AD5B3F68FC7E6 at center_bottom zorder zorder_tag_C92191ED858E430FAE8AD5B3F68FC7E6 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
        $ story_list = [
            { "name": _("异我战纪"), "description": _("忍被社团的后辈武一请求\n保护深受跟踪狂困扰的朋友。\n以此为契机、忍对武力的\n使用方法产生了迷茫……"), "available": C3S1 or (Chapter == 0 and persistent.SystemStoryCache[11]) },
            { "name": _("正义的教训"), "description": _("烦恼着要出什么\n节目的友等人、为了寻找点子\n在街上散步时、谜之英雄出现\n在了他们面前…？"), "available": C3S2 or (Chapter == 0 and persistent.SystemStoryCache[12]) },
            { "name": _("集合！御咲花车祭"), "description": _("参加者逐年减少的花车祭、\n月、空、慎太郎为了\n增加人数、\n费了一番苦功……"), "available": C3S3 or (Chapter == 0 and persistent.SystemStoryCache[13]) },
            { "name": _("傲娇男孩子的激效疗"), "description": _("为了从背后推一把纠结着该\n如何把礼物送给翼的作哉、\n三朗制定了某个计划……"), "available": C3S4 or (Chapter == 0 and persistent.SystemStoryCache[14]) },
            { "name": _("学园怪谈"), "description": _("被鬼怪们困在异空间的\n御咲学生们、为了回到\n原来的世界、\n跟四朗及雪绪一起\n挑战鬼怪……"), "available": C3S5 or (Chapter == 0 and persistent.SystemStoryCache[15]) },
            { "name": _("变革进行曲"), "description": _("被光邀请、成为了吹奏乐部\n外援的友、在为高强度的\n练习苦恼的同时、\n在同伴们的鼓励下\n每日努力奋斗着……"), "available": C3S6 or (Chapter == 0 and persistent.SystemStoryCache[16]) }]
    
    call screen theater_content_screen(theater_current_chapter, story_list)

    hide screen theater_content_preview

    if _return == "CP1":
        $ theater_current_chapter = 1
        jump theater_content
    elif _return == "CP2":
        $ theater_current_chapter = 2
        jump theater_content
    elif _return == "CP3":
        $ theater_current_chapter = 3
        jump theater_content

    if "Chapter" in globals():
        $ SYSTempChapterValue = Chapter
    $ Chapter = theater_current_chapter

    if theater_current_chapter == 1:
        if _return == 0:
            jump block_00002B5F
        elif _return == 1:
            jump block_00002B64
        elif _return == 2:
            jump block_00002B65
        elif _return == 3:
            jump block_00002B66
        elif _return == 4:
            jump block_00002B67
    elif theater_current_chapter == 2:
        if _return == 0:
            jump block_00002F86
        elif _return == 1:
            jump block_00003BE7
        elif _return == 2:
            jump block_00003BE9
        elif _return == 3:
            jump block_00003BEB
        elif _return == 4:
            jump block_00003BED
        elif _return == 5:
            jump block_00003BEF
    elif theater_current_chapter == 3:
        if _return == 0:
            jump block_00004261
        elif _return == 1:
            jump block_00004262
        elif _return == 2:
            jump block_00004263
        elif _return == 3:
            jump block_00004264
        elif _return == 4:
            jump block_00004260
        elif _return == 5:
            jump block_00004265
    if _return == "":
        jump block_00002B68

    return

screen theater_content_screen(chapter, story_list):
    frame at lm_menu_show_hide(0.2, 0.2):
        style "theater_content_frame"
        if chapter == 1:
            text _("第一放映厅") style "theater_content_title_1"
        elif chapter == 2:
            text _("第二放映厅") style "theater_content_title_2"
        elif chapter == 3:
            text _("第三放映厅") style "theater_content_title_3"
        text _("该厅计划上映的电影") style "theater_content_description_" + str(chapter)
        $ y_position = 132
        for i, story in enumerate(story_list):
            frame:
                style "theater_content_frame"
                if story["available"]:
                    imagebutton:
                        xpos 544
                        ypos y_position
                        idle "images/Theater/Button/" + str(chapter) + ".png"
                        hover "images/Theater/Button/" + str(chapter) + " hover.png"
                        hovered Play("effect2", "sound/Effect Sound/System - choose.ogg")
                        action [Hide("theater_content_preview"), Show("theater_content_preview", chapter=chapter, index=i, title=story["name"], description=story["description"])]
                    text story["name"]:
                        style "theater_content_itemtext_" + str(chapter)
                        ypos y_position + 2
                else:
                    add "images/Theater/Button/Disabled.png" pos (544, y_position)
                    text _("片源未到"):
                        style "theater_content_itemtext_disabled"
                        xpos 669
                        ypos y_position + 4
            $ y_position += 55
        $ del y_position
        textbutton _("返回"):
            text_style "theater_content_backbutton"
            xpos 708
            ypos 20
            hovered Play("effect2", "sound/Effect Sound/System - choose.ogg")
            action [Play("effect2", "sound/Effect Sound/System - click.ogg"), Pause(0.2), Return("")]
        if chapter == 1:
            imagebutton: 
                xpos 0
                ypos 41
                idle "images/Theater/Button/Room.png"
                hover "images/Theater/Button/Room 2 hover.png"
                hovered Play("effect2", "sound/Effect Sound/System - choose.ogg")
                action [Play("effect2", "sound/Effect Sound/System - click.ogg"), Pause(0.2), Return("CP2")]
            text _("去第二放映厅") style "theater_content_changeplace_2":
                ypos 45
        else:
            imagebutton: 
                xpos 0
                ypos 41
                idle "images/Theater/Button/Room.png"
                hover "images/Theater/Button/Room 1 hover.png"
                hovered Play("effect2", "sound/Effect Sound/System - choose.ogg")
                action [Play("effect2", "sound/Effect Sound/System - click.ogg"), Pause(0.2), Return("CP1")]
            text _("去第一放映厅") style "theater_content_changeplace_1":
                ypos 45
        if chapter == 3:
            imagebutton: 
                xpos 0
                ypos 95
                idle "images/Theater/Button/Room.png"
                hover "images/Theater/Button/Room 2 hover.png"
                hovered Play("effect2", "sound/Effect Sound/System - choose.ogg")
                action [Play("effect2", "sound/Effect Sound/System - click.ogg"), Pause(0.2), Return("CP2")]
            text _("去第二放映厅") style "theater_content_changeplace_2":
                ypos 100
        else:
            imagebutton: 
                xpos 0
                ypos 95
                idle "images/Theater/Button/Room.png"
                hover "images/Theater/Button/Room 3 hover.png"
                hovered Play("effect2", "sound/Effect Sound/System - choose.ogg")
                action [Play("effect2", "sound/Effect Sound/System - click.ogg"), Pause(0.2), Return("CP3")]
            text _("去第三放映厅") style "theater_content_changeplace_3":
                ypos 100

style theater_content_frame is default
style theater_content_backbutton:
    size 28
    color "#FFFFFF"
    font "font/zcool-happy-ayumi-extended.ttf"
    outlines [(absolute(5), "#000000", absolute(0), absolute(0))]
    hover_color "#000000"
    hover_outlines [(absolute(5), "#FFFFFF", absolute(0), absolute(0))]
style theater_content_itemtext:
    xpos 669
    xalign 0.5
    size 24
    text_align 0.5
    font "font/source-hans-sans-medium.ttc"
style theater_content_itemtext_disabled is theater_content_itemtext:
    color "#00000055"
style theater_content_itemtext_1 is theater_content_itemtext:
    color "#669933"
    outlines [(absolute(4), "#BEF1BE", absolute(0), absolute(0))]
style theater_content_itemtext_2 is theater_content_itemtext:
    color "#337899"
    outlines [(absolute(4), "#B7CCF6", absolute(0), absolute(0))]
style theater_content_itemtext_3 is theater_content_itemtext:
    color "#993370"
    outlines [(absolute(4), "#F0B9C8", absolute(0), absolute(0))]
style theater_content_title:
    xpos 25
    ypos 220
    size 48
style theater_content_title_1 is theater_content_title:
    color "#CBFFC2"
    outlines [(absolute(6), "#99CC66", absolute(0), absolute(0))]
style theater_content_title_2 is theater_content_title:
    color "#C2D9FF"
    outlines [(absolute(6), "#337899", absolute(0), absolute(0))]
style theater_content_title_3 is theater_content_title:
    color "#FFC2CA"
    outlines [(absolute(6), "#993370", absolute(0), absolute(0))]
style theater_content_description:
    xpos 587
    ypos 86
    size 18
style theater_content_description_1 is theater_content_description:
    color "#669933"
style theater_content_description_2 is theater_content_description:
    color "#337899"
style theater_content_description_3 is theater_content_description:
    color "#993370"
style theater_content_changeplace:
    xpos 45
    size 18
style theater_content_changeplace_1 is theater_content_changeplace:
    color "#669933"
style theater_content_changeplace_2 is theater_content_changeplace:
    color "#337899"
style theater_content_changeplace_3 is theater_content_changeplace:
    color "#993370"
style theater_content_playbutton:
    size 42
    color "#FFFFFF"
    font "font/zcool-happy-ayumi-extended.ttf"
    outlines [(absolute(5), "#00000088", absolute(0), absolute(0))]
    hover_color "#00000088"
    hover_outlines [(absolute(5), "#FFFFFF88", absolute(0), absolute(0))]
style theater_content_preview_title:
    size 20
    xpos 411
    ypos 313
    vertical True
    color "#FFFFFF"
style theater_content_preview_content:
    xalign 1.0
    xpos 435
    ypos 328
    size 16
    vertical True
    color "#FFFFFF"

screen theater_content_preview(chapter, index, title, description):
    add "images/Theater/Theater play button.png" pos (0, 10)
    add "images/Theater/Preview/CP" + str(chapter)  + str(index + 1) + ".png" pos (0, 0)
    text description:
        style "theater_content_preview_content"
    textbutton _("播放"):
        text_style "theater_content_playbutton"
        xpos 620
        ypos 493
        action [Play("effect2", "sound/Effect Sound/System - click.ogg"), Return(index)]

label block_0000370F:
    # Node: 0000370F (FLAG: 大家來相撲)
    call block_00003704 from _call_block_00003704_1

    jump block_00003927

    return

label block_00003726:
    # Node: 00003726 (FLAG: 翼的流轉音符)
    call block_00003715 from _call_block_00003715_1

    jump block_00003927

    return

label block_00003918:
    # Node: 00003918 (FLAG: 尋求刺激-解)
    call block_00003900 from _call_block_00003900_1

    jump block_00003927

    return

label block_00002B55:
    # Node: 00002B55 (FLAG: 不可思議！猫狗物語)
    call block_000036FB from _call_block_000036FB_1

    jump block_00003927

    return

label block_00003919:
    # Node: 00003919 (FLAG: 久遠回憶)
    call block_0000390E from _call_block_0000390E_1

    jump block_00003927

    return

label block_00002B5F:
    # Node: 00002B5F (T1: 1)
    $ SYSTheaterState = 11

    jump block_00003A89

    return

label block_00002B64:
    # Node: 00002B64 (T1: 2)
    $ SYSTheaterState = 12

    jump block_00003A89

    return

label block_00002B65:
    # Node: 00002B65 (T1: 3)
    $ SYSTheaterState = 13

    jump block_00003A89

    return

label block_00002B66:
    # Node: 00002B66 (T1: 4)
    $ SYSTheaterState = 14

    jump block_00003A89

    return

label block_00002B67:
    # Node: 00002B67 (T1: 5)
    $ SYSTheaterState = 15

    jump block_00003A89

    return

label block_00002B68:
    # Node: 00002B68 (RESET)
    $ SYSTheaterState = 0

    jump block_00002B74

    return

label block_00002B74:
    # Node: 00002B74 (CLEAR)
    stop effect fadeout 1
    $ sys_effect_current_file = ""

    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C92191ED858E430FAE8AD5B3F68FC7E6
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    pause 0.5

    return

label block_00002FBB:
    # Node: 00002FBB (FLAG: 并駛之舟)
    call block_00003A46 from _call_block_00003A46

    jump block_00003927

    return

label block_00003BE8:
    # Node: 00003BE8 (FLAG: 傲嬌男孩子的治療法)
    call block_00003A0E from _call_block_00003A0E_8

    jump block_00003927

    return

label block_00003BEA:
    # Node: 00003BEA (FLAG: LO-LO-LOVERS)
    call block_00003B11 from _call_block_00003B11

    jump block_00003927

    return

label block_00003BEC:
    # Node: 00003BEC (FLAG: 我是直的，現無對象)
    call block_00003AA3 from _call_block_00003AA3_1

    jump block_00003927

    return

label block_00003BEE:
    # Node: 00003BEE (FLAG: 狐的報恩)
    call block_00003B90 from _call_block_00003B90_1

    jump block_00003927

    return

label block_00003BF0:
    # Node: 00003BF0 (FLAG: 歡迎來到食人狼之館)
    call block_00003BAD from _call_block_00003BAD_1

    jump block_00003927

    return

label block_00002F86:
    # Node: 00002F86 (T2: 1)
    $ SYSTheaterState = 21

    jump block_00003A89

    return

label block_00003BE7:
    # Node: 00003BE7 (T2: 2)
    $ SYSTheaterState = 22

    jump block_00003A89

    return

label block_00003BE9:
    # Node: 00003BE9 (T2: 3)
    $ SYSTheaterState = 23

    jump block_00003A89

    return

label block_00003BEB:
    # Node: 00003BEB (T2: 4)
    $ SYSTheaterState = 24

    jump block_00003A89

    return

label block_00003BED:
    # Node: 00003BED (T2: 5)
    $ SYSTheaterState = 25

    jump block_00003A89

    return

label block_00003BEF:
    # Node: 00003BEF (T2: 6)
    $ SYSTheaterState = 26

    jump block_00003A89

    return

label block_00004267:
    # Node: 00004267 (FLAG: 異我戰紀)
    call block_00003FD7 from _call_block_00003FD7_1

    jump block_00003927

    return

label block_00004268:
    # Node: 00004268 (FLAG: 正義的教訓)
    call block_0000400C from _call_block_0000400C_1

    jump block_00003927

    return

label block_00004269:
    # Node: 00004269 (FLAG: 集合！御咲花車祭)
    call block_00003D92 from _call_block_00003D92_1

    jump block_00003927

    return

label block_0000426A:
    # Node: 0000426A (FLAG: 傲嬌男孩子的激效療)
    call block_00004030 from _call_block_00004030_1

    jump block_00003927

    return

label block_0000426B:
    # Node: 0000426B (FLAG: 學園怪談)
    call block_00003EA1 from _call_block_00003EA1_1

    jump block_00003927

    return

label block_0000426C:
    # Node: 0000426C (FLAG: 變革進行曲)
    call block_00003F8D from _call_block_00003F8D_1

    jump block_00003927

    return

label block_00004261:
    # Node: 00004261 (T3: 1)
    $ SYSTheaterState = 31

    jump block_00003A89

    return

label block_00004262:
    # Node: 00004262 (T3: 2)
    $ SYSTheaterState = 32

    jump block_00003A89

    return

label block_00004263:
    # Node: 00004263 (T3: 3)
    $ SYSTheaterState = 33

    jump block_00003A89

    return

label block_00004264:
    # Node: 00004264 (T3: 4)
    $ SYSTheaterState = 34

    jump block_00003A89

    return

label block_00004260:
    # Node: 00004260 (T3: 5)
    $ SYSTheaterState = 35

    jump block_00003A89

    return

label block_00004265:
    # Node: 00004265 (T3: 6)
    $ SYSTheaterState = 36

    jump block_00003A89

    return

label block_00003A89:
    # Node: 00003A89 (PREPARE)
    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    play effect2 "sound/Effect Sound/Showing alarm 1.ogg" noloop
    $ sys_effect2_current_file = "sound/Effect Sound/Showing alarm 1.ogg"

    hide tag_C92191ED858E430FAE8AD5B3F68FC7E6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_5E96F41F94D54EF78747DC340EFC5CA5

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 11" }]):
        jump block_0000370F
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 12" }]):
        jump block_00003726
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 13" }]):
        jump block_00003918
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 14" }]):
        jump block_00002B55
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 15" }]):
        jump block_00003919
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 21" }]):
        jump block_00002FBB
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 22" }]):
        jump block_00003BE8
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 23" }]):
        jump block_00003BEA
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 24" }]):
        jump block_00003BEC
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 25" }]):
        jump block_00003BEE
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 26" }]):
        jump block_00003BF0
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 31" }]):
        jump block_00004267
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 32" }]):
        jump block_00004268
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 33" }]):
        jump block_00004269
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 34" }]):
        jump block_0000426A
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 35" }]):
        jump block_0000426B
    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState == 36" }]):
        jump block_0000426C

    return
