# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000027FC (慎太郎筆記)

style shintaro_notebook_page_title:
    color "#FFFFFF"
    font "font/zcool-happy-ayumi-extended.ttf"
    size 24
    hover_color "#D7FF9C"

style shintaro_notebook_page_number:
    color "#FFFFFF"
    font "font/zcool-happy-ayumi-extended.ttf"
    size 22
    hover_color "#AEEDCC"

label block_000027FD:
    # Node: 000027FD ()

    image shintaro_notebook_table_of_content = ParameterizedText(font="font/zcool-happy-ayumi-extended.ttf", color="#AEEDCC", size=22)
    image shintaro_notebook_content_addon = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#FF0000",
        size=18,
        outlines=[(absolute(1), "#FFFFFFFF", absolute(0), absolute(0)),
                  (absolute(2), "#FFFFFFCC", absolute(0), absolute(0)),
                  (absolute(3), "#FFFFFF88", absolute(0), absolute(0)),
                  (absolute(4), "#FFFFFF44", absolute(0), absolute(0)),
                  (absolute(5), "#FFFFFF00", absolute(0), absolute(0))])

    jump block_000027FE

    return

label shintaro_notebook_show_content(name, age, height, weight, birthdate, blood_group, club, pants, content):
    image shintaro_notebook_content_title_text = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#000000",
        size=60,
        outlines=[(absolute(1), "#FFFFFFFF", absolute(0), absolute(0)),
                  (absolute(2), "#FFFFFFCC", absolute(0), absolute(0)),
                  (absolute(3), "#FFFFFF88", absolute(0), absolute(0)),
                  (absolute(4), "#FFFFFF44", absolute(0), absolute(0)),
                  (absolute(5), "#FFFFFF00", absolute(0), absolute(0))])
    image shintaro_notebook_content_param_text = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#000000",
        size=20,
        line_spacing=11,
        outlines=[(absolute(1), "#FFFFFFFF", absolute(0), absolute(0)),
                  (absolute(2), "#FFFFFFCC", absolute(0), absolute(0)),
                  (absolute(3), "#FFFFFF88", absolute(0), absolute(0)),
                  (absolute(4), "#FFFFFF44", absolute(0), absolute(0)),
                  (absolute(5), "#FFFFFF00", absolute(0), absolute(0))])
    show shintaro_notebook_content_title_text name at Transform(xpos=318, ypos=23) as shintaro_notebook_content_title_text zorder 400 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ shintaro_notebook_content_param = ""
    if age != "":
        $ shintaro_notebook_content_param += _("年龄：") + age + "\n"
    if height != "":
        $ shintaro_notebook_content_param += _("身高：") + height + "\n"
    if weight != "":
        $ shintaro_notebook_content_param += _("体重：") + weight + "\n"
    if birthdate != "":
        $ shintaro_notebook_content_param += _("生日：") + birthdate + "\n"
    if blood_group != "":
        $ shintaro_notebook_content_param += _("血型：") + blood_group + "\n"
    if club != "":
        $ shintaro_notebook_content_param += _("所属：") + club + "\n"
    if pants != "":
        $ shintaro_notebook_content_param += _("内裤类型：") + pants + "\n"
    
    show shintaro_notebook_content_param_text shintaro_notebook_content_param at Transform(xpos=295, ypos=88) as shintaro_notebook_content_param_text zorder 400 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ del shintaro_notebook_content_param

    show shintaro_notebook_content_param_text content at Transform(xpos=291, ypos=332) as shintaro_notebook_content_param_content zorder 400 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    return

label shintaro_notebook_hide_content:
    hide shintaro_notebook_content_title_text
    hide shintaro_notebook_content_param_text
    hide shintaro_notebook_content_param_content
    hide addon_1
    hide addon_2
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    return

label block_000027FE:
    # Node: 000027FE (Background)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F199D2DF418A4FA4AF82A246453DCC8B = 100
    $ zorder_tag_502E9DA3D50E46328C6B318275CD4DF5 = 200
    show rs_image_344B92C84B9646A6B7D0A379C3B1CEE7 as tag_F199D2DF418A4FA4AF82A246453DCC8B at center_bottom zorder zorder_tag_F199D2DF418A4FA4AF82A246453DCC8B onlayer master
    show rs_image_CCD3961B940D419E84E7EB1A37DCA73B as tag_502E9DA3D50E46328C6B318275CD4DF5 at left_top zorder zorder_tag_502E9DA3D50E46328C6B318275CD4DF5 onlayer master
    show shintaro_notebook_table_of_content (_("目录")) as shintaro_notebook_table_of_content at Transform(xpos=23, ypos=16) zorder 200 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    jump block_00003695

    return

label block_0000372C:
    # Node: 0000372C (CLEAR)
    hide shintaro_notebook_table_of_content
    hide tag_F199D2DF418A4FA4AF82A246453DCC8B
    hide tag_502E9DA3D50E46328C6B318275CD4DF5
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    jump block_0000372D

    return

label block_0000372D:
    # Node: 0000372F (終了)

    return

label block_00003695:
    # Node: 00003695 (Page 1)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_CCD3961B940D419E84E7EB1A37DCA73B as tag_502E9DA3D50E46328C6B318275CD4DF5 zorder zorder_tag_502E9DA3D50E46328C6B318275CD4DF5 onlayer master

    jump block_00003694

    return

label block_000036B0:
    # Node: 000036B0 (Page 2)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_FD41AF7498D24B27A444510FE6BAE032 as tag_502E9DA3D50E46328C6B318275CD4DF5 zorder zorder_tag_502E9DA3D50E46328C6B318275CD4DF5 onlayer master

    jump block_000036AB

    return

label block_000036C5:
    # Node: 000036C5 (Page 3)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_C269A47C07FC4BD295010B0BBE26AD8F as tag_502E9DA3D50E46328C6B318275CD4DF5 zorder zorder_tag_502E9DA3D50E46328C6B318275CD4DF5 onlayer master

    jump block_000036C4

    return

label block_000036DD:
    # Node: 000036DD (Page 4)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_73D6833D732E40178141B753B48A7432 as tag_502E9DA3D50E46328C6B318275CD4DF5 zorder zorder_tag_502E9DA3D50E46328C6B318275CD4DF5 onlayer master

    jump block_000036DF

    return

