# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003836 (小忍問題冊)

label block_00003837:
    # Node: 00003837 ()
    $ CurrentIndex = -1
    $ CorrectCount = 0
    $ QuestionSet = []
    $ QuestionLevel = 0

    $ set_place_title(False)

    image shinobu_question_background_title = ParameterizedText(
        font="font/source-hans-sans-medium.ttc",
        color="#000000",
        xalign=0.5,
        yalign=0.04,
        size=40,
        text_align=0.5)

    image shinobu_question_background_level = ParameterizedText(
        font="font/source-hans-sans-medium.ttc",
        color="#0E4603",
        xalign=0.2,
        yalign=0.19,
        size=30,
        text_align=0.5)

    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == False" }]):
        jump block_0000388A
    if judge_lm_condition([]):
        jump block_00003881

    return

label shinobu_question_answer_sheet(level):
    $ _sys_shinobu_question_generate_answer = ''
    if level == 0:
        call block_0000388A from _call_block_0000388A
    elif level == 1:
        call block_0000388C from _call_block_0000388C
    else:
        call block_0000388D from _call_block_0000388D
    $ del _sys_shinobu_question_generate_answer
    $ _temp_8801ACBCE1EE49529B1EC516C0FD029B = ''
    $ i = 0
    while i < len(_return):
        $ _temp_8801ACBCE1EE49529B1EC516C0FD029B += _return[i]["content"].replace('\n', '') + "\n"
        $ j = 0
        while j < len(_return[i]["choice"]):
            if _return[i]["choice"][j]["target"] == "block_00003895":
                $ _temp_8801ACBCE1EE49529B1EC516C0FD029B += "{color=#D50000}" + _return[i]["choice"][j]["name"] + "{/color}\n"
            $ j += 1
        $ i += 1
    $ del i
    $ del j
    return _temp_8801ACBCE1EE49529B1EC516C0FD029B

label shinobu_question_answer_sheet_show(level):
    call shinobu_question_answer_sheet(level) from _call_shinobu_question_answer_sheet
    if level == 0:
        $ level = "简单"
    elif level == 1:
        $ level = "一般"
    else:
        $ level = "困难"
    $ set_place_title(False)
    $ zorder_tag_17C5925FD8E5420F96A5D7708A5CD875 = 300
    show rs_image_2FC53155DF464987961ABA73E5371AD7 as tag_17C5925FD8E5420F96A5D7708A5CD875 at center_bottom zorder zorder_tag_17C5925FD8E5420F96A5D7708A5CD875 onlayer master
    show rs_image_505E4D67D9E0480190F94440CC260635 "[_return]" as shinobu_question_answer_content at Transform(xpos=196,ypos=57) zorder 1000
    show rs_image_39BDF35F722B4A2FBF52EE3D9BAB608B (_("参考答案")) as shinobu_question_answer_title at Transform(xpos=195,ypos=18) zorder 1000
    show rs_image_FBC78BE31EAE4A92979414FEEEEDE983 (_("难度：[level]")) as shinobu_question_answer_level at Transform(xpos=621,ypos=25) zorder 1000
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    $ set_place_title(_("图书馆"))
    hide tag_17C5925FD8E5420F96A5D7708A5CD875
    hide shinobu_question_answer_content
    hide shinobu_question_answer_title
    hide shinobu_question_answer_level
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    return

label shinobu_question_content(question):
    call screen shinobu_question_content_screen(question)

    $ renpy.jump(_return)

    return

screen shinobu_question_content_screen(question):
    if "with_image" in question:
        add (question["with_image"]) xpos 0 ypos 0
    text question["content"]:
        style "shinobu_question_screen_text"
    for i, item in enumerate(question["choice"]):
        textbutton item["name"]:
            xpos 70
            ypos 395 + i * 62
            text_style "shinobu_question_screen_text_item"
            action Return(item["target"])

