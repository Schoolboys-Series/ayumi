init:
    image scb_flag_title_chapter = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#000000",
        xalign=0.5,
        size=24,
        text_align=0.5)

    image scb_flag_title_chapter_reverse = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#00CAFE",
        xalign=0.5,
        size=24,
        text_align=0.5)
    
    image scb_flag_title_chapter_end = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#FFFFFF",
        xalign=0.5,
        size=24,
        text_align=0.5)

    image scb_flag_title_chapter_local = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#000000",
        xalign=0.5,
        size=14,
        text_align=0.5)

    image scb_flag_title_chapter_local_reverse = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#00CAFE",
        xalign=0.5,
        size=14,
        text_align=0.5)

    image scb_flag_title_chapter_local_end = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#FFFFFF",
        xalign=0.5,
        size=14,
        text_align=0.5)

    image scb_flag_title_name = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#000000",
        xalign=0.5,
        size=55,
        text_align=0.5)

    image scb_flag_title_name_reverse = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#00CAFE",
        xalign=0.5,
        size=55,
        text_align=0.5)

    image scb_flag_title_name_end = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#FFFFFF",
        xalign=0.5,
        size=55)

label scb_flag_title(chapter, title, with_image=None):
    window hide
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 1.5

    play effect "sound/BGM/Flag title.ogg" noloop
    $ sys_effect_current_file = "sound/BGM/Flag title.ogg"

    $ zorder_tag_99488938252D4BC2B7FA91D436D9159B = 0
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_99488938252D4BC2B7FA91D436D9159B at center_bottom zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.4

    show rs_image_F9053C42DFA4452792C00A32912CF739 as tag_99488938252D4BC2B7FA91D436D9159B zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.4

    if chapter == 1:
        $ _scb_flag_title_chapter = "CHAPTER 1 STORY"
        $ _scb_flag_title_chapter_local = _("第一章 事件")
    elif chapter == 2:
        $ _scb_flag_title_chapter = "CHAPTER 2 STORY"
        $ _scb_flag_title_chapter_local = _("第二章 事件")
    elif chapter == 3:
        $ _scb_flag_title_chapter = "CHAPTER 3 STORY"
        $ _scb_flag_title_chapter_local = _("第三章 事件")

    show rs_image_FA4776FF366F4940A99A1C7D6FBB5C6B as tag_99488938252D4BC2B7FA91D436D9159B zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
    show scb_flag_title_chapter (_scb_flag_title_chapter) as scb_flag_title_chapter at Transform(ypos=295) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
    show scb_flag_title_chapter_local (_scb_flag_title_chapter_local) as scb_flag_title_chapter_local at Transform(ypos=325) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    if with_image == None:
        show scb_flag_title_name title as scb_flag_title_name at Transform(ypos=368) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9
    else:
        show scb_flag_title_name title as scb_flag_title_name at Transform(ypos=358) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        show expression with_image as scb_flag_title_with_image at Transform(xpos=0, ypos=0) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 2.5

    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide scb_flag_title_chapter
    hide scb_flag_title_chapter_local
    hide scb_flag_title_name
    hide scb_flag_title_with_image
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    $ del _scb_flag_title_chapter
    $ del _scb_flag_title_chapter_local

    pause 1

    return

label scb_flag_title_end(chapter, title, with_image=None, reverse_color=False):
    window hide
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 2

    if chapter == 1:
        $ _scb_flag_title_chapter = "CHAPTER 1 STORY"
        $ _scb_flag_title_chapter_local = _("第一章 事件")
    elif chapter == 2:
        $ _scb_flag_title_chapter = "CHAPTER 2 STORY"
        $ _scb_flag_title_chapter_local = _("第二章 事件")
    elif chapter == 3:
        $ _scb_flag_title_chapter = "CHAPTER 3 STORY"
        $ _scb_flag_title_chapter_local = _("第三章 事件")

    $ zorder_tag_99488938252D4BC2B7FA91D436D9159B = 0
    if reverse_color:
        show rs_image_9B8FADF0333549F38FB57286D05A2A7E as tag_99488938252D4BC2B7FA91D436D9159B zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        show scb_flag_title_chapter_reverse (_scb_flag_title_chapter) as scb_flag_title_chapter at Transform(ypos=295) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        show scb_flag_title_chapter_local_reverse (_scb_flag_title_chapter_local) as scb_flag_title_chapter_local at Transform(ypos=315) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        show scb_flag_title_name_reverse title as scb_flag_title_name at Transform(ypos=368) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        with rs_effect_995A246CCA8349168AE1D97DE29F1026
    else:
        show rs_image_83608BA0CD514EEE953999E84CE9BFA5 as tag_99488938252D4BC2B7FA91D436D9159B zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        show scb_flag_title_chapter_end (_scb_flag_title_chapter) as scb_flag_title_chapter at Transform(ypos=295) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        show scb_flag_title_chapter_local_end (_scb_flag_title_chapter_local) as scb_flag_title_chapter_local at Transform(ypos=315) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        show scb_flag_title_name_end title as scb_flag_title_name at Transform(ypos=368) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        with rs_effect_995A246CCA8349168AE1D97DE29F1026

    if with_image != None:
        show expression with_image as scb_flag_title_with_image at Transform(xpos=0, ypos=0) zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
        with rs_effect_04F714FDB0E541E4813BA7A0A833CD54
    
    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 100
    if reverse_color:
        show rs_image_98B8B62B35A94921925C747DDFC15186 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
        with rs_effect_995A246CCA8349168AE1D97DE29F1026
    else:
        show rs_image_78397398AE2744EF806FB352AC2BD4C7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
        with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 2.5

    pause

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide scb_flag_title_chapter
    hide scb_flag_title_chapter_local
    hide scb_flag_title_name
    hide scb_flag_title_with_image
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    return