label block_00003694:
    # Node: 00003694 (Page 1)
    $ sys_lm_menu_item = [
        {"pos": (20, 65),"type":"textbutton","text":_("森海友"),"style":"shintaro_notebook_page_title","name": "友","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Tomo.png")},
        {"pos": (20, 101),"type":"textbutton","text":_("绫濑忍"),"style":"shintaro_notebook_page_title","name": "しのぶ","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Shinobu.png")},
        {"pos": (20, 137),"type":"textbutton","text":_("一之濑翼"),"style":"shintaro_notebook_page_title","name": "つばさ","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Tsubasa.png")},
        {"pos": (20, 174),"type":"textbutton","text":_("奥村慎太郎"),"style":"shintaro_notebook_page_title","name": "慎太郎","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Shintaro.png")},
        {"pos": (20, 212),"type":"textbutton","text":_("赤峰月"),"style":"shintaro_notebook_page_title","name": "月","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Tsuki.png")},
        {"pos": (20, 248),"type":"textbutton","text":_("赤峰空"),"style":"shintaro_notebook_page_title","name": "空","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Sora.png")},
        {"pos": (20, 284),"type":"textbutton","text":_("穗海作哉"),"style":"shintaro_notebook_page_title","name": "作哉","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Sakuya.png")},
        {"pos": (20, 321),"type":"textbutton","text":_("猫山三朗"),"style":"shintaro_notebook_page_title","name": "三朗","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Saburo.png")},
        {"pos": (20, 359),"type":"textbutton","text":_("猫山四朗"),"style":"shintaro_notebook_page_title","name": "四朗","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Shiro.png"),"condition":[{"scope":0,"content":"C1S4 == True"},{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 395),"type":"textbutton","text":_("榊雪绪"),"style":"shintaro_notebook_page_title","name": "雪緒","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Yukio.png"),"condition":[{"scope":0,"content":"C1S4 == True"},{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 429),"type":"textbutton","text":_("小翼"),"style":"shintaro_notebook_page_title","name": "ツバサ","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Tsubasa-chan.png"),"condition":[{"scope":0,"content":"C1S4 == True"},{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 465),"type":"textbutton","text":_("小翼（人类版）"),"style":"shintaro_notebook_page_title","name": "ツバサ人","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Tsubasa-chan(Human).png"),"condition":[{"scope":0,"content":"C1S4 == True"}]},
        {"pos": (96, 10),"type":"textbutton","text":"2","style":"shintaro_notebook_page_number","name": "目次２"},
        {"pos": (125, 11),"type":"textbutton","text":"3","style":"shintaro_notebook_page_number","name": "目次３"},
        {"pos": (154, 10),"type":"textbutton","text":"4","style":"shintaro_notebook_page_number","name": "目次４"},
        {"pos": (182, 12),"type":"textbutton","text":"×","style":"shintaro_notebook_page_number","name": "とじる"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.25, 0.25) from _call_lm_menu_368
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友\"" }]):
        jump block_00003696
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00003698
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" },{ "scope": 1, "content": "C2S2 == True" }]):
        jump block_0000369A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_00003699
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" },{ "scope": 1, "content": "C2S4 == True" }]):
        jump block_0000369C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_0000369B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" },{ "scope": 1, "content": "C1S1 == True" }]):
        jump block_0000396D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_0000369F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" },{ "scope": 1, "content": "C1S1 == True" }]):
        jump block_0000396E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_000036A0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" },{ "scope": 1, "content": "C2S2 == True" }]):
        jump block_000036A2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_000036A1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" },{ "scope": 1, "content": "C2S4 == True" }]):
        jump block_000036A5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_000036A4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"四朗\"" }]):
        jump block_000036A6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"雪緒\"" }]):
        jump block_000036A7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ツバサ\"" }]):
        jump block_000036A8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ツバサ人\"" }]):
        jump block_000036A9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次２\"" }]):
        jump block_000036B0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次３\"" }]):
        jump block_000036C5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次４\"" }]):
        jump block_000036DD
    if judge_lm_condition([]):
        jump block_0000372C

    return

label block_0000369D:
    # Node: 0000369D (RESET)
    pause

    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_hide_content from _call_shintaro_notebook_hide_content

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_FB83778318AB4B3A83211AAA57E755D6
    with rs_effect_FC474B930CE449DD8BE5D4980A132631

    jump block_00003695

    return

label block_00003696:
    # Node: 00003696 (友)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_E01AF7C84C654915A26714D9B09781EB as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("森海友"),
        _("中学二年级"),
        _("155cm"),
        _("48kg"),
        _("7月21日"),
        _("O"),
        _("小钢琴部兼一班班长"),
        _("比基尼"),
        _("元气满满的小笨蛋。\n和忍是青梅竹马，住在同一所\n公寓的上面一层。对性的好奇心\n非常旺盛，随时持有“电摩”。\n因为母亲是钢琴家，以前也练习过，\n钢琴很不错。自己做饭，拿手料理\n“蛋包饭”。对呆毛很在意。")) from _call_shintaro_notebook_show_content

    jump block_0000369D

    return

label block_00003698:
    # Node: 00003698 (忍)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_A8F7430A864944B5BF20ACB7F06D0379 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
    call shintaro_notebook_show_content(
        _("绫濑忍"),
        _("中学二年级"),
        _("149cm"),
        _("40kg"),
        _("2月14日"),
        _("A"),
        _("空手道部"),
        _("短裤"),
        _("矮小无口的少年。\n一般来看很酷，但只要和青梅竹马\n的友说起话来就很孩子气。\n因为长相中性常被认错性别，\n对此有些烦恼。空手道黑带。\n生气时常用铁拳制裁。")) from _call_shintaro_notebook_show_content_1

    jump block_0000369D

    return

label block_0000369A:
    # Node: 0000369A (翼 CP2F2后)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_FE021B92D66E41CABC0A6F417EC1278D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("一之濑翼"),
        _("中学二年级"),
        _("155cm"),
        _("45kg"),
        _("1月11日"),
        _("O"),
        _("小钢琴部兼二班班长"),
        _("三角裤"),
        _("总是战战兢兢的弱气的男孩子。\n因为学号是1就被副班主任弄成了\n班长。年级开会时遇到了友，不知所措\n时被友的温柔感动，喜欢上了友。\n现在也仍然如此。之后和友组建了\n小钢琴部。偶尔会有些病娇。")) from _call_shintaro_notebook_show_content_2

    show shintaro_notebook_content_addon (_("追记：终于和作哉重归于好，现在两人一起照顾\n小翼，也开始学习饲育知识了。")) at Transform(xpos=284, ypos=550) as addon_1 zorder 500 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    jump block_0000369D

    return

label block_00003699:
    # Node: 00003699 (翼)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_FE021B92D66E41CABC0A6F417EC1278D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("一之濑翼"),
        _("中学二年级"),
        _("155cm"),
        _("45kg"),
        _("1月11日"),
        _("O"),
        _("小钢琴部兼二班班长"),
        _("三角裤"),
        _("总是战战兢兢的弱气的男孩子。\n因为学号是1就被副班主任弄成了\n班长。年级开会时遇到了友，不知所措\n时被友的温柔感动，喜欢上了友。\n现在也仍然如此。之后和友组建了\n小钢琴部。偶尔会有些病娇。")) from _call_shintaro_notebook_show_content_3

    jump block_0000369D

    return

label block_0000369C:
    # Node: 0000369C (慎太郎 CP2F4后)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_6712284313094E5581A5D8DB867CCB9A as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("奥村慎太郎"),
        _("中学二年级"),
        _("159cm"),
        _("50kg"),
        _("8月1日"),
        _("AB"),
        _("花乃汤前台"),
        _("四角裤"),
        _("性知识丰富的工口工口星人。\n自家的澡堂“花乃汤”其实在\n{color=#FF0000}{s}“那个”圈子里很有名{/s}{/color}。有次\n三朗误闯结果就变成了待宰羔羊。\n会接受恋爱咨询，给各种人建议，\n在御咲学园不断促成一对对情侣。")) from _call_shintaro_notebook_show_content_4

    show shintaro_notebook_content_addon (_("以后不会再有这种事情了")) at Transform(xpos=460,ypos=315,rotate=-5) as addon_1 zorder 500 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    jump block_0000369D

    return

label block_0000369B:
    # Node: 0000369B (慎太郎)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_6712284313094E5581A5D8DB867CCB9A as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("奥村慎太郎"),
        _("中学二年级"),
        _("159cm"),
        _("50kg"),
        _("8月1日"),
        _("AB"),
        _("花乃汤前台"),
        _("四角裤"),
        _("性知识丰富的工口工口星人。\n自家的澡堂“花乃汤”其实在\n“那个”圈子里很有名。有次\n三朗误闯结果就变成了待宰羔羊。\n会接受恋爱咨询，给各种人建议，\n在御咲学园不断促成一对对情侣。")) from _call_shintaro_notebook_show_content_5

    jump block_0000369D

    return

