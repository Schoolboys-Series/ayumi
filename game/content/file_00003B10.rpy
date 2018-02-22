# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003B10 (FLAG: RUN-RUN-LOVERS)

label block_00003B11:
    # Node: 00003B11 ()

    if judge_lm_condition([]):
        jump block_00003B14

    return

label block_00003B14:
    # Node: 00003B14 (Phase: 99)
    if Not(VarExists("TalkOkajimaKojimaF3")):
        $ TalkOkajimaKojimaF3 = False
    if Not(VarExists("TalkSaburoF3")):
        $ TalkSaburoF3 = False
    if Not(VarExists("TalkTomoF3")):
        $ TalkTomoF3 = 0
    if Not(VarExists("C2S3Phase")):
        $ C2S3Phase = 0
    $ C2S3Phase = 99

    if judge_lm_condition([]):
        jump block_00003B13

    return

label block_00003B13:
    # Node: 00003B13 (F3 START)
    call scb_flag_title(2, _("「RUN☆RUN☆LOVERS」")) from _call_scb_flag_title_2

    if judge_lm_condition([]):
        jump block_00003B12

    return

label block_00003B12:
    # Node: 00003B12 (LO-LO-LOVERS 1)
    $ set_window("イベントモード")
    pause 1.2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.8

    window show

    if sys_music_current_file != "sound/BGM/Daily 2.ogg":
        play music "sound/BGM/Daily 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 2.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_33665B8748114E3689513AC58C58D121 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……{w}怎么可以这样……"

    pause 0.3

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 400
    show rs_image_A6E2B83133264FE2AC7ED2F9767DAB76 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯！这个、也只能说是相性不好了……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F22822BF03BF404AA4D836728AC17B45 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "不带这样的！！！是我的错喽？？？\n是我做了那么恶劣的事！？？"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不，不是那个意思。嘛，木村亲没做错什么。\n虽说没做错什么……就只是相性不好而已。"

    pause 0.25

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_08C43A31F7C049DDB885DFB2FB7A471D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "（……嗯？这难道是个……）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_AB41A71939D74FEFBF321DA64B8AFC35 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊——我本来很期待的！\n以后再也不想要这样的恋爱了！"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D648DEFEBFB849EDABEC0C42208FB02C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_59AAF132B57B402BB1B9171904F5D5B2

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "总问言之就是想做！就是要干！\n得找个释放欲望的对象！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "（嗯嗯，这个势头很不错哦～）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "在听人说话嘛吗奥村同学？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "抱歉，木村亲！突然想起了点急事！！\n我得先离开了！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F22822BF03BF404AA4D836728AC17B45 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "诶！？等等！至少给我点建议！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3B13044431874BE09020F9368D6A8C29 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "没关系没关系！肯定很快就能找到新的对象的！！"

    show rs_image_AB41A71939D74FEFBF321DA64B8AFC35 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那我先走了！"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_33665B8748114E3689513AC58C58D121 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……新的对象……哈……算了。\n"
    show rs_image_C9317C0E65354F3E9224B31EF2E574BD as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……我也换个地方好了。"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003B15

    return

label block_00003B15:
    # Node: 00003B15 (CP2 Daytime 慎太郎)
    call block_00000C25 from _call_block_00000C25

    if judge_lm_condition([]):
        jump block_00003B1A

    return

