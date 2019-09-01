# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003B8F (FLAG: 狐的報恩)

label block_00003B90:
    # Node: 00003B90 ()

    if judge_lm_condition([]):
        jump block_00003B94

    return

label block_00003B94:
    # Node: 00003B94 (Phase: 99)
    if Not(VarExists("C2S5Phase")):
        $ C2S5Phase = 0
    $ C2S5Phase = 99

    if judge_lm_condition([]):
        jump block_00003B91

    return

label block_00003B91:
    # Node: 00003B91 (F5 START)
    call scb_flag_title(2, _("「狐的报恩」")) from _call_scb_flag_title_14

    if judge_lm_condition([]):
        jump block_00003B92

    return

label block_00003B92:
    # Node: 00003B92 (狐的報恩 1)
    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C93031E01A5478DBE357440B6071654 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2

    show rs_image_BD20E3AB6F2B49FAAE431177F57B0E33 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.5

    image gratitude_payment_of_fox_extend_image_1 = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#000000",
        size=30,
        text_align=0,
        outlines=[(absolute(2), "#FFFFFF", absolute(0), absolute(0))])

    show gratitude_payment_of_fox_extend_image_1 (_("那本缘起……某个夏日")) as cg_text at Transform(xpos=38, ypos=239)
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 3

    hide cg_text
    show rs_image_C5F762A9CB2F4A829F005CAF45FBECFE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.5

    image gratitude_payment_of_fox_extend_image_2 = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#000000",
        size=30,
        text_align=0.5,
        outlines=[(absolute(2), "#FFFFFF", absolute(0), absolute(0))])

    show gratitude_payment_of_fox_extend_image_2 (_("与友人登山，归途之时\n处羊肠小径，机缘巧合\n恐忽现神像，渐起狐音")) as cg_text at Transform(xalign=0.5, yalign=0.4)
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 6

    hide cg_text
    show rs_image_CBF16F392FD743CB96B6F614D63DD9C1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.5

    image gratitude_payment_of_fox_extend_image_3 = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#FFFFFF",
        size=34,
        text_align=0,
        outlines=[(absolute(4), "#000000", absolute(0), absolute(0))])

    show gratitude_payment_of_fox_extend_image_3 (_("吾乃千岁未朽之“九尾狐”")) as cg_text at Transform(xpos=245, ypos=262)
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 3

    hide cg_text
    show rs_image_1D94063D11F0441BA6ADC05DF58A1143 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AF99178A5BA8436FADEDFE321A1B70F6

    pause 0.8

    image gratitude_payment_of_fox_extend_image_4 = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#000000",
        size=30,
        text_align=0,
        outlines=[(absolute(2), "#FFFFFF", absolute(0), absolute(0))])

    show gratitude_payment_of_fox_extend_image_4 (_("自那之时，我的日常，渐渐脱节……")) as cg_text at Transform(xpos=222, ypos=154)
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 3

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide cg_text
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 3


    if judge_lm_condition([]):
        jump block_00003B93

    return