label block_0000396D:
    # Node: 0000396D (月 CP1F1后)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_74BE632EED8E4475A58CFB241412CCBA as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("赤峰月"),
        _("中学二年级"),
        _("166cm"),
        _("55kg"),
        _("6月9日"),
        _("A"),
        _("剑道部"),
        _("传统兜裆布"),
        _("空的异卵双胞胎哥哥。平时\n稳重冷静，可一旦遇到有关弟弟\n的事就会各种暴走。高智商低情商，\n最近因为视力下降开始戴眼镜。\n剑道部主将，自家也是道场，\n非常有希望成为继承人。")) from _call_shintaro_notebook_show_content_6

    show shintaro_notebook_content_addon (_("追记：已经是赤峰家道场的继承人了")) at Transform(xpos=291,ypos=549) as addon_1 zorder 500 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    jump block_0000369D

    return

label block_0000369F:
    # Node: 0000369F (月)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_74BE632EED8E4475A58CFB241412CCBA as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("赤峰月"),
        _("中学二年级"),
        _("166cm"),
        _("55kg"),
        _("6月9日"),
        _("A"),
        _("剑道部"),
        _("传统兜裆布"),
        _("空的异卵双胞胎哥哥。平时\n稳重冷静，可一旦遇到有关弟弟\n的事就会各种暴走。高智商低情商，\n最近因为视力下降开始戴眼镜。\n剑道部主将，自家也是道场，\n非常有希望成为继承人。")) from _call_shintaro_notebook_show_content_7

    jump block_0000369D

    return

label block_0000396E:
    # Node: 0000396E (空 CP1F1后)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_20494B9D62EA4F279149FD58F937E917 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("赤峰空"),
        _("中学二年级"),
        _("161cm"),
        _("49kg"),
        _("6月9日"),
        _("B"),
        _("剑道部"),
        _("传统兜裆布"),
        _("温柔体贴，朋友很多，害怕虫子，\n喜欢甜食。点心做得很好，女子力\n极高。和哥哥月是双胞胎，但却总\n被认为是有年龄差的兄弟，对此有些\n想法。{color=#FF0000}{s}因为自己总是比不过哥哥怀有\n强烈的劣等感。{/s}{/color}")) from _call_shintaro_notebook_show_content_8

    show shintaro_notebook_content_addon (_("已经不存在这种事了")) at Transform(xpos=449,ypos=421,rotate=10) as addon_1 zorder 500 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    jump block_0000369D

    return

label block_000036A0:
    # Node: 000036A0 (空)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_20494B9D62EA4F279149FD58F937E917 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("赤峰空"),
        _("中学二年级"),
        _("161cm"),
        _("49kg"),
        _("6月9日"),
        _("B"),
        _("剑道部"),
        _("传统兜裆布"),
        _("温柔体贴，朋友很多，害怕虫子，\n喜欢甜食。点心做得很好，女子力\n极高。和哥哥月是双胞胎，但却总\n被认为是有年龄差的兄弟，对此有些\n想法。因为自己总是比不过哥哥怀有\n强烈的劣等感。")) from _call_shintaro_notebook_show_content_9

    jump block_0000369D

    return

label block_000036A2:
    # Node: 000036A2 (作哉 CP2F2后)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_E7F7E8175525416FA6F41D966995C24A as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("穗海作哉"),
        _("中学二年级"),
        _("162cm"),
        _("50kg"),
        _("4月1日"),
        _("B"),
        _("篮球部兼二班体育委员"),
        _("短裤"),
        _("非常强势、有点不良感的少年。\n超喜欢动物，所以悄悄收留了\n在学校里迷路的小狗。对一之濑翼\n非常不友好，但这有原因，并不是\n讨厌。也因为这种极佳的照料水平\n受到低年级某些学生的仰慕。")) from _call_shintaro_notebook_show_content_10

    show shintaro_notebook_content_addon (_("追加：终于和翼和解，现在两人一起在滑子老师\n的援助下照顾小翼，完全变成饲育系了")) at Transform(xpos=284,ypos=543) as addon_1 zorder 500 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    jump block_0000369D

    return

label block_000036A1:
    # Node: 000036A1 (作哉)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_E7F7E8175525416FA6F41D966995C24A as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("穗海作哉"),
        _("中学二年级"),
        _("162cm"),
        _("50kg"),
        _("4月1日"),
        _("B"),
        _("篮球部兼二班体育委员"),
        _("短裤"),
        _("非常强势、有点不良感的少年。\n超喜欢动物，所以悄悄收留了\n在学校里迷路的小狗。对一之濑翼\n非常不友好，但这有原因，并不是\n讨厌。也因为这种极佳的照料水平\n受到低年级某些学生的仰慕。")) from _call_shintaro_notebook_show_content_11

    jump block_0000369D

    return

label block_000036A5:
    # Node: 000036A5 (三朗 CP2F4后)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_62C8494C8D0A46788B2677BC65AFF6B3 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("猫山三朗"),
        _("中学二年级"),
        _("162cm"),
        _("48kg"),
        _("2月22日"),
        _("B"),
        _("{color=#FF0000}{s}篮球部{/s}{/color}"),
        _("四角裤"),
        _("喜欢说关西腔的活泼孩子。\n人如其名，怕狗怕水怕木天蓼。\n虽然在御咲学园却喜欢女人，\n曾向附近的御咲女学院的学生告白被拒。\n{color=#FF0000}{s}很怕慎太郎{/s}{/color}，因为对方试图把自己弄弯。\n不知为何觉得作哉喜欢友。")) from _call_shintaro_notebook_show_content_12

    show shintaro_notebook_content_addon (_("追加：现在是花乃汤前台")) at Transform(xpos=406,ypos=178,rotate=6) as addon_1 zorder 500 onlayer master
    show shintaro_notebook_content_addon (_("追加：终于意识到自己的感情\n开始和慎太郎交往了")) at Transform(xpos=330,ypos=545) as addon_2 zorder 500 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
    
    jump block_0000369D

    return

label block_000036A4:
    # Node: 000036A4 (三朗)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_62C8494C8D0A46788B2677BC65AFF6B3 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("猫山三朗"),
        _("中学二年级"),
        _("162cm"),
        _("48kg"),
        _("2月22日"),
        _("B"),
        _("篮球部"),
        _("四角裤"),
        _("喜欢说关西腔的活泼孩子。\n人如其名，怕狗怕水怕木天蓼。\n虽然在御咲学园却喜欢女人，\n曾向附近的御咲女学院的学生告白被拒。\n很怕慎太郎，因为对方试图把自己弄弯。\n不知为何觉得作哉喜欢友。")) from _call_shintaro_notebook_show_content_13

    jump block_0000369D

    return

label block_000036A6:
    # Node: 000036A6 (四朗)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_EBC5966DE6ED41F7B4A5FE392B4389B6 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("猫山四朗"),
        _("小学六年级"),
        _("144cm"),
        _("35kg"),
        _("5月5日"),
        _("A"),
        _("篮球部"),
        _("三角裤"),
        _("三朗的弟弟。觉得自己的哥哥整个\n就是一反面教材，很鄙视。非常\n仰慕作哉，期待下一年能进入\n御咲学园。性格很认真，经常被\n雪绪恶作剧。")) from _call_shintaro_notebook_show_content_14

    jump block_0000369D

    return

label block_000036A7:
    # Node: 000036A7 (雪緒)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_5986E3F7D3E84E3C84B042C07E57AD7D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("榊雪绪"),
        _("小学六年级"),
        _("143cm"),
        _("37kg"),
        _("10月31日"),
        _("O"),
        _("远足部"),
        _("三角裤"),
        _("四朗的好朋友，喜欢恶作剧。\n说话经常带嘲讽语气。\n喜欢冒险，喜欢探索，所以夏天和\n四朗一起去爬银刚山。本该是\n很高兴的事，但从那之后身体\n经常变得很奇怪。")) from _call_shintaro_notebook_show_content_15

    jump block_0000369D

    return