style shinobu_question_screen_text:
    xpos 57
    ypos 217
    size 26
    line_spacing 4
    font "font/zcool-happy-ayumi-extended.ttf"
    color "#000000"
style shinobu_question_screen_text_item:
    size 30
    font "font/zcool-happy-ayumi-extended.ttf"
    color "#187705"
    outlines [(absolute(2), "#FFFFFF", absolute(0), absolute(0))]
    hover_color "#FFFFFF"
    hover_outlines [(absolute(2), "#187705", absolute(0), absolute(0))]

label block_0000388A:
    # Node: 0000388A (Set: 0)
    $ QuestionSet = [
        { "content": _("森海友经常装在书包里带着走\n的道具是？"), "choice": [{"name":_("3DS"),"target":"block_00003896"},{"name":_("科学计算器"),"target":"block_00003896"},{"name":_("电动按摩器"),"target":"block_00003895"}] },
        { "content": _("忍的姓氏是？"), "choice": [{"name":_("逆濑"),"target":"block_00003897"},{"name":_("绫濑"),"target":"block_00003895"},{"name":_("绫部"),"target":"block_00003897"}] },
        { "content": _("赤峰双子的内裤是什么类型的？"), "choice": [{"name":_("传统兜裆布"),"target":"block_00003895"},{"name":_("比基尼"),"target":"block_00003896"},{"name":_("并没穿"),"target":"block_00003897"}] },
        { "content": _("奥村慎太郎家经营着什么店？"), "choice": [{"name":_("澡堂"),"target":"block_00003895"},{"name":_("基佬酒吧"),"target":"block_00003897"},{"name":_("风俗店"),"target":"block_00003897"}] },
        { "content": _("《见习魔法师的任务》中\n主人公的名字是？"), "choice": [{"name":_("旭日"),"target":"block_00003896"},{"name":_("夕阳"),"target":"block_00003895"},{"name":_("朔"),"target":"block_00003896"}] },
        { "content": _("御咲学园的制服内，泳装\n是什么样子的？"), "choice": [{"name":_("四角泳裤"),"target":"block_00003896"},{"name":_("三角泳裤"),"target":"block_00003895"},{"name":_("过膝短裤"),"target":"block_00003896"}] },
        { "content": _("穗海作哉在校舍内养的狗的\n名字是？"), "choice": [{"name":_("小燕"),"target":"block_00003896"},{"name":_("小翼"),"target":"block_00003895"},{"name":_("小忍"),"target":"block_00003897"}] },
        { "content": _("猫山三朗在学校里参加了什么\n社团？"), "choice": [{"name":_("SM同好会"),"target":"block_00003897"},{"name":_("篮球部"),"target":"block_00003895"},{"name":_("男公关部"),"target":"block_00003897"}] },
        { "content": _("一之濑翼的连帽衫是从谁那里\n得到的？"), "choice": [{"name":_("某正太控大叔"),"target":"block_00003896"},{"name":_("森海友"),"target":"block_00003895"},{"name":_("穗海作哉"),"target":"block_00003896"}] },
        { "content": _("世依木守的恋人是？"), "choice": [{"name":_("夕阳"),"target":"block_00003896"},{"name":_("小熊猫"),"target":"block_00003896"},{"name":_("章鱼章鱼星人"),"target":"block_00003895"}] }
    ]
    $ QuestionLevel = 0

    if "_sys_shinobu_question_generate_answer" in globals():
        return QuestionSet

    jump block_0000387B

    return