label block_00003B93:
    # Node: 00003B93 (狐的報恩 2)
    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_086A7B514AFD41E7A720068C2D941798 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.1

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_086A7B514AFD41E7A720068C2D941798 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.1

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_639CC417D72D4D1EA4F860D883FD9E70 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_5C9C69F3A63F44E0B71087CC0D54D58E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_7C3DD6AA3B724DE9984D6B1A9DC41316 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.5

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "四朗干得好！{w}不愧是篮球部的！"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗好棒哦～"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这点小事不过是饭后消食♪\n阿雪，下次也会刷刷地得分的！"

    show rs_image_BFEF6FC2749A4B06BF8978A9085171B6 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯，我很期待哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "期待什么的，说得和别人的事一样。\n"
    show rs_image_BA8F587A9CFC4AC38660F10FCCA9BD0C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "你也得加把劲！"

    show rs_image_F7C7F82F340647C1A7BB60DE2B1E06CA as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "欸～可是我不擅长球类运动的。"

    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不要抱怨！像远足部那样加油！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "四朗，给！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_D51A6635B0194DA89FB37740879ED03C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.2

    show rs_image_086A7B514AFD41E7A720068C2D941798 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "好！拿下了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_AC46DBAAAEE24C10AECA19E0EDA27051

    rs_character_31C08DBE8A3D4346A8E9496A228BE693 "呵呵，不会这么简单让你过去的～"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔～。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "正好！\n"
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_639CC417D72D4D1EA4F860D883FD9E70 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "阿雪，传球！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "欸？"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    show rs_image_624A7DE580F64A16B64F5454C551EBA2 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊、啊……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "好！——榊传球失误了！{w}轮到我们了！"

    pause 0.4

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_3B4C660F421B4BE392BB540B580F0339 "真是的～阿雪，算我拜托你了——"

    rs_character_7009C1117C004F51829614A203C67DE7 "就算这么说，我也对球类很不拿手的。"

    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔～你还真是呆。就因为这样球都拿不到。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_99C5410C32FF4E188D0338F65716E386 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "唔……来气了。\n等四朗差不多忘掉这件事后，一定要好好发泄这股怨气。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸！难道说又要像上次那样趁我睡觉{color=#008080}到处乱画{/color}！？{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_42CB0BD25FBB4117B00DA963C79425E7 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那个时候真的引起了大骚动的！千万不要了！"

    show rs_image_31F2D47C599D46E285A7CD7414520A6F as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "呼呼呼～至于会做什么，敬请期待～♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊哇……啊哇哇哇哇哇……"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗～手不要那么抖嘛，会没法好好打球的哦～"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "你以为是谁的错！"

    pause 0.3

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    window hide

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_FB8046DBE16F4BA8BE96613E8F3A850C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.7

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_92B6CF7379F442CC89B53814BF20ED94 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "呼……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F2DE1054BB154E3486F8E8EB7C2ECE1F as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "嘿……"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗！不要边走边玩球，很危险的。{w}\n说起来，后半场打的真烂。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_6641FF7BAA7C47A4982CDE1855A35FF0 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "拜、拜你所赐……"

    show rs_image_F7C7F82F340647C1A7BB60DE2B1E06CA as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "真是的～还要闹脾气到什么时候。\n我不记得做过让你这么讨厌的事呐～"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BA8F587A9CFC4AC38660F10FCCA9BD0C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "还敢说！迄今为止你都干了什么自己好好想想。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，球！"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "真是的，我去帮你取～说要报仇什么的只是玩笑……"

    window hide

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    show rs_image_F7B4BBF8CE1F42548986125166418110 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_3FE0E66EE0D042CE8856DAB3814A4CC9 as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=430, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    stop music fadeout 0.4
    $ sys_music_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_FB8046DBE16F4BA8BE96613E8F3A850C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_AC46DBAAAEE24C10AECA19E0EDA27051

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "等等！阿雪，危险！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Brakes 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Brakes 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=430, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_F7B4BBF8CE1F42548986125166418110 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DC107C264C484B3A8306E39B61626CF6

    rs_character_7009C1117C004F51829614A203C67DE7 "！？"

    window hide

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    if sys_music_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.4

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    window show

    pause 0.3

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "好危险啊小子！好好看红绿灯！"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Car 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Car 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 1.5

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    pause 0.5

    show rs_image_624A7DE580F64A16B64F5454C551EBA2 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg"

    pause 0.4

    window show

    pause 0.4

    rs_character_7009C1117C004F51829614A203C67DE7 "啊……我……刚才？应该被车？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3B4C660F421B4BE392BB540B580F0339 "阿雪！还好吗！？"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "欸？啊，嗯。没事……吧。"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "呼～太好了。居然会发生这种事……{w}\n不过刚才好厉害，危急时刻的力量？"

    show rs_image_81749C79DF1A40F3BF020F0ACBD64CA8 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "阿雪能那么敏捷地避开车，快的已经不像是人类了呐。"

    show rs_image_624A7DE580F64A16B64F5454C551EBA2 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "……是吗。刚才一瞬间我的记忆不见了，完全不知道自己做过什么。"

    show rs_image_E0D2132CD8F74B5CB3274596C13F9EA2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "反射性地身体动起来了？人该做的时候还是能做到的嘛！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_D51A6635B0194DA89FB37740879ED03C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "谢谢你帮我拿回球。我们走吧！"

    show rs_image_3FE0E66EE0D042CE8856DAB3814A4CC9 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯、嗯。"

    window hide

    pause 0.3

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 2

    window show

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_FB8046DBE16F4BA8BE96613E8F3A850C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "吓死我了，什么都没发生真是太好了。"

    window hide

    pause 0.6

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 3

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "——这并不是第一次。{w}\n最近，有什么变得很奇怪了。{w}我究竟会变成什么样子——"

    window hide

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5D080AF08B7F40DC9D5EAD63850DA7CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 1

    window show

    pause 0.3

    rs_character_7009C1117C004F51829614A203C67DE7 "（……这难道是成为大人的过程中的什么生理现象？）"

    window hide

    stop effect fadeout 3
    $ sys_effect_current_file = ""

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_F31BFD9162C64D929725A6AF4C2C2823 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    if sys_music_current_file != "sound/BGM/Daily 2.ogg":
        play music "sound/BGM/Daily 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 2.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "早上好呀，阿雪！脸色很不好哦，怎么了吗？好少见。"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗最近有没有觉得自己的身体变了？"

    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸？变、变了？那个……"

    show rs_image_B5B6C21DEF1547C8812C1DFEB1630592 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，说、说起来最近总觉得心情烦躁呐……那个、这个……"

    show rs_image_3FE0E66EE0D042CE8856DAB3814A4CC9 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯——烦躁什么？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "说是什么……\n这个，这有点……"
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "果、果然还是要保密！"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "唔……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "四郎的这个症状，\n之前从电视上看过，是什么病的前兆来着。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸欸欸！？这是病！？\n唔、呜哇。我会被怎么样？住院！？手术！？"

    show rs_image_F7C7F82F340647C1A7BB60DE2B1E06CA as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "倒不至于那么严重不过……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "说不定某天早上起来就会出大事哦。"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "下次找三朗哥问问不就好了？{w}\n一定要把觉得奇怪的地方好好"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_8540C7DB25BA424CAE3F5349B0307CCC as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "拿给他看"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_8540C7DB25BA424CAE3F5349B0307CCC as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "说清楚。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_BFEF6FC2749A4B06BF8978A9085171B6 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "那样的话哥哥肯定会告诉你解决方法的。"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "找、找那个哥哥？那种家伙能派上用场？"

    show rs_image_7C3DD6AA3B724DE9984D6B1A9DC41316 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯，再怎么说也是人生的前辈。"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "好、好。虽说不太情愿这次也只能拜托他了。"

    show rs_image_31F2D47C599D46E285A7CD7414520A6F as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "一定要平安治好哦♪"

    pause 0.4

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.7

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_624A7DE580F64A16B64F5454C551EBA2 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.3

    rs_character_7009C1117C004F51829614A203C67DE7 "（果然四朗没有这个问题。呜～我到底怎么了。）"

    window hide

    pause 0.35

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    stop music fadeout 1
    $ sys_music_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    window show

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}呀————！！{/size}"

    window hide

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    window show

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "怎、怎么了？！"

    window hide

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1.5

    if sys_music_current_file != "sound/BGM/Strange idea.ogg":
        play music "sound/BGM/Strange idea.ogg" loop
        $ sys_music_current_file = "sound/BGM/Strange idea.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_BAD45282754A432397A799074A78B388 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A2F5530406854E5098F52F72EE26DA66

    pause 0.4

    window show

    rs_character_31C08DBE8A3D4346A8E9496A228BE693 "女生别有事没事乱叫唤。"

    rs_character_1DE4030831134D25A45EAB6862904F5B "好厉害！好厉害！！这个可以去节目投稿了！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "诶，这、这是、阿雪的身体被……！！"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_5D080AF08B7F40DC9D5EAD63850DA7CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗～我被怎么了～？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "干嘛还像没事一样坐在那儿！！\n之前远足的照片，你被拍到了很奇怪的东西！"

    show rs_image_3FE0E66EE0D042CE8856DAB3814A4CC9 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "奇怪的东西？"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window hide

    pause 0.5

    # Gallery unlock: images/CG/Gratitude-payment-of-fox/Gratitude-payment-of-fox 2-1.png
    $ zorder_rs_image_3BA596B22A77484494505809CFB86D73 = -100
    show rs_image_3BA596B22A77484494505809CFB86D73 as rs_image_3BA596B22A77484494505809CFB86D73 zorder zorder_rs_image_3BA596B22A77484494505809CFB86D73 onlayer master
    hide rs_image_3BA596B22A77484494505809CFB86D73

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_3BA596B22A77484494505809CFB86D73 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A2F5530406854E5098F52F72EE26DA66

    pause 0.4

    window show

    pause 0.3

    rs_character_7009C1117C004F51829614A203C67DE7 "黄色烟雾一样的东西呐。这是什么？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "噫！心灵照片……阿雪的照片被幽灵附身了……！"

    rs_character_7009C1117C004F51829614A203C67DE7 "欸～不会的，只是光线折射或者相机故障哦？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_31C08DBE8A3D4346A8E9496A228BE693 "不，榊，猫山说得对！这用科学无法解释！"

    rs_character_1DE4030831134D25A45EAB6862904F5B "就是就是太奇怪了。肯定是幽灵～"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_31C08DBE8A3D4346A8E9496A228BE693 "好厉害！现实版的《幽灵手表》{size=12}{color=#808080}*捏他《妖怪手表》{/color}{/size}！\n榊叫一声的话说不定真的会出来！"

    rs_character_1DE4030831134D25A45EAB6862904F5B "会是什么样的幽灵呐，给我们看看给我们看看！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}{color=#FF80C0}快——叫♪快——叫♪快——叫♪{/color}{/size}"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_5D080AF08B7F40DC9D5EAD63850DA7CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    pause 0.4

    rs_character_7009C1117C004F51829614A203C67DE7 "欸，怎么回事，不做不行？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "可真的出现该怎么……？快、快住手比较好哦……？"

    show rs_image_F7C7F82F340647C1A7BB60DE2B1E06CA as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯～真是的。"
    show rs_image_8540C7DB25BA424CAE3F5349B0307CCC as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那就试试了。一二。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    stop music fadeout 1
    $ sys_music_current_file = ""

    window hide

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    if sys_music_current_file != "sound/BGM/Stage of HERO.ogg":
        play music "sound/BGM/Stage of HERO.ogg" loop
        $ sys_music_current_file = "sound/BGM/Stage of HERO.ogg"

    # Gallery unlock: images/CG/Gratitude-payment-of-fox/Gratitude-payment-of-fox 1.png
    $ zorder_rs_image_5CF2995690BF4C87A419E7A4AD05A94D = -100
    show rs_image_5CF2995690BF4C87A419E7A4AD05A94D as rs_image_5CF2995690BF4C87A419E7A4AD05A94D zorder zorder_rs_image_5CF2995690BF4C87A419E7A4AD05A94D onlayer master
    hide rs_image_5CF2995690BF4C87A419E7A4AD05A94D

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_5CF2995690BF4C87A419E7A4AD05A94D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.4

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "我的朋友！出来，小狐狸！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    # Gallery unlock: images/CG/Gratitude-payment-of-fox/Gratitude-payment-of-fox 1.png
    $ zorder_rs_image_5CF2995690BF4C87A419E7A4AD05A94D = -100
    show rs_image_5CF2995690BF4C87A419E7A4AD05A94D as rs_image_5CF2995690BF4C87A419E7A4AD05A94D zorder zorder_rs_image_5CF2995690BF4C87A419E7A4AD05A94D onlayer master
    hide rs_image_5CF2995690BF4C87A419E7A4AD05A94D

    show rs_image_5CF2995690BF4C87A419E7A4AD05A94D as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    rs_character_7009C1117C004F51829614A203C67DE7 "幽灵金属！设定完成！！"

    pause 1

    stop music fadeout 4
    $ sys_music_current_file = ""

    window hide

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5D080AF08B7F40DC9D5EAD63850DA7CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Ding 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D27B53EA4F4A40F6A37E5EFDA04547A5

    pause 1.5

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_C2D77A11D4154926AC40E015A13CABE5 "男生在做什么？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_C2D77A11D4154926AC40E015A13CABE6 "挫爆了，好傻。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_C2D77A11D4154926AC40E015A13CABE5 "真是幼稚。"

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D52CBCDC8A744331840B8088534BFB69 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "你、你们～什么叫出来嘛，根本就是在做羞耻表演啊。"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_D52CBCDC8A744331840B8088534BFB69 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_5C9C69F3A63F44E0B71087CC0D54D58E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "什、什么嘛！什么都没出来嘛！\n啊～好没意思，我本来很期待的呐，阿雪。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_80C5B8F3D2C94DF68490FC8D313B5A26 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗，下次真心给我做好觉悟哦……"

    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "噫？！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    rs_character_31C08DBE8A3D4346A8E9496A228BE693 "不管是不是幽灵，榊都已经很恐怖了……"

    rs_character_1DE4030831134D25A45EAB6862904F5B "同感。猫山，辛苦你了。"

    pause 0.5

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 2.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_C2D77A11D4154926AC40E015A13CABE5 "呐，不做一下驱灵仪式不要紧吗？"

    rs_character_C2D77A11D4154926AC40E015A13CABE6 "嗯，榊君，很令人担心呐……"

    stop music fadeout 2
    $ sys_music_current_file = ""

    window hide

    pause 2.5

    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 1

    window show

    pause 0.3

    rs_character_7009C1117C004F51829614A203C67DE7 "（嗯……果然还是对那张照片很在意。也许和最近时不时地失去意识有关。）"

    rs_character_7009C1117C004F51829614A203C67DE7 "（好，先从能接触到的东西开始。）"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B96

    return

