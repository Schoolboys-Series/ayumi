# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000036FA (FLAG: 不可思議！猫狗物語)

label block_000036FB:
    # Node: 000036FB ()

    if judge_lm_condition([]):
        jump block_000036FD

    return

label block_000036FD:
    # Node: 000036FD (Phase: 99)
    if Not(VarExists("C1S4Phase")):
        $ C1S4Phase = 0
    $ C1S4Phase = 99

    if judge_lm_condition([]):
        jump block_00003982

    return

label block_00003982:
    # Node: 00003982 (F4 START)
    call scb_flag_title(1, _("「不可思议！猫狗物语」")) from _call_scb_flag_title_6

    if judge_lm_condition([]):
        jump block_000036FE

    return

label block_000036FE:
    # Node: 000036FE (不可思議！猫狗物語 1)
    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "好了，再来一次，上，小翼！看好，接住！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_4D386A4E85974A939B464A79CF16AD8A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "厉害厉害！好，拿过来～"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪！"

    show rs_image_56ACC260326D4C1F8B7886CBA55E7D69 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "很好很好，做的很棒哦♪"

    show rs_image_6AB5AA5EB92C42B0B217FDBBA0887900 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！"

    if sys_effect2_current_file != "sound/Effect Sound/Class bell 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "灯等灯等～等灯登等……"

    show rs_image_A2F251A0436149BFB4FBD8A984509442 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……啊，午休要结束了。好遗憾哦，小翼。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_378656EE14E64F23B3B990BE2E8D8E2E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪～……"

    show rs_image_4D386A4E85974A939B464A79CF16AD8A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不过，没关系。小翼之后自由做什么都可以哦。{w}\n我接下来两个小时要好好上课哦。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "真是麻烦啊，小学生那会明明能早点下课的。"

    show rs_image_4CBCF132AF8F49E38C726D5800545B50 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_690522DE38524DA3AF9633C07202989E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "真好啊，\n我要是也能像狗一样每天优哉游哉地过就好了呐……"

    show rs_image_54B4D8C7E9C2423FB3142F892982FDD8 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小翼是不是正相反？有没有想过变成人类呢？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！汪！"

    show rs_image_4D386A4E85974A939B464A79CF16AD8A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊哈哈，随便说说的。\n那社团活动结束后再见了哦，拜拜！"

    window hide

    pause 0.4

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    pause 2

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "Zzz……。"

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "怎么办才好，很困扰啊……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……？"

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Nori.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Nori.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Nori.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Grass 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "真是的……买东西要慎重，\n都那么千叮咛万嘱咐了的说。"

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "居然错买了这么贵的东西……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……？？"

    if sys_effect2_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Grass 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "肯定是小时候被双亲惯坏了才会这样的吧。"

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "作为寄人篱下的回报，一定要好好教育教育。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……。"

    window hide

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 1.png
    $ zorder_rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B = -100
    show rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B as rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B zorder zorder_rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B onlayer master
    hide rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.4

    window show

    rs_character_DCC0CCBA406049E6926152DB3A305950 "遥远星球的{color=#00FFFF}朔大人{/color}的双亲，请放心。"

    if sys_effect3_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "我们触手一定会负起责任，把朔大人\n教育成符合他华丽外表的、"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "文武双全的优秀的人的！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "不过话又说起来，这个药的合格实验体怎么找都找不到呢。"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "朔大人说过扔掉，但这个药太危险，\n已经超过这颗星球的科技极限了。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "如、如果被什么人拿到，可就不得了了啊……！"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_DCC0CCBA406049E6926152DB3A305950 "朔大人就会因为擅自拔高这颗星球的科技水准……"

    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "被总部的上司带走，肯定会被做{color=#FF00FF}这～样那～样{/color}的事情的！！"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "至少这个必须想方设法避免……！\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "能触摸朔大人的只有我们！"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "……不过，最近，{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#00FFFF}那个魔法师{/color}的话……\n就睁一只眼闭一只眼好了。"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    stop music fadeout 1
    $ sys_music_current_file = ""

    window hide

    pause 0.7

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_FFC620A1302E417EBD9CB71C6CDE9274

    window show

    rs_character_DCC0CCBA406049E6926152DB3A305950 "说起来真是冒失啊，\n"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_4E9C02BA48374DFEB9605D0C65F0D140 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "这里明明写着“{color=#FF00FF}动物专用{/color}”的说。"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at left_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    show rs_image_1C82CB9D173841FFB02A50833A57F72E as tag_A469B787E7E7466FA1613F380A4CBF41 at right_bottom zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！！"

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    if sys_music_current_file != "sound/BGM/Flurry 1.ogg":
        play music "sound/BGM/Flurry 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 1.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_72C5A5998E7D458CBB88B53B04EB2D23 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "呀！？\n"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "糟、糟了，药要掉了！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    pause 0.4

    rs_character_DCC0CCBA406049E6926152DB3A305950 "接、接的好。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪。"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_1C82CB9D173841FFB02A50833A57F72E as tag_A469B787E7E7466FA1613F380A4CBF41 at right_bottom zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_DCC0CCBA406049E6926152DB3A305950 "哦，好好送回来了呢，训练得不错的狗嘛。"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "不过，突然在别人背后乱叫也确实吓了一跳。\n以后一定要注意啊。"

    show rs_image_378656EE14E64F23B3B990BE2E8D8E2E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪～。"

    show rs_image_77DA094AA72B4CEDA4B70788981CE585 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "当然对着可疑的人叫本来就是看门狗的职责，\n这也无可奈何……"

    show rs_image_4CBCF132AF8F49E38C726D5800545B50 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪、汪。"

    show rs_image_8B87CA8ABDCB4E2A99D0C6B4CB073303 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "你也肯定被吓了一跳。\n不过，关于我是什么这个话题并不是那么重要。"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "所以，现在就先别管了。"

    show rs_image_C2EBA78177DC4C19BB09CDE7382841A8 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……汪。"

    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "说起来，你很聪明啊，好好被调教过了呢。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！"

    stop music fadeout 2
    $ sys_music_current_file = ""

    show rs_image_8B87CA8ABDCB4E2A99D0C6B4CB073303 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "是嘛，很好。\n"
    show rs_image_77DA094AA72B4CEDA4B70788981CE585 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……好像能当做实验体的样子。"

    show rs_image_4CBCF132AF8F49E38C726D5800545B50 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪？"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "呼呼呼，那么就按照朔大人的模式……"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 1.png
    $ zorder_rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B = -100
    show rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B as rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B zorder zorder_rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B onlayer master
    hide rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_7B83AD9CA240425EA3A9E06C0D24BF7B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Nori.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Nori.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Nori.ogg"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "你好呀，元气满满的小狗狗。"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "其实啊，我手上的这瓶药，有不可思议的魔法哦。"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "居然能实现只要是动物谁都想的\n“{color=#00FFFF}那个愿望{/color}”哦……！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……？"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "完全没相信的样子啊，不过也没法责怪。"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "突然被没见过的人说这么莫名其妙的话，能相信才有鬼了。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "不过，试着想想，自打出生开始，\n你见过我这样会说话的不可思议的生物吗？"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "没有？对，怎么可能有。"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "这简直就像，命运的齿轮转动起来的感觉……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……Zz。"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "你这只狗！这里是重点，好好听！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪、汪！"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "呼呼呼，这一切都掌握在你手中。\n是推动这一切，还是甘愿平凡……。"

    window hide

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 0.5

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C2EBA78177DC4C19BB09CDE7382841A8 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_bottom zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_8B87CA8ABDCB4E2A99D0C6B4CB073303 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at left_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "大概这个感觉！"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "……意下如何？\n担心对身体不好？没事没事，请不用担心！"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "我们的地方非常善于开发动物用药。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪……"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "想不想试试！来，想喝下去！\n再怎么说，能实现那个梦想哦！"

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "再也不只是空中楼阁！！\n这一天，将会成为你一生中最重要的一天！！"

    pause 0.3

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_20A8817D51644BE6A7913BD30673F110

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Battle 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 2.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.5

    if sys_music_current_file != "sound/BGM/The end of touch.ogg":
        play music "sound/BGM/The end of touch.ogg" loop
        $ sys_music_current_file = "sound/BGM/The end of touch.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    window show

    pause 0.3

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#80FFFF}― 致喝下这个药的猫猫狗狗，狸猫，或者是狼 ―{/color}"

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#80FFFF}― 欢迎使用我们\nMedicine Research Team of Wolfs\n开发的人类化药！ ―{/color}"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……？"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#80FFFF}― 也许之前已经被其他人解释过了，这个药，{/color}\n"
    if sys_effect_current_file != "sound/Effect Sound/Trumpet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    extend "{color=#80FFFF}将会赋予你所有动物都憧憬着的，成为人类的时间！ ―{/color}"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "人……类……？"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#80FFFF}― 是的！来，试着想像一下，寄出祈愿，凝聚思想…… ―{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#80FFFF}― 当你成为人类后，将会是什么样子的？ ―{/color}"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……人类……{w}成为人类后……我会是……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……既然……\n……所以……"

    window hide

    pause 0.7

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 100
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_13C4DC022C7E4638BB26DDDEB53212F6 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-150, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_D2A450B39A1A4C46BBF15CFA6979230F as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=0, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D6900DA7D3A54445A3A7BAA4FA959F33 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_57F7A3D31244474680A656FBC7957CCF as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=240, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_E0D00426275740F394D32435264217E5 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=320, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_286CAF074B77418F8F63C88FD5379830 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=400, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_BA68039D702C4EA2A6CF95AF1F2E9D2E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=500, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_E60095D58B7244DA80FA5BD8367449C5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1.5

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2.5

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    window show

    pause 0.3

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "（嗯……？我睡着了？）"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "（做了奇怪的梦呢。{w}不过，\n如果那个是真的，就很有趣了呐。）"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "（……那么，该起来了。\n"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    extend "嗯？……欸……？）"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "（总觉得和平时不一样……\n这是……什么。）"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "（啊咧？我的手是这样子的……？\n脚也是，身体也是……）"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "（为什么？这是什么？？\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "嗯？嗯？嗯嗯？？）"

    window hide

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Hit 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}啪嚓！！{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    show rs_image_72C5A5998E7D458CBB88B53B04EB2D23 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at center_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_DCC0CCBA406049E6926152DB3A305950 "好疼……！不、要突然抬头啊。"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Worried 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Worried 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Worried 1.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "诶？这是什么！？你、你是！？{w}\n也、也就是说……刚才的……！！"

    window hide

    pause 0.5

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A5017E40756A40EC8FEE981F51739B02

    pause 0.6

    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    window show

    pause 0.3

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "我真的变成人类了！！！"

    window hide

    pause 0.4

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    window show

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    show rs_image_8B87CA8ABDCB4E2A99D0C6B4CB073303 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at right_bottom zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_DCC0CCBA406049E6926152DB3A305950 "好的，恭喜恭喜！好好实现梦想了呢。"

    show rs_image_7E51C4889A13482ABF50428CFCF6DE20 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哇～！好厉害！只用后足就站起来了～\n和平时看到的东西完全不同～！"

    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "不愧是Wolfs的发明啊，\n能无事成功真是太好了。"

    show rs_image_77DA094AA72B4CEDA4B70788981CE585 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "既然如此，离能控制{color=#00FFFF}那个力量{/color}也就不远了……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_CBD2AF53D136432CA26466E5BD1ED8E7 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "欸～♪哦哦～♪呼～嗯♪"

    show rs_image_8B87CA8ABDCB4E2A99D0C6B4CB073303 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "有没有觉得活动不便的地方？"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "没有！\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，不过，不想穿衣服。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "作哉有时会给我穿上，但活动弄起来太麻烦了，难受。"

    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "哈哈哈，这也是个难解的问题，\n穿衣服是人类社会的规矩。"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "说起来，\n朔大人的不穿了的衣服居然会这么合身，很好很好。"

    show rs_image_98373C4281014E34B4600634ECD299A4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "朔大人？不穿了的？"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "朔大人就是我的主人，与你所言的作哉同样是人类。"

    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哦哦！蚯蚓先生也有主人呐！"

    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5781D9B591E74403B72B332B3EF20A78 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "蚯、蚯蚓……"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D6F0FC275BF4412592C335747B427772 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "真的呐～有不认识的人的气味！\n好香哦，我很喜欢哦！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_8B87CA8ABDCB4E2A99D0C6B4CB073303 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "那当然了。"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "再怎么说我们触手可是夜复一夜地照顾着朔大人，\n用舌头帮他清洁身体呐。"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "用舌头……欸，听起来好好哦！好舒服的样子！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "是你帮我穿的衣服吗？那时候也那样做了吗？"

    show rs_image_72C5A5998E7D458CBB88B53B04EB2D23 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "确实衣服是我帮你穿的，但除此之外就没有了。"

    rs_character_DCC0CCBA406049E6926152DB3A305950 "再怎么说我也不会对素未相识的狗做出那样的事……"

    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯——{w}\n呐呐！我的人类形态如何？合适吗？？"

    if sys_effect3_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DCC0CCBA406049E6926152DB3A305950 "当然，非常可爱、非常阳光。到底是参考的谁的形象？"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嘿嘿，是我的名字的来源哦，是作哉最喜欢的人哦。"

    window hide

    pause 0.7

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 2.5

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 2.png
    $ zorder_rs_image_9363768CD32C4FE78E30EB697E142B70 = -100
    show rs_image_9363768CD32C4FE78E30EB697E142B70 as rs_image_9363768CD32C4FE78E30EB697E142B70 zorder zorder_rs_image_9363768CD32C4FE78E30EB697E142B70 onlayer master
    hide rs_image_9363768CD32C4FE78E30EB697E142B70

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_9363768CD32C4FE78E30EB697E142B70 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.4

    if sys_music_current_file != "sound/BGM/Angel and Demon.ogg":
        play music "sound/BGM/Angel and Demon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Angel and Demon.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那、那个啊～雪绪同学，这到底是怎么回事……？"

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗之前不是说过嘛，为了能让穗海前辈更喜欢，\n{color=#008080}希望能变成狗的属性{/color}。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_CA3E229E97F94C90B2625561A0657321 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "所以，作为朋友，我就来帮你特训了哦。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "噫、噫～是嘛，阿雪真是为朋友着想……"

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯～总觉得不太好。\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    extend "啊，对了，四朗，衣服全脱了。"

    rs_character_7009C1117C004F51829614A203C67DE7 "狗赤身裸体也完全没问题。\n还有，要称呼我{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    extend "{color=#FFFF00}主人{/color}。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "是、是主人，太好了——这下我就能更接近狗……"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_31F2D47C599D46E285A7CD7414520A6F as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.2

    if sys_effect_current_file != "sound/Effect Sound/Hit 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_music_current_file != "sound/BGM/Something strange 1.ogg":
        play music "sound/BGM/Something strange 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something strange 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "你白痴啊！！别这么得意了！谁说要做那种狗了笨蛋！"

    rs_character_7009C1117C004F51829614A203C67DE7 "欸～我在开始训练前只是说了四足着地哦。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这、这个腹黑{color=#FFFF80}狐狸{/color}！一直都在胡闹！\n这次不管怎么说我都不会轻易原谅了！"

    show rs_image_BFEF6FC2749A4B06BF8978A9085171B6 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "啊哈哈～不要那么生气嘛，\n我也是在尽力帮助你了哦。"

    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "完全没感觉到。我说的是更根本的问题！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我确实对阿雪说了比起我这种接近猫的类型，\n穗海前辈更喜欢狗一样的孩子。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我可是为这件事很烦恼的！"

    show rs_image_F7C7F82F340647C1A7BB60DE2B1E06CA as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "可这是事实呀，不得不去做自己不想做的事情也很麻烦哦。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔、唔……你这个……！"

    show rs_image_7C3DD6AA3B724DE9984D6B1A9DC41316 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "啊，不过，在那之前还有更重要的事情要先确定一下。"

    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "什、什么啊。"

    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗总是把喜欢作哉前辈挂在嘴边，那究竟是什么意义的喜欢？"

    show rs_image_D264D770FEE64C5F8D0ED7B023B96089 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……欸？这是什么问题，不是很明白。"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "唔……不对小孩子的四朗君言传身教的话不能理解么？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    rs_character_7009C1117C004F51829614A203C67DE7 "……比如说，这样的事！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "什！？"

    window hide

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 3.png
    $ zorder_rs_image_D704FBCAA179433EB76BAC3007A3C241 = -100
    show rs_image_D704FBCAA179433EB76BAC3007A3C241 as rs_image_D704FBCAA179433EB76BAC3007A3C241 zorder zorder_rs_image_D704FBCAA179433EB76BAC3007A3C241 onlayer master
    hide rs_image_D704FBCAA179433EB76BAC3007A3C241

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_D704FBCAA179433EB76BAC3007A3C241 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    if sys_effect3_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Wind 1.ogg"

    pause 0.4

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "就是问你是不是抱有着这种禁断的感情。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "禁断……感情……？"

    rs_character_7009C1117C004F51829614A203C67DE7 "对，像这样靠近对方，\n"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "想要覆上嘴唇的感觉。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "阿雪说的这个是……下流的事情？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那、那样的话，我没有这个意思。{w}\n那种事情，我还不太明白……"

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯——是吗。那就算了。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯、嗯。"

    window hide

    pause 0.5

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.9

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D264D770FEE64C5F8D0ED7B023B96089 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_F7C7F82F340647C1A7BB60DE2B1E06CA as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.2

    if sys_music_current_file != "sound/BGM/Daily 2.ogg":
        play music "sound/BGM/Daily 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 2.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "既然如此，四朗就像现在这样不需要做什么改变哦。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "啊……正牌的狗来了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "噫！？……{w=0.4}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "一边去！"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "明明怕成这样子还想变成狗，也是挺奇怪的呐。"

    rs_character_7009C1117C004F51829614A203C67DE7 "实际上，至今为止也确实接触过有那种感觉的人没错？"

    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔……啊。\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_BA8F587A9CFC4AC38660F10FCCA9BD0C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "有的！那个人最接近了！"

    show rs_image_F7C7F82F340647C1A7BB60DE2B1E06CA as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "那个人？"

    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯。我之前有一次{color=#008080}潜入{/color}过哥哥在的御咲学园……{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_EF8AEA2163474044BFEB4CDE9AF6E0CF as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_3FE0E66EE0D042CE8856DAB3814A4CC9 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "啊，之前听三朗哥说过了，\n四朗真是笨蛋呐，给别人添了各种麻烦。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不、不用你瞎操心……"

    show rs_image_7C3DD6AA3B724DE9984D6B1A9DC41316 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "作哉前辈养的狗和某人同名，而且前辈只是在说狗的事情。"

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗却一厢情愿地把这些当做了那个人的事。"

    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "先、先说好，这可不是空穴来风，{w}\n穗海前辈和那个人确实感觉有什么不对劲。"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "什么？那个人就是前辈喜欢的像是狗的人？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯……正是如此。那个人正中前辈的好球带……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BA8F587A9CFC4AC38660F10FCCA9BD0C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "正因如此！我现在必须谨慎注意，\n下次要是再遇到，一定要找那个人问个清楚！！"

    show rs_image_F7C7F82F340647C1A7BB60DE2B1E06CA as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯嗯，适当加加油。"

    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔，什么时候这么没热情了。"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "干脆直接找只真正的狗学习不就好了。\n嗯，肯定没错。要不然现在给你带过来？"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "都是什么事啊这只{color=#FFFF80}狐狸{/color}，感觉好不爽！"

    if sys_effect2_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_80C5B8F3D2C94DF68490FC8D313B5A26 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗，今天已经被说了{color=#00FFFF}两次{/color}狐狸了。\n过来，惩罚游戏。"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "诶？什么时候有这个规矩的！\n"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_2A4B517D0134471FA0C8A1E9DD0DA129

    extend "不、不要过来！！"

    window hide

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    window show

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_BFEF6FC2749A4B06BF8978A9085171B6 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗，明天再见哦～"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "呜……再见……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    stop music fadeout 1
    $ sys_music_current_file = ""

    window hide

    pause 0.9

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A4E74E94E7C549809795CEBC732E6326 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.4

    window show

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3B4C660F421B4BE392BB540B580F0339 "榊雪绪，可怕的孩子……"

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不过，关于穗海前辈，确实应该去问一下。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_BA8F587A9CFC4AC38660F10FCCA9BD0C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我绝对不会认输的！给我等着！一之濑翼！！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "在叫我？"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_3B4C660F421B4BE392BB540B580F0339 "呜哇！？翼、翼前辈？"

    show rs_image_CBD2AF53D136432CA26466E5BD1ED8E7 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "果然是在叫我！\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    extend "呐——呐——是什么！是什么！"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "没、没什么……那个。"

    show rs_image_D6F0FC275BF4412592C335747B427772 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯？（闻闻）……{w}我在散步中遇到过你吗？"

    show rs_image_D264D770FEE64C5F8D0ED7B023B96089 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "？？见面就只有之前学园骚动那一次……"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "啊！嗯嗯想起来了！记得是叫四朗！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "那个时候压得我的尾巴好痛！真的吓了一跳呐！"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "尾、尾巴？那、那个、似乎还在为那次添的麻烦生气的样子……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "关于那件事，我对带来的不便非常抱歉……"

    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "在反省就好了！下次要注意哦。\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_7E51C4889A13482ABF50428CFCF6DE20 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，不过，现在也不会有那种事没关系呐！"

    show rs_image_D264D770FEE64C5F8D0ED7B023B96089 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哦、哦……那个，说起来，学校那边没关系吗？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "今天下课比较早？"

    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "学校的话，今天偷偷溜出来了哦！！"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "啊，这是秘密！告诉别人的话我会生气的哦。"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "意、意外的居然是个不良……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_81749C79DF1A40F3BF020F0ACBD64CA8 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "（唔……这个人之前是这样的性格？）"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "（上次见面的时候，应该是那种更加内向的类型才对。\n"
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "头发也是，是茶色来着？）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_98373C4281014E34B4600634ECD299A4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "怎么了吗？我的脸上有什么东西吗？\n"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7E51C4889A13482ABF50428CFCF6DE20 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，难道说，已经变回原来的狗了！？"

    show rs_image_81749C79DF1A40F3BF020F0ACBD64CA8 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "诶？不、不是的，和狗没有关系……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "（好险……感觉问到了什么不该问的东西。{w}\n这次可要好好问清楚他的事了！）"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_98373C4281014E34B4600634ECD299A4 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_BA8F587A9CFC4AC38660F10FCCA9BD0C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "翼前辈！我就直说了，你和穗海作哉前辈是什么关系？"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "作哉？关系？嗯……唔……"

    window hide

    pause 0.4

    stop music fadeout 0.7
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_140B552F50584401971F8DF480089BE0

    if sys_effect_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at right_top zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.5

    show rs_image_8B87CA8ABDCB4E2A99D0C6B4CB073303 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.5

    show rs_image_98373C4281014E34B4600634ECD299A4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A4E74E94E7C549809795CEBC732E6326 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "啊，{color=#FF80FF}主人{/color}！作哉是我的主人哦！"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "主主主主人……！诶？诶？究竟是什么意思？？"

    if sys_effect_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 2.png
    $ zorder_rs_image_9363768CD32C4FE78E30EB697E142B70 = -100
    show rs_image_9363768CD32C4FE78E30EB697E142B70 as rs_image_9363768CD32C4FE78E30EB697E142B70 zorder zorder_rs_image_9363768CD32C4FE78E30EB697E142B70 onlayer master
    hide rs_image_9363768CD32C4FE78E30EB697E142B70

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_B97A3992A1D24282B85B44E0C876F034 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9363768CD32C4FE78E30EB697E142B70 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_2DC336BC0731483296854FF29AE7380E

    rs_character_3B4C660F421B4BE392BB540B580F0339 "难道说，要四肢着地带上项圈……"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不过啊，我还没有到处舔过呐。所以下次想要试试！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "舔、舔！？下次试试！？等、等一下，不是很明白这个意思。"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "也就是说，到底是怎么回事？\n而且那个“到处舔”到底是什么修辞手法？！"

    show rs_image_D6F0FC275BF4412592C335747B427772 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "“舔”嘛……那个……"

    window hide

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_1C6D8B500DD44C7E8BBB20FC805C715A as tag_D0357FA295AF4FCF969F3B43FCFDDE60 at right_top zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.5

    show rs_image_8B87CA8ABDCB4E2A99D0C6B4CB073303 as tag_D0357FA295AF4FCF969F3B43FCFDDE60 zorder zorder_tag_D0357FA295AF4FCF969F3B43FCFDDE60 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.5

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_D0357FA295AF4FCF969F3B43FCFDDE60
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_A4E74E94E7C549809795CEBC732E6326 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯嗯！用舌头清理干净全身上下每一个角落哦！"

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "用上嘴了！！"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "果、果然两位是那种见不得人的关系……？！"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯嗯～？四朗的话不是很明白……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "怎样都好呐！！呐——呐——四朗！和我一起玩！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔……不、不要。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我才不要和既不良又见不得人的人一起玩！"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "欸～不要嘛……真的不和我一起……？"

    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "就是，为什么我要和你这种把前辈带向不纯深渊的人……"

    if sys_effect3_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_CA8BEA043D254D89B51E4C1CDA09F6EB as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "（呜呜）"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔……"

    if sys_effect3_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_E9375A99A07646228F22AAA83DAFE443 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "（失落……）"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "呃……"

    if sys_effect3_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哭……"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔唔！我、我明白了！！会和你玩的！会和你玩的！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不要用那种被遗弃的小狗一般的视线看我！！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "罪恶感太强了……！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "真的吗！会和我玩嘛！？太好了！！哇！！"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯……会的。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_3B4C660F421B4BE392BB540B580F0339 "（越来越觉得和狗一样了。）"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "（算了。今天就当是在翼前辈这里学习如何更像狗一点好了。）"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呐——呐——去什么地方！？会带我去什么地方！？"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "地方……根本就没决定目的地？"

    show rs_image_98373C4281014E34B4600634ECD299A4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "因为啊，这种时候一直都是被作哉在前面拉着项圈，\n我跟在后面而已。"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "果、果然！！"

    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_BA8F587A9CFC4AC38660F10FCCA9BD0C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "你们究竟都在公共场合做些什么！！\n至少衣服还是穿着的对不～？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "我不喜欢那样子，作哉倒是穿着……"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "遇到真变态了！！"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔，我明白了，那我走在前面好了。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不会有项圈的，要好好跟上哦。"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "好——的！！"

    window hide

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.7


    if judge_lm_condition([]):
        jump block_000036FF

    return

label block_000036FF:
    # Node: 000036FF (CP1 Daytime Misaki 四朗)
    call block_00000F72 from _call_block_00000F72

    if judge_lm_condition([]):
        jump block_00003AF8

    return

label block_00003AF8:
    # Node: 00003AF8 (不可思議！猫狗物語 2)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    $ set_window("イベントモード")
    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC1A95BA21694004A67885C809E98CFF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CBD2AF53D136432CA26466E5BD1ED8E7 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "啊！那边的是！！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_3B4C660F421B4BE392BB540B580F0339 "等等，翼前辈！？"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC1A95BA21694004A67885C809E98CFF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.3

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "好呀！！南——！！小林——！！"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_70D99D32788842A0BECD4C69B8A067DB as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_93EB0F0FAC8C472781F52A7E4C7EC343 as tag_063DF7E916A1424E84C7F9FED562D399 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9A978AAD07624C598B6179F23F51FB2D "欸？"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "谁家的孩子？"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "是我哦！小翼哦——！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "以前来公园的时候不是一直在玩嘛！呐！今天也来嘛！！"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_9F0EFB315BA5436EAF7727A13F09D748 as tag_063DF7E916A1424E84C7F9FED562D399 at left_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    show rs_image_892A36737DA046ACB115A2CF21689897 as tag_3C7A06FF4945452D859E685A41EEAAD5 at right_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "那个人是小林酱的熟人吗？"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "不认识——小翼的话，好像是作哉哥的那只狗狗的名字。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_93EB0F0FAC8C472781F52A7E4C7EC343 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "看起来好像和慎哥以及友哥同年。\n也许是提前介绍新朋友来了？！"

    if sys_effect3_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_CE47F8C1330049CB8C7A20A7BB78F4E3 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "肯定是那样！慎哥也说了，\n不能把朋友排除在外，大家一起玩好了！"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_1B56DE6C51F84A58B16A35F4BDE6EB4F as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_B4F534132BA346E0A49EB9D239D96CBF as tag_063DF7E916A1424E84C7F9FED562D399 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_EA79386263E543A88D4DC03B8BD44485 "可以哦——翼哥！和我们一起玩！"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_3B4C660F421B4BE392BB540B580F0339 "作哉哥和慎哥和友哥都是些什么称呼……"

    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那些孩子好像是我们学校低年级的。{w}\n翼前辈认识的人还真是多呐。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_1944E3EA7F5E4E50AD9B4FBF7E801C0B as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_06F95E46248E49DBB867F4E6ED59FF30 as tag_063DF7E916A1424E84C7F9FED562D399 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "好啊！玩什么好呐？今天要做什么呐——？"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_3B4C660F421B4BE392BB540B580F0339 "成熟的……气场……\n"
    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "肯定是我记错了。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "怎么想也不可能是这种样子，\n只是见过一次，记错也是难免的……。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_CE47F8C1330049CB8C7A20A7BB78F4E3 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_B4F534132BA346E0A49EB9D239D96CBF as tag_063DF7E916A1424E84C7F9FED562D399 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_EA79386263E543A88D4DC03B8BD44485 "呼呼，今天呐，我们，要去秘密基地玩哦。"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "谁也不知道的我们秘藏的家园！\n怎么样？翼哥也要一起来吗？？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_1944E3EA7F5E4E50AD9B4FBF7E801C0B as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "特别招待哦！好吗！来不来呐？"

    show rs_image_98373C4281014E34B4600634ECD299A4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "秘密？隐藏？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯嗯！去去！我也要去——！！"

    show rs_image_CE47F8C1330049CB8C7A20A7BB78F4E3 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "嗯嗯！小翼好活跃呐！"

    show rs_image_19666C937C6048BEAFF2DB1422F5FCD6 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "小林酱，这和对作哉哥带来的狗狗说话的样子很像哦。"

    show rs_image_D618D3BE1E0647DFA9DB5C9EDFB81D02 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "啊哈哈♪因为他很像狗狗嘛！"

    show rs_image_1B56DE6C51F84A58B16A35F4BDE6EB4F as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "啊，对了小翼，一起来的那个哥哥是谁？那个人也是朋友？"

    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯，四朗哦！和我一起玩的哦——！\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "四朗！四朗也要玩——！！"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_81749C79DF1A40F3BF020F0ACBD64CA8 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不、我就……人数好像也满了，我去不去都可以……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "就请你们三位去好了。"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "欸——！不要嘛不要嘛！四朗也要一起！\n呐！一起嘛一起嘛！！"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔、唔……不论如何？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不论如何！！"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我、我明白了，去就是了，去就是了。"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "太好了！呐——！四朗也要一起去哦！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_1944E3EA7F5E4E50AD9B4FBF7E801C0B as tag_3C7A06FF4945452D859E685A41EEAAD5 at Transform(xpos=380, yalign=0.0) zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_06F95E46248E49DBB867F4E6ED59FF30 as tag_063DF7E916A1424E84C7F9FED562D399 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_EA79386263E543A88D4DC03B8BD44485 "那四朗也是朋友了！\n"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    extend "请多关照四朗——！"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "四朗请多关照！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "四朗——！请多关照——！四朗——！"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊、好……{w}好累啊，这个情况……"

    window hide

    pause 0.4

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A924E6FB7A0740108CE21D8D0C0FC8D2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哇——！没来过的地方！好厉害！第一次！"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "翼前辈，从来公园开始精神年龄便急速下跌了……{w}\n真有这么高兴……"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_70D99D32788842A0BECD4C69B8A067DB as tag_3C7A06FF4945452D859E685A41EEAAD5 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_9F0EFB315BA5436EAF7727A13F09D748 as tag_063DF7E916A1424E84C7F9FED562D399 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "呐南，四朗的样子看起来\n与之前那个对我们发火的哥哥不是很像吗！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "真的呐！那个时候真的很可怕呐。"

    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯～为什么会被骂？"

    show rs_image_A5CFF67C1798467B9878EF35A72AAA20 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "那个啊，雨刚停的时候，\n{color=#008080}和小林酱一起摇树造雨玩了。{/color}"

    show rs_image_892A36737DA046ACB115A2CF21689897 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "我们没发现那个哥哥已经走到了树下，全身上下完全弄湿了。"

    show rs_image_9F0EFB315BA5436EAF7727A13F09D748 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "头发也被弄乱了，对我们发了很大的火。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_16FB4411E00C461EA9192E3EBAE4AB44 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那、那个……是你们欠考虑，自作自受。"

    show rs_image_93EB0F0FAC8C472781F52A7E4C7EC343 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "{color=#008080}“请求原谅的终极招式”{/color}对那个哥哥也不管用呐，小林酱。"

    show rs_image_70D99D32788842A0BECD4C69B8A067DB as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "是啊。慎哥交给我们的{color=#008080}秘传绝技{/color}。"

    show rs_image_D264D770FEE64C5F8D0ED7B023B96089 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "招、招式？秘传……？那是要怎么做？"

    show rs_image_CFFC52EE826648E39315AEBC12B90057 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "那个啊～像这样……"

    show rs_image_CA24BBA93D6B4C3EAA40A5F62BDE4EAF as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "然后再这样……"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    rs_character_244536AD39AF4697B223756F943650AA "{size=28}{color=#FF80FF}我们会用身体赔偿的，请原谅我们。{/color}{/size}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_85AFF466AB2E4A76A0B497A934153327 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "！！？"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_D618D3BE1E0647DFA9DB5C9EDFB81D02 as tag_3C7A06FF4945452D859E685A41EEAAD5 at Transform(xpos=380, yalign=0.0) zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_19666C937C6048BEAFF2DB1422F5FCD6 as tag_063DF7E916A1424E84C7F9FED562D399 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "这样做就可以了！！"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "四朗下次也试试？"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我、我就算了……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "请～原～谅～我～"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那边，别起哄。"

    window hide

    pause 0.4

    stop music fadeout 2
    $ sys_music_current_file = ""

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    if sys_effect3_current_file != "sound/Effect Sound/Wave 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Wave 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.6

    show rs_image_7639E4BE73E34BBD9D978953E896CF0C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 1

    window show

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_7E51C4889A13482ABF50428CFCF6DE20 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哇……好厉害……"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸！原来还有这样的地方。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_D618D3BE1E0647DFA9DB5C9EDFB81D02 as tag_3C7A06FF4945452D859E685A41EEAAD5 at right_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_19666C937C6048BEAFF2DB1422F5FCD6 as tag_063DF7E916A1424E84C7F9FED562D399 at left_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "很漂亮的！谁也不知道的我们秘密的基地哦！"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "我们也是最近才找到的哦！"

    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_F31BFD9162C64D929725A6AF4C2C2823 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_98373C4281014E34B4600634ECD299A4 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "我从出生以来，还从没到过这样的地方……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我也是哦。\n像这种美丽的湖泊坐落在群山中间一样的地方。"

    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "下次想和作哉一起来呐。"

    show rs_image_E0D2132CD8F74B5CB3274596C13F9EA2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "穗海前辈会为这种事情感动的么？"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "一定会的。作哉的话，一定会很喜欢的。"

    show rs_image_5C9C69F3A63F44E0B71087CC0D54D58E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……翼前辈这么说的话，一定就是那样了。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_1944E3EA7F5E4E50AD9B4FBF7E801C0B as tag_3C7A06FF4945452D859E685A41EEAAD5 at right_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_06F95E46248E49DBB867F4E6ED59FF30 as tag_063DF7E916A1424E84C7F9FED562D399 at left_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_EA79386263E543A88D4DC03B8BD44485 "快来——你们！在那里站着做什么呐！"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "一起来游泳？"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_CBD2AF53D136432CA26466E5BD1ED8E7 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸、欸欸！？突然这么说，又没带泳衣……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不错嘛不错嘛！我也要去！！\n呐——呐——四朗！不来一起玩吗？"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "明白了明白了，请走好。小心别受伤哦。"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯！明白！！\n"
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我来了——小林！南！我也要——！{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend ""

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不过大家都没带泳衣啊……"

    window hide

    pause 0.5

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 4.png
    $ zorder_rs_image_5E80ED9C3E1F4920A274B420F13A4D82 = -100
    show rs_image_5E80ED9C3E1F4920A274B420F13A4D82 as rs_image_5E80ED9C3E1F4920A274B420F13A4D82 zorder zorder_rs_image_5E80ED9C3E1F4920A274B420F13A4D82 onlayer master
    hide rs_image_5E80ED9C3E1F4920A274B420F13A4D82

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_5E80ED9C3E1F4920A274B420F13A4D82 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.8

    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    window show

    rs_character_EA79386263E543A88D4DC03B8BD44485 "耶！！"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "呀♪"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哇哇！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，是这样……真是元气十足呢。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "四朗——！水里很好玩哦！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯！那就好～我在看哦 ^-^"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "小翼的那个，好大啊——\n不愧比我们年长了那么多呐——！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "是吗？不是很明白。"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "很大哦——！看！和我比一下！"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "我的大概这个样子哦！\n成为中学生后也能那么大就好了呐～"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯～！大家都不一样呐～！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "又在说什么不着边际的话……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呐！四朗的怎么样呢？"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不用你管。"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_29AFB5C1FADA4FAD837A530C0E0638A7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呼————！哈～！好开心呐！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔哇，水都……"
    show rs_image_E0D2132CD8F74B5CB3274596C13F9EA2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "能玩得这么开心真是太好了，那差不多……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_1944E3EA7F5E4E50AD9B4FBF7E801C0B as tag_3C7A06FF4945452D859E685A41EEAAD5 at right_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_06F95E46248E49DBB867F4E6ED59FF30 as tag_063DF7E916A1424E84C7F9FED562D399 at left_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_EA79386263E543A88D4DC03B8BD44485 "小翼！然后是那个了！"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "还有更好玩的事情哦！"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_1944E3EA7F5E4E50AD9B4FBF7E801C0B as tag_3C7A06FF4945452D859E685A41EEAAD5 at Transform(xpos=380, yalign=0.0) zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_06F95E46248E49DBB867F4E6ED59FF30 as tag_063DF7E916A1424E84C7F9FED562D399 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "真的吗！哇——！要去要去～！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.3

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "什、什么东西……\n"
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BA8F587A9CFC4AC38660F10FCCA9BD0C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_7E51C4889A13482ABF50428CFCF6DE20 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，翼前辈！等等！"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "欸～！怎么了嘛，人家想去玩嘛。"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "好好，会让你去的。但在这之前，稍微镇定一下比较好。"

    show rs_image_98373C4281014E34B4600634ECD299A4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "我做错了什么吗？好奇怪哦，\n明明已经和蚯蚓先生好好学习了的。"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那个蚯蚓先生又是谁……{w}\n请振作一点，今年都多大了？"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "按人类来算的话13岁哦！"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "正是，即便如此却和低年级的孩子一样疯……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不过其实只有十个月哦！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "请不要说胡话了。"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_D618D3BE1E0647DFA9DB5C9EDFB81D02 as tag_3C7A06FF4945452D859E685A41EEAAD5 at right_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_19666C937C6048BEAFF2DB1422F5FCD6 as tag_063DF7E916A1424E84C7F9FED562D399 at left_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_EA79386263E543A88D4DC03B8BD44485 "小翼——！四朗——！快点来——！"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "四朗快点快点！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "等、等等。{w}阻止别人还挺难的。"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……算了。那，为什么我也要去。"

    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不去了吗？"

    show rs_image_E0D2132CD8F74B5CB3274596C13F9EA2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……唉，好好，去的去的。"

    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "太好了！小林——！南——！！{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend ""

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "真是的……穗海前辈会被那种头晕目眩的感觉吸引么。"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那就是所谓的像狗一样？\n"
    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "唔，既然如此，我到底能不能学得过来啊……"

    window hide

    pause 0.6

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.2

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_ACE4367C64D24E8C8419DD6CD977E048 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊咧？两人去什么地方了？"

    show rs_image_D6F0FC275BF4412592C335747B427772 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "（闻闻）……嗯？\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_CBD2AF53D136432CA26466E5BD1ED8E7 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哇好厉害！在那么高的地方！！"

    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸？"

    window hide

    pause 0.7

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_75BF283275354957BD957E49079F3659 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.7

    if sys_music_current_file != "sound/BGM/To the future.ogg":
        play music "sound/BGM/To the future.ogg" loop
        $ sys_music_current_file = "sound/BGM/To the future.ogg"

    window show

    rs_character_EA79386263E543A88D4DC03B8BD44485 "哦～这边这边～！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "呃！？两、两人在做什么呢！\n很危险的！很可怕的！"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "没关系没关系！你们也快点上来～！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "上去……要爬那种不安全的东西……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "真好真好！我也要上去！"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "过来，小翼！赶快过来，总之就是很厉害哦！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "真的吗！？我要去！"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "那么，狗狗究竟会不会爬树呐～"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "小林酱完全把对方当成那个小翼了呐。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "唔，当然可以！现在我也不是狗了！\n"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "唔……唔……"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "啊哇哇！？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "翼、翼前辈！不要太勉强比较好！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "很危险的！果然狗上树是不可能的……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "唔……嗯！好痛……"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "加油哦，小翼哥——！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯！唔…………"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    extend "嗯！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_2BA31D3B2AD440D998A205D1812EF75A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "做到了哦！上来了！第一次爬到树顶哦！"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "那当然，会爬树的狗狗可从没听说过呐。"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "所以说不是那个小翼啦。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哇……好——高……！{w}而且…………\n{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    extend "四朗——！四朗也快点上来！！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不、不了，我就算了……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "四朗也要上来！！四朗，来嘛！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这、这么想？……好，真是的。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不过以前也没爬过树呢。\n"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    extend "嗯……{w=0.4}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "唔，意外这么简单？"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "说起来，我家养的猫，经常在树上午睡呐～"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "欸～！也就是说比起狗狗还是猫猫更擅长做这个了呐！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "四朗好厉害，比我还要擅长呐！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    rs_character_3B4C660F421B4BE392BB540B580F0339 "好了！"

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 5-3.png
    $ zorder_rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B = -100
    show rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B as rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B zorder zorder_rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B onlayer master
    hide rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_C7F946EF0FB14A6A9ED6F7A9D18C5E2B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哦哦，很不错嘛。爬到树顶的话，连远处的街道都能看清呐！"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "视野很宽阔的地方哦！"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "这里真的是只有我们的秘密基地哦！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "是呢，这种好地方不是那么简单就能发现的呐。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呐，四朗！来这里是不是很高兴！？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这都是拜南君和小林君，以及翼前辈邀请的福。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "会表扬我吗？会摸摸我吗？？呐——呐——摸一下嘛？？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "真是的，爱撒娇的孩子呐。……乖乖。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "太好了——！被四朗摸摸了——！哇——哇——！"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "啊哈哈！简直就像饲主的宠物一样呐～！"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "明明小翼哥更年长的～啊，不过，和年龄无关的，\n我家的猫猫，按人类来说已经超过20了。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "我能来这里真是太好了，确实是不是现在就做不到的事呐。\n和作哉一起的时候不会来这里的……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯？什么意思？翼前辈。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯嗯，没什么！我绝对不会忘记现在看到的一切的！"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "呐，南，听说狗狗的记忆只能保持五分钟哦！"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "欸～是这样吗！我家的猫猫不知道会不会呐。"

    window hide

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_367D6887C01741AFA0312C70A109F138

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_FB8046DBE16F4BA8BE96613E8F3A850C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    window show

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_1B56DE6C51F84A58B16A35F4BDE6EB4F as tag_3C7A06FF4945452D859E685A41EEAAD5 at right_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_B4F534132BA346E0A49EB9D239D96CBF as tag_063DF7E916A1424E84C7F9FED562D399 at left_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"

    pause 0.3

    rs_character_9A978AAD07624C598B6179F23F51FB2D "在秘密基地玩了好久呐。"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "是啊，比平时晚了好多。\n慎哥他们说不定已经在公园等着了呐。"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_E9375A99A07646228F22AAA83DAFE443 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……"

    show rs_image_D264D770FEE64C5F8D0ED7B023B96089 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "翼前辈，从刚才开始就一直心神不宁的样子，发生什么了？"

    show rs_image_CA8BEA043D254D89B51E4C1CDA09F6EB as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "四朗……那个啊，手指里……看。"

    show rs_image_E0D2132CD8F74B5CB3274596C13F9EA2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯？有一根木刺呢，刚才爬树的时候不小心的？"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯，也许。怎么办四朗，有点疼～"

    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "很在意？"

    show rs_image_CA8BEA043D254D89B51E4C1CDA09F6EB as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯！很在意很在意，刚才也试着咬过了！{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "（咬咬）……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不、不能那么不卫生的！"

    show rs_image_81749C79DF1A40F3BF020F0ACBD64CA8 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯～……既然如此，这里离我家很近，回家拔出来如何？"

    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "能拔出来？\n"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯！去去！一气拔出来！"

    show rs_image_356ECD8406BB49698A4D9CAD3C494C73 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我明白了。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_1B56DE6C51F84A58B16A35F4BDE6EB4F as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_B4F534132BA346E0A49EB9D239D96CBF as tag_063DF7E916A1424E84C7F9FED562D399 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    show rs_image_356ECD8406BB49698A4D9CAD3C494C73 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_3B4C660F421B4BE392BB540B580F0339 "综上所述，南君，小林君，我们就要在这里说再见了。"

    show rs_image_93EB0F0FAC8C472781F52A7E4C7EC343 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "欸～是吗？"

    show rs_image_892A36737DA046ACB115A2CF21689897 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "本来还以为人数多一些会更好玩的。"

    show rs_image_E0D2132CD8F74B5CB3274596C13F9EA2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那个下次再说。\n今天谢谢了！真的很高兴哦！对不对，翼前辈。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯，很高兴哦！下次也要一起玩！！"

    show rs_image_B4F534132BA346E0A49EB9D239D96CBF as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "可以哦～下次再见！"

    show rs_image_CE47F8C1330049CB8C7A20A7BB78F4E3 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "小翼，四朗！再见～！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_F31BFD9162C64D929725A6AF4C2C2823 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那么我们也该走了，翼前辈。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯！\n"
    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不过，请温柔一点哦，不喜欢痛的感觉。"

    show rs_image_5C9C69F3A63F44E0B71087CC0D54D58E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "说不准呢～这个没法保证哦～"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "翼前辈还是做好会有一点痛的心理准备比较好……"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E9375A99A07646228F22AAA83DAFE443 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "欸～不要不要！我不要～！"

    show rs_image_356ECD8406BB49698A4D9CAD3C494C73 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哈哈，没关系的。\n我之前有过{color=#008080}经验{/color}，还没有痛到不能忍受。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_6CC10C417C204D238757DC7C1935E6AE as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "翼前辈的话一定可以的。"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 1.3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_BAA43B4F4198492BA4DCD8836A92877B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 200
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 200
    show rs_image_1B56DE6C51F84A58B16A35F4BDE6EB4F as tag_3C7A06FF4945452D859E685A41EEAAD5 at right_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_B4F534132BA346E0A49EB9D239D96CBF as tag_063DF7E916A1424E84C7F9FED562D399 at left_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.3

    rs_character_EA79386263E543A88D4DC03B8BD44485 "呐，南，知道“拔出来”的意思吗？"

    show rs_image_93EB0F0FAC8C472781F52A7E4C7EC343 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "嗯嗯，不知道哦。四朗和小翼哥要做的事很特别吗？"

    show rs_image_CE47F8C1330049CB8C7A20A7BB78F4E3 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "“拔出来”的意思啊，\n"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_01E90DC92D8B489EAC15D4031843E16E = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CE47F8C1330049CB8C7A20A7BB78F4E3 as tag_01E90DC92D8B489EAC15D4031843E16E at center_top zorder zorder_tag_01E90DC92D8B489EAC15D4031843E16E onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "就是说对对方的那个地方，这样做！"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_9F0EFB315BA5436EAF7727A13F09D748 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_9A978AAD07624C598B6179F23F51FB2D "呀！小、小林酱！？不要摸……！"

    show rs_image_CFFC52EE826648E39315AEBC12B90057 as tag_01E90DC92D8B489EAC15D4031843E16E zorder zorder_tag_01E90DC92D8B489EAC15D4031843E16E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "就是要这样触摸对方哦！"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "等，啊，不、不要～！\n"
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 200
    show rs_image_1B56DE6C51F84A58B16A35F4BDE6EB4F as tag_3C7A06FF4945452D859E685A41EEAAD5 at right_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_A5CFF67C1798467B9878EF35A72AAA20 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_01E90DC92D8B489EAC15D4031843E16E
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    extend "……就是说，他们有H的关系？"

    show rs_image_CE47F8C1330049CB8C7A20A7BB78F4E3 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "就是这样！肯定现在在偷偷地{color=#FF80FF}进进出出{/color}哦！"

    show rs_image_9F0EFB315BA5436EAF7727A13F09D748 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "欸～不过我还不清楚那种事情。"

    show rs_image_1B56DE6C51F84A58B16A35F4BDE6EB4F as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "南还是小孩子呐。\n"
    show rs_image_892A36737DA046ACB115A2CF21689897 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "既然……{w=0.45}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_90C33C4E77BE496D953347A7B8685B56 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "下次、就由我来好教教你好了？"

    show rs_image_93EB0F0FAC8C472781F52A7E4C7EC343 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "欸，小林酱？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "因、因为南是小孩子！作为大人我必须要好好照顾才行！"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_D6C9CA40975A4596A09158FDAFC5E489 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "谢谢小林酱！\n{w=0.4}说得对呐！我们从幼稚园开始就做了以后要结婚的约定呐！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "嗯！因为我们要结婚所以那种H的事情也可以做的！"

    show rs_image_892A36737DA046ACB115A2CF21689897 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "所以，等成为大人后{w=0.4}……要一起哦。"

    show rs_image_B4F534132BA346E0A49EB9D239D96CBF as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "嗯！请温柔一些哦，小林酱。"

    show rs_image_CE47F8C1330049CB8C7A20A7BB78F4E3 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "哈哈！\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_70D99D32788842A0BECD4C69B8A067DB as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……啊，果然慎哥已经在公园了！"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 300
    show rs_image_D618D3BE1E0647DFA9DB5C9EDFB81D02 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_19666C937C6048BEAFF2DB1422F5FCD6 as tag_063DF7E916A1424E84C7F9FED562D399 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_EA79386263E543A88D4DC03B8BD44485 "慎哥！友哥！\n"
    show rs_image_70D99D32788842A0BECD4C69B8A067DB as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_93EB0F0FAC8C472781F52A7E4C7EC343 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……啊，这是……？"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_FD97A7AC280A4AA68D0BEDD058C5C756 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好～呀，小林酱，南酱～！"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天我们带来了新的朋友哦～！"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_225A15956FFB4AC2B4A3ACD0192F135D as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "请、请多多关照……我的名字是……"

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    rs_character_244536AD39AF4697B223756F943650AA "{size=28}小翼！？{/size}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸？？"

    rs_character_C49E8447151A496692350FA6779E4154 "欸？？"

    window hide

    pause 0.6

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 2.5


    if judge_lm_condition([]):
        jump block_00003AF7

    return

label block_00003AF7:
    # Node: 00003AF7 (不可思議！猫狗物語 3)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6C26F2E8F0C540C5B3E93C676156A020 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.5

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_F31BFD9162C64D929725A6AF4C2C2823 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.3

    rs_character_3B4C660F421B4BE392BB540B580F0339 "好了，安全拔出来了。"

    show rs_image_5C9C69F3A63F44E0B71087CC0D54D58E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这可已经很温柔了哦。{w}我的那个时候，\n被阿雪强行按在地上，真的很痛呐。"

    show rs_image_356ECD8406BB49698A4D9CAD3C494C73 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，对了，要不要喝点什么，有什么想喝的吗？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不过也只有水和……\n"
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "翼前辈？"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……？嗯？"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_D6F0FC275BF4412592C335747B427772 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……居、居然睡着了……"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_3B4C660F421B4BE392BB540B580F0339 "刚才一直那么闹，突然安静下来反倒不适应了。"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "翼前辈，翼前辈。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_8A9FD25CF2224DA4B5F560425D3A98A7 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "啊嚏！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "看～在这种地方睡觉不好。真是的，又不是狗……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哦，是不是在湖里游了很长时间的泳身体发冷？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "感冒了也不好，怎么做？要洗个澡吗？"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "唔～嗯……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "翼前辈，洗澡！身体会冷下来的。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E9375A99A07646228F22AAA83DAFE443 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "好累啊～四朗——抱抱～"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哈、啊？自己走。"

    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不要嘛～抱抱～"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这个人真是……\n看！像这样用点力就能站……"
    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，呜哇！？"

    pause 0.5

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呼呼～骑在四朗上面了～"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "翼、翼前辈，很重的。起来，快起来……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "四朗——"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯？"

    pause 0.7

    window hide

    if sys_music_current_file != "sound/BGM/Guitar 2.ogg":
        play music "sound/BGM/Guitar 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Guitar 2.ogg"

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 6.png
    $ zorder_rs_image_A222B7CC30A245E0AB1F1A5B1FC13CC5 = -100
    show rs_image_A222B7CC30A245E0AB1F1A5B1FC13CC5 as rs_image_A222B7CC30A245E0AB1F1A5B1FC13CC5 zorder zorder_rs_image_A222B7CC30A245E0AB1F1A5B1FC13CC5 onlayer master
    hide rs_image_A222B7CC30A245E0AB1F1A5B1FC13CC5

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_A222B7CC30A245E0AB1F1A5B1FC13CC5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 1

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……哇！？做、做什么呢！？"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呼呼～♪"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "等……快停下！不、不要舔我！翼前辈！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "为什么～？为什么不行呢～？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那、那是要和喜欢的人做的！我、我对翼前辈没有……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "再说了，你不是对穗海前辈……对穗海前辈……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "穗——海……作哉？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "…………对啊，不说一声的话！\n"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    extend "……不过在那之前先起来……！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不～要。四朗上面很舒服，我喜欢这样的感觉～"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不、不要！都说了这只能和喜欢的人做！\n翼前辈是喜欢穗海前辈的对不对？"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "嗯，最喜欢了！四朗也最喜欢了！最喜欢四朗了！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "{size=28}PERO{/size}{w=0.3}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "{size=28}PERO{/size}{w=0.3}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "{size=28}PERO{/size}"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哇，都说了住手！{w}\n怎、怎么回事？喜欢我、喜欢前辈？……欸？"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "四朗和作哉都是一直在一起的人！\n一直一起玩的人！所以最喜欢了！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "这只是作为治好手的还礼，为什么这么不愿意呐～？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸……还礼？{w}也就是说对前辈其实并不是那种意义上的喜欢？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "可、可是，都说了像主人这样奇怪的话……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呐——四朗，要去洗澡吗～？好想变得暖和起来哦——"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，嗯，是有这么回事……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "算了，至于翼前辈究竟是狗还是什么，很快就能明白了……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "真正的狗我很棘手呢。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "诶？四朗讨厌狗？？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "有、有点……不论如何见到后都会下意识地逃走。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……{w=0.5}这样……{w=0.5}{size=12}……原来……{/size}"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那要走了哦，请快点起来。"

    if sys_effect3_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……抱抱！"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……"

    window hide

    pause 0.5

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    window show

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_EFC6CF450D5044388FF4E349B9961DFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哈！好重……！！"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "四朗——谢谢！接下来一起去洗澡！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_356ECD8406BB49698A4D9CAD3C494C73 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯，请慢用——那么我就暂且离开了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "一起！一起！"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……好好，毕竟是狗嘛……狗也没法单独洗澡……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "说起来，狗不怕水呢。{w}\n算了……顺便，我的脸上也确实黏黏糊糊的。"

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    window hide

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    pause 1.5

    if sys_effect3_current_file != "sound/Effect Sound/Bathroom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Bathroom 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Bathroom 1.ogg"

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 7.png
    $ zorder_rs_image_BB4914B9F99F4B449F1BD45034C67186 = -100
    show rs_image_BB4914B9F99F4B449F1BD45034C67186 as rs_image_BB4914B9F99F4B449F1BD45034C67186 zorder zorder_rs_image_BB4914B9F99F4B449F1BD45034C67186 onlayer master
    hide rs_image_BB4914B9F99F4B449F1BD45034C67186

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_32BAA0EDDD3E4985B818E253A624C758 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_BB4914B9F99F4B449F1BD45034C67186 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222BBB56F7BA4025B3E942F40786CBC9

    if sys_music_current_file != "sound/BGM/Guitar 1.ogg":
        play music "sound/BGM/Guitar 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Guitar 1.ogg"

    pause 0.4

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 7.png
    $ zorder_rs_image_BB4914B9F99F4B449F1BD45034C67186 = -100
    show rs_image_BB4914B9F99F4B449F1BD45034C67186 as rs_image_BB4914B9F99F4B449F1BD45034C67186 zorder zorder_rs_image_BB4914B9F99F4B449F1BD45034C67186 onlayer master
    hide rs_image_BB4914B9F99F4B449F1BD45034C67186

    show rs_image_C7CD9B9BF390409D921A574173433704 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.5

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "唔！四朗，好痒哦～"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "好了，不要动，泡沫还没冲干净。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不要～那里不行～"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那就自己洗，真是的……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呼呼……四朗，今天真的很开心呐。谢谢你一直陪我玩。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，没关系，我才是获得了不少珍贵的体验。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "谢谢你来邀请我。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "四朗也很开心？太好了～"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……{w}……四朗——洗完澡后，我……就要回去了。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我明白了。{w}那个……虽然这么说有些失礼。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "能一个人回去吗？没关系？"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "没关系哦。都是偶尔自己一个人散步时经过很多次的街道了。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "是吗，那就好……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "不过，要和四朗说再见了。{w}\n……感觉心里不太舒服。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哈哈，下次再见的时候可能的话我还会陪你玩的。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……{w}……嗯……{w}……啊。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "怎么了？"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呐，四朗，刚才眼睛进水了。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "为、为什么选这个时候……？才刚刚开始冲的说。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "啊，又进去了。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……？？"

    pause 0.2

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.3

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……人类的身体{w=0.5}……{size=14}真是奇妙呢。{/size}"

    pause 0.8

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    stop music fadeout 3
    $ sys_music_current_file = ""

    window hide

    pause 5

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_752FA16B677941C5A9A2623B79A40F24 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_F31BFD9162C64D929725A6AF4C2C2823 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_3FE0E66EE0D042CE8856DAB3814A4CC9 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.3

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "今天约好和穗海前辈一起回去了，阿雪也一起好了！"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "三朗哥也会来哦。四朗，不要老无视自己的哥哥了～"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_F31BFD9162C64D929725A6AF4C2C2823 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_7009C1117C004F51829614A203C67DE7 "欸～也就是说和翼前辈关系很好了呐。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "真的，快累死了。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那根本不是什么像狗，那就是活生生的狗。\n至少我最后那一段是真心这么想的。"

    show rs_image_7C3DD6AA3B724DE9984D6B1A9DC41316 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "啊哈哈，好像是很有意思的人呐。"

    show rs_image_E0D2132CD8F74B5CB3274596C13F9EA2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "嗯嗯，说起来，中途去了公园那边那座山哦。"

    show rs_image_356ECD8406BB49698A4D9CAD3C494C73 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "然后啊，最里面……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_BFEF6FC2749A4B06BF8978A9085171B6 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯，那里有个很漂亮的湖泊。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸！？你知道？"

    show rs_image_31F2D47C599D46E285A7CD7414520A6F as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "当然了哦～我可是很喜欢探险的，所以才要加入远足部嘛～"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔唔……可、可是，你至少没爬过那上面的树对不对？"

    show rs_image_3FE0E66EE0D042CE8856DAB3814A4CC9 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯，确实。"

    show rs_image_5C9C69F3A63F44E0B71087CC0D54D58E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哈哈。那就算了！再怎么说也是我们的秘密嘛♪"

    show rs_image_99C5410C32FF4E188D0338F65716E386 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "……总觉得很火大。先说好，狐狸也是能爬树的。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_59434F19656445578114DA38D9F0C893 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哇！终于有自知之明了呐！呀，狐狸狐狸小狐狸！"

    show rs_image_80C5B8F3D2C94DF68490FC8D313B5A26 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "……"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……啊。"

    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window hide

    pause 1.4

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3B4C660F421B4BE392BB540B580F0339 "榊雪绪……恐怖的孩子……"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_8540C7DB25BA424CAE3F5349B0307CCC as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_7009C1117C004F51829614A203C67DE7 "自作自受。"
    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那么，在穗海前辈和三朗哥来之前，\n找个地方打发时间好了。"

    window hide

    pause 0.4

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.8


    if judge_lm_condition([]):
        jump block_00003AF6

    return

label block_00003AF6:
    # Node: 00003AF6 (CP1 Daytime 四朗)
    call block_00000F41 from _call_block_00000F41

    if judge_lm_condition([]):
        jump block_00003AF9

    return

label block_00003AF9:
    # Node: 00003AF9 (不可思議！猫狗物語 4)
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    stop music fadeout 3
    $ sys_music_current_file = ""

    $ set_window("イベントモード")
    pause 1

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_3FE0E66EE0D042CE8856DAB3814A4CC9 as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯？什么声音？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "从草丛里面传来的。\n"
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……那是……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_378656EE14E64F23B3B990BE2E8D8E2E as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_BFEF6FC2749A4B06BF8978A9085171B6 as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7009C1117C004F51829614A203C67DE7 "哇！好可爱的小狗！"

    show rs_image_31F2D47C599D46E285A7CD7414520A6F as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗，不妙了哦，是狗哦是狗哦～看，好可怕哦～"

    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……是前辈养的狗……"

    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "啊？没像平时一样害怕？\n"
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_378656EE14E64F23B3B990BE2E8D8E2E as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    extend "……倒不如说那边倒有些胆怯的样子……"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……小翼……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_7C3DD6AA3B724DE9984D6B1A9DC41316 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "乖乖，到这边来，没关系哦，完全不用害怕哦。"

    show rs_image_4CBCF132AF8F49E38C726D5800545B50 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……"

    show rs_image_F7C7F82F340647C1A7BB60DE2B1E06CA as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "看啊～好像是在顾虑四朗的样子。难道它明白你害怕狗？"

    stop effect3 fadeout 2
    $ sys_effect3_current_file = ""

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……！"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window hide

    pause 1.5

    if sys_effect3_current_file != "sound/Effect Sound/Worried 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Worried 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Worried 1.ogg"

    pause 0.5

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……过来吧。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "没、没关系的。我、我不会讨厌你的。{w}不用那么害怕……"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "……"
    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……汪！"

    window hide

    pause 0.8

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 8.png
    $ zorder_rs_image_A438304BAD244787B1FCBDEB053ED1B2 = -100
    show rs_image_A438304BAD244787B1FCBDEB053ED1B2 as rs_image_A438304BAD244787B1FCBDEB053ED1B2 zorder zorder_rs_image_A438304BAD244787B1FCBDEB053ED1B2 onlayer master
    hide rs_image_A438304BAD244787B1FCBDEB053ED1B2

    show rs_image_A438304BAD244787B1FCBDEB053ED1B2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 0.5

    window show

    if sys_music_current_file != "sound/BGM/The hope.ogg":
        play music "sound/BGM/The hope.ogg" loop
        $ sys_music_current_file = "sound/BGM/The hope.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊哈哈～不要这样，好痒。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪～！汪～！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "四、四朗，你怎么了？？明明那么害怕狗的。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不知为何完全不害怕呐。\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    extend "真的，为什么呐。可能是太可爱了吧！"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哈哈♪"

    window hide

    pause 0.6

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.4

    window show

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_8E2AA2B7E1F047CF8C419F790C9A7329 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "四、四朗！？你怎么了！？居然会抱着小翼！！"

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_985C4F51753342B8B4DE84538D870AD5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呀——！？！？狗啊——！！是狗啊——！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "弟弟居然在和狗玩！！！猫山家的叛徒——！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_F31BFD9162C64D929725A6AF4C2C2823 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哥哥烦死了，怎么可以说这么可爱的狗可怕呢。"

    window hide

    pause 0.4

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 8.png
    $ zorder_rs_image_A438304BAD244787B1FCBDEB053ED1B2 = -100
    show rs_image_A438304BAD244787B1FCBDEB053ED1B2 as rs_image_A438304BAD244787B1FCBDEB053ED1B2 zorder zorder_rs_image_A438304BAD244787B1FCBDEB053ED1B2 onlayer master
    hide rs_image_A438304BAD244787B1FCBDEB053ED1B2

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A438304BAD244787B1FCBDEB053ED1B2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.5

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "雪绪，这到底怎么了？"

    rs_character_7009C1117C004F51829614A203C67DE7 "我、我也不知道……真的，不可思议呐……"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "小翼。下次也要一起玩哦！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！！"

    window hide

    pause 1

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    call scb_flag_title_end(1, _("「不可思议！猫狗物语」")) from _call_scb_flag_title_end_8

    if judge_lm_condition([]):
        jump block_00003701

    return

label block_00003701:
    # Node: 00003701 (Phase: 0)
    $ C1S4Phase = 0
    if Chapter <> 1:
        $ del C1S4Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 1" }]):
        jump block_00003700
    if judge_lm_condition([]):
        jump block_00003702

    return

label block_00003700:
    # Node: 00003700 ()

    return

label block_00003702:
    # Node: 00003702 (FINISH)
    $ C1S4 = True
    $ TalkTsubasaF4After = True

    if judge_lm_condition([]):
        jump block_000038F2

    return

label block_000038F2:
    # Node: 000038F2 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_7

    if judge_lm_condition([]):
        jump block_00003700

    return