label block_0000388C:
    # Node: 0000388C (Set: 1)
    $ QuestionSet = [
        { "content": _("奥村慎太郎家里开的店\n叫什么名字？"), "choice": [{"name":_("宝乃汤"),"target":"block_00003896"},{"name":_("花乃汤"),"target":"block_00003895"},{"name":_("淫乃汤"),"target":"block_00003897"}] },
        { "content": _("友和忍住在哪里？"), "choice": [{"name":_("御咲市"),"target":"block_00003897"},{"name":_("宝咲"),"target":"block_00003895"},{"name":_("伊丹咲"),"target":"block_00003897"}] },
        { "content": _("炎之魔法师夕阳最新习得的\n法术名为？"), "choice": [{"name":_("Phantom Fire"),"target":"block_00003895"},{"name":_("Fire Drive"),"target":"block_00003896"},{"name":_("Explosion"),"target":"block_00003896"}] },
        { "content": _("WOLFS所属的朔的内裤种类是？"), "choice": [{"name":_("传统兜裆布"),"target":"block_00003896"},{"name":_("比基尼"),"target":"block_00003896"},{"name":_("并没有穿"),"target":"block_00003895"}] },
        { "content": _("赤峰空最萌哥哥月的什么样子？"), "choice": [{"name":_("戴眼镜的样子"),"target":"block_00003895"},{"name":_("穿剑道服时"),"target":"block_00003896"},{"name":_("全裸的样子"),"target":"block_00003897"}] },
        { "content": _("二班的伊藤是什么社团的经理？"), "choice": [{"name":_("SM同好会"),"target":"block_00003897"},{"name":_("篮球部"),"target":"block_00003896"},{"name":_("田径部"),"target":"block_00003895"}] },
        { "content": _("猫山三朗的生日是？"), "choice": [{"name":_("一月十一日"),"target":"block_00003896"},{"name":_("二月十四日"),"target":"block_00003896"},{"name":_("二月二十二日"),"target":"block_00003895"}] },
        { "content": _("猫山三朗的弟弟四朗有一个\n好朋友，他的名字是？"), "choice": [{"name":_("榊幸绪"),"target":"block_00003896"},{"name":_("榊雪绪"),"target":"block_00003895"},{"name":_("榊由纪绪"),"target":"block_00003896"}] },
        { "content": _("这位老师的名字是？"), "choice": [{"name":_("安西"),"target":"block_00003897"},{"name":_("海"),"target":"block_00003896"},{"name":_("滑子"),"target":"block_00003895"}], "with_image": "rs_image_93EBA4B3E5A54F26BB82EE143EF84A0F" },
        { "content": _("穗海作哉某次不堪其扰在二班\n后门贴了一张纸，内容为？"), "choice": [{"name":_("御咲风俗店"),"target":"block_00003897"},{"name":_("打开后记得关上"),"target":"block_00003895"},{"name":_("关上后记得打开"),"target":"block_00003896"}] }
    ]
    $ QuestionLevel = 1

    if "_sys_shinobu_question_generate_answer" in globals():
        return QuestionSet

    jump block_0000387B

    return