label block_000036A8:
    # Node: 000036A8 (小翼)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_38C4D56807D34472BB324F9AAB8CC7B5 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("小翼"),
        _("十个月左右"),
        _("50cm"),
        _("5kg"),
        _("12月27日"),
        "",
        "",
        "",
        _("曾迷路在御咲学园的非纯种狗，\n被作哉发现后养起来了。\n目前正在健康成长，对人友善，\n好奇心旺盛，总是元气满满。\n不过特别喜欢舔别人。")) from _call_shintaro_notebook_show_content_16

    jump block_0000369D

    return

label block_000036A9:
    # Node: 000036A9 (小翼（人類版）)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"


    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_E624081C37424A82B0BAAC00405C3656 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("小翼"),
        _("十三岁左右"),
        _("155cm"),
        _("47kg"),
        _("12月27日"),
        "",
        "",
        _("没穿"),
        _("喝下某触手给的药后小翼的样子。\n外表基本是复制了饲主作哉喜欢\n的一之濑翼的外貌。不过药效\n只有一天，天黑就变回狗了。\n之后在想能否有一天再把药买回来\n继续变成人类的样子和大家一起玩。")) from _call_shintaro_notebook_show_content_17

    if judge_lm_condition([]):
        jump block_0000369D

    return

label block_000036AB:
    # Node: 000036AB (Page 2)
    $ sys_lm_menu_item = [
        {"pos": (20, 65),"type":"textbutton","text":_("滑子老师"),"style":"shintaro_notebook_page_title","name": "滑子先生","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Nameko.png")},
        {"pos": (20, 101),"type":"textbutton","text":_("伊藤圭"),"style":"shintaro_notebook_page_title","name": "伊藤","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Itou.png")},
        {"pos": (20, 137),"type":"textbutton","text":_("木村树"),"style":"shintaro_notebook_page_title","name": "木村","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Kimura.png")},
        {"pos": (20, 174),"type":"textbutton","text":_("加藤准太"),"style":"shintaro_notebook_page_title","name": "加藤","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Katou.png")},
        {"pos": (20, 212),"type":"textbutton","text":_("松田健治"),"style":"shintaro_notebook_page_title","name": "松田","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Matsuta.png")},
        {"pos": (20, 248),"type":"textbutton","text":_("泉翔"),"style":"shintaro_notebook_page_title","name": "泉","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Izumi.png")},
        {"pos": (20, 284),"type":"textbutton","text":_("佐藤光"),"style":"shintaro_notebook_page_title","name": "佐藤","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Sato.png")},
        {"pos": (20, 320),"type":"textbutton","text":_("冈岛直弥"),"style":"shintaro_notebook_page_title","name": "岡島","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Okajima.png")},
        {"pos": (20, 356),"type":"textbutton","text":_("小岛正"),"style":"shintaro_notebook_page_title","name": "小島","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Kojima.png")},
        {"pos": (20, 392),"type":"textbutton","text":_("清武一"),"style":"shintaro_notebook_page_title","name":"清","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Kiyo.png"),"condition":[{"scope":0,"content":"C3S1 == True"}]},
        {"pos": (20, 428),"type":"textbutton","text":_("中山花音"),"style":"shintaro_notebook_page_title","name": "中山","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Nakayama.png"),"condition":[{"scope":0,"content":"C3S1 == True"}]},
        {"pos": (20, 464),"type":"textbutton","text":_("冈岛雄介"),"style":"shintaro_notebook_page_title","name": "岡島先輩","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Okajima-senior.png"),"condition":[{"scope":0,"content":"C3S1 == True"}]},
        {"pos": (20, 500),"type":"textbutton","text":_("中山紫音"),"style":"shintaro_notebook_page_title","name": "中山先輩","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Nakayama-senior.png"),"condition":[{"scope":0,"content":"C3S1 == True"}]},
        {"pos": (68, 10),"type":"textbutton","text":"1","style":"shintaro_notebook_page_number","name": "目次１"},
        {"pos": (125, 11),"type":"textbutton","text":"3","style":"shintaro_notebook_page_number","name": "目次３"},
        {"pos": (154, 10),"type":"textbutton","text":"4","style":"shintaro_notebook_page_number","name": "目次４"},
        {"pos": (182, 12),"type":"textbutton","text":"×","style":"shintaro_notebook_page_number","name": "とじる"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.25, 0.25) from _call_lm_menu_369
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子先生\"" }]):
        jump block_000036B1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" },{ "scope": 1, "content": "C2S3 == True" }]):
        jump block_000036B3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤\"" }]):
        jump block_000036B2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" },{ "scope": 1, "content": "C2S3 == True" }]):
        jump block_000036B5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"木村\"" }]):
        jump block_000036B4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"加藤\"" }]):
        jump block_000036B6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田\"" }]):
        jump block_000036B7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉\"" }]):
        jump block_000036B8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"佐藤\"" }]):
        jump block_000036B9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島\"" }]):
        jump block_000036BA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小島\"" }]):
        jump block_000036BB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"清\"" }]):
        jump block_000036BC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中山\"" }]):
        jump block_000036BD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島先輩\"" },{ "scope": 1, "content": "C3S6 == True" }]):
        jump block_000036C0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"岡島先輩\"" }]):
        jump block_000036BE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中山先輩\"" }]):
        jump block_000036BF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次１\"" }]):
        jump block_00003695
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次３\"" }]):
        jump block_000036C5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次４\"" }]):
        jump block_000036DD
    if judge_lm_condition([]):
        jump block_0000372C

    return

label block_000036C2:
    # Node: 000036C2 (RESET)
    pause

    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_hide_content from _call_shintaro_notebook_hide_content_1

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_FB83778318AB4B3A83211AAA57E755D6
    with rs_effect_FC474B930CE449DD8BE5D4980A132631

    jump block_000036B0

    return

label block_000036B1:
    # Node: 000036B1 (滑子老師)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_9B177427B0AE4CA19CD7EA7ED1BBA116 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("滑子老师"),
        _("四十岁"),
        _("175cm"),
        _("80kg"),
        "",
        "",
        _("二年级一班的班主任"),
        "",
        _("生气起来非常可怕、但也非常\n体谅学生的可以信赖的好老师。\n对大型赛事很热衷。\n和二班的海老师关系不错。\n对妻子爱得非常深沉。")) from _call_shintaro_notebook_show_content_18

    jump block_000036C2

    return

label block_000036B3:
    # Node: 000036B3 (伊藤 CP2F3后)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_FC5AF08462664100A6C4F295157BECE8 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("伊藤圭"),
        _("中学二年级"),
        _("157cm"),
        _("49kg"),
        _("6月6日"),
        _("O"),
        _("田径部的经理"),
        _("短裤"),
        _("作哉·三朗·木村所在的DQN集团\n唯一的良心。单恋木村许久，\n{color=#FF0000}{s}一直在因为对方有恋人而烦恼要不要\n放弃{/s}{/color}。按摩很拿手。")) from _call_shintaro_notebook_show_content_19

    show shintaro_notebook_content_addon (_("追加：终于结束单恋和木村顺利交往了")) at Transform(xpos=285,ypos=497) as addon_1 zorder 500 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    jump block_000036C2

    return

label block_000036B2:
    # Node: 000036B2 (伊藤)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_FC5AF08462664100A6C4F295157BECE8 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("伊藤圭"),
        _("中学二年级"),
        _("157cm"),
        _("49kg"),
        _("6月6日"),
        _("O"),
        _("田径部的经理"),
        _("短裤"),
        _("作哉·三朗·木村所在的DQN集团\n唯一的良心。单恋木村许久，\n一直在因为对方有恋人而烦恼要不要\n放弃。按摩很拿手。")) from _call_shintaro_notebook_show_content_20
    
    jump block_000036C2

    return