label block_00003B96:
    # Node: 00003B96 (CP2 Daytime Misaki 雪緒)
    call block_00001098 from _call_block_00001098

    if judge_lm_condition([]):
        jump block_00003B9F

    return

label block_00003B9F:
    # Node: 00003B9F (狐的報恩 3)
    $ set_window("イベントモード")
    stop music fadeout 2
    $ sys_music_current_file = ""

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_8EC5717E792241CB9E9610819A6E1D46

    pause 2.5

    if True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect4 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect4_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AC1B25E38FBD418694C750637E85FC2C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 2.5

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg"

    window show

    pause 0.5

    rs_character_7009C1117C004F51829614A203C67DE7 "（这里就是夏天和四朗一起爬过的山……果然引起身体变化的契机就应该在这里。）"

    rs_character_7009C1117C004F51829614A203C67DE7 "（那个时候，从一条奇怪的小道经过后，就开始时不时出现记忆断片了。）"

    window hide

    pause 1

    stop effect3 fadeout 2
    $ sys_effect3_current_file = ""

    stop effect4 fadeout 2
    $ sys_effect4_current_file = ""

    show rs_image_AA5A1AE584D440DC99437FA80CFEBBD1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_44331B79D1D84C7EAA35F0480004721A

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_8540C7DB25BA424CAE3F5349B0307CCC as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "好！就去那里看看。"

    window hide

    pause 0.4

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    show rs_image_0B29D260FA114D6EB90FB552C6296007 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    show rs_image_9A2C00D43DB248449CE5FEDD6F38139A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 2

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_C06CC60D54D84C9EBF4E360C8EC06DEE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_65412F8CC840413CAE303C4848D4DEA6

    pause 1.5

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    window show

    pause 0.3

    rs_character_7009C1117C004F51829614A203C67DE7 "（四朗应该在这里绊倒过，那时地上倒了一个{color=#FFFF00}狐狸的神像{/color}。）"

    rs_character_7009C1117C004F51829614A203C67DE7 "（之后突然传来不舒服的声音，想要逃走时意识就……）"

    rs_character_7009C1117C004F51829614A203C67DE7 "……{w}……{w}……{w}\n{w=1}狐狸先生。"
    stop music fadeout 1
    $ sys_music_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_5C0E3E0CAA12428E8D037064462B6F3D

    extend "请问在我身体里吗？"

    window hide

    pause 2

    show rs_image_AC1B25E38FBD418694C750637E85FC2C as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_AF99178A5BA8436FADEDFE321A1B70F6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 400
    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_AA5A1AE584D440DC99437FA80CFEBBD1 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_B9C6F3CC89044C67AF17ADF9D3089AC6 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_0B29D260FA114D6EB90FB552C6296007 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_9A2C00D43DB248449CE5FEDD6F38139A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_C06CC60D54D84C9EBF4E360C8EC06DEE as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 3

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C06CC60D54D84C9EBF4E360C8EC06DEE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 2.ogg"

    $ zorder_tag_1AB0074A0ABB40A7B797779771DF877D = 300
    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_1AB0074A0ABB40A7B797779771DF877D at center_top zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 1

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg"

    window show

    pause 0.4

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『呼呼呼。与前所语之怪诞称呼相异，仍识己职呐，小子……』"

    window hide

    pause 0.8

    hide tag_1AB0074A0ABB40A7B797779771DF877D
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_2B3B849B552243179409B8411C157783

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_AA5A1AE584D440DC99437FA80CFEBBD1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_D6BC962AE17948D893E50BE9B4670973

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "！！"

    window hide

    pause 0.3

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_1AB0074A0ABB40A7B797779771DF877D = 300
    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_1AB0074A0ABB40A7B797779771DF877D at Transform(xpos=300, yalign=0.0) zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_CD4E0717885A494B93606FDBEF55AF92

    window show

    pause 0.4

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『正是……迄今所有均为吾之所为。然，汝似甚定。』"

    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『那时以来吾便于此凭依，与汝共度。汝之无心之举时令吾恐。』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_D52CBCDC8A744331840B8088534BFB69 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "到底为什么要附到我身上？\n今天也是，发生了像心灵照片这样的骚动的！"

    show rs_image_92A94B815A0F4834897B355406969B5F as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『何出此言。危急之时吾可曾助汝多次。』"

    show rs_image_96051C62C9264F7E9EB113FA58CDF619 as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『从近所恶意之人处护汝。方昨日球戏之时不正如此？』"

    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "啊……"

    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『此乃等价交换，所做之事当于今后补偿于吾。』"

    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "等、等价交换？到底想用我的身体做什么……？"

    show rs_image_AFC74CA3A841436580FD0BAB259E1E86 as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『呼呼呼。于子过激，于吾不忍直言，此处暂隐。』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "所、所以说，像这种不忍说出来的事情就不要用我的身体做了～！"

    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『有何不可，有何不可。吾之快乐汝仍可感其余韵哦？』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_D52CBCDC8A744331840B8088534BFB69 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "说、说那种东西强行拉开话题也是没用的！总之快从我身上离开！"

    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『不可。吾甚喜汝，如此知遇之人乃首次。』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『简言之，汝甚似狐。』"

    show rs_image_8540C7DB25BA424CAE3F5349B0307CCC as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "所以又怎么样！和我完全无关。难道要我说接下来就这样？"

    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『吾于此仍可护汝。若非如此，昨日归宅之时汝岂欲死乎？』"

    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "唔……这种事情……"

    show rs_image_96051C62C9264F7E9EB113FA58CDF619 as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『相较无数之守护灵，吾远强于其。{w}胆敢忤逆吾之灵，屈指可数。』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『吾可保将来汝独居他处之时仍可于恶质地缚灵下安居乐业。』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "等、等等！我成为大人之后……你打算一直凭依在我身上！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『吾之接受范围甚广。"
    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "实乃略壮硕之人更喜……』"

    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_1AB0074A0ABB40A7B797779771DF877D zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『然现如此契合，不应抱怨。综上，就你了。{w}暂别，小子。』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 2.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_1AB0074A0ABB40A7B797779771DF877D
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    stop music fadeout 2
    $ sys_music_current_file = ""

    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "啊、等等！！！"
    show rs_image_624A7DE580F64A16B64F5454C551EBA2 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……虽说不是我完全同意这么做，\n但似乎也说了一些妥协的话呐。"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_8540C7DB25BA424CAE3F5349B0307CCC as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_7009C1117C004F51829614A203C67DE7 "我接下来会怎么样？呐——九尾？九尾！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『尝他人无处谈起之贵重体验。有何不好。』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "哇！？欸？你在什么地方？根本看不到……\n到底在什么地方和我说话？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『吾与汝同身心，若汝已察吾之存在，则可对话。』"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『甚好，如此即可打发时间。』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "难、难道不只是凭依？！"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『数次交换之时汝即失忆，今后交替之时不会如此。』"

    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "啊？这是什么意思？"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『那么，实际体验为准。"
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_1AB0074A0ABB40A7B797779771DF877D = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_1AB0074A0ABB40A7B797779771DF877D at Transform(xpos=300, yalign=0.0) zorder zorder_tag_1AB0074A0ABB40A7B797779771DF877D onlayer master
    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.3

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_1AB0074A0ABB40A7B797779771DF877D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "哈！』"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_AFC74CA3A841436580FD0BAB259E1E86 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "嗯～人类之身甚适行动，不愧仅两足。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_7009C1117C004F51829614A203C67DE7 "『哇哇！？到底发生什么了！？』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "一气下山了！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『哇！很危险的！！真的很危险的！！不要用我的身体做那种事！！』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_AC1B25E38FBD418694C750637E85FC2C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "呼呼呼。不错！不错！"

    window hide

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_AA5A1AE584D440DC99437FA80CFEBBD1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_0B29D260FA114D6EB90FB552C6296007 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_9A2C00D43DB248449CE5FEDD6F38139A as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_B9C6F3CC89044C67AF17ADF9D3089AC6 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    show rs_image_0CFD79AB1A914971B1C5FF195D73BB2D as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.3

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "啊。"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dive 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dive 1.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 2

    # Gallery unlock: images/CG/Gratitude-payment-of-fox/Gratitude-payment-of-fox 3.png
    $ zorder_rs_image_2B2468BBF68040D7AA817B022CDE842D = -100
    show rs_image_2B2468BBF68040D7AA817B022CDE842D as rs_image_2B2468BBF68040D7AA817B022CDE842D zorder zorder_rs_image_2B2468BBF68040D7AA817B022CDE842D onlayer master
    hide rs_image_2B2468BBF68040D7AA817B022CDE842D

    show rs_image_2B2468BBF68040D7AA817B022CDE842D as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_266255D4821A4095BCA7860D44F0A511

    pause 0.7

    window show

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『什么不错！这不是掉湖里了吗！』"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "气血上脑……苏醒后时日尚浅，仍有不适。"

    rs_character_7009C1117C004F51829614A203C67DE7 "『真是的，比传说中最强的九尾狐呆多了～』"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "呼呼呼，不可早言，假以时日终可恢复。放眼未来。"

    rs_character_7009C1117C004F51829614A203C67DE7 "『唔～……那就请你多多加油了，守护灵的狐狸先生。』"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『不过说起来，{w}这种地方居然会有湖泊呐……{w}好漂亮。』"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "呼呼，为汝吾不得不于此滑下，记得感谢。"

    rs_character_7009C1117C004F51829614A203C67DE7 "『好好……无所谓了，{w}结果好就可以了。』"

    window hide

    pause 1

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_1AB0074A0ABB40A7B797779771DF877D
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 3

    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.4

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "我出门了～！"

    window hide

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    show rs_image_9A49BAFDFC314759B22269AA240FA65C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    show rs_image_752FA16B677941C5A9A2623B79A40F24 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.8

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_D52CBCDC8A744331840B8088534BFB69 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "哈……哈……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『睡眠甚长呐，雪绪。』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_8540C7DB25BA424CAE3F5349B0307CCC as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "你以为是谁的错！？九尾昨天闹过头了，累坏了只能爆睡了！"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『不可怪吾，此乃雪绪体力不支。』"

    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "讲不通道理！啊～坏了！真的要迟到了～！"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『无可奈何。交换？』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_D52CBCDC8A744331840B8088534BFB69 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "拜托了！"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.3

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.7

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_1F8C3AD8E9E848BBAC058C73D0DE01FB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_07BACEE3C1C64F1DAD61CD240DF0C2E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_5F022B91486841699EAC5FE3BDC0F5CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.7

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_7009C1117C004F51829614A203C67DE7 "『呵～♪不错～』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "那个孩子是什么人！？{w}\n好快～！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『哈哈，怎样怎样♪』"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_2B0101A94EBD47F79D5A76B100A72371 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "（被赞之人为吾知否？）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "『不要在意细节～好，快走。』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_B9A9F30A6AE049B0B4030B6673E24958 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "（唔唔……屈辱……）"

    pause 0.5

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    window hide

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5D080AF08B7F40DC9D5EAD63850DA7CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "给我过来榊雪绪！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "上次说的得病是骗人的！！拜你所赐好羞耻的！！"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_015E860A189542C2A5AB44FC16BCD6AD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_930C8D3D0E4F4E469D362E8C86F74A3A as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_7009C1117C004F51829614A203C67DE7 "啊……嗯……抱歉，等下再说。现在快累死了……"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊？怎么了。早上起来去锻炼了？"

    show rs_image_624A7DE580F64A16B64F5454C551EBA2 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "呃……算是……所以现在先让我休息一下……"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "唔，好。等你休息好了我可要好好抱怨的。"

    show rs_image_930C8D3D0E4F4E469D362E8C86F74A3A as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "好～……"
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_930C8D3D0E4F4E469D362E8C86F74A3A as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    extend "唔唔，恶……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『随意使唤吾终得报应，自作自受。』"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（说的也是，毕竟身体是一样的，我肯定也会累。呜，恶……）"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    window hide

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_8F070BDCB04D4336AC7465096F0E3084 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    window show

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_8EF7B22684E3474BB8CDD5FA00563D87 "下一个～谁会第12题～？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_5D080AF08B7F40DC9D5EAD63850DA7CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_624A7DE580F64A16B64F5454C551EBA2 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_7009C1117C004F51829614A203C67DE7 "唔……好想睡觉……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『贫弱啊，现今之童大抵如此，过去……』"

    show rs_image_F7C7F82F340647C1A7BB60DE2B1E06CA as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（我要休息一下。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "九尾，交换。）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『等、等下。如此无趣之时奈何由吾顶替？！』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    rs_character_8EF7B22684E3474BB8CDD5FA00563D87 "那就！榊，你上来写一下答案。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_450F7105136E4BF69CF26683BE486FC1 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_8F070BDCB04D4336AC7465096F0E3084 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_2B0101A94EBD47F79D5A76B100A72371 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "（雪绪！何谓答案！？吾不明白！！）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "『Zzzz……』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_B9A9F30A6AE049B0B4030B6673E24958 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "（雪绪——！起来——！唔唔……若为国语则勉强无事但。）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Ding 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8EF7B22684E3474BB8CDD5FA00563D87 "榊——快点上来写。"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    window hide

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5D080AF08B7F40DC9D5EAD63850DA7CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.4

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_BFEF6FC2749A4B06BF8978A9085171B6 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "今天的午餐是我最喜欢的咖喱——♪\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_80C5B8F3D2C94DF68490FC8D313B5A26 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，不过番茄就……』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『此以咖……冠名之物，看似美味呐。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "嗯，该偿还今日之事了。』"

    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（啊！等等！）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_96051C62C9264F7E9EB113FA58CDF619 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "（嗯嗯，（嚼嚼）。这可真……不愧为人类料理，味重而深邃，美味。）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "『啊～我的…………算了。{w}那作为交换把番茄也一起吃了。』"

    show rs_image_92A94B815A0F4834897B355406969B5F as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "（番茄？是……此物？"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_B9A9F30A6AE049B0B4030B6673E24958 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "唔！？这、这……！交换。）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_7009C1117C004F51829614A203C67DE7 "『哈！？』"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_D52CBCDC8A744331840B8088534BFB69 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "（等等，怎么回事！？）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『曾有尝试，然甚不齿！至今忆起仍不免颤抖，绝对不干。』"

    show rs_image_930C8D3D0E4F4E469D362E8C86F74A3A as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（我也是一样的啊～！唔～不过，不吃的话会被老师骂的……）"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_624A7DE580F64A16B64F5454C551EBA2 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_5C9C69F3A63F44E0B71087CC0D54D58E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_3B4C660F421B4BE392BB540B580F0339 "阿雪，又只剩下番茄了吗？之前也说过了，这次可不帮你了哦！"

    rs_character_7009C1117C004F51829614A203C67DE7 "我知道……呜……捏住鼻子至少好点。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_930C8D3D0E4F4E469D362E8C86F74A3A as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "（张口）。（嚼嚼）……（吞）。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "呜……好臭。"

    show rs_image_356ECD8406BB49698A4D9CAD3C494C73 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不错不错♪干得好哦♪"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『可吞传言恶魔之果，不愧雪绪，不可小看。』"

    window hide

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1.5

    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_639CC417D72D4D1EA4F860D883FD9E70 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.3

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}四朗，投的好——！！{/size}"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_086A7B514AFD41E7A720068C2D941798 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哈哈——♪阿雪，今天可不能再像上次那样发呆了哦！"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "好好……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『又为球戏，吾甚喜。』"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_BFEF6FC2749A4B06BF8978A9085171B6 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_7009C1117C004F51829614A203C67DE7 "（这个叫做篮球，向筐里投中次数越多就能胜利。）"

    show rs_image_7C3DD6AA3B724DE9984D6B1A9DC41316 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（其实还有更多详细的规则的，\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_31F2D47C599D46E285A7CD7414520A6F as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "反正九尾也理解不了～）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『唔。不可侮辱千年之识。要点为，跟从那小子即可？』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『看好，看好九尾之力。』"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.7

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_BA8F587A9CFC4AC38660F10FCCA9BD0C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "阿雪！！过去了！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_31C08DBE8A3D4346A8E9496A228BE693 "呵呵，迟钝的榊没有威胁！就这么投篮！"

    rs_character_1DE4030831134D25A45EAB6862904F5B "嗯！"

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "呼呼呼，休想！"

    window hide

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 4.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 4.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_9F8EA032E81344E3B32B192681064721 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 1

    hide tag_1AB0074A0ABB40A7B797779771DF877D
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    window show

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-160, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}{/color}{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=380, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=20, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=200, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=140, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=320, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-40, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=260, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=440, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}\n{color=#FFFF00}{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=140, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-40, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=440, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=320, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=20, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=200, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=260, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_85C90C914E8E4725943E52CD42611423

    extend "{color=#FFFF00}呼{/color}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-160, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_85C90C914E8E4725943E52CD42611423

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    extend "{color=#FFFF00}呼{/color}{color=#FFFF00}！！{/color}"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_D6BC962AE17948D893E50BE9B4670973

    pause 0.3

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_1DE4030831134D25A45EAB6862904F5B "什么！？"

    rs_character_31C08DBE8A3D4346A8E9496A228BE693 "好、好厉害……落地后马上起跳，马上就能投篮。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那、那家伙有那种瞬间爆发力……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "有破绽！球借走了。"

    window hide

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_AFC74CA3A841436580FD0BAB259E1E86 as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=430, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    window show

    rs_character_1DE4030831134D25A45EAB6862904F5B "啊。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 4.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 4.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "看好看好～！"

    rs_character_31C08DBE8A3D4346A8E9496A228BE693 "太、太快了……！"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "现今之童何等无力。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_639CC417D72D4D1EA4F860D883FD9E70 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "呵。{nw}"
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_53B376EDDA024633A3328E405F058927

    extend ""

    window hide

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    # Gallery unlock: images/CG/Gratitude-payment-of-fox/Gratitude-payment-of-fox 4.png
    $ zorder_rs_image_986D6DD667574B1D83ECEA3AF755AFA3 = -100
    show rs_image_986D6DD667574B1D83ECEA3AF755AFA3 as rs_image_986D6DD667574B1D83ECEA3AF755AFA3 zorder zorder_rs_image_986D6DD667574B1D83ECEA3AF755AFA3 onlayer master
    hide rs_image_986D6DD667574B1D83ECEA3AF755AFA3

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_986D6DD667574B1D83ECEA3AF755AFA3 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 0.6

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "『哦哦～不愧是九尾大人呐。只见过一次就能完全掌握篮球的技巧。』"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "呼，仅此小事……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哦哦哦！！厉害！！阿雪！！什么时候篮球这么好了！？"

    rs_character_31C08DBE8A3D4346A8E9496A228BE693 "刚才好厉害！完全跟不上呐。"

    rs_character_1DE4030831134D25A45EAB6862904F5B "防御也好厉害！简直无敌！！"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "呼呼，正是正是，赞扬即可。为此献上你们的精……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    rs_character_7009C1117C004F51829614A203C67DE7 "哇啊啊啊！谢、谢谢！！今天状态比较好，偶然的偶然的！"

    window hide

    pause 0.8

    stop music fadeout 5
    $ sys_music_current_file = ""

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 2

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 3

    if sys_music_current_file != "sound/Effect Sound/Swallow 1.ogg":
        play music "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_music_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    show rs_image_BAA43B4F4198492BA4DCD8836A92877B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_F31BFD9162C64D929725A6AF4C2C2823 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_3FE0E66EE0D042CE8856DAB3814A4CC9 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "最近，阿雪不知为什么很高兴呐。"

    show rs_image_7C3DD6AA3B724DE9984D6B1A9DC41316 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "哈哈～那肯定是不断度过刺激的日常的原因。"

    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哦——那是什么意思？"

    window hide

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    stop music fadeout 1
    $ sys_music_current_file = ""

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_FB8046DBE16F4BA8BE96613E8F3A850C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    window show

    rs_character_C2D77A11D4154926AC40E015A13CABE5 "就、就是那个孩子！心灵照片上的！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_11D1DFF219FE44D6933AB9F3B6E8BBDA "贫僧知道了，谢谢小施主。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_BAA43B4F4198492BA4DCD8836A92877B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_9A3415044879409B866CD2472C9CB897 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    extend "那边的那位，请留步！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "诶？这群和尚是怎么回事！？"

    show rs_image_A5590FF4F101409FB37BD47AA9881A12 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "有什么事吗？"

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    window hide

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    # Gallery unlock: images/CG/Gratitude-payment-of-fox/Gratitude-payment-of-fox 5.png
    $ zorder_rs_image_52CC474C78C944CABB132D3C2D0EA6A8 = -100
    show rs_image_52CC474C78C944CABB132D3C2D0EA6A8 as rs_image_52CC474C78C944CABB132D3C2D0EA6A8 zorder zorder_rs_image_52CC474C78C944CABB132D3C2D0EA6A8 onlayer master
    hide rs_image_52CC474C78C944CABB132D3C2D0EA6A8

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_52CC474C78C944CABB132D3C2D0EA6A8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    pause 0.8

    if sys_music_current_file != "sound/BGM/Angel and Demon.ogg":
        play music "sound/BGM/Angel and Demon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Angel and Demon.ogg"

    window show

    rs_character_4DCC3C577A8D48B2BBAD4A0EEFF2D0AB "详细的回到本殿再说！总之跟我们来！！"

    rs_character_EB1A89F4BFB24C708DBFFE2AD9447ED9 "这样下去你的身体会很危险！我们是为了拯救你而来。"

    rs_character_4778F2D7D27E4FBDB716AC22DAA81470 "快走！师父已经等了很久了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "阿、阿雪！？"

    rs_character_7009C1117C004F51829614A203C67DE7 "等、请稍等一下！我确实是被什么凭依了但没那么严重的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    rs_character_4DCC3C577A8D48B2BBAD4A0EEFF2D0AB "那当然了，你……我们对附身不附身本来就没什么兴趣嘛，呵呵。"

    rs_character_EB1A89F4BFB24C708DBFFE2AD9447ED9 "总、总之包括那个在内，等下再确认！快快，走了！"

    rs_character_7009C1117C004F51829614A203C67DE7 "哇、哇啊！？"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_6C354BF3257840209C797C6559B792C2

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_BAA43B4F4198492BA4DCD8836A92877B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_596D161914B24A83ACDE5FD1ED935C63 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "阿雪——！！"

    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "怎、怎么会！这到底是怎么回事！？那些看起来就很可疑的人是谁！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_C2D77A11D4154926AC40E015A13CABE5 "之前那张心灵照片我们怎么想也非常在意，\n就去一家很有名的处理幽灵相关事情的事务所咨询了。"

    rs_character_C2D77A11D4154926AC40E015A13CABE5 "然后那边的住持就说要赶快带过去。"

    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "可那些人非常可疑。所谓的有名，不会是因为不靠谱出名的？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_C2D77A11D4154926AC40E015A13CABE5 "放心。我经常在报纸上看到欺诈之类的报导，但那个绝对不是！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    rs_character_C2D77A11D4154926AC40E015A13CABE5 "住持是很厉害的超能力者，在半空中正坐的照片也有！是可以相信的！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7043C167749A4910BA34B56290F443F2 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这就是骗人的节奏……典型的骗人的节奏……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    rs_character_C2D77A11D4154926AC40E015A13CABE5 "这样榊君就从恶灵的威胁里解放了呐！\n做了好事后心情非常舒爽呢！"

    show rs_image_E212CF3B4B47425FB1AEB250438B7593 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "相对的现在有人为的危险了……\n"
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "阿雪，没关系……么。"

    pause 0.4

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    window hide

    pause 2.5


    if judge_lm_condition([]):
        jump block_00003B9D

    return

label block_00003B9D:
    # Node: 00003B9D (狐的報恩 4)
    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Flurry 2.ogg":
        play music "sound/BGM/Flurry 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1B04937674574C949F5F45A3B3BC8B6B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_4DCC3C577A8D48B2BBAD4A0EEFF2D0AB "师父！之前说的孩子带来了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104C616BEBAF48D8B6DC31A70290659F "啊，欢迎欢迎。{w}哦，和照片上一样可爱的孩子呐。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_930C8D3D0E4F4E469D362E8C86F74A3A as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "呜……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "唔哈哈哈，不用那么紧张。我们是来救助你的。"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "现在就从恶灵手中救你出来。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    extend "相信我们{color=#FF00FF}“见梦饮（GYMNO）”{/color}教！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "报酬稍后会找你父母谈的。为少年驱灵的话半价，可是赚了哦～"
    show rs_image_2E3FE0C975FB4C82B9A67BB3B3E98889 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "那个……我其实无所谓。不驱灵也没关系，现状已经很满意了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_4DCC3C577A8D48B2BBAD4A0EEFF2D0AB "说什么呢！被附身就是被附身！不用客气把身心都交给师父就好了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    rs_character_104C616BEBAF48D8B6DC31A70290659F "还被附着身！？这可是很重要的。好了，那么大家，驱灵开始了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    rs_character_104C616BEBAF48D8B6DC31A70290659F "{size=28}{color=#00FFFF}来！BOYS FEEL COMFORTABLE！{/color}{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    rs_character_A2CD1745B0304B48BAE9C1E9830A35D3 "{size=28}{color=#00FFFF}BOYS FEEL COMFORTABLE！！{/color}{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104C616BEBAF48D8B6DC31A70290659F "那么，禊{size=12}{color=#C0C0C0}（古时河边常见的某种仪式，国内也有的）{/color}{/size}开始！\n这是为了清洁一切，绝对不能发出声音哦。"

    rs_character_4778F2D7D27E4FBDB716AC22DAA81470 "那、那么，为了放松全身涂上圣水，先把衣服脱了！"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    # Gallery unlock: images/CG/Gratitude-payment-of-fox/Gratitude-payment-of-fox 6.png
    $ zorder_rs_image_C533C9DBA54D4CAFAD4F08DA43EB9A55 = -100
    show rs_image_C533C9DBA54D4CAFAD4F08DA43EB9A55 as rs_image_C533C9DBA54D4CAFAD4F08DA43EB9A55 zorder zorder_rs_image_C533C9DBA54D4CAFAD4F08DA43EB9A55 onlayer master
    hide rs_image_C533C9DBA54D4CAFAD4F08DA43EB9A55

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C533C9DBA54D4CAFAD4F08DA43EB9A55 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_BAF3BF757577455980E802743F48D2F9

    pause 0.5

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "噫！？啊……不要过来。啊……不要……！"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "这么快就有效果了呐，这种辗转不安无所适从的样子\n正是你心中潜伏着恶灵的证据。"

    rs_character_7009C1117C004F51829614A203C67DE7 "只是因为很痒而已！不要，那里不行……！"

    rs_character_4DCC3C577A8D48B2BBAD4A0EEFF2D0AB "呵呵呵！……师、师父，清洁完成了！"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "好的，那就平放到中央那里，开始正式驱灵了。"

    stop music fadeout 2
    $ sys_music_current_file = ""

    window hide

    pause 0.8

    # Gallery unlock: images/CG/Gratitude-payment-of-fox/Gratitude-payment-of-fox 7.png
    $ zorder_rs_image_9C54D280900F4385BDFF754A33B420AF = -100
    show rs_image_9C54D280900F4385BDFF754A33B420AF as rs_image_9C54D280900F4385BDFF754A33B420AF zorder zorder_rs_image_9C54D280900F4385BDFF754A33B420AF onlayer master
    hide rs_image_9C54D280900F4385BDFF754A33B420AF

    show rs_image_9C54D280900F4385BDFF754A33B420AF as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_569EF50A3F874CA8BB70A4454CCFCEF3

    pause 0.8

    window show

    pause 0.3

    if sys_music2_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg":
        play music2 "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg"

    rs_character_E1CA6A5E73164697AB8F4837C9AD8BF3 "色丽子，邓布利多，多布丽邓，邓即是多，\n多即是邓，受想行事♂亦复如是……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "（啊……好像身体真的有违和感……？好像真的有效果？九尾，还在吗？）"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『……』"

    rs_character_7009C1117C004F51829614A203C67DE7 "（啊咧？九尾？呐，九尾！）"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『…………』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "（九尾！！这样下去会被驱灵的！呐！！回答我！！！）"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『…………』"

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "（我不要这样！！九尾！！！！）"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『……{w}……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    # Gallery unlock: images/CG/Gratitude-payment-of-fox/Gratitude-payment-of-fox 7.png
    $ zorder_rs_image_9C54D280900F4385BDFF754A33B420AF = -100
    show rs_image_9C54D280900F4385BDFF754A33B420AF as rs_image_9C54D280900F4385BDFF754A33B420AF zorder zorder_rs_image_9C54D280900F4385BDFF754A33B420AF onlayer master
    hide rs_image_9C54D280900F4385BDFF754A33B420AF

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_9C54D280900F4385BDFF754A33B420AF as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "……嗯？抱歉，睡了。』"

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1B04937674574C949F5F45A3B3BC8B6B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A7A23927BF8B4CA991AE79FB2ABD3252

    if sys_music_current_file != "sound/BGM/Flurry 2.ogg":
        play music "sound/BGM/Flurry 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 2.ogg"

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FAA8296BB55F46B4A52CA33A78BB77ED as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（哈！？从我被带走开始就一言不发果然！真是的在干什么呐！）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『吾亦需休息。汝未睡之时难以自由行动。』"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『……那，此事如何？"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "乐享其中？』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_D52CBCDC8A744331840B8088534BFB69 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（怎么可能——！好了快点逃出去！）"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『呵，无趣。汝之日常过于无趣，此等刺激稍显不足。』"

    show rs_image_8540C7DB25BA424CAE3F5349B0307CCC as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "不要说胡话了快点！"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『吾已知之。…………"
    extend "然，汝，{w}反抗了呐。』"

    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（嗯？）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_1AB0074A0ABB40A7B797779771DF877D
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『自言自语。"
    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    extend "那好。』"

    window hide

    pause 0.4

    hide tag_1AB0074A0ABB40A7B797779771DF877D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "你们，拿出毅力。此等少年正处眼前，然何无人上前。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_AFC74CA3A841436580FD0BAB259E1E86 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "非为无趣？小试如何？尝博吾欢心。"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EB1A89F4BFB24C708DBFFE2AD9447ED9 "欸欸……可、可以吗！？不过我不想再被请去喝茶了……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_92A94B815A0F4834897B355406969B5F as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "呼，毫无毅力。"
    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那，汝乃长官否？\n汝作何感想？与此等人不同否？"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104C616BEBAF48D8B6DC31A70290659F "震惊！！！那那那那当然，早就想做了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_1B04937674574C949F5F45A3B3BC8B6B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_104C616BEBAF48D8B6DC31A70290659F "不，等等，突然这种态度……\n你这家伙是恶灵！！！如果是的话，立刻镇压！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104C616BEBAF48D8B6DC31A70290659F "这是为了驱灵不得已而为之！绝对和我的个人兴趣无关……"

    window hide

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.8

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1B04937674574C949F5F45A3B3BC8B6B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_92A94B815A0F4834897B355406969B5F as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 2

    stop effect3 fadeout 1.5
    $ sys_effect3_current_file = ""

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_EB3224B590D54A16B907ED1317CF7FCF as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Thunder 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Thunder 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_AFC74CA3A841436580FD0BAB259E1E86 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.4

    window show

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "呼呼呼……可试令吾悦。"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "『九尾这个笨蛋！！占着别人的身体说什么呐！！我绝不要这样的大叔！！』"

    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "（不愿？奈何如此不满，亦可体验该日之舒爽哦。）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『不要不要这种不要！！好了赶紧逃！！』"

    show rs_image_96051C62C9264F7E9EB113FA58CDF619 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "（唔……不得已。）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_92A94B815A0F4834897B355406969B5F as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.4

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "气氛已无，暂且离去。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_53B376EDDA024633A3328E405F058927

    extend "后会有期！"

    window hide

    pause 0.9

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_1B04937674574C949F5F45A3B3BC8B6B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_104C616BEBAF48D8B6DC31A70290659F "怎、怎么可以！？！？{w}这种……"

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6C349ECA854742E3A20CD1589DE42DF3

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 6.ogg"

    show rs_image_46726D80EC7B4D48AD2EFED4CDD37F1C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_E1CA6A5E73164697AB8F4837C9AD8BF3 "{size=36}生不如死啊啊啊！！{/size}"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window hide

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.7

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_96051C62C9264F7E9EB113FA58CDF619 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_7009C1117C004F51829614A203C67DE7 "『九尾太差劲了——再也不相信你了。』"

    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "不需如此气急败坏。此乃稍稍笑谈。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『不——要！——不认识你！我讨厌九尾！』"

    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "讨厌？呼呼。既然如此奈何驱灵之时\n以“不驱灵也没关系”之言拒否？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『那……那种肯定没效果所以才这么说的！\n被那些人摸起来很难受，只是这样而已。』"

    rs_character_7009C1117C004F51829614A203C67DE7 "『而且和九尾一起也很方便。只是这样而已，没有什么喜欢不喜欢！』"

    show rs_image_AFC74CA3A841436580FD0BAB259E1E86 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "毫不坦率呐。也罢，此处吾亦甚喜。"

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_AFC74CA3A841436580FD0BAB259E1E86 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_7009C1117C004F51829614A203C67DE7 "『等、等等，驱灵前你是醒着的！？九尾！』"

    show rs_image_1D6B4ED84D444E77A62AE65DA304045E as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "正是。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『真是的！最讨厌了！坏心眼！笨蛋！』"

    show rs_image_6F3F613C2A0C41D5A4BD1790183DB8ED as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "呼呼呼呼。"

    rs_character_7009C1117C004F51829614A203C67DE7 "『……真是的。』"

    window hide

    pause 0.4

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A6EB165FEA4F43D98FA0D7F5088E39A4 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.8

    window show

    pause 0.3

    rs_character_7009C1117C004F51829614A203C67DE7 "『……我，很喜欢四处探险。』"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "确实。若非如此汝无由与吾相见。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『那、那是四朗的错……』"

    rs_character_7009C1117C004F51829614A203C67DE7 "『可是，我的体力不足，身体也没发育好，有很多地方是去不到的。』"

    rs_character_7009C1117C004F51829614A203C67DE7 "『不过，和九尾一起的话，也许就能去到了。就像之前的湖一样。』"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "有理。驱吾之力如此愿景稍事即可。"

    rs_character_7009C1117C004F51829614A203C67DE7 "『这是我的梦想，能看到谁也不知道的、\n谁也为之赞叹的美妙景色。所以，九尾是必需的。』"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "如此所言，吾之用处仅剩于此，实乃悲伤之事。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『不、不要说得那么露骨。还、还是……有喜欢的地方的。』"

    rs_character_7009C1117C004F51829614A203C67DE7 "『比起一个人旅行，肯定和九尾一起更有趣。景色当然是要和别人一起看的。』"

    rs_character_7009C1117C004F51829614A203C67DE7 "『所以……"
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_92A94B815A0F4834897B355406969B5F as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    extend "以后也要一直在一起哦。』"

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_AFC74CA3A841436580FD0BAB259E1E86 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "呼呼。可爱小童之约怎可拒绝。定可令汝目睹无从忘却之景。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    rs_character_7009C1117C004F51829614A203C67DE7 "『哇——！好高兴哦！我会期待的哦。约好了哦，九尾！』"

    window hide

    pause 0.6

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1B04937674574C949F5F45A3B3BC8B6B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 1

    if sys_music_current_file != "sound/BGM/Strange idea.ogg":
        play music "sound/BGM/Strange idea.ogg" loop
        $ sys_music_current_file = "sound/BGM/Strange idea.ogg"

    window show

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "（哭）。太过分了！真是太过分了！我被玩弄了！\n而且那个孩子还没付钱！！！"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "和那种时间短的比起来，这种强行中断的性质更恶劣！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "这股冲动现在该怎么处理！！这种……就像个笨蛋！！（哭）。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1B04937674574C949F5F45A3B3BC8B6B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_4DCC3C577A8D48B2BBAD4A0EEFF2D0AB "啊……师父，完全被打击到了呐。"

    rs_character_EB1A89F4BFB24C708DBFFE2AD9447ED9 "之前还是人妖CLUB的妈妈桑。\n就是那里破产后迷茫街头之时才走上这条道路的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_104C616BEBAF48D8B6DC31A70290659F "噫——！！那个令人生厌的小子，都怪他在同一幢楼里\n开了家一模一样的店，要不然现在肯定业务还很好的！"

    rs_character_4778F2D7D27E4FBDB716AC22DAA81470 "受过很多苦的样子呐……我们好像也能明白……"

    rs_character_4DCC3C577A8D48B2BBAD4A0EEFF2D0AB "师父，请放下过去重整心情。下一件工作需要做了。"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "连休养生息的时间都没有……但这只能这样，这就是我选择的道路。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_1B04937674574C949F5F45A3B3BC8B6B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_104C616BEBAF48D8B6DC31A70290659F "好，工作是？"

    window hide

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_7662CADE8A614BF4A4CEFF3DAB9450A7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.6

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg"

    rs_character_4DCC3C577A8D48B2BBAD4A0EEFF2D0AB "这个箱子好像是古时传说的有诅咒的箱子，\n过去还没什么问题，好好被封印着……"

    rs_character_4DCC3C577A8D48B2BBAD4A0EEFF2D0AB "最近好像封印的效力减弱了，所以想请我们重新封印。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "啊～好好，原来如此，很常见的模式。无非就是想要图个安慰什么的。"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104C616BEBAF48D8B6DC31A70290659F "撕下所谓的古时候的封印换上新的就行了。\n刷刷刷地就完事了，"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "好，弄好了！"

    rs_character_104C616BEBAF48D8B6DC31A70290659F "箱子的话这次就没什么折扣了。对了，这个工作是何处来的？"

    rs_character_4DCC3C577A8D48B2BBAD4A0EEFF2D0AB "啊，是一所初高中一贯的男校。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "在我们业界很有名的"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    extend "{size=28}那・{/size}{w=0.2}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    extend "{size=28}地・{/size}{w=0.2}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    extend "{size=28}方{/size}。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    rs_character_104C616BEBAF48D8B6DC31A70290659F "什么！！既然如此我必须直接送过去！哇哈哈哈哈！"

    window hide

    pause 0.5

    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    window show

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_450F7105136E4BF69CF26683BE486FC1 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『唔……？』"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "怎么了？"

    show rs_image_92A94B815A0F4834897B355406969B5F as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『不，无甚。』"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.6

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "（似有怪异之气。然终究不配与吾为敌……）"

    call scb_flag_title_end(2, _("「狐的报恩」")) from _call_scb_flag_title_end_16

    if judge_lm_condition([]):
        jump block_00003B9C

    return

label block_00003B9C:
    # Node: 00003B9C (Phase: 0)
    $ C2S5Phase = 0
    if Chapter <> 2:
        $ del C2S5Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_00003B97
    if judge_lm_condition([]):
        jump block_00003B9E

    return

label block_00003B97:
    # Node: 00003B97 ()

    return

label block_00003B9E:
    # Node: 00003B9E (FINISH)
    $ C2S5 = True
    $ TalkSumoRikuF5After = True

    if judge_lm_condition([]):
        jump block_00003BA1

    return

label block_00003BA1:
    # Node: 00003BA1 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_19

    if judge_lm_condition([]):
        jump block_00003B97

    return