label block_0000388D:
    # Node: 0000388D (Set: 2)
    $ QuestionSet = [
        { "content": _("“御咲”的日文读法是？"), "choice": [{"name":_("GOSAKI"),"target":"block_00003896"},{"name":_("ONSAKI"),"target":"block_00003896"},{"name":_("MISAKI"),"target":"block_00003895"}] },
        { "content": _("朔高价买入的这只\n触手的名字是？"), "choice": [{"name":_("梅菲蒙特"),"target":"block_00003896"},{"name":_("艾森蒙特"),"target":"block_00003895"},{"name":_("鹊"),"target":"block_00003897"}], "with_image": "rs_image_50EB6BEE5CC74D72828F89A01D1A8B61" },
        { "content": _("榊雪绪参加了什么俱乐部？"), "choice": [{"name":_("SM研究俱乐部"),"target":"block_00003897"},{"name":_("远足俱乐部"),"target":"block_00003895"},{"name":_("篮球俱乐部"),"target":"block_00003896"}] },
        { "content": _("上次一班和二班的游泳比赛\n最后赢的是？"), "choice": [{"name":_("一班"),"target":"block_00003896"},{"name":_("二班"),"target":"block_00003896"},{"name":_("平手"),"target":"block_00003895"}] },
        { "content": _("一之濑翼的连帽衫多少钱？"), "choice": [{"name":_("950日元"),"target":"block_00003895"},{"name":_("1500日元"),"target":"block_00003896"},{"name":_("10000"),"target":"block_00003896"}] },
        { "content": _("穗海作哉新年参拜的愿望是？"), "choice": [{"name":_("与一之濑翼和好"),"target":"block_00003896"},{"name":_("干死森海友"),"target":"block_00003896"},{"name":_("希望变成狗"),"target":"block_00003895"}] },
        { "content": _("奥村慎太郎介绍过的某寿司店\n的独特计价系统是？"), "choice": [{"name":_("闻一闻算给钱"),"target":"block_00003896"},{"name":_("脱衣服算给钱"),"target":"block_00003895"},{"name":_("摸一摸算给钱"),"target":"block_00003896"}] },
        { "content": _("森海友在电摩坏掉时作为\n替代会找什么？"), "choice": [{"name":_("绫濑忍"),"target":"block_00003926"},{"name":_("公园的滑梯"),"target":"block_00003895"},{"name":_("花乃汤的进水口"),"target":"block_00003896"}] },
        { "content": _("夕阳和守对什么敌人最不擅长？"), "choice": [{"name":_("火属性"),"target":"block_00003896"},{"name":_("水属性"),"target":"block_00003896"},{"name":_("工口型"),"target":"block_00003895"}] },
        { "content": _("忍开始练习空手道的理由是？"), "choice": [{"name":_("保护重要的人"),"target":"block_00003895"},{"name":_("受漫画影响"),"target":"block_00003895"},{"name":_("打倒WOLFS"),"target":"block_00003896"}] }
    ]
    
    $ QuestionLevel = 2

    if "_sys_shinobu_question_generate_answer" in globals():
        return QuestionSet

    jump block_0000387B

    return

