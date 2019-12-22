# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003714 (FLAG: 翼的流轉音符)

label block_00003715:
    # Node: 00003715 ()

    if judge_lm_condition([]):
        jump block_00003721

    return

label block_00003721:
    # Node: 00003721 (Phase: 99)
    if Not(VarExists("C1S2Phase")):
        $ C1S2Phase = 0
    $ C1S2Phase = 99

    if judge_lm_condition([]):
        jump block_00003981

    return

label block_00003981:
    # Node: 00003981 (F2 START)
    call scb_flag_title(1, _("「翼的流转音符」")) from _call_scb_flag_title

    if judge_lm_condition([]):
        jump block_00003720

    return

label block_00003720:
    # Node: 00003720 (翼的流轉音符 1)
    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.6

    $ set_window("イベントモード")
    $ set_place_title("")
    window show

    if True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect4 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect4_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "喔，原来是森海啊。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at right_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，滑子老师好！\n{w=0.5}{nw}"
    show rs_image_64D8D1E21F7F40938F719E0070CF195B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "正是我哦！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这间教室放学后好像没什么人用的样子，\n我偶尔会来这里弹钢琴喔〜"

    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……{w=0.5}{nw}"
    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "难、难道……这是不允许的？"

    show rs_image_3CDBB93600FA40048DE19330047E1350 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "唔，也不能说是没问题。嘛，现在先不提这个。"

    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B08F170752C74A09BC000D1CF77FA609 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "话说回来，弹得还挺不错呢，是你母亲教的？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谢谢！"

    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对喔，虽然我经常是一个人在弹但是……"

    window hide

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.5

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_FACF02D10C574EC8ABF41E3D996A6E34 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君，久等了，小钢琴部今天的活动也请多多关照了。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at left_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    show rs_image_DB50197E13884F45AFBB23A957B18CA1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……啊，滑、滑子老师，下午好……"

    show rs_image_F4E69F65605A49BCA7659DDD9B7624D5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个……发生什么了？"

    show rs_image_C0F02B9EC0484E97848C810E5DD5BB34 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "一之濑，你们聚集在这里是在进行社团活动吗？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    extend "小钢琴部什么的我可是第一次听说。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_4E534C3CC3ED418EA9C8155C87F1BCBB as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-90, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=400, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、那个，只是我们擅自这么称呼而已。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "至于按照正式的社团流程登记什么的，当然也没有做过……"

    show rs_image_F4E69F65605A49BCA7659DDD9B7624D5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是不是不太合适？"

    show rs_image_87A4A951CCF94134BEC8CCB7D574B6E1 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "如果规模变大的话，为了监督学生说不定会需要顾问老师啊。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_158D8E25C4414ECF868A62B83D40B99B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "没、没关系的！小钢琴部，只是友君和我，两个人的秘密聚会而已！！"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_4E534C3CC3ED418EA9C8155C87F1BCBB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_55AA9D3ECD6A49F888891037C386D65A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "对不对，友君！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？嗯、嗯！\n"
    show rs_image_8A80B90628C143D1B3A53C71240BBE2D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "虽说是秘密，但也没有在刻意隐瞒啦。"

    show rs_image_86500D05C8934AE7B4E71CC1D50E5D36 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "总而言之！人数肯定不会再增加了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Onboard 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Onboard 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_158D8E25C4414ECF868A62B83D40B99B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "请务必、"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Onboard 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Onboard 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不论如何、\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_86500D05C8934AE7B4E71CC1D50E5D36 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "就让这件事维持现状！！"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_8A80B90628C143D1B3A53C71240BBE2D as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3CDBB93600FA40048DE19330047E1350 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    show rs_image_55AA9D3ECD6A49F888891037C386D65A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=400, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "明、明白了。怎么说也不会让你们解散的，放心。"

    window hide

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_C0F02B9EC0484E97848C810E5DD5BB34 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "说起来……对了。"
    show rs_image_9BAD09B7F4DE47339C69A165D80E6844 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "怎么样，我这里有个委托要不要试试？"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0BDBAB46852441A1A55BE2EB34CF561F as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "委托？"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C0F02B9EC0484E97848C810E5DD5BB34 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    show rs_image_0BDBAB46852441A1A55BE2EB34CF561F as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "有个敬老会要在御咲市的公民馆开，说是让我们学校也要出个节目。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "公民馆的舞台很小，表演节目的话几个人就足够了，\n不过，也正因为人数少，节目很难想。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0F13158E12E14CB6AA93F6FE189A9B15 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "怎么样，你们小钢琴部愿不愿意上去表演？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2028F963C6F041949E94C771B899A6AE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦哦～！！也就是说，大家都要来听我们的演奏！？"

    show rs_image_D2BB5C80C5EC436C81AD2A89675FF109 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当然了！请一定要、一定要让我们来做！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_2CADF8378C504B23B59B06DFEDCA17ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸～要、要在观众前表演？？\n"
    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "唔……这样的事情……做、做不做得到啊。"

    show rs_image_B08F170752C74A09BC000D1CF77FA609 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "当然，会给你们加平时分的。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "而且，小钢琴部有了社团成绩，\n以后要是人数增加了想要申请正式社团也比较容易通过审核。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "这次委托的责任人是我，你们就尽情去做吧。"

    show rs_image_64D8D1E21F7F40938F719E0070CF195B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "明白！那么，我会和翼君一起好好思考节目内容的。"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个，翼君！一起加油哦！！"

    show rs_image_EAF549F11EDE4A5AA68FCD7AECAB1DEF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君……"

    show rs_image_D6900DA7D3A54445A3A7BAA4FA959F33 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "说、说的也是。\n和友君一起的话，不管发生什么都一定能迎刃而解。"

    show rs_image_FACF02D10C574EC8ABF41E3D996A6E34 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯，我也会在力所能及的范围内尽力去做的！"

    show rs_image_9BAD09B7F4DE47339C69A165D80E6844 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "很好。那就拜托你们了，我还有事先走了。"

    window hide

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.5

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_64D8D1E21F7F40938F719E0070CF195B as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——！！小钢琴部也像真的社团一样开始活动了……！"

    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……啊，不过，我还是觉得像现在这样只和翼君两个人一起比较好呐。"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这样轻松愉快的氛围还是很不错的。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "是不是，翼君！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1DB92443238942EB873783BEE27CA495

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸……唔？翼君？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_8676A882850344248D70E3A3623F329F as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1DB92443238942EB873783BEE27CA495

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个……翼君……\n这种时候要是不高兴地回答可是会很令人不好意思的～！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8676A882850344248D70E3A3623F329F as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    show rs_image_2CADF8378C504B23B59B06DFEDCA17ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊！！太感动了一瞬间没能反应过来，对、对不起。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈哈哈哈！！什么嘛～！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_11E9CB4CF92548E88CF101664A977D06 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的～翼君真的好有趣呐。\n我就是喜欢你那样的地方哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_8676A882850344248D70E3A3623F329F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1DB92443238942EB873783BEE27CA495

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"

    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "又来了。"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呼、呼姆～……！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_158D8E25C4414ECF868A62B83D40B99B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友、友君！请不要总是这样让我太激动了！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "如果意识拉不回来可怎么是好！！"

    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊哈哈！抱歉哦！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那么，现在开始说正事，来想演出的节目哦♪"

    show rs_image_6C7D131D881A4E7296FCD71C208CF53F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "真、真是的，下次再做这种事的话，我……"

    show rs_image_40378AEBEABC4F1181A8ACEC0693C48A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "就只能叫出{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#00FFFF}『另一个我』{/color}了。"

    show rs_image_8DB9EBBA116648CAAA85C0A0F67B04D2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶！！翼君还有那样的技能！？"

    show rs_image_040651EB0DB9405AB3B73494D241B34C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "最、最近总有这样的感觉……"

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～！是什么样的是什么样的？？想看想看～！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不可以的。那个除了恶作剧什么都不会！"

    show rs_image_DEB70960E8944B33903B14177D8DC211 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "说、说起来，现在应该认真考虑演出节目才对！"

    show rs_image_CC45620E61634BCBAE100C11F0CF029B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……好的。"

    window hide

    pause 0.4

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.8

    show rs_image_4B5F763E9F424591A5E354CF41830363 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.8

    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_C41C40E37C4246589AACD915ED8F7B0E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎样，翼君？这首曲子能弹吗？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_08C285D4068B443CA62FFF7164C88026 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "唔……虽然很抱歉……这首对我来说好像太难了……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "之前弹的《踩了只猫》已经是全力了。{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_E2961E29DD534903971BBB479D5034B8 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_3F533DA3CF494DEBA1146743852331E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这样啊。不过，那么弹肯定会被老人们群起攻之的啊。"

    show rs_image_225A15956FFB4AC2B4A3ACD0192F135D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那个，演奏就由友君来，\n我做一下曲目介绍呀翻乐谱呀之类的辅助性的……"

    show rs_image_26ACCF5B48104DD4A398798576538F0E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不可以！我想和翼君两个人一起表演！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好不容易迎来小钢琴部的第一次活动，\n只有我参加不就没有意义了嘛！{w=0.3}{nw}"
    show rs_image_EAF549F11EDE4A5AA68FCD7AECAB1DEF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_B8B73F5DF2F7457F9EB83538FFFD4FE7 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君……为什么你总是这么的……"
    show rs_image_63FF180F6A0743D4A3C1B1F8A07A1881 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "{size=14}{color=#C0C0C0}……（脸红心跳）。{/color}{/size}"

    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "{size=14}{color=#C0C0C0}（……帅气又刚强……好过头了、太完美了、太耀眼了……）{/color}{/size}"

    pause 0.35

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_DEB70960E8944B33903B14177D8DC211 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……明白了。\n我一定会尽全力在正式演出前学会别的曲子的！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_158D8E25C4414ECF868A62B83D40B99B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "一定不会让友君的心意白费的！！"

    show rs_image_D2BB5C80C5EC436C81AD2A89675FF109 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "喔～这想法很棒啊！！\n那么，比起选曲子，现在要做的是多练习呢！"

    show rs_image_55AA9D3ECD6A49F888891037C386D65A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯。指导就拜托了！"

    window hide

    pause 0.5

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E58D83DB9E234DE7AAB86A64350E6FC8

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_86500D05C8934AE7B4E71CC1D50E5D36 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_10B88B501E394D0BB0E3D5ECDC8DF543 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8676A882850344248D70E3A3623F329F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……这里手指总是来不及换回来……！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_4E534C3CC3ED418EA9C8155C87F1BCBB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼、翼君，稍微放松一点，好吗？"

    show rs_image_8676A882850344248D70E3A3623F329F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可、可现在完全没时间了，\n为什么无名指和小指总是不听使唤啊！？\n{w}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_10B88B501E394D0BB0E3D5ECDC8DF543 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "好烦！！听话啊，我的手指……！！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我、我还是第一次见到翼君这么生气……"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……不行，总是做不到……"

    show rs_image_3F533DA3CF494DEBA1146743852331E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……也是呐。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不要一直在脑袋里强迫自己去那么做，试着想像一下乐曲的旋律如何？"

    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "想像一下和乐曲融为一体弹奏着的自己，\n比如顺着乐曲的旋律操控手指之类的。"

    show rs_image_DEB70960E8944B33903B14177D8DC211 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好、好的！我会试试的。"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 1

    # Gallery unlock: images/CG/Tsubasas-Cantabile/Tsubasas-Cantabile 1.png
    $ zorder_rs_image_1DF1A98336DB4A81BE40028C743F7DF8 = -100
    show rs_image_1DF1A98336DB4A81BE40028C743F7DF8 as rs_image_1DF1A98336DB4A81BE40028C743F7DF8 zorder zorder_rs_image_1DF1A98336DB4A81BE40028C743F7DF8 onlayer master
    hide rs_image_1DF1A98336DB4A81BE40028C743F7DF8

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_1DF1A98336DB4A81BE40028C743F7DF8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6B0609ABE3C348F3A84F5E9250E70BE7

    pause 0.7

    window show

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……♪……♪♪……♪～♪"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……嗯，翼君的歌声真的好棒啊。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我、我还是第一次被这么说呐。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个，对了，试着唱一下现在在弹的曲子。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……嗯。♪……♪～～♪"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_E6A0D20A1A914A0CBCF8DCED075CD75A

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.5

    window show

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_F4E69F65605A49BCA7659DDD9B7624D5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "怎、怎么样……？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_3F533DA3CF494DEBA1146743852331E9 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w}唔……嗯嗯……"
    show rs_image_EEDE17A0523340C4B70747B46FC7D04C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "嗯！！！"

    stop effect fadeout 0.1
    $ sys_effect_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DB50197E13884F45AFBB23A957B18CA1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_D2BB5C80C5EC436C81AD2A89675FF109 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我想到了！！！{w}\n翼君，别管谱子了，钢琴不练了！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸！？到、到底发生什么了！？"

    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君！{w=0.5}{nw}"
    show rs_image_D2BB5C80C5EC436C81AD2A89675FF109 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "你啊……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_2028F963C6F041949E94C771B899A6AE as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{b}{/b}一定要负责“{color=#FF80C0}声部{/color}”！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_0F13158E12E14CB6AA93F6FE189A9B15 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2CADF8378C504B23B59B06DFEDCA17ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸————！！？？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_0F13158E12E14CB6AA93F6FE189A9B15 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_28A01C08CFC245F2B5B451B8E36AF5EB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君的歌声又好听又清澈，应该还是童音。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "在这之上多加练习的话，肯定会变得更好的！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那那那、那种事当然做不到啦！！\n绝对不行！！"

    show rs_image_EEDE17A0523340C4B70747B46FC7D04C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "肯定能行！我来伴奏，翼君来唱。"

    show rs_image_D2BB5C80C5EC436C81AD2A89675FF109 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "钢琴和女高音的双重演奏！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    show rs_image_8F24F3F0856A427BBFD119767177B781 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "务必要相信悠久正统的森海家一员的音乐直觉！"

    show rs_image_40378AEBEABC4F1181A8ACEC0693C48A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……{w}……\n{w=0.5}{nw}"
    show rs_image_55AA9D3ECD6A49F888891037C386D65A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "我明白了。毕竟决定是两个人一起来做了嘛。"

    show rs_image_DEB70960E8944B33903B14177D8DC211 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那么，为了能做出不会遗憾的成绩，我会努力的。"

    window hide

    pause 0.4

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那、首先肯定是训练！来来来，翼君，来这边躺下～"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸，哦、哦……这样？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好的那么——！！仰卧起坐开始了——！！\n来，一！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "为为为为什么？！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唱歌需要腹部用力对不对？\n提高音量的话音域也能扩展，好好做！！"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "是、是的～！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_8BDBB77570FB403298B922FBAAF4CFF1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "一二！一……二！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "别停别停！继续继续！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸～！腹、腹部、好痛……！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那就是你在锻炼肌肉的证据！为了能让小钢琴部拿出更好的成果，加油！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯！啊！！不、不行了！让、让我休息一下友君～！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "还不行还不行！！\n过去翼君可是对我{color=#008080}做过更过分的事{/color}呢！{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_DE3C56F304D94AD1AC2BFAEF18EC33B3 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就这点程度怎么可能免掉你的训练～！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "怎、怎么这样…！真的很痛，真的很累啊，友君～！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼……再拿出点毅力来。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "等超越自己的极限，肯定会觉得舒服起来的哦……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不要不要！怎么可能会觉得舒服嘛～！{w}\n好痛……不行了……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_DEF4707300154D00B22225E4F8282BA7

    pause 0.4

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼。那今天就到此为止。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不过，明天的训练可是会比今天严酷百倍哦。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_11E9CB4CF92548E88CF101664A977D06 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……什么的！！\n有点像{color=#8080FF}某魔法师漫画里的大反派{/color}一样的台词呐！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君，你很努力了！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "因果报应就是这么回到人身上的啊……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_8A80B90628C143D1B3A53C71240BBE2D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "（倒）……。"

    window hide

    pause 0.4

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    show center_title (_("{color=#7FBFFF}不过，不管怎样……{/color}")) as center_title zorder 1000
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    pause 2.0

    hide center_title
    with rs_effect_FC474B930CE449DD8BE5D4980A132631

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    $ zorder_tag_A366FE92B81D404585614E7D29CFAD20 = 100
    $ zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 = 100
    $ zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 = 100
    show rs_image_5292DFFBD4504E32A867FDA807E432BB as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_C52D954B3F3542A190DBAEBA87A65574 as tag_A366FE92B81D404585614E7D29CFAD20 at center_bottom zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    show rs_image_6D45A5BE9C9849C4B100BAF176A71634 as tag_DD234F3A788F4BD5954C8F12B53FB442 at center_bottom zorder zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 onlayer master
    show rs_image_D2B56AAA5B8F493FAD89F3FF93092C1A as tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 at center_bottom zorder zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君，发音练习啊，要像这样使用腹部……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这、这样？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不对不对，用腹肌的力量。{w}\n你看，根本还是软软的不是嘛～？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "噫呀！？好、好痒……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好，再来一次！注意力集中到腹部哦～"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为了确认是不是真的在用我会先拿手按着的。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我、我明白了。{w}啊～啊～啊～"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对就是这样！很好很好♪"

    window hide

    show rs_image_45583EC272F14EC3A9B7AF35F751AEE2 as tag_A366FE92B81D404585614E7D29CFAD20 zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    show rs_image_810C5B5E946148C0A282F18E48729D08 as tag_DD234F3A788F4BD5954C8F12B53FB442 zorder zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "♪～♪♪♪～♪"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，不错嘛！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过好不容易有一次被观众注目的机会，\n表情能更明快一些就好了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "看，像这样……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "{size=28}NICO！！！{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shock 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜哇好耀眼！！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君，笑一个，笑一个～"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好、好的……NI、NICO。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嘴再张大一点！翼君是只要想做就能做到的！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "顺便两手做剪刀状！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "NI、NICONICONI……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（就是现在！！）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊！！翼君的{color=#FF0000}正上方{/color}\n有《电摩战队电击游侠》的周边！！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "诶……？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好的可以了！！{w}看到好东西了，辛苦了哦，翼君。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "最、最后那个到底是是什么意思……"

    window hide

    show rs_image_6D45A5BE9C9849C4B100BAF176A71634 as tag_DD234F3A788F4BD5954C8F12B53FB442 zorder zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    show rs_image_2811AD30D4904CCCAD92CB38A9CE09B7 as tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 zorder zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "现在先听一下所有候选的曲子，觉得好的要说出来哦。{w}要放了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君戴好耳机了吗～？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯、嗯……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "（啊啊，距离好近……离得太近了～！！）"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……刚才那首是不错，不过我还是更喜欢这一首。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "对呢。我觉得这一首确实是最好的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真的嘛！？太好了！我和翼君喜欢的音乐类型一样呐。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好高兴呐。我还担心这么下去有一天我们会因为音乐喜好\n而“道不同不相为谋！”呐，现在看来没关系了，很好很好♪"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯嗯，是呐。我们两人未来一定可以在一起哦。"

    window hide

    pause 0.7

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_8BDBB77570FB403298B922FBAAF4CFF1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_C52D954B3F3542A190DBAEBA87A65574 as tag_A366FE92B81D404585614E7D29CFAD20 zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    show rs_image_810C5B5E946148C0A282F18E48729D08 as tag_DD234F3A788F4BD5954C8F12B53FB442 zorder zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 onlayer master
    show rs_image_2811AD30D4904CCCAD92CB38A9CE09B7 as tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 zorder zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 onlayer master
    with rs_effect_DF233E8792E9400F941FC5BF3484A344

    pause 0.7

    show center_title (_("{color=#7FBFFF}能和友君单独在一起努力\n我真的非常幸福……！{/color}")) as center_title zorder 1000
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    pause 3.0

    hide center_title
    with rs_effect_FC474B930CE449DD8BE5D4980A132631

    pause 1

    stop music fadeout 0.1
    $ sys_music_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A366FE92B81D404585614E7D29CFAD20
    hide tag_DD234F3A788F4BD5954C8F12B53FB442
    hide tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6
    with rs_effect_C29BFF9F2C814823B4B63C9D37A39E79

    pause 1.4

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D6ADB3B2DBE647DC91A820FFA6D351E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_7F6C95985A7641738465E73831D557C2

    show rs_image_014C49487C644BFD95C49FCA0B26030E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_7F6C95985A7641738465E73831D557C2

    show rs_image_9C6627EBA4894AB883E9F13296A23034 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_7F6C95985A7641738465E73831D557C2

    show rs_image_D6ADB3B2DBE647DC91A820FFA6D351E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_7F6C95985A7641738465E73831D557C2

    show rs_image_014C49487C644BFD95C49FCA0B26030E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_7F6C95985A7641738465E73831D557C2

    show rs_image_9C6627EBA4894AB883E9F13296A23034 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_7F6C95985A7641738465E73831D557C2

    pause 1.4

    stop effect3 fadeout 2.5
    $ sys_effect3_current_file = ""

    if sys_music_current_file != "sound/BGM/Angel and Demon.ogg":
        play music "sound/BGM/Angel and Demon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Angel and Demon.ogg"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 = 300
    show rs_image_48586B09A4E440199E581E9739B7423E as tag_D6FC9B6B4F4A4A158D4717FDA034AC56 at right_top zorder zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.5

    window show

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "等、等等等等！！\n刚才就在看了，你这股怠惰劲是怎么回事！！"

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "明明有那么多次气氛那么好，完全可以直接袭击过去的好不好！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_FC96DA18D96F4848B6116D014A875A5C = 300
    show rs_image_965284A0C1094C6A86DE0DD970592C02 as tag_FC96DA18D96F4848B6116D014A875A5C at left_top zorder zorder_tag_FC96DA18D96F4848B6116D014A875A5C onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_414B71521382454B97E8531A1ED4B265 "出、出现了啊～恶魔翼！！"

    rs_character_414B71521382454B97E8531A1ED4B265 "现在我和友君有着共同的目标，应该好好努力才对！"

    rs_character_414B71521382454B97E8531A1ED4B265 "这次可绝不会放任你不管！"

    show rs_image_1F91EE70C8AF49D9BD92023E162566F6 as tag_D6FC9B6B4F4A4A158D4717FDA034AC56 zorder zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "不不不，这才是该我出手的时候！"

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "要是真完全照你说的做，像友君这么完美的人很快就会被别人夺走了，\n这也无所谓！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_AD6E7660972A4480B36669B408D84C52 as tag_FC96DA18D96F4848B6116D014A875A5C zorder zorder_tag_FC96DA18D96F4848B6116D014A875A5C onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_414B71521382454B97E8531A1ED4B265 "什……！{w}可、可是！现在最重要的是练习！\n我怎么可能认同那种不正当的……"

    show rs_image_F955850AC94149A8B0457B07B6888C3C as tag_D6FC9B6B4F4A4A158D4717FDA034AC56 zorder zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "那我问你，放过这次机会，何时才能得到友君？\n到那时候，他不早就成了别人的东西了？"

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "你这种主张多一事不如少一事的家伙真的能好好处理那时候的关系么。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "连个解决方案都没有净说些漂亮话，太没责任感了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_244A47A10443417BAC419CFC285CD946 as tag_FC96DA18D96F4848B6116D014A875A5C zorder zorder_tag_FC96DA18D96F4848B6116D014A875A5C onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_414B71521382454B97E8531A1ED4B265 "唔……！可、可是……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7DCCC152C2B441A2A9B0877A32237163 as tag_D6FC9B6B4F4A4A158D4717FDA034AC56 zorder zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "恋爱永远是先下手为强。那点毅力都没有就给我闪一边去！\n友君就由我拿下了！！"

    window hide

    pause 0.8

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_D6FC9B6B4F4A4A158D4717FDA034AC56
    hide tag_FC96DA18D96F4848B6116D014A875A5C
    with rs_effect_BF9939EFC91941EDBE78E126AA0B953F

    pause 1.5


    if judge_lm_condition([]):
        jump block_0000371F

    return

label block_0000371F:
    # Node: 0000371F (翼的流轉音符 2)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.5

    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    if sys_music_current_file != "sound/BGM/Something strange 1.ogg":
        play music "sound/BGM/Something strange 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something strange 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    $ zorder_tag_A366FE92B81D404585614E7D29CFAD20 = 100
    $ zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 = 100
    $ zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 = 300
    show rs_image_8BDBB77570FB403298B922FBAAF4CFF1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_45583EC272F14EC3A9B7AF35F751AEE2 as tag_A366FE92B81D404585614E7D29CFAD20 at center_bottom zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    show rs_image_6D45A5BE9C9849C4B100BAF176A71634 as tag_DD234F3A788F4BD5954C8F12B53FB442 at center_bottom zorder zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 onlayer master
    show rs_image_D2B56AAA5B8F493FAD89F3FF93092C1A as tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 at center_bottom zorder zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君！今天的腹肌锻炼也要开始了哦！{w}来，加油——♪"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "一二……一二。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好好，再加把劲，这次再怎么抱怨辛苦也不会停下的哦～"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……说起来，友君，{w}之前说过那是\n{color=#8080FF}某（魔法师）漫画中大反派{/color}的台词呐。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？嗯，是这样没错。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那干脆……！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_5C67F5A7AC1B4BB8A1D784ECBD8849C1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1DB92443238942EB873783BEE27CA495

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫诶！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_B410AEB92D534DC9B260343C4B1BB0C6 as tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 zorder zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不像这样猛地压上去，用恐怖支配对方的身体和精神的话，\n可是一点都不像的哦。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸。嗯、嗯。也许正如你所说……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "果然，友君比起做的那一方还是被做的那一方比较合适。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔。总觉得有点不甘心，又觉得这样好像也不错……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "翼、翼君，你到底怎么了啊——？？"

    window hide

    pause 0.6

    show rs_image_C52D954B3F3542A190DBAEBA87A65574 as tag_A366FE92B81D404585614E7D29CFAD20 zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好，接下来是发音练习！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "来，翼君，开始——！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "♪——♪——♪——"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君，虽说用腹腔的力量很重要。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "有意夹紧屁股的话，效果会更好的哦！"

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那么，就请友君来一个示范。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "明白。像这样用力一下，然后发声就可以了！\n好了，翼君也……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_CB6A1F1EB2CD4DEEBAB41DE63AA5F71A as tag_A366FE92B81D404585614E7D29CFAD20 zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    with rs_effect_1DB92443238942EB873783BEE27CA495

    show rs_image_5DB1B061F0E8460AAAB0F037C54BECF9 as tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 zorder zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "噫！？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "果然。屁股很紧，手指都插不进去呢。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、不用确认到那种程度！\n这这、这本来是该翼君做的事情！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，好像差一点就能到里面了。来，友君，放松一下。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、不要————！！"

    window hide

    pause 0.6

    show rs_image_810C5B5E946148C0A282F18E48729D08 as tag_DD234F3A788F4BD5954C8F12B53FB442 zorder zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君，今天也要回想起笑脸喔！唱歌时一定要用笑脸来唱。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯～好像很难的样子呐。{w}友君，像上次那样示范一下。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的～这次要看好了哦～看，就像这样……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "NICO！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_43E21489B13247FC8B6DEEAC4B071954 as tag_DD234F3A788F4BD5954C8F12B53FB442 zorder zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 onlayer master
    with rs_effect_1DB92443238942EB873783BEE27CA495

    show rs_image_610DC15A95984D11BC38EA57E0504978 as tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 zorder zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那，就这样两手做剪刀状，视线上抬。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶，不，那个是……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不是对我做过同样的事吗。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "难道说，是在指挥我做毫无意义的事？肯定不是那样的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……我，可是认真在练习的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯、嗯！嗯！！绝对没有绝对没有！\n那个动作是有意义的！有意义的！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那请。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "NI、NICO……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    extend "{color=#FF80FF}阿嘿……{/color}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，就这样先不要动。{w}\n为了能作为以后的参考，请务必让我先拍一张。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那……个，手机放什么地方了……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    show rs_image_07C32F7FA30C4FE89C4E6C3367EC6F03 as tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 zorder zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "等、等等啦翼君！！一直这个姿势会死人的！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "脸要麻了！麻……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_414B71521382454B97E8531A1ED4B265 "……{w}这也太……"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_A366FE92B81D404585614E7D29CFAD20
    hide tag_DD234F3A788F4BD5954C8F12B53FB442
    hide tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 3.ogg"

    # Gallery unlock: images/CG/Tsubasas-Cantabile/Tsubasas-Cantabile 7.png
    $ zorder_rs_image_2B9BE937603E4E96969F3C4CE130A6F5 = -100
    show rs_image_2B9BE937603E4E96969F3C4CE130A6F5 as rs_image_2B9BE937603E4E96969F3C4CE130A6F5 zorder zorder_rs_image_2B9BE937603E4E96969F3C4CE130A6F5 onlayer master
    hide rs_image_2B9BE937603E4E96969F3C4CE130A6F5

    # Gallery unlock: images/CG/Tsubasas-Cantabile/Tsubasas-Cantabile 8.png
    $ zorder_rs_image_689A15BAED4D45EAA7879993C605248F = -100
    show rs_image_689A15BAED4D45EAA7879993C605248F as rs_image_689A15BAED4D45EAA7879993C605248F zorder zorder_rs_image_689A15BAED4D45EAA7879993C605248F onlayer master
    hide rs_image_689A15BAED4D45EAA7879993C605248F

    # Gallery unlock: images/CG/Tsubasas-Cantabile/Tsubasas-Cantabile 3.png
    $ zorder_rs_image_2F3A55DB5E7D426AA2695C5D1B97A040 = -100
    show rs_image_2F3A55DB5E7D426AA2695C5D1B97A040 as rs_image_2F3A55DB5E7D426AA2695C5D1B97A040 zorder zorder_rs_image_2F3A55DB5E7D426AA2695C5D1B97A040 onlayer master
    hide rs_image_2F3A55DB5E7D426AA2695C5D1B97A040

    $ zorder_tag_A366FE92B81D404585614E7D29CFAD20 = 0
    $ zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 = 100
    $ zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 = 200
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_2B9BE937603E4E96969F3C4CE130A6F5 as tag_A366FE92B81D404585614E7D29CFAD20 at center_bottom zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    show rs_image_689A15BAED4D45EAA7879993C605248F as tag_DD234F3A788F4BD5954C8F12B53FB442 at center_bottom zorder zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 onlayer master
    show rs_image_3145D0A7BB104D08B1367C96EB757F95 as tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 at center_bottom zorder zorder_tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6 onlayer master
    show rs_image_2F3A55DB5E7D426AA2695C5D1B97A040 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_414B71521382454B97E8531A1ED4B265 "你个大笨蛋！！！！！！"

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "唔！"

    window hide

    pause 0.5

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_A366FE92B81D404585614E7D29CFAD20
    hide tag_DD234F3A788F4BD5954C8F12B53FB442
    hide tag_80FB9A001A5F41E9B9BA13BFEDC0F2D6
    with rs_effect_3FBF9470026545738C69B18D7D539AA9

    pause 2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Swallow 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.7

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_5E7D24311EEA4507B1FE775C8265EADA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯……被另一个自己顺从欲望就这么暴走，吗。"

    stop effect fadeout 2
    $ sys_effect_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_08C285D4068B443CA62FFF7164C88026 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_music_current_file != "sound/BGM/Daily 2.ogg":
        play music "sound/BGM/Daily 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 2.ogg"

    pause 0.4

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜，是这样的……我到底……"

    show rs_image_324C77394BC349DB995FB24E2E90630F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那种事情不用在意。不论是谁都会这样的。"

    show rs_image_DB50197E13884F45AFBB23A957B18CA1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "是、是这样吗！？"

    show rs_image_7780BD482A234B81970D2A4B4EE70A97 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "虽说每个人都不同，\n"

    extend "在喜欢的人面前心跳不已静不下来也是常有的事。"

    show rs_image_B8B73F5DF2F7457F9EB83538FFFD4FE7 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "唔，嗯……嗯？"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_0F13158E12E14CB6AA93F6FE189A9B15 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "欸！？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2CADF8378C504B23B59B06DFEDCA17ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我难道对绫濑君说过喜欢友君！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B2BA8BCD25E24F30AEBD6E8214BF9D0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_8676A882850344248D70E3A3623F329F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊！！这不就说出来了……！！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "一之濑君的话，差不多已经和写在脸上一个意思了……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_2CADF8378C504B23B59B06DFEDCA17ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不是的！\n毕竟我们、我们都是男孩子，这、这种事情！"

    show rs_image_C66A56F89C43490FBD87D2164FFD98A5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "话题中途好像偏了啊，那先不管这个。\n总之，这种程度的慌乱是很正常的。"

    show rs_image_04B589B0BDD948F4BB727589A05C0593 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "对喜欢的人十分在意，心中无法平静，\n"

    extend "想要触摸，想要亲吻，想要做那个，也是很正常的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "做、做做那个什么的！！\n怎、怎么可以！那个还太早了……！"

    show rs_image_3938BA4DFD63427F90A7EFC10C734A7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嘛，嘴上是这么说，另一个自己肯定忍了很久吧。"

    show rs_image_AF27F47A0A09448EA5BA5B2F3878BBA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "唔……我……我讨厌只会想那种事的自己……"

    show rs_image_75FC3AE6556E4AB0BF49FDBF4A6E9FD1 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嘛，不要这么说，\n将那些也都算进去才是完整的一之濑君。"

    show rs_image_F4E69F65605A49BCA7659DDD9B7624D5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "话、话是这么说……可……"

    show rs_image_324C77394BC349DB995FB24E2E90630F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不像是愿意接受的样子呐。"

    show rs_image_5E7D24311EEA4507B1FE775C8265EADA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "要是有一个能让自己喜欢上那样的一面的机会的话说不定更有说服力，\n不过该怎么找这种机会呢……"

    show rs_image_040651EB0DB9405AB3B73494D241B34C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哈啊……"

    show rs_image_75FC3AE6556E4AB0BF49FDBF4A6E9FD1 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "算了，这也不是说有就有的嘛。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "总而言之，把自己的感受和心中的冲动分开处理如何？"

    show rs_image_04B589B0BDD948F4BB727589A05C0593 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "毕竟一之濑君的贞操观念还是很保守的。"

    show rs_image_EAF549F11EDE4A5AA68FCD7AECAB1DEF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "贞操观念？……不明白是什么意思，\n不过之前友君谈到绫濑君的时候……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "“{color=#FF8080}无节操太郎{/color}”记得这么说了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_12E87FF557504657A6A268BFA1305C64 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……那个混蛋……。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_08917E60F7E24896AA5D34106EADD613 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "算、算了，具体什么意思不需要知道。"

    show rs_image_151D5EA5EE3B4D7BA2D61C7C63F972CC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "简单来说就是，“再多多享受一下也没关系？”\n这个意思！"

    show rs_image_70C4C5BDAB0647638B31D8F61A4438FD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "明、明白了……"
    show rs_image_AF27F47A0A09448EA5BA5B2F3878BBA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "可、可是，如果真的出现无法忍耐的情况，\n我该怎么做……"

    show rs_image_AF32E0AC0DFE44B0B1AD4FA76A696E36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "如果真的忍不住了没有关系！\n"
    show rs_image_04B589B0BDD948F4BB727589A05C0593 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过，如果真的做了，就要负责到最后哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3CC2CAAD5140495DAF5927162F832557 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说起来很简单，做起来很难的。说不定还会给你带来一生的悔恨。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯。一定、不能、完全顺从欲望，要小心小心再小心……"

    show rs_image_C66A56F89C43490FBD87D2164FFD98A5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯嗯。加油，一之濑君。"

    show rs_image_9C9BE421F7E44A6E9376D93AB2B16371 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……说是这么说……"

    pause 0.3

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "下次要在友君家里两人单独练习了，{w}真的没关系吗……"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_CAE7E1A8F1B9452F9A07D2E1DAAE9E40

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DB5AB8A1EA534F3F81A68748DB089DF3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.8

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_64D8D1E21F7F40938F719E0070CF195B as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，想了挺有趣的问候语嘛！\n这个是在电视上学到的吗？"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_225A15956FFB4AC2B4A3ACD0192F135D as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯，是从喜欢的相声节目上……"

    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯嗯！！这下子不管是老爷爷还是老婆婆肯定都能高兴起来了呐！"

    show rs_image_FACF02D10C574EC8ABF41E3D996A6E34 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "太好了。那么到时候就这样做。"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯。这下应该就可以了呐。{w}呼……好累啊！"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_64D8D1E21F7F40938F719E0070CF195B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    show rs_image_E60095D58B7244DA80FA5BD8367449C5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "钻进被窝休息一下休息一下～"

    show rs_image_55AA9D3ECD6A49F888891037C386D65A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "剩下的就是如何克服紧张发挥自己的最大实力了！\n"
    show rs_image_B8B73F5DF2F7457F9EB83538FFFD4FE7 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哈……现在也一直心跳不止……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DA81DF1010164DD7BCD31DA585749FFD as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼……那种东西想了也没用的～"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "如果不是真的站到舞台上是没有干劲的！\n好啦，翼君也一起来～"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_DB50197E13884F45AFBB23A957B18CA1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸！？那、那句话是几个意思……"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DA81DF1010164DD7BCD31DA585749FFD as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君也很累了对不对～？稍微躺下休息一会儿嘛。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "看～旁边的位置是空的哦！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_2CADF8378C504B23B59B06DFEDCA17ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不行不行不行！！怎么可以！\n像我这样的人怎么可以那么不知好歹，"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "现在这样就算冷一点也没关系的，\n没没没没关系的！"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的～好了好了，过来！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不可以！{w}欲望……！{w}责任！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    extend "啊哇哇！？"

    window hide

    pause 0.8

    # Gallery unlock: images/CG/Tsubasas-Cantabile/Tsubasas-Cantabile 4.png
    $ zorder_rs_image_361696A1939D46CEBF91C8115642936C = -100
    show rs_image_361696A1939D46CEBF91C8115642936C as rs_image_361696A1939D46CEBF91C8115642936C zorder zorder_rs_image_361696A1939D46CEBF91C8115642936C onlayer master
    hide rs_image_361696A1939D46CEBF91C8115642936C

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_361696A1939D46CEBF91C8115642936C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_338B12F993214B9CA45CE53965EE33E0

    pause 0.6

    window show

    if sys_music_current_file != "sound/BGM/Guitar 1.ogg":
        play music "sound/BGM/Guitar 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Guitar 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哦……！没想到会变成这个样子……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那、那个？翼君？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么了？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……这可是友君的错。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我明明已经在尽力忍耐了，{w}\n友、友君非要那么强硬。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "恶质的那个我……可又要出来了哦……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼、翼君……？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……。\n"
    # Gallery unlock: images/CG/Tsubasas-Cantabile/Tsubasas-Cantabile 5.png
    $ zorder_rs_image_BB15BC7CC853407495EB41EE25D1EFAD = -100
    show rs_image_BB15BC7CC853407495EB41EE25D1EFAD as rs_image_BB15BC7CC853407495EB41EE25D1EFAD zorder zorder_rs_image_BB15BC7CC853407495EB41EE25D1EFAD onlayer master
    hide rs_image_BB15BC7CC853407495EB41EE25D1EFAD

    show rs_image_BB15BC7CC853407495EB41EE25D1EFAD as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "可以哦，不管做什么。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "诶……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 200
    show rs_image_2CADF8378C504B23B59B06DFEDCA17ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_top zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 = 300
    show rs_image_7DCCC152C2B441A2A9B0877A32237163 as tag_D6FC9B6B4F4A4A158D4717FDA034AC56 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_FC96DA18D96F4848B6116D014A875A5C = 300
    show rs_image_244A47A10443417BAC419CFC285CD946 as tag_FC96DA18D96F4848B6116D014A875A5C at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_FC96DA18D96F4848B6116D014A875A5C onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_3F675A01E7044320A4E7310837DE6C60 "{size=36}诶诶诶！？！？{/size}"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_D6FC9B6B4F4A4A158D4717FDA034AC56
    hide tag_FC96DA18D96F4848B6116D014A875A5C
    with rs_effect_DCD8B79F49964D74AC066FB7F605BC72

    pause 0.4

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈……翼君的话，我是可以接受的哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊啊啊、啊？这、这这这就是说！！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "如果演奏能成功的话……{w}呐？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这个、那个……嗯……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "呜、呜哇！"

    window hide

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 200
    show rs_image_DB5AB8A1EA534F3F81A68748DB089DF3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DB50197E13884F45AFBB23A957B18CA1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这样一来，就可以积攒想要对外释放的力量，当天不就可以尽全力了吗？"

    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "所以，奖励要稍・后・再・说♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_B8B73F5DF2F7457F9EB83538FFFD4FE7 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好的……{w=0.4}{size=15}好的……{/size}{w=0.4}{size=14}好的……{/size}"

    show rs_image_943958ACE1594083BA9B66D14E70D431 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "如何？翼君，真的明白了？？"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哇、嗯。奖励……奖励……奖励……。{w}\n明白，没关系……"

    show rs_image_28A01C08CFC245F2B5B451B8E36AF5EB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好的！！那么继续之前，向着正式表演多加练习～！！！"

    show rs_image_DA81DF1010164DD7BCD31DA585749FFD as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……不过在那之前果然先让我睡一觉～{w}晚安～～"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_9C6627EBA4894AB883E9F13296A23034 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 = 300
    $ zorder_tag_FC96DA18D96F4848B6116D014A875A5C = 300
    show rs_image_48586B09A4E440199E581E9739B7423E as tag_D6FC9B6B4F4A4A158D4717FDA034AC56 at right_top zorder zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 onlayer master
    show rs_image_244A47A10443417BAC419CFC285CD946 as tag_FC96DA18D96F4848B6116D014A875A5C at left_top zorder zorder_tag_FC96DA18D96F4848B6116D014A875A5C onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "紧急！紧急！"

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "现在先停战！！为了奖励也要赶紧练习！！"

    show rs_image_965284A0C1094C6A86DE0DD970592C02 as tag_FC96DA18D96F4848B6116D014A875A5C zorder zorder_tag_FC96DA18D96F4848B6116D014A875A5C onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_414B71521382454B97E8531A1ED4B265 "不是为了奖励是为了让活动成功！！\n居然怀着这种心态，太差劲了！！"

    show rs_image_1F91EE70C8AF49D9BD92023E162566F6 as tag_D6FC9B6B4F4A4A158D4717FDA034AC56 zorder zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_2EBE5D3FE4D24B89A65C688BA8BED15A "无所谓了，反正结果一样，\n就算是为了这个，人多力量怎么说也会大嘛？"

    show rs_image_244A47A10443417BAC419CFC285CD946 as tag_FC96DA18D96F4848B6116D014A875A5C zorder zorder_tag_FC96DA18D96F4848B6116D014A875A5C onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_414B71521382454B97E8531A1ED4B265 "……也对，合作！要让“我”发挥出最大的实力！！{w}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7DCCC152C2B441A2A9B0877A32237163 as tag_D6FC9B6B4F4A4A158D4717FDA034AC56 at right_top zorder zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 onlayer master
    show rs_image_AD6E7660972A4480B36669B408D84C52 as tag_FC96DA18D96F4848B6116D014A875A5C zorder zorder_tag_FC96DA18D96F4848B6116D014A875A5C onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_21E8D962FC074E31A97895C928270046 "总之这里要先战胜自己！！！"

    window hide

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_D6FC9B6B4F4A4A158D4717FDA034AC56
    hide tag_FC96DA18D96F4848B6116D014A875A5C
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 0.8

    stop music fadeout 2
    $ sys_music_current_file = ""

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DB5AB8A1EA534F3F81A68748DB089DF3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_55AA9D3ECD6A49F888891037C386D65A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_DA81DF1010164DD7BCD31DA585749FFD as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……我、{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_158D8E25C4414ECF868A62B83D40B99B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我会努力的！！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦～加油哦～呼……"

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2


    if judge_lm_condition([]):
        jump block_0000371E

    return

label block_0000371E:
    # Node: 0000371E (CP1 Daytime 翼)
    call block_00000EE7 from _call_block_00000EE7

    if judge_lm_condition([]):
        jump block_00003AF5

    return

label block_00003AF5:
    # Node: 00003AF5 (翼的流轉音符 4)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    show rs_image_28CB16F81175458EA97C8F0250448304 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 1.5

    show rs_image_4B5F763E9F424591A5E354CF41830363 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 0.7

    if sys_music_current_file != "sound/BGM/To the future.ogg":
        play music "sound/BGM/To the future.ogg" loop
        $ sys_music_current_file = "sound/BGM/To the future.ogg"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_86500D05C8934AE7B4E71CC1D50E5D36 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_8DB9EBBA116648CAAA85C0A0F67B04D2 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜哇！？翼、翼君，怎么了那么慌张！？"

    show rs_image_55AA9D3ECD6A49F888891037C386D65A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "今天我们要在音乐室给敬老会的节目彩排，{w}\n已经得到了老师的许可，观众也已经到场了！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶！？这种事……什么时候做的！？{w}\n全都是翼君一个人做的？"

    show rs_image_70C4C5BDAB0647638B31D8F61A4438FD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "是、是的……擅自做这种事很抱歉。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不过，我无论如何都做不到像友君那样干净磊落。"

    show rs_image_AF27F47A0A09448EA5BA5B2F3878BBA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "就这样的状态，万一连累友君，我真的会后悔到无以复加的。"

    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔、嗯……"

    show rs_image_DEB70960E8944B33903B14177D8DC211 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "所以，为了不变成那样，我觉得必须要做点什么。"

    show rs_image_F4E69F65605A49BCA7659DDD9B7624D5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不过这只是我的任性，抱歉。{w}\n这是我的问题，最差的情况下，就算友君不愿意……"

    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不，这么说就不对了。"

    show rs_image_0BDBAB46852441A1A55BE2EB34CF561F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸……"

    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "小钢琴部是我们两个人的问题！{w}翼君能这么关心这件事我真的很高兴哦。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "一起奋斗的同伴这么努力，这比任何鼓励的言语都有效哦。"

    show rs_image_D2BB5C80C5EC436C81AD2A89675FF109 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "走了，彩排！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "把我们的双重演奏的实力给大家展现出来，吓他们个措手不及！"

    show rs_image_E60095D58B7244DA80FA5BD8367449C5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯！！"

    window hide

    pause 0.6

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2

    if sys_music_current_file != "sound/BGM/Treasure-Spring-of-Graduate.ogg":
        play music "sound/BGM/Treasure-Spring-of-Graduate.ogg" loop
        $ sys_music_current_file = "sound/BGM/Treasure-Spring-of-Graduate.ogg"

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_B08F170752C74A09BC000D1CF77FA609 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.2

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_DFF43C28E0D9414492DE4927927BBDBF as tag_61A891D6A6D047DC93695DA12E13CC75 at center_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_D4EA402CA6DB46BC8B23322A9C6C4D92 as tag_724406A84D7141298EFF0D864FAE1534 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_C3D494057B75425DB7D4CF5C9BEEF358 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_top zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 300
    show rs_image_5B33B923BAE5473B856DF55BACE9E1D7 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_C95D7A9489554E95B60C95F27C1215FF as tag_DCBDF256A1E242E78A25910AE27C0954 at left_top zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    show rs_image_3806F899C04B4F119D261714031BD373 as tag_CC4336DE74164173AC47C2C317367F10 at right_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_535CA73FE5F041DC934ADD42483CCCF6 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_A5121F2F859A490B9808D2589018163C as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_E0D00426275740F394D32435264217E5 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_C66A56F89C43490FBD87D2164FFD98A5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_0D5BC78C8923442DB3E842DF9CA717D4 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.2

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_286CAF074B77418F8F63C88FD5379830 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_D2A450B39A1A4C46BBF15CFA6979230F as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_13C4DC022C7E4638BB26DDDEB53212F6 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.2

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(0.5, hard=True)

    # Gallery unlock: images/CG/Tsubasas-Cantabile/Tsubasas-Cantabile 1.png
    $ zorder_rs_image_1DF1A98336DB4A81BE40028C743F7DF8 = -100
    show rs_image_1DF1A98336DB4A81BE40028C743F7DF8 as rs_image_1DF1A98336DB4A81BE40028C743F7DF8 zorder zorder_rs_image_1DF1A98336DB4A81BE40028C743F7DF8 onlayer master
    hide rs_image_1DF1A98336DB4A81BE40028C743F7DF8

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_1DF1A98336DB4A81BE40028C743F7DF8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Clap 1.ogg"

    # Gallery unlock: images/CG/Tsubasas-Cantabile/Tsubasas-Cantabile 2.png
    $ zorder_rs_image_DF4B118410C548ADBD1EA7899F30BCCF = -100
    show rs_image_DF4B118410C548ADBD1EA7899F30BCCF as rs_image_DF4B118410C548ADBD1EA7899F30BCCF zorder zorder_rs_image_DF4B118410C548ADBD1EA7899F30BCCF onlayer master
    hide rs_image_DF4B118410C548ADBD1EA7899F30BCCF

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_DF4B118410C548ADBD1EA7899F30BCCF as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B6D2CFDC1CB5407EACD7FBC1D100D198

    pause 4

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    stop effect fadeout 4
    $ sys_effect_current_file = ""

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6158BA9B7EE24D2EA88699A9FDB26B97 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.8

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君，昨天真的辛苦了！练习的成果终于出来了呐！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是至今为止最完美的歌声哦。"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_D6900DA7D3A54445A3A7BAA4FA959F33 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯！我自己也觉得已经尽全力了。"

    show rs_image_943958ACE1594083BA9B66D14E70D431 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊咧？翼君，总觉得……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "声音是不是比平时低了……"

    show rs_image_E60095D58B7244DA80FA5BD8367449C5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊哈哈……是呢。表演结束时总觉得有点不舒服……"

    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "难、难道说是变声了！？{w}翼君，那是二次性征哦！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好厉害！！果然眉毛浓的话发育也会早嘛。"

    show rs_image_225A15956FFB4AC2B4A3ACD0192F135D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这、这并没有关系！{w}\n如果真的是变声，在表演结束后才开始真是太好了。"

    show rs_image_FACF02D10C574EC8ABF41E3D996A6E34 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "明明很不擅长在大家面前表演，竟然还能感觉到如此的兴奋……"

    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这不是好事嘛～！今后作为小钢琴部的声部担当，请多多关照了！"

    show rs_image_40378AEBEABC4F1181A8ACEC0693C48A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不过，像之前那样高的声音以后再也发不出来了也有可能……"

    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那下次就不唱女高音试试女低音！{w}\n如果变得更低，还有男高音！男中音！！男低音！！！"

    show rs_image_28A01C08CFC245F2B5B451B8E36AF5EB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没关系的。不论如何都有适合你的声部哦。"

    show rs_image_D6900DA7D3A54445A3A7BAA4FA959F33 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "说的是呢！又有自信了。那么，今后也会努力练习歌唱的。"

    show rs_image_39A751328FDE46FAB3026BEC1F2E6B1C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "～～♪"

    show rs_image_FACF02D10C574EC8ABF41E3D996A6E34 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，是我刚才唱的歌，真的很好听呐。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "下次想要请友君教我口笛的吹奏方法了，不知道可不可以呐……"

    show rs_image_39A751328FDE46FAB3026BEC1F2E6B1C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "～～～♪"

    show rs_image_EAF549F11EDE4A5AA68FCD7AECAB1DEF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"
    show rs_image_B8B73F5DF2F7457F9EB83538FFFD4FE7 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……。\n"
    show rs_image_6C7D131D881A4E7296FCD71C208CF53F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    extend "友君，之前的约定，还记得吗？"

    show rs_image_39A751328FDE46FAB3026BEC1F2E6B1C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "～♪"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_8DB9EBBA116648CAAA85C0A0F67B04D2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……欸。那个……那个啊。"

    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "约定本身、还记得。不过，唔……"

    show rs_image_8A80B90628C143D1B3A53C71240BBE2D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那时候到底在想什么呐，\n睡糊涂了呐，内容有些记不清了呢……哈哈哈～……"

    show rs_image_08C285D4068B443CA62FFF7164C88026 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……我就觉得会是这样。友君，班级游泳比赛竞争的时候也是这样的。"

    show rs_image_952D06E912C54776B1C4F5BB577DFB95 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊、啊哈哈。对、对不起……"

    show rs_image_40378AEBEABC4F1181A8ACEC0693C48A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我……会在表演中这么开心，一定是多亏了和友君在一起。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "练习的时候也很辛苦、很开心。\n能和我一起度过这么幸福的时间，已经非常满足了。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "所以，那时候说的过高的期望……就算了。\n"
    show rs_image_6C7D131D881A4E7296FCD71C208CF53F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "我、{w=0.4}{nw}"
    show rs_image_40378AEBEABC4F1181A8ACEC0693C48A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "我只是想要友君的表扬罢了。"

    show rs_image_E262B3AC8BDF48E4A8BEEBA281DFA194 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……表扬，什么比较好……{w}\n翼君希望我怎么做？"

    show rs_image_DB50197E13884F45AFBB23A957B18CA1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸。这个……那个……"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"
    show rs_image_55AA9D3ECD6A49F888891037C386D65A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "{size=14}亲{/size}……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B8B73F5DF2F7457F9EB83538FFFD4FE7 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么！？"

    show rs_image_158D8E25C4414ECF868A62B83D40B99B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我希望、友君、能、亲我一口……\n"
    show rs_image_AF27F47A0A09448EA5BA5B2F3878BBA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……不行吗……？"

    show rs_image_E262B3AC8BDF48E4A8BEEBA281DFA194 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……唔嗯……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_DB50197E13884F45AFBB23A957B18CA1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2CADF8378C504B23B59B06DFEDCA17ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "抱、抱歉说了奇怪的话！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "刚才说的，那个……是玩笑！\n都那么说了肯定是玩笑了嘛！！那个、那个……"

    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……。"
    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "好啊，没问题。\n本来这件事就是我忘掉内容不好嘛。"

    show rs_image_0F13158E12E14CB6AA93F6FE189A9B15 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸欸！真、真的…？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "作、作为同意的交换条件，只是亲脸哦！！好了！闭上眼睛！！"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "是、是的！\n"
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Worried 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Worried 1.ogg"

    extend "……"

    window hide

    pause 2

    stop effect fadeout 0.3
    $ sys_effect_current_file = ""

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……翼君，你真的辛苦了！{w}……你真的很努力了！"

    window hide

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 2

    # Gallery unlock: images/CG/Tsubasas-Cantabile/Tsubasas-Cantabile 6.png
    $ zorder_rs_image_A1E7CA7F049F49908469DC30E836FCEF = -100
    show rs_image_A1E7CA7F049F49908469DC30E836FCEF as rs_image_A1E7CA7F049F49908469DC30E836FCEF zorder zorder_rs_image_A1E7CA7F049F49908469DC30E836FCEF onlayer master
    hide rs_image_A1E7CA7F049F49908469DC30E836FCEF

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_A1E7CA7F049F49908469DC30E836FCEF as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.5

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……欸……！？"

    window hide

    pause 0.7

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6158BA9B7EE24D2EA88699A9FDB26B97 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 1

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg"

    window show

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_B8B73F5DF2F7457F9EB83538FFFD4FE7 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……本、本来只是想亲一下脸算了的，可想到翼君已经先一步开始成长……"

    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "如果亲到嘴唇不知道行不行啊……这么一想就……没、没别的意思！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好了！奖励已经给了！！结束！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_8EAA741E3DC64ADE86CF2622687CB541

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_158D8E25C4414ECF868A62B83D40B99B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_8EAA741E3DC64ADE86CF2622687CB541

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_8676A882850344248D70E3A3623F329F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_8EAA741E3DC64ADE86CF2622687CB541

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊哇……{w}啊哇哇哇……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "刚、刚才的有没有被人看到！？应该没关系……"

    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那我回教室了！！拜拜！！"

    window hide

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.8

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 0.7

    show center_title (_("{color=#7FBFFF}我一直都梦想着，或许有一天\n这份奖励能走出梦境，进入现实……{/color}")) as center_title zorder 1000
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    pause 3.5

    hide center_title
    with rs_effect_FC474B930CE449DD8BE5D4980A132631


    $ set_window("イベントモード")
    $ zorder_tag_FC96DA18D96F4848B6116D014A875A5C = 300
    $ zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 = 300
    show rs_image_BA352EDF384A442A8803EE8B218482A7 as tag_FC96DA18D96F4848B6116D014A875A5C at left_top zorder zorder_tag_FC96DA18D96F4848B6116D014A875A5C onlayer master
    show rs_image_1F91EE70C8AF49D9BD92023E162566F6 as tag_D6FC9B6B4F4A4A158D4717FDA034AC56 at right_top zorder zorder_tag_D6FC9B6B4F4A4A158D4717FDA034AC56 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.5

    window show

    pause 0.3

    rs_character_21E8D962FC074E31A97895C928270046 "阿门……"

    window hide

    pause 0.8

    hide tag_FC96DA18D96F4848B6116D014A875A5C
    hide tag_D6FC9B6B4F4A4A158D4717FDA034AC56
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 2.5

    show left_title (_("第二天")) as left_title
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    pause 1.0

    hide left_title
    with rs_effect_FC474B930CE449DD8BE5D4980A132631

    pause 0.8

    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.6

    window show

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_D6900DA7D3A54445A3A7BAA4FA959F33 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好像并不是变声只是太累了，声音又变回来了哦！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！！是这样吗！？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "唔、唔哇……那、我那个时候的亲……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_0BDBAB46852441A1A55BE2EB34CF561F as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "诶？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？"

    show rs_image_225A15956FFB4AC2B4A3ACD0192F135D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个……{w}其实，从友君那里得到奖励的时候，\n一瞬间失神了，脑袋里只剩下一片空白……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸、欸欸欸欸！！！\n那、那时候的事情难道没有印象了！？"

    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜呜～！我明明那么不好意思的！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "而且声音也没有变，果然当时该亲脸才对！！"

    show rs_image_F4E69F65605A49BCA7659DDD9B7624D5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸，难道不是在脸上亲的？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_B8B73F5DF2F7457F9EB83538FFFD4FE7 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，那、那种无谋的要求肯定是不现实的呐……{w}\n那个那个，那个时候到底做了什么啊？"

    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "秘、秘密！！绝不会说的！！绝对——不会说的！"

    show rs_image_8676A882850344248D70E3A3623F329F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "怎么这样……告诉我嘛～真的很在意的！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不要不要不——要！！真是的！！翼君这个大笨蛋！！"

    show rs_image_1906DCD87DCD4B098761C02DBFA1F2B8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……！！告诉我嘛～说一下嘛～！"

    window hide

    pause 0.8

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_367D6887C01741AFA0312C70A109F138

    call scb_flag_title_end(1, _("「翼的流转音符」")) from _call_scb_flag_title_end

    if judge_lm_condition([]):
        jump block_0000391D

    return

label block_0000391D:
    # Node: 0000391D (Phase: 0)
    $ C1S2Phase = 0
    if Chapter <> 1:
        $ del C1S2Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_0000391C
    if judge_lm_condition([]):
        jump block_0000391B

    return

label block_0000391C:
    # Node: 0000391C (終了)

    return

label block_0000391B:
    # Node: 0000391B (FINISH)
    $ C1S2 = True

    if judge_lm_condition([]):
        jump block_000038F4

    return

label block_000038F4:
    # Node: 000038F4 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF

    if judge_lm_condition([]):
        jump block_0000391C

    return