label block_00003B1A:
    # Node: 00003B1A (LO-LO-LOVERS 2)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    stop music fadeout 1
    $ sys_music_current_file = ""

    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ set_window("イベントモード")
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_51D4DEBA46FA459DA3B4413148F30900 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_8C8329CA4FC34C279A723168C0AA6CC0 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.2

    if sys_music_current_file != "sound/BGM/Flurry 2.ogg":
        play music "sound/BGM/Flurry 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 2.ogg"

    pause 0.4

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "伊藤酱{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "伊藤酱{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "伊藤酱————！！"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "怎么了{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "怎么了{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "怎么了！？"

    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "其实，木村亲他……！！\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_D88BEA8DA4D145D5B87F3A179B88BE87 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哦不好，随便说别人的八卦可是很失礼的。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "诶？什么东西……木村到底怎么了？？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀，啊哈哈哈～果然什么都没有发生哦～♪"

    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    show rs_image_C2D928E50B6A4036912698848DAC99D0 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_F5B3A302BF394B7D97ED83BF270F3B88 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_C2D928E50B6A4036912698848DAC99D0 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_710A38AC94C841779DB701B5AC1010FD "说！绝对发生什么了那家伙，是什么！？说！\n木村他！？到底怎么了！！！"

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    show rs_image_F5B3A302BF394B7D97ED83BF270F3B88 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_72C7208BCF0A400195B83FAF43272EFD as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_59AAF132B57B402BB1B9171904F5D5B2

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "喘、喘不动气了！！\n别、别勒我！！认输！我认输！！！"

    pause 0.45

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window hide

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.6

    window show

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_D88BEA8DA4D145D5B87F3A179B88BE87 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼……哈……\n"
    if sys_music_current_file != "sound/BGM/Daily 2.ogg":
        play music "sound/BGM/Daily 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 2.ogg"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "直、直接找木村亲问的话他不就会告诉你了吗？"

    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "直白了说，去找木村亲随便聊点什么，\n那样谈话不就好好进行下去了嘛。"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "那、那是什么意思啊……现、现在直说不就好了……"

    show rs_image_A15B5B9C211846009204F1689FC8781E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不——要！仔细想想，绝对是伊藤酱亲自去找木村亲问更好！！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 0
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_07EEAD26B9C44798806C86D199A70194 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "所以说去！不要害怕大胆上！！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "哈？什么意思。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 0
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_002A89DFBF4D4BD99E942D6EA4C98777 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我也是为了伊藤酱好啊！！！行了行了，赶～紧～去～！！！"

    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "我、我明白了，真是的。去就好了，去就好了。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_07EEAD26B9C44798806C86D199A70194 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊！等等，绝对别把我供出来，不能说从我这里走漏的消息哦！？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "自然点以“最近怎么样？发生什么了吗？”之类的话开场，别弄错了哦！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_710A38AC94C841779DB701B5AC1010FD "……"

    window hide

    pause 0.4

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    $ set_window("イベントモード")
    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_44139882A2934049BD03747ECC64C40D as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B


    if judge_lm_condition([]):
        jump block_00003B18

    return

label block_00003B18:
    # Node: 00003B18 (Atrium 慎太郎)
    $ sys_lm_menu_item = [{"pos": (328, 181),"image": "images/Chapter 2/Menu/F3/Shintaro.png","hover": "images/Chapter 2/Menu/F3/Shintaro hover.png","name": "慎太郎"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_8
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B27
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00003B17

    return

label block_00003B27:
    # Node: 00003B27 (LO-LO-LOVERS 3)
    $ set_window("イベントモード")
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1.3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 1

    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 1

    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 1.4

    show rs_image_531E9A5102504415AD59CA198E9086DB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_C46634B9C9074ACF920FA6C4B088E135

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "不管是楼梯间还是别的地方都不在。\n真是的，到底去什么地方了？"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Toilet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Toilet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Toilet 1.ogg"

    show rs_image_98508F03C2B54E6595F99F669212CD79 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_531E9A5102504415AD59CA198E9086DB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 1.5

    stop effect fadeout 2
    $ sys_effect_current_file = ""

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_51D4DEBA46FA459DA3B4413148F30900 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_297E564A7C1544469FB88A41AB85B6C9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    pause 0.7

    window show

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_C9317C0E65354F3E9224B31EF2E574BD as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……呼。{w=0.3}\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_F82BC248415F46ACBF47A770CDE09E67 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "啊……好、好啊，伊藤。"

    if sys_music_current_file != "sound/BGM/Afternoon.ogg":
        play music "sound/BGM/Afternoon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Afternoon.ogg"

    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "木村～总算找到了。你藏在厕所里干什么呢。"

    show rs_image_90F6FB714E4147838D8ADFBBCA0DAD3C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_E3F6ADD43DE44A428E1224756613C694 "有、有点小事。"

    show rs_image_98508F03C2B54E6595F99F669212CD79 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "为什么脸红？发烧了？？没事？？"

    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔——真失败……\n作为田径部经理我竟然连选手身体有恙都察觉不到……"

    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "没、什么事都没有！真的没关系的放心就好！"

    show rs_image_98508F03C2B54E6595F99F669212CD79 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "真的？算了，没事就好。"

    show rs_image_D3B5E9C8BFE741C7984F78EC2C463ECC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "身体就算没问题好了，精神方面要是有什么问题也是很麻烦的。"

    show rs_image_D7BB405DB3414FDEBB860FB2D50A49B9 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "类似那种烦心事干脆都说出来就好，\n我会听着的，轻松一下也没什么不好。{w=0.3}{nw}"
    show rs_image_F7D7B352CD83455890C4C8C5271F3058 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend ""

    show rs_image_F82BC248415F46ACBF47A770CDE09E67 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……啊——也是呐。既然如此伊藤也听听好了。"

    show rs_image_D76820B84EB8486B8205116A7D46FEFC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯。是什么？说什么都行。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_0FEF4A90E57948179FD23929AD85763D as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "嗯？你刚说“什么都行（务必）”了？"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "这个段子已经老过头了……赶快说。"

    show rs_image_F82BC248415F46ACBF47A770CDE09E67 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊，嗯……{nw}"
    stop music fadeout 2
    $ sys_music_current_file = ""

    extend "其实我……"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "和前任分手了。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "欸？"
    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "真……真的假的！！？"

    if sys_music_current_file != "sound/BGM/Flurry 1.ogg":
        play music "sound/BGM/Flurry 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 1.ogg"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_33665B8748114E3689513AC58C58D121 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呜……"

    show rs_image_3B561EDD5FE14AB3949693F15E6C2035 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "为什么！？你……你之前不是说都连亲亲都做过了吗！"

    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哈……和奥村同样的反应……这个，真的必须解释？"

    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯、嗯，如果可以的话，请务必。"

    show rs_image_E8124A11D49145D0AE386AB993200B49 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "总之，就是太着急了。对面似乎不是很对这个感兴趣的类型啊。"

    show rs_image_33665B8748114E3689513AC58C58D121 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "花了好久才终于亲上，我觉得既然都做到这一步了，\n肯定会想直接一冲到底做到最后一步的对不对？"

    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "诶？最、最后一步是……"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……H？"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……"
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_12C16002CB7242BA9D0C2BD3BC6B40C2 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "是啊！就是H！SEX！！！\n我就是想和他做怎么了！！！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "声、声音太大了你个笨蛋！！"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_0FEF4A90E57948179FD23929AD85763D as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "确实，我的做法是有些强硬……也许是积累太多了的原因。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D648DEFEBFB849EDABEC0C42208FB02C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "可是啊，对于恋人来说这很普通对不对？\n既然亲嘴OK的话那个不也该OK才对吗！？！？"

    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯？{w=0.3}嗯……{w=1}嗯？"

    show rs_image_33665B8748114E3689513AC58C58D121 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "所以，直白说了"
    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "……{nw}"
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_90F6FB714E4147838D8ADFBBCA0DAD3C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "“想做”后，那孩子突然就哭了……"
    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_AB41A71939D74FEFBF321DA64B8AFC35 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "“这不是人家理想中的交往！分手！”直接朝我这么喊了！！！"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "为什么！为何会变成这个样子！！根本不明所以——！！！"

    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "啊……原来是想要柏拉图式的精神恋爱啊。"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_D648DEFEBFB849EDABEC0C42208FB02C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "不不不，又不是小学生！有什么顾虑？！"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_710A38AC94C841779DB701B5AC1010FD "{size=14}（哈……好羡慕。）{/size}"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_0A09C10186E9411AA23729763A351890 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "确实，完全不可理解，那个人。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_AB41A71939D74FEFBF321DA64B8AFC35 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "是不！？太好了～！伊藤能明白我的心情！！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3B561EDD5FE14AB3949693F15E6C2035 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_710A38AC94C841779DB701B5AC1010FD "{size=14}{color=#C0C0C0}（居然连木村都会拒绝，那个人也是，太废了！）{/color}{/size}"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_0A09C10186E9411AA23729763A351890 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔，那种类型真令人火大……！"

    show rs_image_82BA14DF187F4770B2333382BE5C5B0C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦哦，很气人！！\n"
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "等等，伊藤，你为什么会这么……？"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3B561EDD5FE14AB3949693F15E6C2035 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_710A38AC94C841779DB701B5AC1010FD "{size=28}（我也……我可也……我也一直对你！！）{/size}"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_0A09C10186E9411AA23729763A351890 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "连木村的帅气之处都察觉不到，简直是个大笨蛋……"

    show rs_image_F82BC248415F46ACBF47A770CDE09E67 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸，哦、哦，谢……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_0A09C10186E9411AA23729763A351890 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    rs_character_710A38AC94C841779DB701B5AC1010FD "哈……哈……"

    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "伊、伊藤？怎么了？还好吗？？"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "我……我可也是……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "嗯？"

    rs_character_710A38AC94C841779DB701B5AC1010FD "我……我……啊啊……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "怎、怎么了？？伊藤？伊藤！"

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 0
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔————！！！{w}\n{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 1.png
    $ zorder_rs_image_7D1E6CD76A3F4377B4251D3865FE5B7C = -100
    show rs_image_7D1E6CD76A3F4377B4251D3865FE5B7C as rs_image_7D1E6CD76A3F4377B4251D3865FE5B7C zorder zorder_rs_image_7D1E6CD76A3F4377B4251D3865FE5B7C onlayer master
    hide rs_image_7D1E6CD76A3F4377B4251D3865FE5B7C

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_7D1E6CD76A3F4377B4251D3865FE5B7C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "我也、我也想！和你做那种事情啊！！"

    rs_character_710A38AC94C841779DB701B5AC1010FD "就、就是说！！想做！！！！！\n我！！和木村！！！啊……呜……！！！"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸？不是……？肯定不是真的！！开玩笑的吧！"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊哈哈～吓我一跳！\n伊藤居然也会开这样的玩笑，真是意外！"

    rs_character_710A38AC94C841779DB701B5AC1010FD "才、才才才才不是！！不是说笑！！呜……给、给我过来！！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    stop music fadeout 0.4
    $ sys_music_current_file = ""

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸？呜哇！！"

    if sys_effect2_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    pause 0.8

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1C833F0E5AB54E79BCEE6017035686BE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 0.8

    window show

    if sys_effect_current_file != "sound/Effect Sound/Worried 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Worried 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Worried 1.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "真、我是真心的……！想、想和木村……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "伊、伊藤……（吞口水）。"

    stop effect fadeout 0.4
    $ sys_effect_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    window hide

    pause 3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_531E9A5102504415AD59CA198E9086DB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_297E564A7C1544469FB88A41AB85B6C9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_DB38897E47104CBDB5C47922CC6869D1 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_90F6FB714E4147838D8ADFBBCA0DAD3C as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window show

    pause 0.4

    rs_character_7DAD4CE5E17E4F44BB8A78EA7CC54328 "……"

    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "回教室吧？"

    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦、哦……"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    window hide

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 2

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_46B09605979B44EBA877032E0832F21E as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_12E394DC341C4685AB17E83FEED856C9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_D76820B84EB8486B8205116A7D46FEFC as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window show

    pause 0.3

    rs_character_710A38AC94C841779DB701B5AC1010FD "奥、奥村……！啊，哈。能、能打扰一下吗？"

    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "别来无恙啊！伊藤酱。怎么了？\n看上去像发生了什么好事情的样子哦？"

    show rs_image_345057B7305848F5BDB887834F34062E as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "欸、嘿嘿。其实啊，我和木村……"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.2

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D3B5E9C8BFE741C7984F78EC2C463ECC as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦、哦哦！真的呀！！！很能干嘛伊藤酱！！"

    if sys_effect_current_file != "sound/Effect Sound/Trumpet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    show rs_image_8C8329CA4FC34C279A723168C0AA6CC0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "恭喜！！恭喜！！！单恋这么久终于得到回报了！！"

    show rs_image_345057B7305848F5BDB887834F34062E as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "哈哈……谢谢。\n以后要是再发生点什么我还会来商谈的……那等会见！！"

    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "Aye aye sir～♪"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_46B09605979B44EBA877032E0832F21E as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼姆～♪伊藤酱看上去真的很高兴呐～恋爱真好～！"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "祝两人能永远幸福在一起！南无南～无♪"

    window hide

    pause 0.5

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Class bell 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.7

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.7

    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.7

    show rs_image_297E564A7C1544469FB88A41AB85B6C9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 1

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 2.png
    $ zorder_rs_image_9CFDDCA65C8A45049A67D61DA2BEBB7B = -100
    show rs_image_9CFDDCA65C8A45049A67D61DA2BEBB7B as rs_image_9CFDDCA65C8A45049A67D61DA2BEBB7B zorder zorder_rs_image_9CFDDCA65C8A45049A67D61DA2BEBB7B onlayer master
    hide rs_image_9CFDDCA65C8A45049A67D61DA2BEBB7B

    show rs_image_9CFDDCA65C8A45049A67D61DA2BEBB7B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 0.5

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "伊藤，能、能再来一次吗？"

    rs_character_710A38AC94C841779DB701B5AC1010FD "又来了啊～确实，你的性欲真的很强，所以体毛才会这么浓？"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "不、不用你操心。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "不过，一直都只是你帮我做，那个……{w}我什么都不做也可以吗？"

    rs_character_710A38AC94C841779DB701B5AC1010FD "诶！？不，那个……我、我就算了！\n我是……那个……{color=#FF0000}专门给别人做{/color}的！"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "这样？……那就好。"

    rs_character_710A38AC94C841779DB701B5AC1010FD "（一时控制不住说了奇怪的话……"
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "可一直这个样子，简直就像……）"

    window hide

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    window show

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_9387C2EF08BB4EFABA360A19A1E02C8B as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_51D4DEBA46FA459DA3B4413148F30900 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸～真的在各种做啊，你们这对变态情侣！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "不、不用你管！这样……就算是这样也没什么不好！"

    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嘛，说的也是。"

    show rs_image_12E394DC341C4685AB17E83FEED856C9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "话说回来，基本没怎么听你提起过约会的事情啊，那方面没关系吗？"

    show rs_image_DB38897E47104CBDB5C47922CC6869D1 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "约会……这么一说，好像还从来没有过呢。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_D88BEA8DA4D145D5B87F3A179B88BE87 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊？！是、是这样！？这有点……"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嘛算了，这种情侣也是有的吧……{w=0.5}大概。"

    show rs_image_51D4DEBA46FA459DA3B4413148F30900 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯，就是这样。\n说起来，最近，还有一个不知道如何解决的事……"

    show rs_image_40F4B3A56AFE46FCB14F4500CD625791 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦哦！是什么呢，说来听听。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "要亲吻的话……挑什么时机比较合适？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F5B3A302BF394B7D97ED83BF270F3B88 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呃？你们没亲过？！"

    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……肯定是想做的。\n可完全不知道该怎么说出口……很不好意思的。"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "诶……呃……可、可是，你们都已经H过了？"

    show rs_image_DB38897E47104CBDB5C47922CC6869D1 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "啊——嗯。一直都是我帮他做完就结束了。"

    show rs_image_08C43A31F7C049DDB885DFB2FB7A471D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……那个时候说不就好了？\n你想，首先从拥抱开始，按慢慢顺序来？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "不太一样，我们的情况是，首先拉下内裤，我再给他口……"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D88BEA8DA4D145D5B87F3A179B88BE87 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "等、先等下！先解释一下！你们一直都是在什么地方H的？"

    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……学、学校的……厕所。"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "伊藤酱难道没去过木村亲的家里？？"

    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "还没有。"

    show rs_image_D88BEA8DA4D145D5B87F3A179B88BE87 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈……嗯……唔……"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "没、没关系的，伊藤酱！亲吻什么的很简单♪\n说不定什么时候木村亲就会主动想做了也说不准哦！"

    show rs_image_D3B5E9C8BFE741C7984F78EC2C463ECC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "是、是嘛。那家伙确实也有经验呐！\n"
    show rs_image_D76820B84EB8486B8205116A7D46FEFC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "谢了，奥村！回见！"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    show rs_image_E435B1F7BF9B4AB280BA8F0C6B392FB1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔……这个样子，简直就是……"

    stop music fadeout 1
    $ sys_music_current_file = ""

    window hide

    pause 1.4

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 400
    $ zorder_tag_F7FA86CC15A84129AD8823E67B40BF5D = 400
    $ zorder_tag_A2C7502F2E8A4813A2C0B55096B32ADE = 300
    show rs_image_F82BC248415F46ACBF47A770CDE09E67 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_F7FA86CC15A84129AD8823E67B40BF5D at right_top zorder zorder_tag_F7FA86CC15A84129AD8823E67B40BF5D onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_A2C7502F2E8A4813A2C0B55096B32ADE at center_bottom zorder zorder_tag_A2C7502F2E8A4813A2C0B55096B32ADE onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_E3F6ADD43DE44A428E1224756613C694 "伊藤，现在……行不？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_75C80A83F7F041D68B6E846A9F01B148 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_F7FA86CC15A84129AD8823E67B40BF5D zorder zorder_tag_F7FA86CC15A84129AD8823E67B40BF5D onlayer master
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_A2C7502F2E8A4813A2C0B55096B32ADE zorder zorder_tag_A2C7502F2E8A4813A2C0B55096B32ADE onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_E3F6ADD43DE44A428E1224756613C694 "开始之前……最近那个拜托了。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_82BA14DF187F4770B2333382BE5C5B0C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_F7FA86CC15A84129AD8823E67B40BF5D zorder zorder_tag_F7FA86CC15A84129AD8823E67B40BF5D onlayer master
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_A2C7502F2E8A4813A2C0B55096B32ADE zorder zorder_tag_A2C7502F2E8A4813A2C0B55096B32ADE onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_E3F6ADD43DE44A428E1224756613C694 "伊藤，一起去厕所吧～"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_F7FA86CC15A84129AD8823E67B40BF5D zorder zorder_tag_F7FA86CC15A84129AD8823E67B40BF5D onlayer master
    show rs_image_D138810390DC4843A14969EAD39A7E06 as tag_A2C7502F2E8A4813A2C0B55096B32ADE zorder zorder_tag_A2C7502F2E8A4813A2C0B55096B32ADE onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呀啊～伊藤酱真的好拿手啊！口活好到名器级别。\n我都迷上了♪所以说……"

    if sys_effect_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    hide tag_F7FA86CC15A84129AD8823E67B40BF5D
    hide tag_A2C7502F2E8A4813A2C0B55096B32ADE
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_C29BFF9F2C814823B4B63C9D37A39E79

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Battle 6.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 6.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_72C7208BCF0A400195B83FAF43272EFD as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_C2D928E50B6A4036912698848DAC99D0 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_46726D80EC7B4D48AD2EFED4CDD37F1C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    window show

    pause 0.3

    if sys_music_current_file != "sound/BGM/Flurry 2.ogg":
        play music "sound/BGM/Flurry 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 2.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "这怎么看、我、都是、\n{size=28}木村的{/size}{size=28}{color=#8000FF}性奴隶{/color}{/size}{size=28}不是吗！！！！！{/size}"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "等下等下！冷静下来伊藤酱！！声音太大了！一点都不像伊藤酱了。"

    window hide

    show rs_image_E1008DFA2F09467D84B2358A572E4D70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.8

    window show

    show rs_image_0A09C10186E9411AA23729763A351890 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "就算是我也慢慢觉得有问题了！！\n倒不如说，这肯定不对劲！是不是！？"

    show rs_image_C2D928E50B6A4036912698848DAC99D0 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "奥村你之前察觉到违和感了对不对！？？"

    show rs_image_D88BEA8DA4D145D5B87F3A179B88BE87 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不、那个……虽说是那样可毕竟情侣也有各种各样的……"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不过，既然伊藤酱自己都这个觉得，果然是有问题的吧……"

    show rs_image_3B561EDD5FE14AB3949693F15E6C2035 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "那家伙真的有把我当恋人看！？\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Gun 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Gun 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Gun 1.ogg"

    extend "怎么想也只是把我当成了个{color=#FF00FF}飞〇杯{/color}对不！！"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 400
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_0FEF4A90E57948179FD23929AD85763D as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_72C7208BCF0A400195B83FAF43272EFD as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_C2D928E50B6A4036912698848DAC99D0 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_E1008DFA2F09467D84B2358A572E4D70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    rs_character_710A38AC94C841779DB701B5AC1010FD "“你好歹也是田径部经理，选手下半身的妥善管理\n也不能放松，那就是你的使命。”"
    if sys_effect_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    hide tag_F7FA86CC15A84129AD8823E67B40BF5D
    hide tag_A2C7502F2E8A4813A2C0B55096B32ADE
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_C29BFF9F2C814823B4B63C9D37A39E79

    extend "这么个意思！？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "冷、冷静下来！！谁也没这么说过！！"

    show rs_image_0A09C10186E9411AA23729763A351890 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "我、要是再这么下去，什么时候真的受不了了，\n八成得给他那玩意狠狠来上一口！！"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F5B3A302BF394B7D97ED83BF270F3B88 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "噫！！（胯下一紧）！！！\n明白了！我完全明白了！！"

    show rs_image_D88BEA8DA4D145D5B87F3A179B88BE87 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我会去找木村亲谈谈试探一下\n他到底是怎么看待和伊藤酱的关系的！"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那之后听一下他的想法再下决定好吗！好吗？"

    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……也好。我本人去问的话说不定也不会很好回答。"

    show rs_image_07EEAD26B9C44798806C86D199A70194 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "对对！所以不要再想那些奇怪的事情了！"

    show rs_image_DB38897E47104CBDB5C47922CC6869D1 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "我只是开玩笑……那就拜托了。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A6E2B83133264FE2AC7ED2F9767DAB76 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_F7D7B352CD83455890C4C8C5271F3058 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 1

    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.7

    show rs_image_90F6FB714E4147838D8ADFBBCA0DAD3C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.7

    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.7

    window show

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    pause 0.3

    rs_character_E3F6ADD43DE44A428E1224756613C694 "伊藤是——{w=0.8}{size=28}炮友{/size}。"

    show rs_image_72C7208BCF0A400195B83FAF43272EFD as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "…………"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{size=14}（好孩子的各位，炮友即是sex friend。）{/size}"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "（只为了快感而H的纯粹的肉体关系……\n木村亲居然觉得伊藤酱只是这种程度的……）"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D76820B84EB8486B8205116A7D46FEFC as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.3

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "哈哈哈。那种家伙，{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Gun 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Gun 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Gun 1.ogg"

    extend "{color=#800000}宰了{/color}。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F5B3A302BF394B7D97ED83BF270F3B88 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_D76820B84EB8486B8205116A7D46FEFC as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "等等等等！！！不要太早下结论！！冷静一下！！！"

    rs_character_710A38AC94C841779DB701B5AC1010FD "好的好的，呵呵。对了奥村，我突然想起来一件需要商量的事呐。"

    if sys_effect_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_9C6627EBA4894AB883E9F13296A23034 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_C24B76269DD44146B275B63410BDD8E9 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    rs_character_710A38AC94C841779DB701B5AC1010FD "之前说的那个，一口咬残，你觉得怎么样？"

    if sys_effect2_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    show rs_image_72C7208BCF0A400195B83FAF43272EFD as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "噫——！！等下等下！！不要放弃，还有能做的事的！！"

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7F497F24D349433FB39C83C619E61AB8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D76820B84EB8486B8205116A7D46FEFC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "一定是伊藤酱的告白没能好好传达到，出现了什么恶不必要的误解！"

    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "肯定不会是不把伊藤酱的心意当回事这种的！对方肯定是没有恶意的！"

    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_3B13044431874BE09020F9368D6A8C29 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "你、你看，木村亲这样的，有点天然呆的类型，\n误会的可能性也是很大的对不对！"

    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "所以没关系！！再一次，真真正正地好好传达出去！"

    window hide

    pause 0.4

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_A46E468ABE0345679EB63CE570AD59F9

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 0.5

    window show

    pause 0.3

    if sys_music_current_file != "sound/BGM/Daily 2.ogg":
        play music "sound/BGM/Daily 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 2.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "我……我明明那么喜欢他，他却完全不把我当回事，好不甘心。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯嗯，只要伊藤酱还有那个心情就没有问题！"

    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "再去一次！木村亲也是个善良的人，肯定不会随便践踏伊藤酱的心意的！"

    show rs_image_D7BB405DB3414FDEBB860FB2D50A49B9 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "也、也是。毕竟俗话说，先喜欢上的总是输，\n虽说很窝火，还是得找那个笨蛋从头再来一次。"

    pause 0.3

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼……这次可一定、保佑两个人顺利和好。南无南～无♪"

    window hide

    pause 0.7

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A5B05E7D36FC49258CAE9B6EEA5B58E4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    window show

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_DB38897E47104CBDB5C47922CC6869D1 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_710A38AC94C841779DB701B5AC1010FD "（话又说回来，直接把话说明白基本不可能，想想就觉得不好意思。）"

    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "（不好好考虑一下说辞的话，我就和他之前那个恋人没什么区别了。）"

    show rs_image_98508F03C2B54E6595F99F669212CD79 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "（等等，那个恋人应该就是木村喜欢的类型。记得是……气场很温柔的那种感觉……）"

    show rs_image_D3B5E9C8BFE741C7984F78EC2C463ECC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "（我要是能和那个人变得相似一些的话，木村会不会开始认可我作为恋人了呢？）"

    show rs_image_D7BB405DB3414FDEBB860FB2D50A49B9 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "（好，现在学校里找找类似的家伙，试着参考一下。\n总之以“{color=#FF8080}蓬松系{/color}”男生为目标！）"

    window hide

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B19

    return

label block_00003B19:
    # Node: 00003B19 (CP2 Daytime 伊藤)
    call block_0000102E from _call_block_0000102E

    if judge_lm_condition([]):
        jump block_00003B1E

    return

label block_00003B1E:
    # Node: 00003B1E (LO-LO-LOVERS 4)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1084DAF07A574EC18C0EDEF9E03F423C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.8

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_710A38AC94C841779DB701B5AC1010FD "（唔……真不舒服，那根本那就不是我，和那些天然呆们不同，这根本就是小聪明。）"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_710A38AC94C841779DB701B5AC1010FD "（啊……好无趣。{w}这么在意别人的视线，根本就是我在自惭形秽。）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_E8124A11D49145D0AE386AB993200B49 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呐，伊藤，你今天样子有些不对劲啊，发生什么了？"

    show rs_image_DB38897E47104CBDB5C47922CC6869D1 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_710A38AC94C841779DB701B5AC1010FD "没什么……"

    show rs_image_0FEF4A90E57948179FD23929AD85763D as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "身体不舒服？偶尔和我商量一下也可以啊。"

    show rs_image_5A94C5E893564B9E8154C0AACF4B7DD1 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "你啊，一直都只在关心我们的事，都不怎么表露自己的烦恼呢。"

    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "所以，一直窝在心里也不好，\n"
    show rs_image_7FBD6043466E42E3AC6ECBFECEBB3005 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_51D4DEBA46FA459DA3B4413148F30900 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "诚实一点找我倾诉就可以了呀！"

    show rs_image_D3B5E9C8BFE741C7984F78EC2C463ECC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯……我……还是很喜欢你这种无忧无虑的地方的……"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3B561EDD5FE14AB3949693F15E6C2035 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    rs_character_710A38AC94C841779DB701B5AC1010FD "所以才有问题！木村！！\n你现在，马上说你到底喜欢我什么地方！！"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1084DAF07A574EC18C0EDEF9E03F423C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F22822BF03BF404AA4D836728AC17B45 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸！？喜欢的地方！？？怎么了这么突然！？\n你现在的烦恼难不成是找不到合适的自我定位？"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_F82BC248415F46ACBF47A770CDE09E67 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "不是，可……嗯，也许。那，怎么说？？喜欢什么地方？"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "嗯～是呢……"
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Gun 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Gun 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Gun 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{color=#FF0000}○○○{/color}很拿手。\n从入门开始一点点教会的支配感很让人兴奋哦。"

    window hide

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    if sys_effect_current_file != "sound/Effect Sound/Hit 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_4D8F1D6A70C24A34A3E6C37B69619470 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Hit 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Hit 3.ogg"

    show rs_image_51451FBF94C8444AA5696178E72CE210 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Hit 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 3.ogg"

    show rs_image_E04DFA4059EE40D18051F1CAA5223C75 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 1.5

    if sys_music2_current_file != "sound/BGM/Theme/Schoolboys Theme - Fear.ogg":
        play music2 "sound/BGM/Theme/Schoolboys Theme - Fear.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Theme/Schoolboys Theme - Fear.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_D6ADB3B2DBE647DC91A820FFA6D351E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_C2D928E50B6A4036912698848DAC99D0 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_F22822BF03BF404AA4D836728AC17B45 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_BF9939EFC91941EDBE78E126AA0B953F

    if sys_effect_current_file != "sound/Effect Sound/Thunder 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Thunder 1.ogg"

    window show

    pause 0.3

    rs_character_710A38AC94C841779DB701B5AC1010FD "{color=#FF0000}你个混蛋……下边儿那个还算不错的东西，\n给你变成再也不能用的废物怎么样啊？{/color}"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "噫！！玩笑开玩笑的！！！！那个那个……你的优点你的优点！"

    stop music2 fadeout 0.5
    $ sys_music2_current_file = ""

    pause 0.3

    $ reverse_volume("music", 1)

    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_1084DAF07A574EC18C0EDEF9E03F423C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_E3F6ADD43DE44A428E1224756613C694 "温柔的地方。虽说不是很会察言观色，但认真的一面也非常好。\n能知道最后那条不能跨越的界限……"

    show rs_image_33665B8748114E3689513AC58C58D121 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "还有那个……那个……唔……"

    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔……可以了，谢谢。"

    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦，不客气。怎样？能当做寻找自我的好素材吗？"

    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "完——全不行！虽说也有进一步加强自己的长处的想法，\n可也并不是现在说几句话就能解决的。"

    show rs_image_5A94C5E893564B9E8154C0AACF4B7DD1 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "是嘛。不过，我觉得你像现在这样就很好了，\n不是说某一部分，全部，我都很喜欢哦。"

    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔……{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_DB38897E47104CBDB5C47922CC6869D1 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "是、是吗。"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_F7D7B352CD83455890C4C8C5271F3058 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C2D928E50B6A4036912698848DAC99D0 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "可、可反正我就是个便利的性处理工具而已吧？"

    show rs_image_0A09C10186E9411AA23729763A351890 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "嘴上说“喜欢”，可根本就不是认真的吧！呵！"

    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "为、为何要为那个生气啊？\n道具什么的，我可从来没这样想过。你可是我的好朋友啊？"

    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_710A38AC94C841779DB701B5AC1010FD "朋友……呢。"

    show rs_image_E8124A11D49145D0AE386AB993200B49 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "再说了，那种事，不是你先开口对我说想做的嘛。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3B561EDD5FE14AB3949693F15E6C2035 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "我确实说了……说是说了……可我不是那个意思……"

    show rs_image_F7D7B352CD83455890C4C8C5271F3058 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_E3F6ADD43DE44A428E1224756613C694 "嗯？"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_F6470A84AD8845BE97EAAA615A68C2F5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    extend "呀！？\n伊藤，运动场上的栏杆没全都收起来！"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_F7D7B352CD83455890C4C8C5271F3058 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_F6470A84AD8845BE97EAAA615A68C2F5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_710A38AC94C841779DB701B5AC1010FD "呃……真的。"

    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……肯定又是那些一年级的～你先回去也没关系，剩下的就是经理的责任了。"

    show rs_image_7FBD6043466E42E3AC6ECBFECEBB3005 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "说什么呢，我也要帮忙♪\n总觉得伊藤今天很累的样子，我还是有些担心的哦。"

    show rs_image_D7BB405DB3414FDEBB860FB2D50A49B9 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_710A38AC94C841779DB701B5AC1010FD "……谢了。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    window hide

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_13EBB8F4C25D40BE99634653B5FEC540 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    window show

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_0FEF4A90E57948179FD23929AD85763D as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_E3F6ADD43DE44A428E1224756613C694 "好，这就是全部了。"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_D3B5E9C8BFE741C7984F78EC2C463ECC as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "哦，谢了木村，真的帮大忙了。"

    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "You are welcome！\n啊，这不就是漫画里常见的那种被关在屋里的剧情嘛～♪"

    show rs_image_D76820B84EB8486B8205116A7D46FEFC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "实际上并不会发生。那么不小心的家伙怎么会有呢。"

    pause 0.3

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Key 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Key 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Key 1.ogg"

    pause 0.7

    rs_character_7DAD4CE5E17E4F44BB8A78EA7CC54328 "欸。"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_13EBB8F4C25D40BE99634653B5FEC540 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    window show

    if sys_music_current_file != "sound/BGM/Flurry 1.ogg":
        play music "sound/BGM/Flurry 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 1.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "等、等等！别开玩笑了！？里面还有人！！开门！！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_A3714E6A137141DFB3129AAB260E0111 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哇哈哈哈哈好强！！简直就是奇迹！！\n太那个了——！这种事情居然真的会有啊～！"

    show rs_image_3B561EDD5FE14AB3949693F15E6C2035 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "说什么不着边际的话！！这么下去我们可就会被关到明早了啊！？"

    show rs_image_7FBD6043466E42E3AC6ECBFECEBB3005 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "别那么不开窍嘛，作为现代人，\n手机可是强力的……"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "欸？书包呢？"

    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "搬栏杆的时候因为太碍事就放在社团活动室里了……"

    show rs_image_F82BC248415F46ACBF47A770CDE09E67 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊、啊哈哈，好像是呢。不过，方法总会有的嘛。"

    show rs_image_C9317C0E65354F3E9224B31EF2E574BD as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "就算真的被关到明天也不会有什么大事嘛！"

    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……你啊，最近几天晚上可都是很冷的，会感冒的。\n啊……真是的……不幸。"

    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "没事没事，这也是校园生活中宝贵的体验嘛，\n肯定会变成一个有趣的饭后笑料的♪"

    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "你还真是乐观……哈……嘛，能这么想也能轻松一点。"

    show rs_image_82BA14DF187F4770B2333382BE5C5B0C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "对对！今天就是两人的外宿之夜！！快快乐乐地过就好！"

    window hide

    pause 0.6

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003B1F

    return

label block_00003B1F:
    # Node: 00003B1F (LO-LO-LOVERS 5)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Night insect 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5333E0D1BE9A4EB995FB5238B3E3566A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 2

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    if sys_music_current_file != "sound/BGM/Guitar 2.ogg":
        play music "sound/BGM/Guitar 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Guitar 2.ogg"

    show rs_image_D48DCF4EB71044FB8F5604BD9EE77358 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 0.7

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    show rs_image_F7D7B352CD83455890C4C8C5271F3058 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_5A94C5E893564B9E8154C0AACF4B7DD1 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    show rs_image_D76820B84EB8486B8205116A7D46FEFC as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 0.7

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5A94C5E893564B9E8154C0AACF4B7DD1 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_D48DCF4EB71044FB8F5604BD9EE77358 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    window show

    pause 0.3

    rs_character_E3F6ADD43DE44A428E1224756613C694 "总之先做了个临时床铺，睡觉应该没问题了。"

    show rs_image_82BA14DF187F4770B2333382BE5C5B0C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "都到这一步了，干脆不被发现才好玩嘛♪"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "只要灯开着，夜里巡视的人肯定会发觉……\n"
    show rs_image_DB38897E47104CBDB5C47922CC6869D1 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "啊嚏！"

    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "那就关灯。"
    if sys_effect_current_file != "sound/Effect Sound/Switch 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Switch 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Switch 1.ogg"

    show rs_image_2837EFB33CFE46DB8928FA91D426F820 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "这就没问题了哦♪"

    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "笨蛋……啊，有点冷……"

    show rs_image_E8124A11D49145D0AE386AB993200B49 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "从刚才开始气温果然下降了呢，要不要借我的上衣用？"

    show rs_image_EE9DD9B67FED43F8996CB8973865AD90 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "算了，你要是觉得冷了也不好。"

    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "我没事！稍微冷点完全无所谓！"

    show rs_image_51D4DEBA46FA459DA3B4413148F30900 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "是吗。不过还是算了，作为经理要是让选手感冒了会很过意不去的。"

    show rs_image_75C80A83F7F041D68B6E846A9F01B148 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……"
    stop music fadeout 2
    $ sys_music_current_file = ""

    extend "那……这样？"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 3.png
    $ zorder_rs_image_335BF89B88F641B8B8DB66BE58875FEA = -100
    show rs_image_335BF89B88F641B8B8DB66BE58875FEA as rs_image_335BF89B88F641B8B8DB66BE58875FEA zorder zorder_rs_image_335BF89B88F641B8B8DB66BE58875FEA onlayer master
    hide rs_image_335BF89B88F641B8B8DB66BE58875FEA

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_335BF89B88F641B8B8DB66BE58875FEA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    if sys_music_current_file != "sound/BGM/Guitar 1.ogg":
        play music "sound/BGM/Guitar 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Guitar 1.ogg"

    pause 0.8

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "哇！？你、你在干什么？！"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "密室里只有两人，而且还有床！\n那距离自然会慢慢靠近，逐渐浮现出淫乱的感觉……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "这种展开，小(tong)黄(ren)本(zhi)里经常会有♪"

    rs_character_710A38AC94C841779DB701B5AC1010FD "我、我怎么知道！快放开。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "抱一会又怎么了嘛！至少这样不冷对不对！\n你也没觉得冷对不？？就当是被子。"

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔……嗯……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊——像这样抱着，感觉又想起和那孩子交往时的事来了。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "嘛，一般来说，这种事不是和恋人也不会做的。"

    rs_character_710A38AC94C841779DB701B5AC1010FD "……{w}是啊，一般来说，只会和恋人。{w}\n一直以来在厕所做的那个也是……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸，不对～也不能说不对。但这个和那个还是不一样的，怎么说呢……"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.6

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "不一样？解释一下。"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_F82BC248415F46ACBF47A770CDE09E67 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸？那个，就是说，互相为了满足欲望……？\n你看，性欲毕竟是三大欲求之一嘛。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_7FBD6043466E42E3AC6ECBFECEBB3005 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_E3F6ADD43DE44A428E1224756613C694 "饿了就吃，困了就睡，道理都是一样的……"

    window hide

    pause 0.5

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.9

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "…………"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "伊、伊藤？"

    if sys_effect_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    rs_character_710A38AC94C841779DB701B5AC1010FD "你、你……你这个人……该不会……\n觉得我只是在追求那种无聊的东西……？"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "全、全身都在发抖啊…………你……很冷？"

    window hide

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    pause 0.5

    if sys_effect3_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Impact 2.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 4.png
    $ zorder_rs_image_A3F0B5B71ACF44378505551EAB95D2D5 = -100
    show rs_image_A3F0B5B71ACF44378505551EAB95D2D5 as rs_image_A3F0B5B71ACF44378505551EAB95D2D5 zorder zorder_rs_image_A3F0B5B71ACF44378505551EAB95D2D5 onlayer master
    hide rs_image_A3F0B5B71ACF44378505551EAB95D2D5

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A3F0B5B71ACF44378505551EAB95D2D5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 0.8

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg"

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "我啊！！怎么可能怀着那种无所谓的心情告白！！\n你怎么就是不明白！！"

    rs_character_710A38AC94C841779DB701B5AC1010FD "再、再说了！！\n只是欲求不满我怎么可能会心甘情愿地给连喜欢都不喜欢的人做那个！！"

    rs_character_710A38AC94C841779DB701B5AC1010FD "你觉得我是那种轻浮的货色？\n你觉得我会那么容易就对被别人投怀送抱！？啊！？"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "对、对不起！我、我从没那么……"

    rs_character_710A38AC94C841779DB701B5AC1010FD "混蛋！！越想越觉得烦！！！"

    rs_character_710A38AC94C841779DB701B5AC1010FD "我的感情根本一丁点都没传达到，还把我想成那种货色！！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 4.png
    $ zorder_rs_image_A3F0B5B71ACF44378505551EAB95D2D5 = -100
    show rs_image_A3F0B5B71ACF44378505551EAB95D2D5 as rs_image_A3F0B5B71ACF44378505551EAB95D2D5 zorder zorder_rs_image_A3F0B5B71ACF44378505551EAB95D2D5 onlayer master
    hide rs_image_A3F0B5B71ACF44378505551EAB95D2D5

    show rs_image_A3F0B5B71ACF44378505551EAB95D2D5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_710A38AC94C841779DB701B5AC1010FD "我！！"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 4.png
    $ zorder_rs_image_A3F0B5B71ACF44378505551EAB95D2D5 = -100
    show rs_image_A3F0B5B71ACF44378505551EAB95D2D5 as rs_image_A3F0B5B71ACF44378505551EAB95D2D5 zorder zorder_rs_image_A3F0B5B71ACF44378505551EAB95D2D5 onlayer master
    hide rs_image_A3F0B5B71ACF44378505551EAB95D2D5

    show rs_image_A3F0B5B71ACF44378505551EAB95D2D5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "是真的对你抱有恋爱感情！！\n"
    if sys_effect_current_file != "sound/Effect Sound/Hit 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 3.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 4.png
    $ zorder_rs_image_A3F0B5B71ACF44378505551EAB95D2D5 = -100
    show rs_image_A3F0B5B71ACF44378505551EAB95D2D5 as rs_image_A3F0B5B71ACF44378505551EAB95D2D5 zorder zorder_rs_image_A3F0B5B71ACF44378505551EAB95D2D5 onlayer master
    hide rs_image_A3F0B5B71ACF44378505551EAB95D2D5

    show rs_image_A3F0B5B71ACF44378505551EAB95D2D5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "是带着那种明确的理由和目的和你做那些事情的！！！"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "怎么可能只是因为欲求不满这种粗俗的原因啊！！！！！"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "噫！？对对对、对不起！！！"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 5.png
    $ zorder_rs_image_61A27D51005E46C3BB478FEE8106B863 = -100
    show rs_image_61A27D51005E46C3BB478FEE8106B863 as rs_image_61A27D51005E46C3BB478FEE8106B863 zorder zorder_rs_image_61A27D51005E46C3BB478FEE8106B863 onlayer master
    hide rs_image_61A27D51005E46C3BB478FEE8106B863

    show rs_image_61A27D51005E46C3BB478FEE8106B863 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_710A38AC94C841779DB701B5AC1010FD "……哈……哈……明白了没，笨蛋木村……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "是、是……完全明白……"

    rs_character_710A38AC94C841779DB701B5AC1010FD "也就是说……我……喜欢……你。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……嗯。"

    rs_character_710A38AC94C841779DB701B5AC1010FD "我、我真的很想和你交往。谁都不行，我要你只陪在我身边。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "……唔……"

    rs_character_710A38AC94C841779DB701B5AC1010FD "……你啊，被我用如此重要的心情对待，却在厕所里只想着那种事……"

    rs_character_710A38AC94C841779DB701B5AC1010FD "关于这个，你怎么说……？有什么要辩解的……？"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "诶、那个……{w}能给我点时间吗？好不容易明白你的心情……"

    rs_character_710A38AC94C841779DB701B5AC1010FD "时间，你要多久？"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "一直以来我都只是把你当成最好的朋友，现在脑袋里有点……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "至少，得考虑能不能和你顺利交往下去，至于结果需要在仔细考……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "不可能，我等不了了。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "诶！？"

    rs_character_710A38AC94C841779DB701B5AC1010FD "已经到极限了！！你这种脑袋里空空如也的家伙\n怎么可能考虑得了这么复杂的问题！！"

    rs_character_710A38AC94C841779DB701B5AC1010FD "……想要确认就干脆直接和我交往。\n"
    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 5.png
    $ zorder_rs_image_61A27D51005E46C3BB478FEE8106B863 = -100
    show rs_image_61A27D51005E46C3BB478FEE8106B863 as rs_image_61A27D51005E46C3BB478FEE8106B863 zorder zorder_rs_image_61A27D51005E46C3BB478FEE8106B863 onlayer master
    hide rs_image_61A27D51005E46C3BB478FEE8106B863

    show rs_image_61A27D51005E46C3BB478FEE8106B863 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "绝对不会让你后悔的。"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    window hide

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_53C43FF5997344BAAADBDF967F5E5DBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.3

    rs_character_710A38AC94C841779DB701B5AC1010FD "已经忍到极限了。我已经、一刻也等不了了，我要做你的恋人。"

    rs_character_710A38AC94C841779DB701B5AC1010FD "……已经单恋你这么久，只是一点点任性，满足一下我的要求又怎么了……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "我……我明白了。交往，我和你交往，剩下的就后面再说……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "不过……和你的话，不知为何总觉得……或许……能行吧……"

    rs_character_710A38AC94C841779DB701B5AC1010FD "当然了。我和之前那个人不一样，我们相性很好，我也有这个自信。"

    stop effect2 fadeout 0.7
    $ sys_effect2_current_file = ""

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    show rs_image_2837EFB33CFE46DB8928FA91D426F820 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if sys_effect_current_file != "sound/Effect Sound/Boom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 2.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "{size=28}所以、没关系。绝对会让你幸福的！{/size}"

    pause 0.3

    window hide

    pause 0.6

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_8C5B9D09E3154FABA2E732547E9321D0

    pause 0.7

    window show

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_E3F6ADD43DE44A428E1224756613C694 "你啊……是这么强硬的性格来着……"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "就因为你是个笨蛋，我不主动一点就没下文了！"

    show rs_image_90F6FB714E4147838D8ADFBBCA0DAD3C as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "怎么会——要说现充的经验的话我明明更丰富才对。"

    show rs_image_345057B7305848F5BDB887834F34062E as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "看不明白气氛被分手的家伙还装什么前辈，\n前辈该做的事，你做过几个？"

    show rs_image_F7D7B352CD83455890C4C8C5271F3058 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "嗯……也对啊～{w}……哦。"

    show rs_image_51D4DEBA46FA459DA3B4413148F30900 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "嗯？"

    window hide

    pause 0.4

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 6.png
    $ zorder_rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE = -100
    show rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE as rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE zorder zorder_rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE onlayer master
    hide rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 6.png
    $ zorder_rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE = -100
    show rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE as rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE zorder zorder_rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE onlayer master
    hide rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE

    show rs_image_1C2DDB742E8E4804A215E5C68FF7CBFE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.7

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "保证不会背叛你的誓约之吻。今后，作为恋人，请多多指教了。"

    rs_character_710A38AC94C841779DB701B5AC1010FD "！！？哈……等……哦。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    window show

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_FDFBAD9B5DBD42D1A353D0492FAF5B9F as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哈哈，伊藤本来肤色就白，脸红瞬间就写在脸上了，好可爱♪"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "那，你的回答是～？"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "～～～！！"

    window hide

    pause 0.3

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 7.png
    $ zorder_rs_image_CAB89628D892438290F5EEAEE6FDA3AE = -100
    show rs_image_CAB89628D892438290F5EEAEE6FDA3AE as rs_image_CAB89628D892438290F5EEAEE6FDA3AE zorder zorder_rs_image_CAB89628D892438290F5EEAEE6FDA3AE onlayer master
    hide rs_image_CAB89628D892438290F5EEAEE6FDA3AE

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_CAB89628D892438290F5EEAEE6FDA3AE as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.6

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show center_title (_("彼此彼此……请多多指教了")) as center_title zorder 1000
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 2.5

    hide center_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.2

    $ set_window("イベントモード")
    stop music fadeout 3.5
    $ sys_music_current_file = ""

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_5E3CEBB8F0274753AF8265882C8A0B46

    pause 4

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.8

    if sys_music_current_file != "sound/BGM/To the future.ogg":
        play music "sound/BGM/To the future.ogg" loop
        $ sys_music_current_file = "sound/BGM/To the future.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_0101F60E8D4C4A89BD84419B1BA7FB61 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "典型的吊桥效果呐！！呀～真是太好了！"

    show rs_image_6AFA224BDF2C45518704201E9789649B as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……嗯，真的，从旁人眼光看来或许乱七八糟的，无所谓了。"

    show rs_image_0101F60E8D4C4A89BD84419B1BA7FB61 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "结果，终于是和那家伙开始交往了。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_40F4B3A56AFE46FCB14F4500CD625791 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "吼～吼♪本就没什么基础不稳固就无法成为恋人的制约。"

    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "等开始交往后再一点点稳固根基，也是一个不错的方法哦。"

    show rs_image_185C3E8EC48345399624EAC41C89E140 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……谢谢，奥村这么说的话我更有些自信了。"

    show rs_image_4C1E5313E76B46C7820213CD711B9387 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "啊，对了。这次还有一件想要商讨的事。"

    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯？什么？"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    rs_character_710A38AC94C841779DB701B5AC1010FD "{nw}"
    window hide

    extend "{size=14}关于开发……{/size}{nw}"
    window hide

    extend ""

    pause 0.3

    show rs_image_A3C244E638B14C1D8D471099D0041B0E as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦！！终于这个时刻还是到来了！！！\n好，很好！！老司机会好好教你的！！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_9387C2EF08BB4EFABA360A19A1E02C8B as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那，谁是受？？"

    show rs_image_6AFA224BDF2C45518704201E9789649B as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "……嘛，应该是我。至少，不能影响他在田径场上自由奔跑吧。"

    show rs_image_40F4B3A56AFE46FCB14F4500CD625791 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "原来如此……话说回来，伊藤酱真的是很优秀的经理呐♪"

    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "能考虑到这么仔细的人可是找不出几个的。"

    show rs_image_FEB9C9E997AB414BBA9F8CACC040FC81 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "没、没这种事。我做的都很普通……所以，这次也要拜托你指导了。"

    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯♪记得空出时间哦！\n"
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哦，那位一圈练完回来了哦。"

    window hide

    pause 0.5

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    # Gallery unlock: images/CG/Run-Run-Lovers/Run-Run-Lovers 8.png
    $ zorder_rs_image_E4328112D39C4B68A1C267CCCE49C938 = -100
    show rs_image_E4328112D39C4B68A1C267CCCE49C938 as rs_image_E4328112D39C4B68A1C267CCCE49C938 zorder zorder_rs_image_E4328112D39C4B68A1C267CCCE49C938 onlayer master
    hide rs_image_E4328112D39C4B68A1C267CCCE49C938

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_E4328112D39C4B68A1C267CCCE49C938 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.6

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg"

    window show

    pause 0.3

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说起来他还是很有人气的哦，稍微注意一下比较好。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "欸？注、注意谁！？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "看，那边，是来参观学习的孩子们，\n木村亲的运动装，给他们带来的刺激还是挺大的。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这类事情遇到对胃口的人可是会欲罢不能的，尤其木村亲体型也很好♪"

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔……真的。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呼……好累啊～伊藤，毛巾拿来……\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "……嗯？怎么了？"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_710A38AC94C841779DB701B5AC1010FD "说的是啊，延长距离的话，时间也会变长，\n可放任不管的话，其他的家伙就……"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "怎、怎么了，这家伙。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼呼♪经理也是有很多要考虑的事情的嘛。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那我就先告辞了！你们两位，今后也请一定要幸福哦♪"

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_47EDA5202ED44FEDB4C0ABBE5F35D734 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_1EEC48C516054F7AB9D93B395C0E8776 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.6

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 2

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_B6D2CFDC1CB5407EACD7FBC1D100D198

    call scb_flag_title_end(2, _("「RUN☆RUN☆LOVERS」")) from _call_scb_flag_title_end_2

    if judge_lm_condition([]):
        jump block_00003B20

    return

label block_00003B20:
    # Node: 00003B20 (Phase: 0)
    $ C2S3Phase = 0
    $ del TalkOkajimaKojimaF3
    $ del TalkSaburoF3
    $ del TalkTomoF3
    if Chapter <> 2:
        $ del C2S3Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_00003B24
    if judge_lm_condition([]):
        jump block_00003B21

    return

label block_00003B24:
    # Node: 00003B24 ()

    return

label block_00003B21:
    # Node: 00003B21 (FINISH)
    $ C2S3 = True
    $ TalkIzumiF3After = True

    if judge_lm_condition([]):
        jump block_00003B25

    return

label block_00003B25:
    # Node: 00003B25 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_2

    if judge_lm_condition([]):
        jump block_00003B24

    return

label block_00003B17:
    # Node: 00003B17 (慎太郎)
    $ set_window("(標準)")
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_D64DA6E75BDF4404B914047221EB0B38 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "木村亲应该在二楼楼梯间那里！\n快点上比较好哦♪"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00003B18

    return

