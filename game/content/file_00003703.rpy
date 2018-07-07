# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003703 (FLAG: 大家來相撲)

label block_00003704:
    # Node: 00003704 ()

    if judge_lm_condition([]):
        jump block_00003705

    return

label block_00003705:
    # Node: 00003705 (Phase: 99)
    if Not(VarExists("C1S1Phase")):
        $ C1S1Phase = 0
    $ C1S1Phase = 99

    if judge_lm_condition([]):
        jump block_0000397F

    return

label block_0000397F:
    # Node: 0000397F (F1 START)
    call scb_flag_title(1, _("「大家来相扑」")) from _call_scb_flag_title_1

    if judge_lm_condition([]):
        jump block_00003706

    return

label block_00003706:
    # Node: 00003706 (大家來相撲 1)
    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1

    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    $ set_window("イベントモード")
    pause 0.6

    window show

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_DFF43C28E0D9414492DE4927927BBDBF as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_81D16F74A3C44B8982DB528D7D934850 "班长，听我说。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_8A80B90628C143D1B3A53C71240BBE2D as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好的好的，是什么呢——？"

    show rs_image_6342DEF8AE284F3280186A636EF8A454 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "今天放学前的总结会那时我有想对大家说的事。"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "所以先和班长打声招呼。"

    show rs_image_943958ACE1594083BA9B66D14E70D431 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "和体育委员的工作相关的吗？"

    show rs_image_655BD81414F14C09820C0C956BC1B072 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "不，先看看这张传单。"

    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯——什么什么～"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "『“{color=#FF80C0}御咲市大相扑比赛{/color}”{w}\n不论是孩子还是大人都能参加，大家一起开心起来！』"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "『方式：根据年龄分不同段位的个人战。\n优胜奖金："
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    extend "{size=20}{color=#00FFFF}五万日元（各段位）{/color}{/size}』"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DFF43C28E0D9414492DE4927927BBDBF as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "五、五万！？八年的零花钱……\n"
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "难道说想要大家参加这个比赛吗？"

    show rs_image_29B8A648E5754D2CB7C3C7D85E72E60B as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯嗯！能参加大赛的人越多，最后获胜的机会也就越大。"

    show rs_image_CC45620E61634BCBAE100C11F0CF029B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的。气势和{color=#008080}与二班对战{/color}的时候完全不同呐～。\n仅仅只是因为有奖金，功利的家伙！{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_F87A8299C1A14C6895DFA0B9DD950727 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2028F963C6F041949E94C771B899A6AE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那那，奖金该怎么分！？平分？！平分！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_D225376486A6442D884B00D8B01FDB1E as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嘛，这个等获胜再说。{w}那么，放学时就拜托争取一点时间了！"

    show rs_image_64D8D1E21F7F40938F719E0070CF195B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "义不容辞～！"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.5

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.9

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_8F070BDCB04D4336AC7465096F0E3084 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DFF43C28E0D9414492DE4927927BBDBF as tag_61A891D6A6D047DC93695DA12E13CC75 at right_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    window show

    pause 0.3

    rs_character_81D16F74A3C44B8982DB528D7D934850 "……就是这样，我觉得去参加大会是很好的，大家呢？"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_792B06DE656A4438ACA72247908EF057 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦哦——！有何不可有何不可！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "少年们交缠在一起的裸装场面就在那里，怎么会有不参加的理由！！"

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_1439FC37B6EB4D19A2C3CA56559E02E4 as tag_724406A84D7141298EFF0D864FAE1534 at right_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "居然是那个。"

    show rs_image_D809612C8CDB4FB284662AAF7934647E as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "只要能获胜奖金就能到手，找个专业的来替我们去好了。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_8F070BDCB04D4336AC7465096F0E3084 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_CC45620E61634BCBAE100C11F0CF029B as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DFF43C28E0D9414492DE4927927BBDBF as tag_61A891D6A6D047DC93695DA12E13CC75 at right_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "出现了，只会推给别人的松君！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "明明体型很棒运动也拿手，完全可以算作选手后补的嘛？"

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    show rs_image_3A7E89EDEEA5454B9333DFCC45F75B0A as tag_724406A84D7141298EFF0D864FAE1534 at center_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "欸……我不想有那种挫爆了的经历。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    hide tag_724406A84D7141298EFF0D864FAE1534
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_6FE023B7DF9C43AF8BB8D3CB36E7C410 = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C960A410B16048EF9183EA327408B624 as tag_6FE023B7DF9C43AF8BB8D3CB36E7C410 at right_top zorder zorder_tag_6FE023B7DF9C43AF8BB8D3CB36E7C410 onlayer master
    show rs_image_9E61D0A55E554AAC9894E8AA00A7E5A4 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "唔！这可不能当做没听到啊，松田。相扑装到底怎么挫了？"

    show rs_image_1439FC37B6EB4D19A2C3CA56559E02E4 as tag_6FE023B7DF9C43AF8BB8D3CB36E7C410 zorder zorder_tag_6FE023B7DF9C43AF8BB8D3CB36E7C410 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "啊……不，这是误会，月。\n我的意思是，除了我还有更合适的人选。"

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_6FE023B7DF9C43AF8BB8D3CB36E7C410
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_ECBA0CF7876045D4AE8665A90CDBF4B6 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "确实～要说谁最适合，就像画卷中所绘一样的话……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_131650F3DE4F41EEA1B2254515052B4E as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_9CD3C176C2984BC8A0E4278BB4CFD818 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "除你之外还能有谁！{w}\n所以说，加油阿月！！"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_3CC2CAAD5140495DAF5927162F832557 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "同感。"

    show rs_image_F98CA2A6977F4950A23DA67286D889BA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "我会好好期待的。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C7F47B899A04C1E9877716E2B4CC7B5 "加油——！！力士——！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_7C7F47B899A04C1E9877716E2B4CC7B5 "拿出你的剑道精神！剑道精神！"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_9ABA8E855F5D4363AA61610B30E5ACB1 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我、我……\n大家都如此认为的话，我会接受的。"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_FFF830B97C0146FD92D3A791B1913CEA as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……加油哦，哥哥。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_8F070BDCB04D4336AC7465096F0E3084 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_52907CFE4828483C99DC76C46D873DD0 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    rs_character_81D16F74A3C44B8982DB528D7D934850 "啊……"
    show rs_image_90E48F9CDC734D43AD577A32B4E6F01F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "咳、咳咳！这里就拜托给月好了。"

    show rs_image_173B284E6DC843AF812C237128860894 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "其实啊，我一开始觉得松田啊，绫濑啊，{w}\n以及，空！都是很合适的人选！"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "可现在当然就只能决定是月了……\n"
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_554DE31DA9EA412EB667D4EF459DEFDC = 200
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8092DF33E83946BBBB08607F3AE764C2 as tag_554DE31DA9EA412EB667D4EF459DEFDC at right_top zorder zorder_tag_554DE31DA9EA412EB667D4EF459DEFDC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "对不对，班长！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶？嗯、嗯。\n{w}……刚才发生什么了？"

    show rs_image_173B284E6DC843AF812C237128860894 as tag_554DE31DA9EA412EB667D4EF459DEFDC zorder zorder_tag_554DE31DA9EA412EB667D4EF459DEFDC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "不，没什么……"
    hide tag_554DE31DA9EA412EB667D4EF459DEFDC
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_8092DF33E83946BBBB08607F3AE764C2 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "就这么决定了。\n那么，应援就要拜托大家了！"

    show rs_image_D225376486A6442D884B00D8B01FDB1E as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "顺利得到奖金，一口气用个痛快！！"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Impact 2.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}哦——！{/size}"

    window hide

    pause 0.8

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.5

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_8092DF33E83946BBBB08607F3AE764C2 as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "班长！留步！！"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦、哦。这次又怎么了啊，加藤酱。"

    show rs_image_655BD81414F14C09820C0C956BC1B072 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "那个很不妙啊，非常不妙……"

    show rs_image_8A80B90628C143D1B3A53C71240BBE2D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什、什么啊？"

    show rs_image_6342DEF8AE284F3280186A636EF8A454 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "没注意到？\n那种面色不善萎靡不振的表情……{w=0.65}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    extend "我是说{color=#FF8080}空{/color}……"

    show rs_image_943958ACE1594083BA9B66D14E70D431 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "空？空怎么了？"

    show rs_image_FCAFA927EAA1420E8D01012A37344D27 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "长点心啊班长。\n"
    show rs_image_90E48F9CDC734D43AD577A32B4E6F01F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊～不过，{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "班长不知道{color=#00FFFF}那件事{/color}来着啊……"

    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "？"

    show rs_image_262829AECEA1468AB738E042DA70F096 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "虽说不知道，之前也有{color=#008080}和二班的游泳比赛{/color}来着。{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_16ABF96E559E49FBB84B601A9048F82F as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "空不知为何总是喜欢和作为哥哥的月比较，\n每次都觉得很不甘心的样子。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_8DB9EBBA116648CAAA85C0A0F67B04D2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……啊！是这样！抱、抱歉抱歉。是这个地方想不开啊。"

    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这次果然也觉得很……？"

    show rs_image_655BD81414F14C09820C0C956BC1B072 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯。大家全都一致推崇月，空完全没得到任何关注。"

    show rs_image_6342DEF8AE284F3280186A636EF8A454 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "作为班长，你怎么想？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "现在的班里，就算只有一个人也好，这种有人失落的情况！"

    show rs_image_80AC1FBCF08D4C6283030181039745BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当、当然要做些什么！可是，究竟该怎么做……"

    show rs_image_3F533DA3CF494DEBA1146743852331E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "都已经决定是阿月了，事到如今想要改变选手……。"

    show rs_image_DFF43C28E0D9414492DE4927927BBDBF as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯，所以啊，这里就算是只有我们明白空的心情，"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "也要在紧急时刻做好支援他的准备。"

    show rs_image_28A01C08CFC245F2B5B451B8E36AF5EB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "原来如此！二年一班可是御咲学园最幸福快乐的班级了嘛！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_80AC1FBCF08D4C6283030181039745BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为了不让空失落，我们要在力所能及的范围内尽可能支援！"

    show rs_image_D225376486A6442D884B00D8B01FDB1E as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯嗯。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_3D6A04F77BD14290ACB4CB84A6D7781B as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "总觉得有谁在叫我的样子，是你们？"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E0D00426275740F394D32435264217E5 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_BFC0B3388AA14C13AB88519DEBCF6FA7 as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_81D16F74A3C44B8982DB528D7D934850 "呜哇！啊，空！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没、没有。那个、那个啊！"

    show rs_image_4E534C3CC3ED418EA9C8155C87F1BCBB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对了！我们在想如果有团队战的话，\n小空和阿月一起出场就好了呐！"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_173B284E6DC843AF812C237128860894 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "{size=15}（班、班长干得好！）{/size}"

    show rs_image_FCAFA927EAA1420E8D01012A37344D27 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "对对，到时候会场里很定会出现“哇——双胞胎啊——”这样的盛况的。"

    show rs_image_FFF830B97C0146FD92D3A791B1913CEA as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哈哈，也许吧。我会和哥哥一起加油的。"

    show rs_image_E3117F92902F437EBCACCE96F9CB84FC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不过，是呢……"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_90E48F9CDC734D43AD577A32B4E6F01F as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=15}（啊、啊咧咧！？不会踩到地雷了！？）{/size}"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "{size=15}（交、交给我班长！）{/size}"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_E0D00426275740F394D32435264217E5 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_8A80B90628C143D1B3A53C71240BBE2D as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_173B284E6DC843AF812C237128860894 as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=-50, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "空！我不是很明白相扑不过，应该不只是比体力！虽然我真的不明白！"

    if True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect4 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect4_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_8092DF33E83946BBBB08607F3AE764C2 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "所以说比起月更加敏捷的空说不定更合适什么的。"

    show rs_image_6FBE5139BFEB4724AB6A1B34DD49E654 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊，那个不用担心，瞬间爆发力的话，哥哥比起我要强多了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……"
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "哦，对了！！"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "小空！之前{color=#008080}和慎酱一起去的拉面店{/color}，{nw}"
    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_3EE0D1670313498FBA59858D3D4CA4F3 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    pause

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "\n有时间再去好不好！加藤酱也一起，三人一起！好不好！？"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FCAFA927EAA1420E8D01012A37344D27 as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_80AC1FBCF08D4C6283030181039745BE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_81D16F74A3C44B8982DB528D7D934850 "{size=15}（这个话题和现在完全无关啊？）{/size}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=15}（这就行！不转换话题继续谈下去只会有反效果的！）{/size}"

    show rs_image_52907CFE4828483C99DC76C46D873DD0 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "{size=15}（原、原来如此。）{/size}"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_3D6A04F77BD14290ACB4CB84A6D7781B as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D225376486A6442D884B00D8B01FDB1E as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=-50, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_81D16F74A3C44B8982DB528D7D934850 "对对！三人一起！嗯嗯！大家一起去！{w}我不论何时都站在空这一边哦！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！"

    show rs_image_73F69A7FB68D4D8684029D4486A79854 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "呃、这个……不算是很明白你们的逻辑，不过谢谢。"
    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对了！别下次了，今天就去！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "两人的社团活动结束前我会在小钢琴部消磨时间的！"

    show rs_image_29B8A648E5754D2CB7C3C7D85E72E60B as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "好主意！不愧是班长！呐，空！"

    show rs_image_E0D00426275740F394D32435264217E5 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯，可以哦！\n"
    show rs_image_8AB2D0A532704204BF8A3765D345D6E0 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "既然如此也把哥哥叫……"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_8092DF33E83946BBBB08607F3AE764C2 as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_80AC1FBCF08D4C6283030181039745BE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_907B8C088A814A069D35867C58E3A86C "{size=28}只有我们三个。{/size}"

    show rs_image_6342DEF8AE284F3280186A636EF8A454 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "就这么决定了。"

    show rs_image_28A01C08CFC245F2B5B451B8E36AF5EB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9B9DCA74086B43A197B7D71BB87CC11D as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哦、哦。"

    window hide

    pause 0.6

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Afternoon.ogg":
        play music "sound/BGM/Afternoon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Afternoon.ogg"

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A6EB165FEA4F43D98FA0D7F5088E39A4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_E1008DFA2F09467D84B2358A572E4D70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    window show

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "好咧，久等了！味增拉面，豚骨拉面，酱油拉面！"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "请慢用。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "真、真心赞……{color=#FF00FF}(´艸｀){/color}"
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_D225376486A6442D884B00D8B01FDB1E as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=-50, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_BC8B9AC6BDD34EE7B445866E23D6D5C1 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_11E9CB4CF92548E88CF101664A977D06 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_127E405385CE4B76A1EA75C16E25761B "我开动了！"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "哦哦～空点的豚骨版好棒！不愧是空，有品味！"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_D225376486A6442D884B00D8B01FDB1E as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=-50, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_64D8D1E21F7F40938F719E0070CF195B as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "比起豚骨我更喜欢味增哦——"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_554DE31DA9EA412EB667D4EF459DEFDC = 300
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BFC0B3388AA14C13AB88519DEBCF6FA7 as tag_554DE31DA9EA412EB667D4EF459DEFDC at center_top zorder zorder_tag_554DE31DA9EA412EB667D4EF459DEFDC onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好烫。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_554DE31DA9EA412EB667D4EF459DEFDC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    window hide

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 1.png
    $ zorder_rs_image_D8229CDD6C214636928DC6C6FCFCA4FB = -100
    show rs_image_D8229CDD6C214636928DC6C6FCFCA4FB as rs_image_D8229CDD6C214636928DC6C6FCFCA4FB zorder zorder_rs_image_D8229CDD6C214636928DC6C6FCFCA4FB onlayer master
    hide rs_image_D8229CDD6C214636928DC6C6FCFCA4FB

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_D8229CDD6C214636928DC6C6FCFCA4FB as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.4

    window show

    pause 0.3

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么给加藤君尝一口。请。"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "哦，谢了！空真温柔呐。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（吸——）嗯嗯，我也真的这么认为哦！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "空那种治愈般的气息我很喜欢哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸，真的吗？啊哈哈，会、会不好意思的。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "谢谢。以后要好好加强这个优点呢。"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "（吸——）总是保持着进步之心，我也要好好参考呢。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "真、真是的，两人都抬举过头了，\n现在我没有那么厉害，什么也没得参考的哦？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（吸——）有的话不就可以参考了嘛。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嘛，前提是有的话呐。"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "（吸——）真的很温柔呐～说起来，之前的点心多谢了。"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "老妈说非常好吃。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "真的吗？哇～好高兴～！请帮我转告我很感动哦！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "空做的点心一直很好吃呐～！下次请教教我怎么做！"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "（吸——）空的话，感觉随便教教别人就能学会呐。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯，那下次就在我家。{w}…………{w}这个先不说……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "喂，你们两个，今天到底怎么了？为何一直在想方设法夸我？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_9634AD61C6DB42439EDE1028A82EA8C9 "诶？我们的崇拜发自真心哦？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "是、是吗，是这样就好。{w}（吸……）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "{size=15}（大事不好啊班长，对方好像察觉到什么啦，再自然一些。）{/size}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=15}（是、是呢。）{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说起来，我之前就这么觉得了{size=15}。{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "剑道服上面是白色下面是深蓝色的组合感觉最帅了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯嗯，确实是啊！"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "哦，说起来啊，空的剑道服好像就是这种组合！？不愧是空～！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "果、果然不对劲……\n不，与其说不对劲应该说更不对劲了。"

    window hide

    pause 0.5

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2


    if judge_lm_condition([]):
        jump block_00003707

    return

label block_00003707:
    # Node: 00003707 (大家來相撲 2)
    window hide

    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Manzai.ogg":
        play music "sound/BGM/Manzai.ogg" loop
        $ sys_music_current_file = "sound/BGM/Manzai.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.8

    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "那么那么！现在，御咲市相扑大赛开始了～！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 300
    show rs_image_1561FC74CECA43F896E80A6050FD4EB8 as tag_0C07D2341065492CB0EDF00452D574E1 at right_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "主持是我，陆田！以及……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "来了来了！在下杉本。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    extend "事不宜迟，先从读者来信开……"

    show rs_image_EAA2EF7FB3CF4DC8B7F90D9F76D373E7 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "等下，今天不是演出！我们是作为相扑大赛的主持来的！"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "哦，说起来也是。那么，重来一遍。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "让我们从赞助商……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F68539D279214C24AB4E888AA6B342A0 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "都说了不是演出！"

    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不过那个，开始比预定晚了一些，\n这还是沾了陆田……{w=0.5}{nw}"
    show rs_image_D7FF18D0A8E140CE95D5B9C6EE2CC48D as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不对，好像是我迟到的光……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    if sys_music2_current_file != "sound/Effect Sound/Clap 1.ogg":
        play music2 "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Clap 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=30}啊哈哈哈哈！！{/size}"

    window hide

    pause 0.4

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    stop music2 fadeout 0.6
    $ sys_music2_current_file = ""

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4E74502696E847418F9F14C16FA3311B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_792B06DE656A4438ACA72247908EF057 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀～！！没想到那两位竟然会来御咲市！！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "今天会不会有霸王硬上弓的机会啊！！\n超想摸……不对，握手啊！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_2304A61C05D54DD6B9E15DDB5A3D3949 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_08917E60F7E24896AA5D34106EADD613 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "求你了，别这么露骨，千万别把自己送上新闻社会版。{w=0.3}{nw}"
    show rs_image_D349535598D24CEA9EC5562CF5D3C393 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_57F7A3D31244474680A656FBC7957CCF as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_D809612C8CDB4FB284662AAF7934647E as tag_724406A84D7141298EFF0D864FAE1534 at left_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "不错嘛，会场气氛炒起来了！月！别被气氛影响，三下五除二完事哦。"

    show rs_image_04CE6801CFBD460096381A21558DE1D7 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯嗯，交给我。仔细看好了，一定会让你明白相扑装的帅气之处的。"

    show rs_image_3A7E89EDEEA5454B9333DFCC45F75B0A as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "居、居然还记着那个。"

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_28A01C08CFC245F2B5B451B8E36AF5EB as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D225376486A6442D884B00D8B01FDB1E as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "空！今天一定要成为明星哦！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "加油！"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_9B9DCA74086B43A197B7D71BB87CC11D as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "什么？为何？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_B5266B4702AD4685B763598227C3363A as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at Transform(xpos=-90, yalign=0.0) zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "……嗯？"

    show rs_image_40E483C4D53C4FC98736811ED60C24CC as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "呐，大家！那边不是二班的人吗！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BFC0B3388AA14C13AB88519DEBCF6FA7 as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=0, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_376CA53D8BF64CE497CF774B53A38857 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C960A410B16048EF9183EA327408B624 as tag_724406A84D7141298EFF0D864FAE1534 at Transform(xpos=160, yalign=0.0) zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    show rs_image_9E61D0A55E554AAC9894E8AA00A7E5A4 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=240, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_AB2BF05BDC1F4A03A6AE31A2155DDE4D as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=320, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_E4936993CD54440BBFC2EF0FBF5D4248 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=400, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_BA68039D702C4EA2A6CF95AF1F2E9D2E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=480, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C7F47B899A04C1E9877716E2B4CC7B5 "{size=32}什么——！？{/size}"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_177F59374F16409DB2C167CEC51615A0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊啦，一班的各位。真是超赞的绝望表情啊。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嘛，都看到我们了也难怪嘛。\n不用比结果就已经出来了呐。"

    show rs_image_6DE09DD52652423591DA6B8BC9069B45 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "当然是你们大败。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊啦，二班的各位啊！\n"

    extend "…………（词汇储量不足）。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_08917E60F7E24896AA5D34106EADD613 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "突然来这么一出完全无话可说了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 300
    show rs_image_E644C115F82B4FF7971F3C7A7279D94F as tag_346FE7CD97BB4FB18CB50E78275F4E23 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "呵呵。虽然很抱歉，奖金就由我们二班拿下了。"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_B948584405374875B0548BD5B5989750 as tag_CC4336DE74164173AC47C2C317367F10 at center_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "然后买两张{color=#8000FF}Worversal Studio Japan{/color}的年票在班里互相传着去玩！\n{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{size=15}{color=#C0C0C0}※该组织仅存在于SCB世界中{/color}{/size}"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_4B4CF6F6178F455DBD43D650E8EF05B0 as tag_DCBDF256A1E242E78A25910AE27C0954 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "在班里找到想要一起去的人，一起度过愉快的时光。"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_00E7E377A7304AEDB8426852161513BB as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_710A38AC94C841779DB701B5AC1010FD "……"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_535CA73FE5F041DC934ADD42483CCCF6 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_4E4E0F803024464E912750289454A1EB as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_15C167A596C24CA5ABBDDF10433FFF71

    rs_character_710A38AC94C841779DB701B5AC1010FD "（瞥）"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_4E74502696E847418F9F14C16FA3311B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_FFF830B97C0146FD92D3A791B1913CEA as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哇。听起来好浪漫哦。"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_08C285D4068B443CA62FFF7164C88026 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "每人一次是说，必须去不可……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9C9BE421F7E44A6E9376D93AB2B16371 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "对像我这样不讨人喜欢的某种意义上就是惩罚游戏……"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_3A5FA7C5CE1B4F32887149BCB2FBA0A3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_6DE09DD52652423591DA6B8BC9069B45 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "总而言之，就是这么回事。你们就尽情努力好了，呵呵。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_F25DC387CDE74829BF90A4EF4C34AAAF as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "你们要派谁出场？"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_338FF3739E7848C2944283BC7DDB8ED9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呼呼，我来介绍……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_00D0008B11054042A14DAD5B35850FA9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "二班代表……那身汗味，正是猛男的味道！{w}\n田径部所属・木村君！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3F25FD2AAC994C4D9C20BF33ED9A4117 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "别那么形容别人！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_360023C492FA4C66B98EABE6E39B3FD3 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "如上所述，请多指教！！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_59759FB9DA7E42C1AE0F25BD7F9EB4B2 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "获胜的话，要找谁去比较好呐。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "嗯～{w=0.4}……{w=0.4}……{w=0.4}{nw}"
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_AA33B0FCE2BC4F429904AEEE5D417557 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "伊藤就好了。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_70599C5025FC45F69279010EDB3E637D as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_D474DA018EE64BEABBA0AEC9825003C3 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_710A38AC94C841779DB701B5AC1010FD "……！！"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_D474DA018EE64BEABBA0AEC9825003C3 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "绝对……绝对给我赢啊你个笨蛋！！！"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_2304A61C05D54DD6B9E15DDB5A3D3949 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "吼吼。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_4E74502696E847418F9F14C16FA3311B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_86BB7A17393E4CA3AA3BEA8164C0DA78 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "很抱歉不过，我是不可能输的。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这场比赛，我背负着一班所有人的期待，绝不可能失败！！"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_64D8D1E21F7F40938F719E0070CF195B as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "很好！！不愧是御咲学园的力士代表！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……空也是。"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_8AB2D0A532704204BF8A3765D345D6E0 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊，对了对了，今天好不容易大家来应援，我做了一些点心哦。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "来，请。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C66A56F89C43490FBD87D2164FFD98A5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_F98CA2A6977F4950A23DA67286D889BA as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    show rs_image_29B8A648E5754D2CB7C3C7D85E72E60B as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "谢谢，空。"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "哦哦，不愧是空，真会关照人～"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "哇，很好吃哦！这样一来应援团也有动力了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_ACCBB5778CE64EAE8879E2A479FFD7B8 as tag_2C4A74BADF6540698EF3E9A300893D1A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊，很不错的样子呐～我也想要！{w}\n我们班有没有类似的东西？"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_F333E5317DFA468389E2DA087896D09E as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "啊……嗯……下次我会做的。"

    show rs_image_C64639FE9D59433C9FF31626E4C08405 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸～！你真能做出来？"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_03330D456CDE49F8BA389C403ECD8A56 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "伊藤做点心什么的……哈哈哈！完全不合适——！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_66D9D0432451460BA68E7AAF477C1F70 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "闭嘴傻猫！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_81339CBB1684406EB266897AD5F0330B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "为毛只骂我？！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_7C178421D3DA4E2CB70D4336919888FB "那么那么，各位观众，请跟着陆田君的指示做好准备。"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "继续折腾下去真的好？告诉大家一个小情报，\n别看陆田君这样，发起火来可是很可怕的哦。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "他的巴掌可是有砖头，或者说小型射线那样的威力哦。"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_C0C28FE32BFE40499B29AC9C92887630 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_0D5BC78C8923442DB3E842DF9CA717D4 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "好了，我去了。"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "绝对不会输的！"

    window hide

    pause 0.6

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    pause 1.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC46DBAAAEE24C10AECA19E0EDA27051

    pause 0.7

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_50A435C5B0AC4E28829C9C49CF8DA478 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at right_center zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    pause 0.5

    window show

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "请看！赤峰同学华丽的出招！！"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "他作为剑道部主将，果然脚步就像生根一般无法被撼动。"

    window hide

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 3.png
    $ zorder_rs_image_9ACE399648824FD884F39266417CDDBD = -100
    show rs_image_9ACE399648824FD884F39266417CDDBD as rs_image_9ACE399648824FD884F39266417CDDBD zorder zorder_rs_image_9ACE399648824FD884F39266417CDDBD onlayer master
    hide rs_image_9ACE399648824FD884F39266417CDDBD

    show rs_image_9ACE399648824FD884F39266417CDDBD as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.4

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "这一方则是隶属田径部的木村的攻击，\n他强势压制住对方，果然还是平时锻炼腰部力量的一方更有利！"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "在中学段位比赛里，两人压倒性地击败了所有遇到的对手！！"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "两人的势头会一直贯穿到决赛吗！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Clap 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_140B552F50584401971F8DF480089BE0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "阿月！干得漂亮！！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥加油！！"

    rs_character_710A38AC94C841779DB701B5AC1010FD "木村啊！！你可绝对不能输啊！！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "给他们看看你的毅力——！！"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "观众一方也是盛况空前呐～！！那么请容许我随机采访几位观众。"

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嗯——谁比较好呐……从这位开始！"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_4E74502696E847418F9F14C16FA3311B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_9B9DCA74086B43A197B7D71BB87CC11D as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸，我、我？"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 at right_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_73F69A7FB68D4D8684029D4486A79854 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "刚才“哥哥”这么喊了，选手中的……？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "啊！你是赤峰月同学的弟弟！确实很像呐。{w}\n和帅气型的哥哥不同，气场很温柔呐。"

    show rs_image_20AA9A405C08411899D11DA9EB2EE47D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊，嗯。经常被这么说。"

    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嗯也对～！我的话说起来还是更喜欢弟弟君这种可爱型的呐！"

    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "陆田简直就是反面教材。"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 300
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D7FF18D0A8E140CE95D5B9C6EE2CC48D as tag_0C07D2341065492CB0EDF00452D574E1 at center_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_59AAF132B57B402BB1B9171904F5D5B2

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "给我回来杉本！！别说多余的话！！"

    hide tag_0C07D2341065492CB0EDF00452D574E1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_4E74502696E847418F9F14C16FA3311B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_55BA6F9211CF475F8927D40CFEC977B2 as tag_DFA3500588174872BA20EBF28D506BD4 at right_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_3D6A04F77BD14290ACB4CB84A6D7781B as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "每个人都有不同的魅力才更有趣嘛。"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_52907CFE4828483C99DC76C46D873DD0 as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_9634AD61C6DB42439EDE1028A82EA8C9 "！"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 at right_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_E3117F92902F437EBCACCE96F9CB84FC as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    rs_character_7C178421D3DA4E2CB70D4336919888FB "那么最后，对哥哥说一句鼓励的话！"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_05F784F04C004906B34CE8B18FDE28D3 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥，大家都在关注着哦！当然，我也是一样的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_256DCF0FD3C145C4BFF308F96CE078E2 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我相信哥哥一定能行的！加油！！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_1624997D37FC499DAD5C4C36FF3A0F38 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空……\n"
    show rs_image_B3DAA2550AAE4F9FAE97DA3D43696AFC as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯嗯，必胜！！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_4E74502696E847418F9F14C16FA3311B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 at right_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_E0D00426275740F394D32435264217E5 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "好的，哥哥那边好像也很高兴的样子呐，多谢合作！"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "那么接下来是……"
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "好，就决定是你了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_F36BF6393ED64182944426D6B3A88D37 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "欸？我、我！？"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "刚才对木村同学的应援真是狂热呢…………"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4E74502696E847418F9F14C16FA3311B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_FCAFA927EAA1420E8D01012A37344D27 as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_81D16F74A3C44B8982DB528D7D934850 "那个，班长，空的话应该冷静不下来才对啊？"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_E262B3AC8BDF48E4A8BEEBA281DFA194 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯、嗯……"

    show rs_image_655BD81414F14C09820C0C956BC1B072 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "可是啊，为什么呢，根本没有一丁点兆头啊。"

    show rs_image_90E48F9CDC734D43AD577A32B4E6F01F as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "刚才被主持人那么说，一般情况下肯定会很在意的……"

    show rs_image_EEDE17A0523340C4B70747B46FC7D04C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我也觉得……为什么我们要这么折腾呢。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "有些茫然，不知所措……"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 300
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_A6BDA5B155414D99AB52F15BEBCC03D6 as tag_0C07D2341065492CB0EDF00452D574E1 at right_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "好的，终于到决战了！！\n果然双方和之前预想中的一样呢，杉本先生。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "是啊，两边都异常顺利地一路赢上来的话，\n最后果然就会变成这个样子呢。"

    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "究竟胜利将会花落谁家！？"

    show rs_image_1561FC74CECA43F896E80A6050FD4EB8 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "那么中学段位比赛总决赛即将开始！两位准备好了吗！？"

    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_32514C8811F942ADBFB6E33B2766E3F0 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_1624997D37FC499DAD5C4C36FF3A0F38 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "当然！"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦！"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 300
    show rs_image_09DED7760EFE4B239C4CB18C936E91D7 as tag_0C07D2341065492CB0EDF00452D574E1 at center_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "那么，准备……！"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    extend "开始！！！"

    window hide


    if judge_lm_condition([]):
        jump block_00003708

    return

label block_00003708:
    # Node: 00003708 (大家來相撲 3)
    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg"

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_BB1CA2833FCD4482B4072835E4104A8E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at right_center zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.1

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Boom 1.ogg"

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 5.png
    $ zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 = -100
    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as rs_image_1C9982B11CB6440DBBEE2B161A425C30 zorder zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 onlayer master
    hide rs_image_1C9982B11CB6440DBBEE2B161A425C30

    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.5

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "唔！！"

    if True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect4 "sound/Effect Sound/Boom 2.ogg" noloop
        $ sys_effect4_current_file = "sound/Effect Sound/Boom 2.ogg"

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 5.png
    $ zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 = -100
    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as rs_image_1C9982B11CB6440DBBEE2B161A425C30 zorder zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 onlayer master
    hide rs_image_1C9982B11CB6440DBBEE2B161A425C30

    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "?！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Hit 3.ogg"

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 5.png
    $ zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 = -100
    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as rs_image_1C9982B11CB6440DBBEE2B161A425C30 zorder zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 onlayer master
    hide rs_image_1C9982B11CB6440DBBEE2B161A425C30

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "互相右插！！决赛两人终于得以全力对抗。"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "就连观战的我们也不由得为这场火热的争霸战捏紧了拳头！！"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "正是，年轻的身体，流淌的汗水，\n不管是心里还是那里都目不暇接。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "看……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    extend "{color=#FF00FF}某些观众{/color}发出了无比愉悦的声音哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "好、好像也对。不愧是御咲，和传闻中的一样……"

    rs_character_710A38AC94C841779DB701B5AC1010FD "上啊啊啊木村！！给他们看看田径部的毅力！！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "到边界了！压上去干掉他啊啊啊！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 5.png
    $ zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 = -100
    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as rs_image_1C9982B11CB6440DBBEE2B161A425C30 zorder zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 onlayer master
    hide rs_image_1C9982B11CB6440DBBEE2B161A425C30

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "哦哦！！木村同学的上手投！{w}\n……可惜！赤峰同学没能完全出局！！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦哦哦哦哦！！！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥——！！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "阿月——！！！"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "月——！！！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 5.png
    $ zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 = -100
    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as rs_image_1C9982B11CB6440DBBEE2B161A425C30 zorder zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 onlayer master
    hide rs_image_1C9982B11CB6440DBBEE2B161A425C30

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "唔?！！看招！！！！"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呜哇！！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 5.png
    $ zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 = -100
    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as rs_image_1C9982B11CB6440DBBEE2B161A425C30 zorder zorder_rs_image_1C9982B11CB6440DBBEE2B161A425C30 onlayer master
    hide rs_image_1C9982B11CB6440DBBEE2B161A425C30

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1C9982B11CB6440DBBEE2B161A425C30 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 6.png
    $ zorder_rs_image_5BAF87FE15234238AB0865FE6CEABB74 = -100
    show rs_image_5BAF87FE15234238AB0865FE6CEABB74 as rs_image_5BAF87FE15234238AB0865FE6CEABB74 zorder zorder_rs_image_5BAF87FE15234238AB0865FE6CEABB74 onlayer master
    hide rs_image_5BAF87FE15234238AB0865FE6CEABB74

    $ zorder_tag_A366FE92B81D404585614E7D29CFAD20 = 200
    show rs_image_5BAF87FE15234238AB0865FE6CEABB74 as tag_A366FE92B81D404585614E7D29CFAD20 at center_bottom zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "哦哦！！赤峰同学把对方押倒了～！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "！！"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7C178421D3DA4E2CB70D4336919888FB "啊！！比起木村同学赤峰同学的手先着地了！"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "结果将会是……？"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "裁判的判定……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_A366FE92B81D404585614E7D29CFAD20
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    extend "{color=#00FFFF}护手{/color}！{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_A366FE92B81D404585614E7D29CFAD20 = 0
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_A366FE92B81D404585614E7D29CFAD20 at center_bottom zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "{color=#FFFF00}赤峰同学的胜利！！！{/color}"

    if sys_music2_current_file != "sound/Effect Sound/Clap 1.ogg":
        play music2 "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Clap 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}哇啊啊啊啊！！！{/size}"

    window hide

    pause 1.5

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_A366FE92B81D404585614E7D29CFAD20
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    stop music2 fadeout 1.5
    $ sys_music2_current_file = ""

    pause 2.5

    if sys_music_current_file != "sound/BGM/To the future.ogg":
        play music "sound/BGM/To the future.ogg" loop
        $ sys_music_current_file = "sound/BGM/To the future.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C567CA6BD8324AA8B0D4355C0967B0A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    window show

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_05F784F04C004906B34CE8B18FDE28D3 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "做得好哦，哥哥！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_1624997D37FC499DAD5C4C36FF3A0F38 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空……多谢大家的声援，让我能努力到最后。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_151D5EA5EE3B4D7BA2D61C7C63F972CC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_A48D56FF0F2D4651AFB35C1789C78F07 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "很棒哦阿月！！辛苦了！！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "力士装很不错哦。打了一场名赛，辛苦了。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_AD0A1253421A4619B2C6792B88C585C3 as tag_724406A84D7141298EFF0D864FAE1534 at right_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    show rs_image_F98CA2A6977F4950A23DA67286D889BA as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at left_top zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "不愧是月，太好了！"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "恭喜获胜！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_52442263709249C69EEA3B5650B921EC as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呜～……果然赤峰家的哥哥很强啊。{w}\n要从那个地方大踏步反击根本没戏。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_C7E9DD4D1B084A15A4D4060F41AF9B55 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_C0489618AF3A47C089B8F4BA43A59A66 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_710A38AC94C841779DB701B5AC1010FD "……不过，你也很努力了，辛苦了。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是哦，一开始还想相扑挺没意思的，不过刚才的比赛很激动人心呐！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "面对体力测试全年级第一的那家伙也完全不甘示弱。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_52442263709249C69EEA3B5650B921EC as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "说的也是呐…对面毕竟是第一啊。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊——不甘心！！至少上的是弟弟那边的话就能赢了啊！"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_CAE9E92D7F644421A40585EE4A43F483 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊～啊，要是那边来点决策失误派弟弟出场，毫无疑问就是木村的优胜了啊……"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_C567CA6BD8324AA8B0D4355C0967B0A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BFC0B3388AA14C13AB88519DEBCF6FA7 as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "混蛋——！！那些人为什么嘴这么贫啊——！！"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "好不容易才避开地雷的——！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_C567CA6BD8324AA8B0D4355C0967B0A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D129C92CD1DC426BBAEA334FBC7FCF90 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……看，空，那些家伙完全小看你了啊。"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_145DF74E1B2140DABD280C00261D5D85 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "是呢～这下子不论如何也要挽回名誉了呐。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_52907CFE4828483C99DC76C46D873DD0 as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呃……？"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "怎么还杠上了？"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 300
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A6BDA5B155414D99AB52F15BEBCC03D6 as tag_0C07D2341065492CB0EDF00452D574E1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_5E7D24311EEA4507B1FE775C8265EADA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……那个，稍微打扰一下。"

    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "好啊好啊。"

    show rs_image_6B387DE0988444BA9024CD57D9D7D7D2 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "请问怎么了？"

    show rs_image_7780BD482A234B81970D2A4B4EE70A97 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "其实……"

    window hide

    pause 0.3

    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 300
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D2E31CDD8AE14CA4A56BC2EFC98D23CB as tag_0C07D2341065492CB0EDF00452D574E1 at right_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.3

    window show

    rs_character_7C178421D3DA4E2CB70D4336919888FB "咳——咳——嗯嗯……哦！这下子很有趣了啊！！"

    show rs_image_EAA2EF7FB3CF4DC8B7F90D9F76D373E7 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "笨、笨蛋！没事对无关人员瞎承诺什么！"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "这种东西肯定不能擅自决定的。"

    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "有什么不好嘛陆田君。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "这可是地区大会哦，肯定要以让市民高兴为优先。"

    show rs_image_D2E31CDD8AE14CA4A56BC2EFC98D23CB as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "可、可是……"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "真是的～又不是电视，没必要非跟着剧本来。"

    show rs_image_683E53C2576646F995F440B69E45074E as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "……是呐，毕竟是祭典。不论如何让大家开心最重要！"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_A6BDA5B155414D99AB52F15BEBCC03D6 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……好！！"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_C567CA6BD8324AA8B0D4355C0967B0A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_AE31149E5F7F4DC79066D77A5F625EC2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_37DF69F2B47C45148B6FB8E9B2E339C5 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_710A38AC94C841779DB701B5AC1010FD "笨、笨蛋！你们怎么可以说这么缺德的话！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "就是就是，还没见过这么不服输的。"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_D47A02E2410B4E4F8CE4650D74C08F1A as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_690522DE38524DA3AF9633C07202989E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呵——！可我们说的就是事实嘛！对不对作哉。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "就是就是～"

    pause 0.4

    stop music fadeout 0.3
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "大家，紧急事件！！"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "之前一直在观众席加油的赤峰同学的弟弟，现在作为赤峰军的里BOSS登场了！"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "然后，根据赤峰同学和木村同学的意见，将会再举行一场比赛！！"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "这对木村同学来说可谓是难得的复活战！"

    window hide

    if sys_music2_current_file != "sound/Effect Sound/Clap 1.ogg":
        play music2 "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Clap 1.ogg"

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C567CA6BD8324AA8B0D4355C0967B0A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 2

    window show

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    stop music2 fadeout 0.9
    $ sys_music2_current_file = ""

    rs_character_7C178421D3DA4E2CB70D4336919888FB "击败赤峰同学的情况下，木村同学将会获得大赛的优胜，以上可否？"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_9B9DCA74086B43A197B7D71BB87CC11D as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸，拜托我到这个程度上确定没问题？"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_286CAF074B77418F8F63C88FD5379830 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "喵事哦。大家都相信小空的实力哦。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_256DCF0FD3C145C4BFF308F96CE078E2 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……明白了，这次就由我来背负一班大家的期望了。\n"
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_5DD3379558464E468EC278100ACA9047 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 1.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 1.ogg"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Yoo 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Yoo 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_C567CA6BD8324AA8B0D4355C0967B0A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_5C665F7923F5414CBEE65EC1F5A0C7E5 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "综上，请多关照。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_089CCDD9D55A42938F9FE5A507FD82ED as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_8E2AA2B7E1F047CF8C419F790C9A7329 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦欸！？怎么回事！？"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那家伙！什么时候换的衣服……！？"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_C567CA6BD8324AA8B0D4355C0967B0A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_1C902348EEC9420F8F227A1170E81330 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_5C665F7923F5414CBEE65EC1F5A0C7E5 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "就按你们所说，这次由我来挑战。好了，放马过来。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空，没必要手下留情。"

    show rs_image_73794BFFDDBC45A89751C639FB7264C8 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯！交给我！！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A6CD95C1323642CAAC0AB7556E2714B3 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_127C3AB9174642D0AF0137C9B33451D2 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈、哈！一群笨蛋，居然会那么心安理得地挑衅别人。"

    show rs_image_CAE9E92D7F644421A40585EE4A43F483 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "上木村，好机会！把他按地上干！"

    show rs_image_0D8E132788D04C859F1767AA604447C6 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "好——！你们就尽情后悔给我这个机会好了！赤峰兄弟！！"

    window hide

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 11.png
    $ zorder_rs_image_18A77FEE59614E49AA0660833A369388 = -100
    show rs_image_18A77FEE59614E49AA0660833A369388 as rs_image_18A77FEE59614E49AA0660833A369388 zorder zorder_rs_image_18A77FEE59614E49AA0660833A369388 onlayer master
    hide rs_image_18A77FEE59614E49AA0660833A369388

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_18A77FEE59614E49AA0660833A369388 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.4

    window show

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "准备开始了！！{w}那么，预备……！！"

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呵呵呵，跟刚才的哥哥比起来也太细了，这种一招就干掉了！！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "别得意！看上去不一样，我的力气可一点也不必哥哥小！！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……"
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_6064CD40E31B4755841BF91DF3F69061 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    extend "其实并不是不过……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "……开始！！"

    window hide

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    show rs_image_6B8530D4694547F895CE3D23E9CC981F as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_CD4E0717885A494B93606FDBEF55AF92

    pause 0.7

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哇？！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "有破绽！！！"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 2.ogg"

    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window show

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "赤峰同学突然绕到了对手身后，见机击倒对方了——！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸！？"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C567CA6BD8324AA8B0D4355C0967B0A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_81339CBB1684406EB266897AD5F0330B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_D9EB6D62064144068D274D1F211D0A39 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "刚、刚才怎么了！？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "真聪明，明白得用假动作……"

    window hide

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 300
    show rs_image_1561FC74CECA43F896E80A6050FD4EB8 as tag_0C07D2341065492CB0EDF00452D574E1 at right_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "胜者！！这次也是！！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "赤峰兄弟！！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    window hide

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clap 1.ogg"

    pause 2

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C567CA6BD8324AA8B0D4355C0967B0A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.4

    window show

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_90E48F9CDC734D43AD577A32B4E6F01F as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好、好厉害！！"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "和月不同，智商压制……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_C7BD395661A249B48A9120BE7F9AC4F9 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_AE31149E5F7F4DC79066D77A5F625EC2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_710A38AC94C841779DB701B5AC1010FD "好了，木村，输都输了，快对弟弟君道歉。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你也去，穗海。真是的，只要对手是一班智商一下子就降到幼儿水准了。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_52442263709249C69EEA3B5650B921EC as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_0101B4A16FA94D81BACA3AB5A5E27790 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=400, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "非常抱歉……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "{size=12}………我的错。{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_1209D298FCAF4E62993FA6F9C54C9FCE as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "有声没气的，听不见。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C567CA6BD8324AA8B0D4355C0967B0A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_09643DF2A11A4AFFA89DE3807C6AD014 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_1C902348EEC9420F8F227A1170E81330 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "可以了，都已经道歉了。我也有做的欠考虑的地方。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得漂亮，空，很不错的切入，剑道锻炼出的步伐不是盖的。"

    show rs_image_D129C92CD1DC426BBAEA334FBC7FCF90 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "利用对手的体势拉倒对方，考虑得不错。"

    show rs_image_5C665F7923F5414CBEE65EC1F5A0C7E5 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "比赛里木村君也很有力气的哦。\n虽说最后比赛变得不像是单纯的相扑了。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    show rs_image_A5121F2F859A490B9808D2589018163C as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_51D0433151524E13BEC3562515EB54AF as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_E3F6ADD43DE44A428E1224756613C694 "不……是被冷静击破弱点的我的失败。你们兄弟两人真的很厉害呐。"

    pause 0.3

    window hide

    pause 0.5

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    stop music fadeout 3
    $ sys_music_current_file = ""

    pause 2

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91


    if judge_lm_condition([]):
        jump block_00003709

    return

label block_00003709:
    # Node: 00003709 (大家來相撲 4)
    $ set_window("イベントモード")
    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B496D03F24964A56B67F493D25F33F8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    window show

    rs_character_21160A04FFC74FBB81589F31D9E93E93 "接下来请出场的所有选手合影留念！"

    window hide

    pause 1.5

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    if sys_music_current_file != "sound/BGM/Afternoon.ogg":
        play music "sound/BGM/Afternoon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Afternoon.ogg"

    show rs_image_A6EB165FEA4F43D98FA0D7F5088E39A4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.7

    show rs_image_0E336DDE12744B46802212D5D9F9FDB1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.7

    show rs_image_A08F830C7B7A48D9AE269614FEAC7E8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.7

    show rs_image_91F4C74E7B844945A9976F914A36207F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_20AA9A405C08411899D11DA9EB2EE47D as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.3

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊哈哈，原来如此。所以两位才会那么顾虑我的心情啊。"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DFF43C28E0D9414492DE4927927BBDBF as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，不过看今天的样子似乎完全没事。\n说实话，我们也被吓了一跳。"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "二班那些笨蛋小看空的时候，真的捏了一把汗。"

    show rs_image_E3117F92902F437EBCACCE96F9CB84FC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这样啊。谢谢你们这么为我着想。"

    show rs_image_BC8B9AC6BDD34EE7B445866E23D6D5C1 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不过，我已经不再纠结那些事情了。"

    show rs_image_943958ACE1594083BA9B66D14E70D431 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不再纠结……？"

    show rs_image_E0D00426275740F394D32435264217E5 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯，两位应该知道我家开的是{color=#FF8080}剑道场{/color}。"

    window hide

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B97A3992A1D24282B85B44E0C876F034 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E9B6763A09A744A9BE6ABBF987F70AEB as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_195F518B89564C98A557F130D2E603F0

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯。"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "我也知道。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "其实，不久之前，哥哥已经被选为道场的继承人了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！！是这样……\n这么重大的新闻完全不知道呐。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "抱歉抱歉，一直找不到说的机会。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……所以，我也不再太过注意这个了。\n至今为止一直都理所当然般地跟在哥哥后面向着同一方向前进。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不过，也该考虑一下自己未来的道路了，我这么觉得。"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show rs_image_91F4C74E7B844945A9976F914A36207F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_6342DEF8AE284F3280186A636EF8A454 as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_20AA9A405C08411899D11DA9EB2EE47D as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    rs_character_81D16F74A3C44B8982DB528D7D934850 "欸……原来如此。"

    show rs_image_E0D00426275740F394D32435264217E5 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这么下定决心后，也就不再和哥哥事事比较了……\n{w=0.45}{nw}"
    show rs_image_73F69A7FB68D4D8684029D4486A79854 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "倒不如说，本就是我单方面的意识过剩。"

    show rs_image_FFF830B97C0146FD92D3A791B1913CEA as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这样的意识过剩也逐渐消失了。"

    show rs_image_256DCF0FD3C145C4BFF308F96CE078E2 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "所以，对于我们被比较这件事，最近也就不那么敏感了。\n"
    show rs_image_20AA9A405C08411899D11DA9EB2EE47D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "毕竟，我和哥哥本就不同嘛。"

    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个，就像今天主持人说的那个一样？\n有不同的魅力，气场温柔什么的……之类的？"

    show rs_image_FCAFA927EAA1420E8D01012A37344D27 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "第二句话有点意义不明。"

    show rs_image_05F784F04C004906B34CE8B18FDE28D3 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我也有自己擅长和不擅长的事。比如做点心，或者刚才那样。"

    show rs_image_E0D00426275740F394D32435264217E5 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这么想之后，至今只有哥哥背影的世界，突然变得开阔了。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_C403187E92D8402D89D64200C5B1A7F2 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我不是赤峰月的劣化版，{w}我就是赤峰空。"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_ECBA0CF7876045D4AE8665A90CDBF4B6 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "对对！友亲和加藤酱很担心小空不过。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那也只是强行和阿月比较，试图找闪光点的行为罢了。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_C66A56F89C43490FBD87D2164FFD98A5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "今后，在我们眼前的不会再是“月的弟弟”，而是“赤峰空”。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "最近看到似乎想开了什么的空的样子后，我们自然就察觉到了。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_B37B38F0EAF54165807FC3B0DED8A099 as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_E262B3AC8BDF48E4A8BEEBA281DFA194 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "抱歉……我们……"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "我们没有恶意，可也确实一直在给空造成麻烦也说不定……"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_E3117F92902F437EBCACCE96F9CB84FC as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不用道歉，完全没关系的。"

    show rs_image_20AA9A405C08411899D11DA9EB2EE47D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "两位可能没有意识到，我收到的话语中也有很令我高兴的。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "或许那些是自信的来源呐。{w=0.3}{nw}"
    show rs_image_52907CFE4828483C99DC76C46D873DD0 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_11E9CB4CF92548E88CF101664A977D06 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天做的点心也非常好吃哦！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_D225376486A6442D884B00D8B01FDB1E as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_81D16F74A3C44B8982DB528D7D934850 "相扑也是，华丽取胜了呐！！"

    show rs_image_FFF830B97C0146FD92D3A791B1913CEA as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊哈哈，谢谢。"

    window hide

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    pause 1.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_97F953D82737458C83905085327ADE8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_0D5BC78C8923442DB3E842DF9CA717D4 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "摄影结束了。"
    show rs_image_04CE6801CFBD460096381A21558DE1D7 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "绫濑，奥村，谢谢你们这次忙了这么多。"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_FD97A7AC280A4AA68D0BEDD058C5C756 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=400, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_324C77394BC349DB995FB24E2E90630F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欢迎回来～阿月——知道你们两个的事情也就只有我们呐～"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不要在意。不过说起来，空确实在向好的方向前进呐，太好了。"

    show rs_image_497B60616E5F449190127FA9DF44549A as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{color=#00FFFF}和阿月商谈的时候{/color}，完全没想到会有这样的展开……"

    show rs_image_5C35B097B2134B2BBEC8D37C4611A558 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "{color=#00FFFF}那个时候{/color}体育馆的社团活动还没结束，\n现场真是一片混乱啊……"

    window hide

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_C1C2CE7359074118823499ABE4772311

    pause 2

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 400
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 0.8

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_D0E469E7282E414682019E0511FE6A43 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.8

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "其实……最近，空都不和我一起回去了。\n社团活动结束后，总是一个人不知道去什么地方。"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_F25DC387CDE74829BF90A4EF4C34AAAF as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸～小空嘛。到底怎么回事呐？"

    show rs_image_86BB7A17393E4CA3AA3BEA8164C0DA78 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不清楚。\n以前一起回去后，他会比所有人都早开始练习，可现在也不做了。"

    show rs_image_F5A88DE19235425A81D30DF2D7E4C7CD as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "急着回家是有什么别的事嘛？"

    show rs_image_9411BF701D2449FE8F9E028276FF004F as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯，好像是要去别的什么地方，回家也很晚。\n问去了什么地方也总是被蒙混过去。"

    show rs_image_AE9F4E24733A457786C1C0BFE009DD20 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "也不想我跟着。啊啊，空到底在做什么呐。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_1DF71C5D65C84CAB8B731887B3EA91A6 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "哥哥我啊……哥哥我啊……"

    show rs_image_D54E703CD633470FAE473BD8F3BE65FA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "也许是着迷于什么新游戏了吧？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "小空也不是小孩子，也不可能完全听某人的话。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    show rs_image_2304A61C05D54DD6B9E15DDB5A3D3949 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说不定有着对那些东西的下流念头，晚上在花街……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_319DADD51F7C413586B41BFF2D47BF78 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_AB0AD4E5EF9A4CFCA7D8F63B134013E8 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "～～～！！！（切）"

    show rs_image_497B60616E5F449190127FA9DF44549A as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "开、开玩笑的！我明白了……"

    show rs_image_21529C10E6144ED983C35EA511250F8A as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那么这次就由我去问问正经事好了～"

    show rs_image_CC552F66007B496498438F25BBBBDDF2 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "奥村比较会说话，帮大忙了，就拜托你了。{w}\n最近空对我有些不太待见的样子。"

    show rs_image_FD97A7AC280A4AA68D0BEDD058C5C756 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嘛～我们毕竟是中学二年级，正好是反抗期嘛。"

    show rs_image_1DF71C5D65C84CAB8B731887B3EA91A6 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空到底有什么烦恼，请务必问出来。然后我们一起思考对策。"

    show rs_image_2B2701CC98B242CDADF7C3CC5583AD9D as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我们是出生前就在一起的兄弟。所以不论什么应该都是能理解的……"

    show rs_image_286CAF074B77418F8F63C88FD5379830 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "也许～不过，正因为过于亲近有些话才说不出来呐。"

    show rs_image_9CD3C176C2984BC8A0E4278BB4CFD818 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "总之这里交给我。不过，阿月真的很为弟弟着想呐。"

    show rs_image_AE9F4E24733A457786C1C0BFE009DD20 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……作为兄长，这是理所当然的。"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.5

    window show

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_1F1908ECF899471E8BF52561AF2B4AC4 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔……说起来有些不好意思，一般来讲就是所谓的“寻找自我”……"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_098C675E48A24C839259B55EAD2E93A8 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "听说经常会到街上各种店去的样子。"

    show rs_image_05F784F04C004906B34CE8B18FDE28D3 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这都被知道了啊～不愧是慎酱，情报达人！{w}\n只是想看看不同的人都过着怎样多姿多彩的生活而已。"

    show rs_image_F5A88DE19235425A81D30DF2D7E4C7CD as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不过，为什么要这么做？小空不是还有剑道嘛。"

    show rs_image_E3117F92902F437EBCACCE96F9CB84FC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……嗯，说的是，我明白。所以，也想再挑战一次哥哥……"

    show rs_image_F25DC387CDE74829BF90A4EF4C34AAAF as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……再说了，所谓的寻找自我是？"

    show rs_image_76E6EE066C7849F8B316D30CB17821CF as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不论如何都无法战胜的人就在附近……不，就在自己身边……"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "一直这样，慢慢地自信一点都没有了……"

    show rs_image_21529C10E6144ED983C35EA511250F8A as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦～阿月的事啊……所以钻自己的牛角尖了？"

    show rs_image_AC91243D19574029BF9A6A4913C5C847 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔。其实，唔………\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_10FB6CFF67AA4500B487D28FFF10F8EB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_71A891A4964F44A5848FC63BB0CCE0E7 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "火大、后悔不是当然的吗！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_497B60616E5F449190127FA9DF44549A as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "小、小空，冷静……冷静。和治愈系完全不符了哦。"

    show rs_image_76E6EE066C7849F8B316D30CB17821CF as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "同样入睡，一起早起，吃同样的饭，一起上学。\n一起学习，一起练习，为什么只有我一直在输。"

    show rs_image_AC91243D19574029BF9A6A4913C5C847 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "明明哪里都是一样的……生日也一样。"

    show rs_image_8FC7B994836E4084B027C2E8010AD725 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……"

    show rs_image_1F1908ECF899471E8BF52561AF2B4AC4 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "想到这里了，就想看看大家都过着怎样的生活，毕竟世界这么大。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "结果，每个人都有自己独一无二的地方呢。"

    show rs_image_FD97A7AC280A4AA68D0BEDD058C5C756 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那不是个很好的成果吗？"

    show rs_image_6FBE5139BFEB4724AB6A1B34DD49E654 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯，但结果还是回到原点了。"

    show rs_image_20AA9A405C08411899D11DA9EB2EE47D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "至今为止的一切，我果然还是不能放弃，我会再一次试着挑战剑道的。"

    show rs_image_286CAF074B77418F8F63C88FD5379830 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "是嘛，那就回到平时的空了呐。"

    show rs_image_E3117F92902F437EBCACCE96F9CB84FC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯，谢谢你为我担心。{w}\n今后我也会努力的。"

    window hide

    pause 0.6

    stop music fadeout 2.2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 1.2

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_59836EDB597846F2A2C0A683B909166F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.8

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_339BA4D7ABC047BEAC11139BEC751D5A "行礼！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}请多多指教！{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_F59CF92171C0495BA4E334AC96BA8B63 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    rs_character_ADB48B13DBE445C3BA33DF9581F85369 "空前辈好厉害——对着月前辈来了一记漂亮的一招制胜呢。"

    rs_character_D92A15E0A1704F9992AB818DB80DFE4D "嗯，果然那两位很厉害啊。能看到这么高水准的比试真是太好了。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……{w}\n……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "可恶！！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_59836EDB597846F2A2C0A683B909166F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "什么声音？{w}\n空、空前辈刚才……拿竹刀敲地面了……{w}\n那个温柔的空君……？"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空，你想做什么！？怎么可以这么对待竹刀……！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥，刚才和我的比赛，是不是手下留情了……！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "诶……说、说什么呢……"

    window hide

    pause 0.8

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 8.png
    $ zorder_rs_image_83F732F048574A3294F4B648F4D0DFC8 = -100
    show rs_image_83F732F048574A3294F4B648F4D0DFC8 as rs_image_83F732F048574A3294F4B648F4D0DFC8 zorder zorder_rs_image_83F732F048574A3294F4B648F4D0DFC8 onlayer master
    hide rs_image_83F732F048574A3294F4B648F4D0DFC8

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_83F732F048574A3294F4B648F4D0DFC8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    pause 0.6

    window show

    if sys_music_current_file != "sound/BGM/Series - Akamine brothers.ogg":
        play music "sound/BGM/Series - Akamine brothers.ogg" loop
        $ sys_music_current_file = "sound/BGM/Series - Akamine brothers.ogg"

    pause 0.3

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "别开玩笑了！为什么要那么做？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我本来还想从今天开始转换心情重新努力，\n为什么要做这种从开端否认我的事！！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不、不是的，我、我是为你好。希望你至少能找回一点自信……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不用你自作多情！！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "对手是初学者的话再说，本来全力也无法战胜，\n可水准相似的对手还这么做是有多看不起对方？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "被哥哥这样对待，以为我会高兴！？"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不是这样的！我只是、只是担心你而已。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "突然要改变生活，要寻找理由，结果你不是什么都没找到！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这种事……也不能这么说！！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "是想让我亲口说出不管做什么都不可能战胜哥哥！？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "稍微顾虑一下我的心情！！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我也是想尽可能去体谅的！！关于没做到这一点我道歉。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "但是，你的所谓的烦恼果真如你所说的话，为此生气就有些说不过去了。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "根本没什么见不得人的事不是嘛。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "居然大言不惭地说这种话！？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不管做什么都会“不愧是哥哥”“果然是弟弟”这样被比较，\n只有在没什么差距的时候才会有“不愧是双胞胎”这样的说法！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "但这些到头来都只是在夸奖哥哥。\n哥哥什么都能做到，我只是所谓的二流品。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "做得到就会“因为是双胞胎”，做不到的话“毕竟是弟弟”。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "为什么，为什么只期待哥哥能做到。\n为什么哥哥做得到，我就做不到。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这种心情真的能明白？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "被哥哥巨大的背影笼罩，压力和劣等感不断积累，\n无论如何都想要从大家的印象中消除无能的自己。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "根本找不到自己存在的意义，真的能明白？\n总是被第一个评价的哥哥明白不了的！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_59836EDB597846F2A2C0A683B909166F as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "刚、刚才是空的声音？到底怎么了？{w}\n空……月？"

    rs_character_339BA4D7ABC047BEAC11139BEC751D5A "空、空手道部那边也听到了？其实是赤峰兄弟在……"

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 8.png
    $ zorder_rs_image_83F732F048574A3294F4B648F4D0DFC8 = -100
    show rs_image_83F732F048574A3294F4B648F4D0DFC8 as rs_image_83F732F048574A3294F4B648F4D0DFC8 zorder zorder_rs_image_83F732F048574A3294F4B648F4D0DFC8 onlayer master
    hide rs_image_83F732F048574A3294F4B648F4D0DFC8

    show rs_image_83F732F048574A3294F4B648F4D0DFC8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_C3C334499A6D467E8E19829741D4482F

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我不知道你竟然感到如此痛苦……"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "完全不明白这种感觉，完全不明白却装作关切地说三道四，\n总有忍不下去的时候……"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "可是，空，这种感觉我也明白。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "又是……这种话。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，反过来又如何？"

    if sys_music_current_file != "sound/BGM/Series - Akamine brothers.ogg":
        play music "sound/BGM/Series - Akamine brothers.ogg" loop
        $ sys_music_current_file = "sound/BGM/Series - Akamine brothers.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空所拥有的，我所没有的那些，温柔的笑容，善良的声音，灵巧的双手。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "匀称结实的体格，追寻理想的道路的过程中的不变的温柔。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "以及，相似的举剑时的帅气之处，\n这些我所憧憬的一切，我所持有的憧憬又是什么！？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哈、哈啊？说什么不明所以的话呢？"

    window hide

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.8

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 9.png
    $ zorder_rs_image_EAE467ED476446099F36A59024BEB550 = -100
    show rs_image_EAE467ED476446099F36A59024BEB550 as rs_image_EAE467ED476446099F36A59024BEB550 zorder zorder_rs_image_EAE467ED476446099F36A59024BEB550 onlayer master
    hide rs_image_EAE467ED476446099F36A59024BEB550

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_EAE467ED476446099F36A59024BEB550 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 0.6

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空有着和我不同的无数优点！！所以我才会这么喜欢空的！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "错误的地方，吸引人的地方，全都包含在一起的喜欢！！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥、哥哥，等等，话题不太对劲，我不是在说这个。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不，你太轻视自己了。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "明白了吗？我明明这么喜欢你，可是，空却觉得自己没有存在的意义。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "无从自知，令人伤感。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……什、什么啊……"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "要是能再对自己有一些自信的话，就不会这么责怪自己了。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "最了解你的魅力，最能告诉你这一切的，不是别人正是我。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不管怎么说，我们在一起度过的时间也是最长的！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "要是我能早点发觉这一切，一定会不厌其烦地让空意识到自己的优点的。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "花朵沐浴阳光则更显爱怜，人若居于赞颂则渐生魅力。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "你绝不可能毫无魅力。赞扬的言辞不多，只是因为还没有被赞扬。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不要再一个人烦恼了，把所有烦恼都告诉我。\n我和空，共同分享，互相勉励。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "你不是我，你将会以自己独有的姿态{color=#FF0080}绽放{/color}。"

    window hide

    pause 0.4

    # Gallery unlock: images/CG/Let-us-sumo-together/Let-us-sumo-together 9.png
    $ zorder_rs_image_EAE467ED476446099F36A59024BEB550 = -100
    show rs_image_EAE467ED476446099F36A59024BEB550 as rs_image_EAE467ED476446099F36A59024BEB550 zorder zorder_rs_image_EAE467ED476446099F36A59024BEB550 onlayer master
    hide rs_image_EAE467ED476446099F36A59024BEB550

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_EAE467ED476446099F36A59024BEB550 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥……\n哥哥说的东西太难理解了无法判断。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不过，我还是明白真的在为我考虑、很喜欢我的部分的……"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯，喜欢，最喜欢了，无与伦比的。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔……那，首先，从能被喜欢上的自信开始，重新审视一下自己好了。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空……"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "抱歉，大吼大叫的……"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "没事，拜此所赐所有事情都理顺了。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯……"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_E2311FF4F5B04C91942F417922856D96

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E1008DFA2F09467D84B2358A572E4D70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 0.5

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_943958ACE1594083BA9B66D14E70D431 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "赤峰家的后继人已经决定了什么的，真是吓一跳啊～"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_6342DEF8AE284F3280186A636EF8A454 as tag_61A891D6A6D047DC93695DA12E13CC75 at right_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "啊啊，稍有点太早了。"

    show rs_image_3F533DA3CF494DEBA1146743852331E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说起来，加藤酱是怎么知道这些事的？"

    show rs_image_262829AECEA1468AB738E042DA70F096 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "啊，那些人上周社团活动的时候，\n好像在为了{color=#00FFFF}园艺{/color}的事打架。"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "似乎是有什么很了不得的{color=#00FFFF}花{/color}似的，\n双方互不退让，气氛非常紧张。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "花！？那是什么……庭院明明很大，想种就种不就好了。"

    show rs_image_39A751328FDE46FAB3026BEC1F2E6B1C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "加——油啊——种出的花——不管——几个——都——是～♪{w}\n漂・亮・地盛开——的话——就——好了——呐～♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_FCAFA927EAA1420E8D01012A37344D27 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "给你钱拜托唱对词……"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 1.5

    window hide

    if sys_music2_current_file != "sound/Effect Sound/Night insect 1.ogg":
        play music2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_0D1A14CC6DD549EA877967C087A4F0E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 2

    show rs_image_4C61A914626C4C7D8E8E416B93066056 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1.5

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    show rs_image_1EA93E6083954B758043E518146A295A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg"

    pause 0.6

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_9399CFDBEDD4474B9D69F052A68BEA10 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空，不参加纪念照相真的可以吗？"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_8851F33C736744C1A310921E6A3D64D7 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯，本来就是中途强行参加的。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那种照片肯定只能由正式的选手参加嘛。"

    show rs_image_DAE7A6E538674BB9A132983C730C7EBC as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是吗。\n"
    show rs_image_553DCA76699644D795FB721B561E6915 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那个……空。"

    show rs_image_7A9E860165FD4D76BDCB391171572EFC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯？怎么了？"

    show rs_image_D1B9009B1F834C2B9585C35FB19DE0E8 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空最近，变强了……呢。很……耀眼……很厉害。"

    show rs_image_8851F33C736744C1A310921E6A3D64D7 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……嗯……"

    show rs_image_E2E9CE3DD96C41C4AADEDAD41C16C3F9 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "可是……可是啊，还会有不顺心的时候也说不定。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "能隐藏起那些在人前自立当然也是很厉害的。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "可……在我面前就不要了，表露出一切来也是没关系的。"

    show rs_image_D1B9009B1F834C2B9585C35FB19DE0E8 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我们毕竟永远都会是兄弟。"

    show rs_image_0A588099B792438891B5071225E15832 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥……"
    show rs_image_17DDFDAB7E2D4E5FBDCB9B727508BEE0 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "是呢。\n那么，真有那样的时候就允许我像弟弟一样小小任性一下好吗。"

    show rs_image_433F0A88855147318866B6C5D208894F as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "啊啊，就这样……{w}不论何时都可以。"

    show rs_image_533A8779B5534514AE4D6BB11A554A30 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那，今天晚上，我就不客气了……"

    show rs_image_589A0E5D90374FD4B884810D95A6E2E5 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯，交给我。"

    window hide

    pause 0.6

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    call scb_flag_title_end(1, _("「大家来相扑」")) from _call_scb_flag_title_end_1

    if judge_lm_condition([]):
        jump block_0000370A

    return

label block_0000370A:
    # Node: 0000370A (Phase: 0)
    $ C1S1Phase = 0
    if Chapter <> 1:
        $ del C1S1Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_0000370D
    if judge_lm_condition([]):
        jump block_0000370B

    return

label block_0000370D:
    # Node: 0000370D ()

    return

label block_0000370B:
    # Node: 0000370B (FINISH)
    $ C1S1 = True
    $ TalkTsukiSoraF1After = True
    $ TalkTsubasaF1After = True
    $ TalkItouKimuraF1After = True

    if judge_lm_condition([]):
        jump block_000038F3

    return

label block_000038F3:
    # Node: 000038F3 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_1

    if judge_lm_condition([]):
        jump block_0000370D

    return