label block_000036B5:
    # Node: 000036B5 (木村 CP2F3后)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_89F64643C65A43439A34522141B94FAF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("木村树"),
        _("中学二年级"),
        _("165cm"),
        _("53kg"),
        _("10月10日"),
        _("A"),
        _("田径部"),
        _("四角裤"),
        _("典型的脑袋是肌肉长的。\n{color=#FF0000}{s}有恋人，但交往不怎么顺利。{/s}{/color}\n体型很好，所以传运动服的样子很\n吸引人，有不少粉丝。本人则非常迟钝，\n{color=#FF0000}{s}所以伊藤长久的单恋完全没有效果，{/s}{/color}\n罪恶深重的男人。性欲超强。")) from _call_shintaro_notebook_show_content_21

    show shintaro_notebook_content_addon (_("已经分手了")) at Transform(xpos=550,ypos=340,rotate=10) as addon_1 zorder 500 onlayer master
    show shintaro_notebook_content_addon (_("已经两情相悦了")) at Transform(xpos=500,ypos=420,rotate=5) as addon_2 zorder 500 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    jump block_000036C2

    return

label block_000036B4:
    # Node: 000036B4 (木村)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_89F64643C65A43439A34522141B94FAF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("木村树"),
        _("中学二年级"),
        _("165cm"),
        _("53kg"),
        _("10月10日"),
        _("A"),
        _("田径部"),
        _("四角裤"),
        _("典型的脑袋是肌肉长的。\n有恋人，但交往不怎么顺利。\n体型很好，所以传运动服的样子很\n吸引人，有不少粉丝。本人则非常迟钝，\n所以伊藤长久的单恋完全没有效果，\n罪恶深重的男人。性欲超强。")) from _call_shintaro_notebook_show_content_22

    jump block_000036C2

    return

label block_000036B6:
    # Node: 000036B6 (加藤)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_C2107624B4DA4FE381D544BCF84DAB48 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("加藤准太"),
        _("中学二年级"),
        _("160cm"),
        _("51kg"),
        _("7月20日"),
        _("O"),
        _("棒球部兼一班体育委员"),
        _("四角裤"),
        _("元气满满的体育系男生！\n也完全不介意光膀子！\n成绩差到和友一个程度。\n放学后有时会和同学一起在\n商店街比谁吃得多。\n喜欢的类型是年上肌肉男！？")) from _call_shintaro_notebook_show_content_23

    jump block_000036C2

    return

label block_000036B7:
    # Node: 000036B7 (松田)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_E6E3DDA4CA604E848DC7C32D2873D5BD as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("松田健治"),
        _("中学二年级"),
        _("167cm"),
        _("55kg"),
        _("9月17日"),
        _("O"),
        _("篮球部兼一班音乐委员"),
        _("短裤"),
        _("很有大人的样子，看起来像不良，\n其实很认真很喜欢照顾人。\n经常带着打火机，但只是为了\n掩盖拿了哥哥的烟的事实。\n觉得作哉很可爱。")) from _call_shintaro_notebook_show_content_24

    jump block_000036C2

    return

label block_000036B8:
    # Node: 000036B8 (泉)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_9F2673517D4345F5A839B4E8FB07E7F3 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("泉翔"),
        _("中学二年级"),
        _("160cm"),
        _("48kg"),
        _("4月3日"),
        _("A"),
        _("排球部"),
        _("四角裤"),
        _("温柔善良的性格。\n之前一直单恋排球部的前辈，\n在和慎太郎商讨过后成功交往。\n现在正因为恋人之间事情越来越多\n越来越复杂而困扰。")) from _call_shintaro_notebook_show_content_25

    jump block_000036C2

    return

label block_000036B9:
    # Node: 000036B9 (佐藤)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_21A6F9F3C84C40F4B12D3B4268F655AF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("佐藤光"),
        _("中学二年级"),
        _("157cm"),
        _("47kg"),
        _("12月22日"),
        _("B"),
        _("吹奏乐部兼二班体育委员"),
        _("短裤"),
        _("看着老实，实则闹腾，喜欢古典\n音乐，经常说要精通这个。\n进入御咲学园似乎是因为这里的\n吹奏乐部很厉害。\n似乎在部内有在意的前辈，\n但本人极力否认。")) from _call_shintaro_notebook_show_content_26

    jump block_000036C2

    return

label block_000036BA:
    # Node: 000036BA (岡島)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_654A32CF419D4537B5CC1EF9B8EEE58F as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("冈岛直弥"),
        _("中学二年级"),
        _("161cm"),
        _("47kg"),
        _("2月21日"),
        _("AB"),
        _("新闻部"),
        _("四角裤"),
        _("学习优秀、成绩进步的学霸。\n但却是一个和小岛一起成立新闻部、\n醉心于搞大新闻的奇怪少年。\n根本就没有性知识，那方面的话题\n完全跟不上。一般总是和小岛佐藤\n在一起。有一个三年级的哥哥，\n制服也是这麽来的。")) from _call_shintaro_notebook_show_content_27

    jump block_000036C2

    return

label block_000036BB:
    # Node: 000036BB (小島)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_6B1CFD1FA2ED4B17AA2D93EA13D4D41B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("小岛正"),
        _("中学二年级"),
        _("148cm"),
        _("38kg"),
        _("11月30日"),
        _("AB"),
        _("新闻部"),
        _("三角裤"),
        _("在新闻部负责摄影，和部长不同是\n个很安静的怪孩子。会给提供有趣\n情报的人对方喜欢的照片。据本人说，\n“我们尊重肖像权”。非常喜欢部长\n冈岛，但有些过保护。")) from _call_shintaro_notebook_show_content_28

    jump block_000036C2

    return

label block_000036BC:
    # Node: 000036BC (清)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_6483F4D019204BA4928CFDA096B127C4 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("清武一"),
        _("中学一年级"),
        _("150cm"),
        _("45kg"),
        _("10月25日"),
        _("O"),
        _("空手道部"),
        _("四角裤"),
        _("人如其名，清廉正直富有正义感。\n非常敬爱同部的前辈绫濑忍，\n梦想能成为前辈一样的人。")) from _call_shintaro_notebook_show_content_29

    jump block_000036C2

    return

label block_000036BD:
    # Node: 000036BD (中山)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_20B24213AA8D489C8242741503719913 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("中山花音"),
        _("中学一年级"),
        _("150cm"),
        _("41kg"),
        _("3月6日"),
        _("A"),
        _("排球部"),
        _("短裤"),
        _("腹黑性格。在和之前的恋人分手后，\n某天拾到了相性不错的大叔，\n开始了调教之旅。\n和清关系不错。")) from _call_shintaro_notebook_show_content_30

    jump block_000036C2

    return

label block_000036C0:
    # Node: 000036C0 (岡島前輩 CP3F6后)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_14E20A5CB6CC4ADF9E335516B88D375B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("冈岛雄介"),
        _("中学三年级"),
        _("165cm"),
        _("53kg"),
        _("3月14日"),
        _("AB"),
        _("吹奏乐部"),
        _("四角裤"),
        _("新闻部的冈岛直弥的哥哥。\n{color=#FF0000}{s}因为是吹奏乐部唯一的钢琴手，\n态度偶尔不端正。而后辈中的佐藤\n对此觉得很是问题。{/s}{/color}")) from _call_shintaro_notebook_show_content_31

    show shintaro_notebook_content_addon (_("在佐藤的计策下已经改掉这个问题了\n期待两人今后的发展")) at Transform(xpos=322,ypos=357,rotate=-10) as addon_1 zorder 500 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
    
    jump block_000036C2

    return