label block_0000387B:
    # Node: 0000387B (Start 1)
    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    if Chapter == 1:
        show rs_image_9BD621E351A14C56AEDB2731A3325E33 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
    elif Chapter == 2:
        show rs_image_D798B398B8514593AA6107349A76BEA1 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
    else:
        show rs_image_52B5BCA8CBE443D4BB4698E2E1D83A45 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那么，测试……{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "开始！"

    window hide

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_59AAF132B57B402BB1B9171904F5D5B2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    if Chapter == 1:
        show rs_image_3F98719CBD9B41E087611F52C3582403 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
        show shinobu_question_background_title (_("关于SCB的十个小知识")) as shinobu_question_background_title zorder 1000 onlayer master
        with rs_effect_59AAF132B57B402BB1B9171904F5D5B2
    elif Chapter == 2:
        show rs_image_81983A1D78754F1D8D21DE2FA8D39EEC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
        show shinobu_question_background_title (_("关于SCB的十个小知识")) as shinobu_question_background_title zorder 1000 onlayer master
        with rs_effect_59AAF132B57B402BB1B9171904F5D5B2
    else:
        show rs_image_81983A1D78754F1D8D21DE2FA8D39EEC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
        show shinobu_question_background_title (_("关于SCB的十个小知识")) as shinobu_question_background_title zorder 1000 onlayer master
        with rs_effect_59AAF132B57B402BB1B9171904F5D5B2

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg"

    if QuestionLevel == 0:
        show shinobu_question_background_level (_("难易度：简单")) as shinobu_question_background_level zorder 1000 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
    elif QuestionLevel == 1:
        show shinobu_question_background_level (_("难易度：中等")) as shinobu_question_background_level zorder 1000 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
    else:
        show shinobu_question_background_level (_("难易度：困难")) as shinobu_question_background_level zorder 1000 onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_00003891

    return

label block_00003891:
    # Node: 00003891 (Update)
    $ CurrentIndex = CurrentIndex + 1
    if CurrentIndex < 10:
        $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
        if Chapter < 2:
            show rs_image_3F98719CBD9B41E087611F52C3582403 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
        else:
            show rs_image_81983A1D78754F1D8D21DE2FA8D39EEC as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    if CurrentIndex < 10:
        call shinobu_question_content(QuestionSet[CurrentIndex]) from _call_shinobu_question_content
    else:
        jump block_0000389B

    return

label block_00003895:
    # Node: 00003895 (對)
    $ CorrectCount = CorrectCount + 1

    if sys_effect_current_file != "sound/Effect Sound/Correct 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Correct 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Correct 1.ogg"

    if Chapter < 2:
        show rs_image_D2B043653E9E43BBB3300DC502B5CD32 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
    else:
        show rs_image_B85A5498D1A24C64A3082FE1A1AEE1D2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "很好，正确。"

    window hide

    jump block_00003891

    return

label block_00003896:
    # Node: 00003896 (錯 1)
    if sys_effect_current_file != "sound/Effect Sound/Wrong 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    if Chapter < 2:
        show rs_image_B6E56AD94AD1447EA91DA630DD1F4DA4 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
    else:
        show rs_image_DADE47E42845480DA1A7E16DE9D5553D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "可惜，错了。"

    window hide

    jump block_00003891

    return

label block_00003897:
    # Node: 00003897 (錯 2)
    if sys_effect_current_file != "sound/Effect Sound/Wrong 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    if Chapter < 2:
        show rs_image_06AAFADDF42C47829EB9CF423F50ADD5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01

    else:
        show rs_image_9438592C13C348829472611A97183D38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你在逗我吗。"

    window hide

    jump block_00003891

    return

label block_00003926:
    # Node: 00003926 (錯 3)
    if sys_effect_current_file != "sound/Effect Sound/Wrong 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    if Chapter < 2:
        show rs_image_06AAFADDF42C47829EB9CF423F50ADD5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01
    else:
        show rs_image_9438592C13C348829472611A97183D38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
        with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不要找我。"

    window hide

    jump block_00003891

    return

label block_0000389B:
    # Node: 0000389B (Finish)
    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "所有问题都已完毕。辛苦了。"

    window hide

    pause 0.5

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_34ED1C93E5674224903A7A34F4DE4738
    hide shinobu_question_background_title
    hide shinobu_question_background_level
    with rs_effect_A964D3CEFC594EDBA25D5CB975CB28E5

    $ set_window("(標準)")
    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 0.7

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([{ "scope": 0, "content": "END == True" },{ "scope": 1, "content": "CorrectCount == 10" }]):
        jump block_00003F3C
    if judge_lm_condition([{ "scope": 0, "content": "END == True" },{ "scope": 1, "content": "CorrectCount > 5" }]):
        jump block_00003F3B
    if judge_lm_condition([{ "scope": 0, "content": "END == True" },{ "scope": 1, "content": "CorrectCount > 0" }]):
        jump block_00003F3A
    if judge_lm_condition([{ "scope": 0, "content": "END == True" }]):
        jump block_00003F39
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 3" },{ "scope": 1, "content": "CorrectCount == 10" }]):
        jump block_000038A8
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 3" },{ "scope": 1, "content": "CorrectCount > 5" }]):
        jump block_000038A9
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 3" },{ "scope": 1, "content": "CorrectCount > 0" }]):
        jump block_000038AA
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 3" }]):
        jump block_000038AB
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 2" },{ "scope": 1, "content": "CorrectCount == 10" }]):
        jump block_000038A3
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 2" },{ "scope": 1, "content": "CorrectCount > 0" }]):
        jump block_000038A1
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 2" },{ "scope": 1, "content": "CorrectCount > 5" }]):
        jump block_000038A2
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 2" }]):
        jump block_000038A0
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 1" },{ "scope": 1, "content": "CorrectCount == 10" }]):
        jump block_0000389E
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 1" },{ "scope": 1, "content": "CorrectCount > 5" }]):
        jump block_0000389D
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 1" },{ "scope": 1, "content": "CorrectCount > 0" }]):
        jump block_0000389F
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 1" }]):
        jump block_0000389C

    return

label block_00003F3C:
    # Node: 00003F3C (10)
    pause 0.3

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_09D0AFA678734FA2930394DBEB002EF7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦！不错嘛友！居然会全对！恭喜了！！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——！哇——！！有什么奖励吗——？？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1AD02FE68F6D4BDAB1AFC4AE07A4FB53 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那种东西就算现在突然想要也……{w}\n不过，努力的事实是不会改变的。"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "乖乖。{nw}"
    show rs_image_FA0792F08F984B9D83A186CB5D20C588 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    extend "（摸摸）{w}\n你很努力了♪"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "汪汪♪"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_000038AF:
    # Node: 000038AF (CLEAR)

    if judge_lm_condition([{ "scope": 0, "content": "CXQShinoQuestion == False" }]):
        jump block_000038AC
    if judge_lm_condition([]):
        jump block_000038AE

    return

label block_000038AC:
    # Node: 000038AC (CXQShinoQuestion)
    $ CXQShinoQuestion = True

    if judge_lm_condition([]):
        jump block_000038AD

    return

label block_000038AD:
    # Node: 000038AD (QUEST FINISH)
    if sys_music2_current_file != "sound/BGM/Quest Finished.ogg":
        play music2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.8


    if judge_lm_condition([]):
        jump block_000038AE

    return

label block_000038AE:
    # Node: 000038AE (終了)
    $ del CurrentIndex
    $ del CorrectCount
    $ del QuestionSet

    return

label block_00003F3B:
    # Node: 00003F3B (6-9)
    pause 0.3

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_09D0AFA678734FA2930394DBEB002EF7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，合格了。比想象中好多了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈哈——！下次就能全对了！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_00003F3A:
    # Node: 00003F3A (1-5)
    pause 0.3

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_356A3FE1B14B49EFAB18B8F38E699BA1 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "该说是和想象中一样还是……{w}\n不管是好的还是坏的意义上，\n你都没能背叛期待呐。"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……我要重来。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_00003F39:
    # Node: 00003F39 (0)
    pause 0.3

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1C184058A2E0497CB599FB0AC5567432 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "吼吼——{w}\n森海——需要调教呐——"

    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好痛痛痛痛——！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_000038A8:
    # Node: 000038A8 (10)
    pause 0.3

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_09D0AFA678734FA2930394DBEB002EF7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦！不错嘛友！居然会全对！恭喜了！！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——！哇——！！有什么奖励吗——？？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1AD02FE68F6D4BDAB1AFC4AE07A4FB53 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那种东西就算现在突然想要也……{w}\n不过，努力的事实是不会改变的。"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "乖乖。{nw}"
    show rs_image_FA0792F08F984B9D83A186CB5D20C588 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    extend "（摸摸）{w}\n你很努力了♪"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "汪汪♪"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_000038A9:
    # Node: 000038A9 (6-9)
    pause 0.3

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_09D0AFA678734FA2930394DBEB002EF7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，合格了。比想象中好多了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈哈——！下次就能全对了！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_000038AA:
    # Node: 000038AA (1-5)
    pause 0.3

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_356A3FE1B14B49EFAB18B8F38E699BA1 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "该说是和想象中一样还是……{w}\n不管是好的还是坏的意义上，\n你都没能背叛期待呐。"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……我要重来。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_000038AB:
    # Node: 000038AB (0)
    pause 0.3

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1C184058A2E0497CB599FB0AC5567432 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "吼吼——{w}\n森海——需要调教呐——"

    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好痛痛痛痛——！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_000038A3:
    # Node: 000038A3 (10)
    pause 0.3

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A43C35FAF6E4488E87E8829D5D8E84E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦！不错嘛友！居然会全对！恭喜了！！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——！哇——！！有什么奖励吗——？？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9133C483CCA9460C804D7FCD561DE619 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那种东西就算现在突然想要也……{w}\n不过，努力的事实是不会改变的。"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "乖乖。{nw}"
    show rs_image_CE498AFB1E3D4DA78B270436EF373DE6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    extend "（摸摸）{w}\n你很努力了♪"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "汪汪♪"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_000038A1:
    # Node: 000038A1 (1-5)
    pause 0.3

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_12E3E3C881C34AC09EF31505C89F7982 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "该说是和想象中一样还是……{w}\n不管是好的还是坏的意义上，\n你都没能背叛期待呐。"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……我要重来。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_000038A2:
    # Node: 000038A2 (6-9)
    pause 0.3

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A43C35FAF6E4488E87E8829D5D8E84E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，合格了。比想象中好多了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈哈——！下次就能全对了！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_000038A0:
    # Node: 000038A0 (0)
    pause 0.3

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F7EF54A04EA54BD787EEA1BA6BA047AF as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "吼吼——{w}\n森海——需要调教呐——"

    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好痛痛痛痛——！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_0000389E:
    # Node: 0000389E (10)
    pause 0.3

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_53AE820BA9E64560B2C6D962DEE9DD33 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦！不错嘛友！居然会全对！恭喜了！！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——！哇——！！有什么奖励吗——？？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DCEACCC9997B48C3B9B0A54DA87D50DC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那种东西就算现在突然想要也……{w}\n不过，努力的事实是不会改变的。"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "乖乖。{nw}"
    show rs_image_A8343F8158BB4E2885E19013FD4B2809 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    extend "（摸摸）{w}\n你很努力了♪"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "汪汪♪"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_0000389D:
    # Node: 0000389D (6-9)
    pause 0.3

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_53AE820BA9E64560B2C6D962DEE9DD33 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，合格了。比想象中好多了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈哈——！下次就能全对了！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_0000389F:
    # Node: 0000389F (1-5)
    pause 0.3

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_718B13A73C1D499B8D43BB96215026E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "该说是和想象中一样还是……{w}\n不管是好的还是坏的意义上，\n你都没能背叛期待呐。"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……我要重来。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_0000389C:
    # Node: 0000389C (0)
    pause 0.3

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CBA8857325074E53AAED9ECA4918832E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "吼吼——{w}\n森海——需要调教呐——"

    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好痛痛痛痛——！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_000038AF

    return

label block_00003881:
    # Node: 00003881 (難易度選択)
    $ sys_lm_menu_item = [{"pos": (90, 128),"image": "images/Games/Shinobus-question-set/Easy.png","hover": "images/Games/Shinobus-question-set/Easy hover.png","name": "かんたん"}, {"pos": (490, 128),"image": "images/Games/Shinobus-question-set/Normal.png","hover": "images/Games/Shinobus-question-set/Normal hover.png","name": "ふつう"}, {"pos": (90, 328),"image": "images/Games/Shinobus-question-set/Hard.png","hover": "images/Games/Shinobus-question-set/Hard hover.png","name": "ちょいむず"}, {"pos": (490, 328),"image": "images/Games/Shinobus-question-set/Return.png","hover": "images/Games/Shinobus-question-set/Return hover.png","name": "やめておく"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - popup.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_329
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"かんたん\"" }]):
        jump block_0000388A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ふつう\"" }]):
        jump block_0000388C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ちょいむず\"" }]):
        jump block_0000388D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"やめておく\"" }]):
        jump block_000038ED

    return

label block_000038ED:
    # Node: 000038ED ()
    $ del CurrentIndex
    $ del CorrectCount
    $ del QuestionSet
    $ del QuestionLevel

    return