label block_000036BE:
    # Node: 000036BE (岡島前輩)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_14E20A5CB6CC4ADF9E335516B88D375B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("冈岛雄介"),
        _("中学三年级"),
        _("165cm"),
        _("53kg"),
        _("3月14日"),
        _("AB"),
        _("吹奏乐部"),
        _("四角裤"),
        _("新闻部的冈岛直弥的哥哥。\n因为是吹奏乐部唯一的钢琴手，\n态度偶尔不端正。而后辈中的佐藤\n对此觉得很是问题。")) from _call_shintaro_notebook_show_content_32

    jump block_000036C2

    return

label block_000036BF:
    # Node: 000036BF (中山前輩)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_4834E50CF63D43A1897DB60B5DEBFF7B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("中山紫音"),
        _("中学三年级"),
        _("172cm"),
        _("56kg"),
        _("4月7日"),
        _("A"),
        _("排球部"),
        _("短裤"),
        _("中山花音的哥哥。和弟弟不同对各种事\n非常无所谓。恋人是排球部的泉。\n偶尔冷战，但一直很重视对方。")) from _call_shintaro_notebook_show_content_33

    jump block_000036C2

    return

label block_000036C4:
    # Node: 000036C4 (Page 3)
    $ sys_lm_menu_item = [
        {"pos": (20, 65),"type":"textbutton","text":_("夕阳"),"style":"shintaro_notebook_page_title","name": "ユウヒ","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Yuuhi.png"),"condition":[{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 101),"type":"textbutton","text":_("世依木守"),"style":"shintaro_notebook_page_title","name": "マモル","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Mamoru.png"),"condition":[{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 174),"type":"textbutton","text":_("触手A"),"style":"shintaro_notebook_page_title","name": "触手A","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Tentacle-earthworm.png"),"condition":[{"scope":0,"content":"C2S6 == True"}]},
        {"pos": (20, 212),"type":"textbutton","text":_("触手B"),"style":"shintaro_notebook_page_title","name": "触手B","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Tentacle-starfish.png"),"condition":[{"scope":0,"content":"C2S6 == True"}]},
        {"pos": (20, 248),"type":"textbutton","text":_("导游"),"style":"shintaro_notebook_page_title","name": "使用人","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Tour-guide.png"),"condition":[{"scope":0,"content":"C2S6 == True"}]},
        {"pos": (20, 137),"type":"textbutton","text":_("朔"),"style":"shintaro_notebook_page_title","name": "朔","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Nori.png"),"condition":[{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 284),"type":"textbutton","text":_("晦"),"style":"shintaro_notebook_page_title","name": "晦","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Kai.png"),"condition":[{"scope":0,"content":"C2S6 == True"}]},
        {"pos": (20, 321),"type":"textbutton","text":_("暗黑小熊猫"),"style":"shintaro_notebook_page_title","name": "ダークレッサー","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Dark lesser.png"),"condition":[{"scope":0,"content":"C2S6 == True"},{"scope":0,"content":"C3S5 == True"}]},
        {"pos": (20, 357),"type":"textbutton","text":_("妖怪A"),"style":"shintaro_notebook_page_title","name": "お化けA","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/MonsterA.png"),"condition":[{"scope":0,"content":"C3S5 == True"}]},
        {"pos": (20, 392),"type":"textbutton","text":_("妖怪B"),"style":"shintaro_notebook_page_title","name": "お化けB","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/MonsterB.png"),"condition":[{"scope":0,"content":"C3S5 == True"}]},
        {"pos": (20, 429),"type":"textbutton","text":_("妖怪C"),"style":"shintaro_notebook_page_title","name": "お化けC","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/MonsterC.png"),"condition":[{"scope":0,"content":"C3S5 == True"}]},
        {"pos": (68, 10),"type":"textbutton","text":"1","style":"shintaro_notebook_page_number","name": "目次１"},
        {"pos": (96, 10),"type":"textbutton","text":"2","style":"shintaro_notebook_page_number","name": "目次２"},
        {"pos": (154, 10),"type":"textbutton","text":"4","style":"shintaro_notebook_page_number","name": "目次４"},
        {"pos": (182, 12),"type":"textbutton","text":"×","style":"shintaro_notebook_page_number","name": "とじる"},
        {"pos": (24, 64),"type":"textbutton","text":_("等待补充"),"style":"shintaro_notebook_page_title","name": "Waiting","condition":[{"scope":0,"content":"Chapter < 2"}]}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.25, 0.25) from _call_lm_menu_370
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ユウヒ\"" }]):
        jump block_000036D6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"マモル\"" }]):
        jump block_000036D5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手A\"" }]):
        jump block_000036D4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"触手B\"" }]):
        jump block_000036D3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"使用人\"" }]):
        jump block_000036D2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"朔\"" }]):
        jump block_000036CF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"晦\"" }]):
        jump block_000036D1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ダークレッサー\"" }]):
        jump block_000036CD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"お化けA\"" }]):
        jump block_000036D0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"お化けB\"" }]):
        jump block_000036CE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"お化けC\"" }]):
        jump block_000036CC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次１\"" }]):
        jump block_00003695
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次２\"" }]):
        jump block_000036B0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次４\"" }]):
        jump block_000036DD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Waiting\"" }]):
        jump block_000036C4
    if judge_lm_condition([]):
        jump block_0000372C

    return

label block_000036D8:
    # Node: 000036D8 (RESET)
    pause

    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_hide_content from _call_shintaro_notebook_hide_content_2

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_FB83778318AB4B3A83211AAA57E755D6
    with rs_effect_FC474B930CE449DD8BE5D4980A132631

    jump block_000036C5

    return

label block_000036D6:
    # Node: 000036D6 (夕阳)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_44EA2B7B1FCB4729960A6B607033A5BC as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("夕阳"),
        _("中学一年级"),
        _("157cm"),
        _("50kg"),
        _("9月2日"),
        _("O"),
        _("足球部兼魔法师"),
        _("四角裤或比基尼"),
        _("被师父认可才能后作为正义的\n魔法师守护着城市的和平。\n因为不愿学习，初级魔法都\n用不好。一直在和企图征服世界\n的WOLFS的朔进行工口战斗，打着\n打着就喜欢上对方了。")) from _call_shintaro_notebook_show_content_34

    jump block_000036D8

    return

label block_000036D5:
    # Node: 000036D5 (守)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_E11FA5E6563E408B9021A0E86E907F5E as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("世依木守"),
        _("中学一年级"),
        _("157cm"),
        _("46kg"),
        _("6月1日"),
        _("A"),
        _("足球部兼英雄"),
        _("四角裤"),
        _("和魔法师夕阳一起守护城市的\n正义的英雄，特技是GYMNO BEAM。\n恋人是过去战斗过并打倒的\n章鱼章鱼星人。似乎在不为人知\n的地方会做这样那样的事？")) from _call_shintaro_notebook_show_content_35

    jump block_000036D8

    return

label block_000036D4:
    # Node: 000036D4 (触手A)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_04A3A4B29A1A4C5CBBBAEFA035EEE021 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("触手A"),
        _("不知"),
        _("不知"),
        _("似乎很轻？"),
        _("不知"),
        "",
        _("WOLFS"),
        "",
        _("WOLFS的一员。最早开始侍奉朔\n的触手，同时也是管家。说话\n像老妈子，很绅士。\n被其他触手信赖。")) from _call_shintaro_notebook_show_content_36

    jump block_000036D8

    return

label block_000036D3:
    # Node: 000036D3 (触手B)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_4FF3727EA934419DBF919D282949D9AF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("触手B"),
        _("不知"),
        _("不知"),
        _("不知"),
        _("不知"),
        "",
        _("WOLFS"),
        "",
        _("WOLFS的一员。才刚开始加入朔\n的队伍。背后有无数触手，\n是备受期待的新人。看起来似乎\n不很努力，但也在奋力学习\n如何侍奉。")) from _call_shintaro_notebook_show_content_37

    jump block_000036D8

    return

label block_000036D2:
    # Node: 000036D2 (導遊)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_55A8161EDC0140BCB61A4ECC9EAE5AFB as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("导游？"),
        _("不知"),
        _("190cm"),
        _("不详"),
        "",
        "",
        "",
        "",
        _("离岛的度假酒店的导游……\n才不是，其实里面是触手A和触手B。\n整个旅行都是朔的计划。")) from _call_shintaro_notebook_show_content_38

    jump block_000036D8

    return

label block_000036CF:
    # Node: 000036CF (朔)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_C6C1AACA8FE54D6FBAB0EBBBE2D57179 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("朔"),
        _("十三岁左右？"),
        _("152cm"),
        _("40kg"),
        _("不详"),
        _("不知"),
        _("WOLFS"),
        _("没有资料"),
        _("企图征服世界的组织WOLFS的一员。\n操纵着触手怪物，喜欢玩弄敌人。\n某些意义上和忍关系很好，\n偶尔一起出门。\n正在进行从欲望中提取能量的研究，\n为此不断寻找实验体。")) from _call_shintaro_notebook_show_content_39

    jump block_000036D8

    return

label block_000036D1:
    # Node: 000036D1 (晦)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_E2F8D2458EA448CBA5461F5E15D3732D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("晦"),
        _("二十左右"),
        _("159cm"),
        _("46kg"),
        _("未知"),
        _("不知道"),
        _("WOLFS"),
        _("这……"),
        _("朔的哥哥，豪迈奔放。\n和WOLFS一贯的方针不同，\n现在正在地球上离岛的宾馆悠闲度日。\n在梅咲开的酒吧一下子就成了热门。\n好像有个高中生恋人。")) from _call_shintaro_notebook_show_content_40

    jump block_000036D8

    return

label block_000036CD:
    # Node: 000036CD (Dark lesser)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_ADD5336B0677481F9A5FB075EBAE89FE as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("暗黑小熊猫"),
        "",
        _("两到三米"),
        _("150kg-250kg"),
        "",
        "",
        "",
        "",
        _("英文叫Dark lesser，是小熊猫型的巨大怪兽。\n外表凶恶，爪子锋利，\n但其实只是好奇心旺盛，无甚危害。\n喜欢苹果。")) from _call_shintaro_notebook_show_content_41

    jump block_000036D8

    return

label block_000036D0:
    # Node: 000036D0 (妖怪A)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_7C460B05CEF34685BE88806719BAA87D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("妖怪A"),
        _("未知"),
        _("不知"),
        _("天知道"),
        "",
        "",
        "",
        "",
        _("从“上古封印之箱”里逃出来的\n妖怪中的一个。因为兴致总是\n很好，被认为是妖怪们的领导。\n计划把御咲学园封闭在异空间内，\n但被以忍为首的救援组打败了。")) from _call_shintaro_notebook_show_content_42

    jump block_000036D8

    return

label block_000036CE:
    # Node: 000036CE (妖怪B)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_24C49F4CA7A74F4B8E38A9889A217BC2 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("妖怪B"),
        _("不知"),
        _("不详"),
        _("天知道"),
        "",
        "",
        "",
        "",
        _("从“上古封印之箱”里逃出来的\n妖怪中的一个。总是很知性、很\n做作的样子，在和作哉们所在的\n回收组战斗时最后在九尾手上\n灰飞烟灭。")) from _call_shintaro_notebook_show_content_43

    jump block_000036D8

    return

label block_000036CC:
    # Node: 000036CC (妖怪C)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_30E5366165794F999DA744CC2310A193 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("妖怪C"),
        _("未知"),
        _("不详"),
        _("天知道"),
        "",
        "",
        "",
        "",
        _("从“上古封印之箱”里逃出来的\n正太控妖怪的一个。曾经从箱子\n里出来过一次夜里“拜访”\n慎太郎，但手都没下去，为此\n耿耿于怀，最后被常磐给的\n符咒打败。")) from _call_shintaro_notebook_show_content_44

    jump block_000036D8

    return

label block_000036DF:
    # Node: 000036DF (Page 4)
    $ sys_lm_menu_item = [
        {"pos": (20, 101),"type":"textbutton","text":_("小林"),"style":"shintaro_notebook_page_title","name": "小林","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Kobayashi.png"),"condition":[{"scope":0,"content":"C1S4 == True"},{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 137),"type":"textbutton","text":_("南"),"style":"shintaro_notebook_page_title","name": "南","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Minami.png"),"condition":[{"scope":0,"content":"C1S4 == True"},{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 174),"type":"textbutton","text":_("杉本志"),"style":"shintaro_notebook_page_title","name": "杉本","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Sumoto.png"),"condition":[{"scope":0,"content":"C1S4 == True"},{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 210),"type":"textbutton","text":_("陆田功"),"style":"shintaro_notebook_page_title","name": "陸田","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Rikuta.png"),"condition":[{"scope":0,"content":"C1S4 == True"},{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 65),"type":"textbutton","text":_("常磐进"),"style":"shintaro_notebook_page_title","name": "常磐","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Tokiwa.png")},
        {"pos": (20, 321),"type":"textbutton","text":_("九尾"),"style":"shintaro_notebook_page_title","name": "九尾","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Kyubi.png"),"condition":[{"scope":0,"content":"C2S5 == True"}]},
        {"pos": (20, 248),"type":"textbutton","text":_("诹访部翔银时"),"style":"shintaro_notebook_page_title","name": "翔銀時","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Shougintoki.png"),"condition":[{"scope":0,"content":"C1S4 == True"},{"scope":0,"content":"Chapter > 1"}]},
        {"pos": (20, 285),"type":"textbutton","text":_("诹访部翔平"),"style":"shintaro_notebook_page_title","name": "翔平","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Shouhei.png"),"condition":[{"scope":0,"content":"C3S1 == True"}]},
        {"pos": (20, 357),"type":"textbutton","text":_("逆濑荒哉"),"style":"shintaro_notebook_page_title","name": "逆瀬","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Sakase.png"),"condition":[{"scope":0,"content":"C1SG1 and C1SG2 and C2SG1 and C2SG2 and C3SG1 and C3SG2 == True"}]},
        {"pos": (20, 392),"type":"textbutton","text":_("黑——"),"style":"shintaro_notebook_page_title","name": "へー","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/He--.png"),"condition":[{"scope":0,"content":"C1SG1 and C1SG2 and C2SG1 and C2SG2 and C3SG1 and C3SG2 == True"}]},
        {"pos": (20, 429),"type":"textbutton","text":_("贝——"),"style":"shintaro_notebook_page_title","name": "ベー","preview": (0, 0, "images/Shintaro-notebook/BACKGROUND/Be--.png"),"condition":[{"scope":0,"content":"C1SG1 and C1SG2 and C2SG1 and C2SG2 and C3SG1 and C3SG2 == True"}]},
        {"pos": (68, 10),"type":"textbutton","text":"1","style":"shintaro_notebook_page_number","name": "目次１"},
        {"pos": (96, 10),"type":"textbutton","text":"2","style":"shintaro_notebook_page_number","name": "目次２"},
        {"pos": (125, 11),"type":"textbutton","text":"3","style":"shintaro_notebook_page_number","name": "目次３"},
        {"pos": (182, 12),"type":"textbutton","text":"×","style":"shintaro_notebook_page_number","name": "とじる"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.25, 0.25) from _call_lm_menu_371
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" }]):
        jump block_000036F1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" }]):
        jump block_000036F0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"杉本\"" }]):
        jump block_000036EF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"陸田\"" }]):
        jump block_000036ED
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"九尾\"" }]):
        jump block_000036EB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" }]):
        jump block_000036EE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"翔銀時\"" }]):
        jump block_000036EC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"翔平\"" }]):
        jump block_000036E8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"逆瀬\"" }]):
        jump block_000036E7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"へー\"" }]):
        jump block_000036E9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ベー\"" }]):
        jump block_000036EA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次１\"" }]):
        jump block_00003695
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次２\"" }]):
        jump block_000036B0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目次３\"" }]):
        jump block_000036C5
    if judge_lm_condition([]):
        jump block_0000372C

    return

label block_000036F2:
    # Node: 000036F2 (RESET)
    pause

    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_hide_content from _call_shintaro_notebook_hide_content_3

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_FB83778318AB4B3A83211AAA57E755D6
    with rs_effect_FC474B930CE449DD8BE5D4980A132631

    jump block_000036DD

    return

label block_000036F1:
    # Node: 000036F1 (小林)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_887B793042884C33A9EC38D1DEF0C5D9 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("小林"),
        _("小学四年级"),
        _("133cm"),
        _("30kg"),
        _("1月17日"),
        _("O"),
        "",
        _("三角裤"),
        _("放学后总是和南在公园玩的活泼\n的男孩子，也经常和友、慎太郎、\n空、散歩中的作哉玩。最近迷上了\n老游戏。本人言：每当看到南时\n心跳就会不自觉加快……")) from _call_shintaro_notebook_show_content_45

    jump block_000036F2

    return

label block_000036F0:
    # Node: 000036F0 (南)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_CA7B9E39B71643C69E7A3D2AD94BABC0 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("南"),
        _("小学四年级"),
        _("132cm"),
        _("31kg"),
        _("2月28日"),
        _("O"),
        "",
        _("三角裤"),
        _("和小林关系好到不得了。\n有小气的一面，但好奇心旺盛，\n经常和小林到处捣乱。\n完全不知道下流梗。\n家里养了只猫。")) from _call_shintaro_notebook_show_content_46

    jump block_000036F2

    return

label block_000036EF:
    # Node: 000036EF (杉本)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_28CF9DD5B34E484AA69F066F5BE39B74 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("杉本志"),
        _("小学六年级"),
        _("146cm"),
        _("38kg"),
        _("8月9日"),
        _("B"),
        "",
        _("三角裤"),
        _("吉木与行所属“陆田&杉本”中的\n玩梗担当。成为艺人刚一年多。\n经常玩以前从没有人玩过的梗，\n外加体型问题，在部分人中获得了讚赏。\n刚出道所以只在关西地方偶像圈，\n不过目标是全国！\n大家也要来多多应援！")) from _call_shintaro_notebook_show_content_47

    jump block_000036F2

    return

label block_000036ED:
    # Node: 000036ED (陸田)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_39FE2F2BE36B4E199D448269DAD930AD as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("陆田功"),
        _("小学六年级"),
        _("145cm"),
        _("38kg"),
        _("11月5日"),
        _("B"),
        "",
        _("四角裤"),
        _("吉木与行所属“陆田&杉本”中的\n吐槽担当。槽点都是杉本想的，\n不过在听到内容后也能给出精彩的吐槽。\n和杉本是青梅竹马，虽説舞台上吐槽\n毫不留情，但其实比谁都要重视杉本，\n认为他是自己最重要的人。")) from _call_shintaro_notebook_show_content_48

    jump block_000036F2

    return

label block_000036EB:
    # Node: 000036EB (九尾)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_C1D6E1AC4DF64F598C901E6DD0C6CD9C as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("九尾"),
        _("千岁以上"),
        _("不知道"),
        _("不知道"),
        _("怎么可能知道"),
        _("真的有？"),
        _("不知道"),
        _("和雪绪一样吧"),
        _("银刚山深处作为神受到祭祀的狐狸。\n似乎是顶级妖怪。\n以前凭依体毁坏所以失去了大部分力量，\n现在附身在波长吻合的雪绪身上。\n通过在各种意义上不断做各种事情\n正逐渐取回力量。")) from _call_shintaro_notebook_show_content_49

    jump block_000036F2

    return

label block_000036EE:
    # Node: 000036EE (常磐)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_2B4E1D0E60784ECA9F516335487F9B75 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("常磐进"),
        _("中学三年级？"),
        _("160cm"),
        _("46kg"),
        _("问不到"),
        _("问不出来"),
        _("不知道"),
        _("三角裤"),
        _("不知为何一直静静地站在学园外的厕所旁。\n总能事先察觉到周围的异常和未来的事情，\n并据此给各种人各种有益的建议。\n表情一直很寂寞，似乎并不开心。")) from _call_shintaro_notebook_show_content_50

    jump block_000036F2

    return

label block_000036EC:
    # Node: 000036EC (翔銀時)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_7B26878392544D52B9C0AB455948179F as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("诹访部翔银时"),
        _("八十八岁"),
        _("180cm"),
        _("74kg"),
        "",
        "",
        "",
        "",
        _("经常光顾花乃汤的老大爷，\n被其他客人称呼为“会长”。\n曾是御咲学园的学生，性格\n硬派刚正。现在非常担心慎太郎的\n身体健康。有一个25岁的孙子。")) from _call_shintaro_notebook_show_content_51

    jump block_000036F2

    return

label block_000036E8:
    # Node: 000036E8 (翔平)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_8854BA78EA1E429B969E4C7D768CFC36 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("诹访部翔平"),
        _("二十五岁"),
        _("176cm"),
        _("65kg"),
        "",
        "",
        "",
        "",
        _("超重度正太控上班族。\n经常目不转睛看着各种少年，\n要是少年什么都好。\n人型自走大变态。\n当然，被请去喝茶还是没有过的。\n持有合气道段位，意外很强。")) from _call_shintaro_notebook_show_content_52

    jump block_000036F2

    return

label block_000036E7:
    # Node: 000036E7 (逆瀬)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_09EF459DD19D45668BEEF4FAF6C1844B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("逆濑荒哉"),
        _("中学二年级"),
        _("162cm"),
        _("50kg"),
        _("4月30日"),
        _("A"),
        _("暂时不知道"),
        _("四角裤"),
        _("小学的时候特别喜欢欺负友和忍。\n因为父母的工作经常搬家，\n那时候也因为这个有半年\n转到了其他学校。\n现在住在关东。")) from _call_shintaro_notebook_show_content_53

    jump block_000036F2

    return

label block_000036E9:
    # Node: 000036E9 (黑ー)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_92AFC6243E214497A70410CF4A4C6400 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("黑——"),
        "",
        _("60cm"),
        _("6kg"),
        "",
        "",
        "",
        "",
        _("感情内敛的小熊猫。\n脾气不大好。")) from _call_shintaro_notebook_show_content_54

    jump block_000036F2

    return

label block_000036EA:
    # Node: 000036EA (貝ー)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    $ zorder_tag_FB83778318AB4B3A83211AAA57E755D6 = 300
    show rs_image_A2D77BA68BFA400B8E702884EE46D84B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_E0B202A5A11A4A18AFFF420F47345085 as tag_FB83778318AB4B3A83211AAA57E755D6 at center_bottom zorder zorder_tag_FB83778318AB4B3A83211AAA57E755D6 onlayer master
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    call shintaro_notebook_show_content(
        _("贝——"),
        "",
        _("60cm"),
        _("6kg"),
        "",
        "",
        "",
        "",
        _("和小翼很要好的小熊猫。\n不知为何不待见友。")) from _call_shintaro_notebook_show_content_55

    jump block_000036F2

    return
