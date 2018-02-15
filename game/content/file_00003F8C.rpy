# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003F8C (FLAG: 變革進行曲)

label block_00003F8D:
    # Node: 00003F8D ()
    $ C3F6Route = 0

    image concert_description = ParameterizedText(
        font="font/source-hans-sans-medium.ttc",
        color="#000000",
        size=18,
        text_align=1.0)

    if judge_lm_condition([]):
        jump block_0000403F

    return

label block_0000403F:
    # Node: 0000403F (Phase: 99)
    $ C3S6Phase = 99
    if Not(VarExists("C3S6Phase")):
        $ C3S6Phase = 0

    if judge_lm_condition([]):
        jump block_0000403C

    return

label block_0000403C:
    # Node: 0000403C (F6 START)
    call scb_flag_title(3, _("「变革进行曲」")) from _call_scb_flag_title_3

    if judge_lm_condition([]):
        jump block_0000403B

    return

label block_0000403B:
    # Node: 0000403B (變革進行曲 1)
    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6158BA9B7EE24D2EA88699A9FDB26B97 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 1

    if sys_effect3_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.6

    window show

    rs_character_36353B410ECB489694882A5BA1EF4DF1 "吹奏乐部的外援？？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.25

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！是别人来拜托的事哦！！今天开始就要参加社团活动了，特训特训！"

    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈——！很厉害对不对！被拜托在比赛上负责{color=#FFFF00}钢琴{/color}部分了！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_E8DD9768D82A468CA794353ED73907AD as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君好帅哦～！不愧是友君～！！"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "比赛的话，就是下次的大赛？被委托那么重要的位置了啊。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DA3F8B10BDD94A2EA7654CAF57BE44D6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这就是承认我在音乐上的才能了！果然我钢琴弹得很好呐——♪哈哈——！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_959CCF2FB8CB4C7A859CD9B384B728FF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君的钢琴演奏非常美妙！从未听过在那之上更好的了！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_6A862C1FCD4240298711F04F27EDD9E0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "一之濑君，表扬过头了。"

    show rs_image_3C4C246AAFC1459DBB1711584019784D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不过，大会已经临近，这时候还特意把不是部员的友请去帮忙，\n确实很厉害。可这真的没问题？"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "详情不清楚，但毕竟是被直接找去的，\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_34E241C96D16409BBECDFE411E12F665 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "为了不辜负期待要好好努力了——！！"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这么高兴倒是没关系，不过真的没问题吗……"

    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，不过，这样的话和翼君正在做的那个呢？"
    show rs_image_332D35DF942A4E11AF6CD9B932EC0FD0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "暂时休息？{w=0.3}{nw}"
    show rs_image_186B19EF8A8141319DE9B5EB9DE2BAC0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend ""

    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "小钢琴部本来就是一半在玩的，停就停。\n"
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "而且最近翼君也很忙的样子。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_A2534044EF094540BC82F97E1E03D950 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊哇哇，对不起。其实真的是想和友君多相处一会的。"

    show rs_image_6636F3FA642745AE8103D258F3BF47F2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没关系没关系！不要在意我，翼君就好好努力学习！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_BEF582EB5C1541099B31FB6D3CD3509F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "别站着说话不腰疼，你也学学人家。\n"
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "说起来一之濑君为什么要突然急着开始学习了呢？"

    show rs_image_E3D2D87C0D4C4A54B7016B01E2AC7D10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，不，这个学习和课堂上的东西没有关系，\n只是想尽可能多了解一些动物的事……"

    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "毕竟和技安一起负责饲育了。真了不起呐～照顾狗可是很费劲的～"

    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "最近中午都不能一起吃饭了，\n"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "千万别被那家伙当奴隶一样使唤哦？"

    show rs_image_332D35DF942A4E11AF6CD9B932EC0FD0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不会有那种事的！我真的没关系。\n"
    show rs_image_E3D2D87C0D4C4A54B7016B01E2AC7D10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "这是和作哉君约好的事情。"

    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸～……"
    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "友，这么下去一之濑君就要被穗海君夺走了哦。"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——不要不要！翼君是我的东西！是我可爱的宠物——！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BA79E21F6467495A849CFF33257777BB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友、友啾……！！\n"
    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_8C106322A86B43E599BD9F3A2962F305 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "是……我是友君的宠物……汪汪。"

    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，大家都是在认真对待社团活动的，不要太轻视了。\n"
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "要做的话就要认真做，我会为你加油的。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_2A528A20757145A78087B876421EFAF4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好，我明白了！我会加油的！！\n"
    show rs_image_0DCD6DA8D946484F9F316BDB90DB6D40 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……给前辈的回答就像这样子可以吗？"

    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，可以。"
    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不过，在不完全明白事情原委的前提下可不要乱说。"

    show rs_image_E8DD9768D82A468CA794353ED73907AD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君和大家的演奏我一定会去听的！！我也会来应援的，请一定加油哦！"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！谢谢你们，忍，翼君！"

    pause 0.3

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.5

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好！！那我走了！！第一次社团活动，加油了——！！"

    window hide

    pause 1.5

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 3

    if sys_music_current_file != "sound/BGM/My precious time of now.ogg":
        play music "sound/BGM/My precious time of now.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time of now.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A6EB165FEA4F43D98FA0D7F5088E39A4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E580C53DC9094B758B4CEDC63D288AE4

    pause 2

    show rs_image_530777FF5DE0403C85E0F13A632298D3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A46E468ABE0345679EB63CE570AD59F9

    pause 1.5

    show rs_image_E7A7EFABF8B949FEADD23029D844B4E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A46E468ABE0345679EB63CE570AD59F9

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_BCC96979835C48B5A3DDA509A4B82C4B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "来了！三碗关东煮！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "谢谢，猫山君。打工的样子很适合你呐。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_83EC28B74F5D4A5183578B04B4D9A0A5 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "话说回来，友亲进吹奏乐部了……\n听说吹奏乐部的练习非常辛苦，身体没问题？"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔……不过，本人兴致很足的样子。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_CB70B28808D840B5A51436CA4E858F49 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_BDC291B5081C42168C8A1886FB5FACD3 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "毕竟也是有着会被劝诱过去的实力，没必要那么担心吧？"

    show rs_image_A51FC16534344AB291AA801BC1DAFEA2 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥，吹奏乐部是要团队出演的。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "就算友君个人多么厉害，能不能顺利融入周围人的步调也是个问题。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_CBC28DF4FE744E2DBFAA01C4CA8D0800 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_1C45CEC369864BC3AF002C8A27C7ED32 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_26E8E308C5D84ECE97F965170D14D1FD as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "对对！音乐就是要团队合作。就算是想一个人练习也做不到。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "哦，是、是这样的啊。看来我想的太天真了……"

    show rs_image_EB3DAC64783B4D1F8C107F2E3CAC5873 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "毕竟阿月对音乐完全没兴趣嘛。剑道的比赛也是一对一的。"

    show rs_image_83EC28B74F5D4A5183578B04B4D9A0A5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不过，练习的问题先不管，\n比起这个我更担心他处在不熟悉的环境里承受的压力会不会太大。"

    show rs_image_EB3DAC64783B4D1F8C107F2E3CAC5873 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说起来，友亲现在是怎么安排的？社团活动结束后不打算来汇合吗？"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_48394E3397A94AD090308D24BFC677E3 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_1D259A10CEC9474D9310090F507D010A as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "吹奏乐部的练习还没结束。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "大赛已经近在咫尺，练习量非常大。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_614A7B0CDA2845D99530292D79173496 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那孩子真的没问题！？\n简直就像昨天还是家里蹲今天突然就开始当兵了呀！？"

    show rs_image_95CA49C0BE02488AAFE3F571D52DA8FE as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "现在去接他回来比较好哦！妈妈真的很担心啊！！\n"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_95CA49C0BE02488AAFE3F571D52DA8FE as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_F24BC1486C2D4C41B7A831D9B0A4E954 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "对不对，孩子他爸？！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "奥村……要相信自己的孩子。那孩子不会因为这点事就放弃的！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯嗯，谢谢大家这么关心。\n"
    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "友也是男子汉，一定能拿出毅力来的。"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不过，如果友真的看起来很辛苦，请一定要适当鼓励他一下。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "应该一看就能明白的，他什么都写在脸上。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯，交给我们。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "当然可以了！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_FB754CCE843B4E0CBFC3A31DFD06CCCB as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_E69DF80260AE46A1B5DD2D386D60E435 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "在下明了～！"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F95856ACBC5A49B2B61D4DBB1E7B4294 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 0.8

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "前辈辛苦了——！{w}\n辛苦了！{w}\n失礼了。"

    window hide

    pause 0.6

    show rs_image_E9592A382F574338BCE51B690BEBEF00 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "累死了……只是一点点活动就累成这样……比想像中还难受。"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜，这个还要一直持续下去……早知道就不接受了。"

    window hide

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_633EE8E0E8604D0A9FB1BAE76DEA33AB as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.4

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "森海，辛苦了！怎么样～？吹奏乐部的练习。"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_3DF1699B103D4492AAD9F78AF0406858 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at left_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇，佐藤君……"
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "真的好好上了一课，\n非常过激的那种……快累死了……"

    show rs_image_48B621B61D744137AB3444EC6DA27FB0 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "是嘛是嘛，不过也能坚持下来对不对？\n我和大家都很期待你的表现，就拜托你了哦！"

    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔、呜，好……会加油的。"

    show rs_image_F640D24E91BC44AB8E0808AF82ED2885 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "那明天再见！"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，拜拜。"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_96013754928A470894D94BAC81A99E0D as tag_346FE7CD97BB4FB18CB50E78275F4E23 at left_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "对了，明天开始就有晨练了，不要迟到哦！\n因为不是单人练习，所以迟到是要受罚的哦！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好、好的……"
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    extend "呜……晨练居然也有……\n累。麻烦。快化了……"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可现在也无法退出，\n一开始毕竟是自己接受的……"

    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "还说了敬请期待那种话……{w}\n{w=0.3}{nw}"
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "咳咳……救救我，忍A梦……"

    pause 0.7

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_E7A7EFABF8B949FEADD23029D844B4E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1

    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友的话没问题，一定不会有问题的。"

    window hide

    pause 1

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 3

    if sys_effect_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 2

    show rs_image_52A4FB95B188448396BFCDB678787F82 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B444FDE4EF1A43E5A2345A44A71061D5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Switch 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Switch 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Switch 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D8F88F968B9E4B3CBEED302C0FA2B323 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，起床了！有晨练不是吗？！快起来了！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_BEF582EB5C1541099B31FB6D3CD3509F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9B8DAC89E5144010A4E0E9EF7657680E as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜～呜，好困……才五点半……"

    show rs_image_F9B0C2D0E2D84D6D85BC37C697E5F928 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "昨天开始你就是吹奏乐部的部员了！自己决定的事就要说一不二！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哦……{w=0.3}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_FAE04D9AEB58490C92EEB463378364AF

    extend ""

    window hide

    pause 1.5

    if sys_music2_current_file != "sound/Effect Sound/Train 1.ogg":
        play music2 "sound/Effect Sound/Train 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Train 1.ogg"

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_0FE13B27C36F40D6A48872A82DF3AE41 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_217A4C9242A54EB08D3CEBF5B98B0435 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼……呼……呼……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "居然睡在了座椅上……看来真的很辛苦。\n算了，这个时间带也没什么人，好好休息……"

    rs_character_63EB8D07C5894F3AA957DE8833800788 "下一站是御咲，御咲。下车的乘客请带好随身物品……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_D5EEA08F613D4581B90B56569FE7A25D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_217A4C9242A54EB08D3CEBF5B98B0435 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，到了，起床了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼……呼……"

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友？友！"

    rs_character_63EB8D07C5894F3AA957DE8833800788 "现在到站的是：御咲。下车的乘客请从最近的……"

    if sys_effect2_current_file != "sound/Effect Sound/Train 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Train 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Train 2.ogg"

    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "糟了……车门已经开了。\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "起来了友！友！！"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "……啊真是的！！"

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 1.png
    $ zorder_rs_image_48B08BE8EC9F4E278E32DF739320F0D9 = -100
    show rs_image_48B08BE8EC9F4E278E32DF739320F0D9 as rs_image_48B08BE8EC9F4E278E32DF739320F0D9 zorder zorder_rs_image_48B08BE8EC9F4E278E32DF739320F0D9 onlayer master
    hide rs_image_48B08BE8EC9F4E278E32DF739320F0D9

    show rs_image_48B08BE8EC9F4E278E32DF739320F0D9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 1

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "呼……千钧一发。没想到有一天还会做这样的事……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼……呼……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "还在睡！？到底为什么！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼……呼……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w}只限今天哦。"

    window hide

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 2.png
    $ zorder_rs_image_111AB42F949B4430BA74B6ADE590935E = -100
    show rs_image_111AB42F949B4430BA74B6ADE590935E as rs_image_111AB42F949B4430BA74B6ADE590935E zorder zorder_rs_image_111AB42F949B4430BA74B6ADE590935E onlayer master
    hide rs_image_111AB42F949B4430BA74B6ADE590935E

    show rs_image_111AB42F949B4430BA74B6ADE590935E as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    window show

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 2.png
    $ zorder_rs_image_111AB42F949B4430BA74B6ADE590935E = -100
    show rs_image_111AB42F949B4430BA74B6ADE590935E as rs_image_111AB42F949B4430BA74B6ADE590935E zorder zorder_rs_image_111AB42F949B4430BA74B6ADE590935E onlayer master
    hide rs_image_111AB42F949B4430BA74B6ADE590935E

    show rs_image_111AB42F949B4430BA74B6ADE590935E as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    rs_character_A1E4458713DF4089A94BCAD1B8D4D614 "呀～♪快看快看！都是男孩子但公主抱了哦！"

    rs_character_4A2CA25FB4B640959638DB7E4E820D2A "明明那么小巧可爱竟然是王子什么的！好厉害！好棒！！反差萌！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔……果然太羞耻……了……！可……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼……呼……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……。"

    window hide

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1F8C3AD8E9E848BBAC058C73D0DE01FB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    pause 1.3

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A1E4458713DF4089A94BCAD1B8D4D614 "呀，突然加快速度了！多么勇敢的姿态！"

    rs_character_4A2CA25FB4B640959638DB7E4E820D2A "帅过头了。肯定是想独占恋人的睡颜吧！"

    window hide

    pause 0.8

    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 1

    show rs_image_153E9CF7193C4513869D54FA898561FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 0.8

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈……呼……"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 200
    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_D34F60C882F0425E93252349E8C3BC8D "早上好，绫濑前辈！"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "早上好……"

    show rs_image_B1B2F785D2ED49CF8DA090E58CB79206 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "发、发生什么了吗？从早上就很累的样子。"

    show rs_image_DD2521E5C93C4C7A9DD6C7B09A64AD4B as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "难道已经开始自主练习了！？"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_19EA6CF277DB411DAAFC4FAD639EE7DA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不愧是前辈……！\n最伟大了！是我的憧憬！！"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔、哦，谢谢……"
    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……唉～……"

    window hide

    pause 1

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_C46634B9C9074ACF920FA6C4B088E135

    pause 2.5

    $ set_window("イベントモード")
    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6B0609ABE3C348F3A84F5E9250E70BE7

    pause 2.5

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 1.2

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好～午休到了！来～友亲，和大家一起吃午饭！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……是呐。"
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "至少吃饭的时候要开心一些，\n试着取回平时的感觉！"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "好，今天大家就围坐在森海旁，至于森海已经累坏了，就不用动了。"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_A52160C305F54813BC6542DBBC09E25D as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好～的。我去把桌子搬过来，稍等一下哦。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "太好了呐，友，大家都很温柔哦。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯～我真的很幸福呐！\n"
    show rs_image_34E241C96D16409BBECDFE411E12F665 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "多亏了大家，今天也要好好加油呐！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好了。"
    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那么，我开动了。"

    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好～！我也开动了！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我开……"

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.9

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_0B4D1CA8EB3342D881C010956B338E02 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    rs_character_EA9AA88E88D84B559B925363E2931756 "森海～！抱歉忘记告诉你中午有会议了！！"
    show rs_image_48B621B61D744137AB3444EC6DA27FB0 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "来。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "综上所述我得走了……再见。连我的一起好好享受……（哭）。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_4BA562125E914D049B3A68EC3F0DB8A1 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "亲爱的……别走……！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好好～……{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    extend ""

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_B4378AE67E6A4B08A37DF8E3C2E65B17 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀！！这样居然也没有任何反应……！\n"
    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "走好不送……"

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.7

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_BDC291B5081C42168C8A1886FB5FACD3 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_A51FC16534344AB291AA801BC1DAFEA2 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "比想像中还要复杂。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这才只是第二天，友君，真的没关系吗？……"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……"

    window hide

    pause 1.2

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7962041686F34839A342E7B6E33F2B84 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2A62662A9A9C44A1A266E7BB1BDCA6A0

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.7

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_633EE8E0E8604D0A9FB1BAE76DEA33AB as tag_346FE7CD97BB4FB18CB50E78275F4E23 at left_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 1.5

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_038A3EB7489F4B51B2A1AD7FBC2E0808

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.5

    show rs_image_0B3E62D93B474CFA80C2DE4B381FEC4B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 2

    show rs_image_252BF7698DE74958A11FE49DFDF6370C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F7C0A55C2AAD46A09EC5C9F64521E3DB

    pause 0.7

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1.7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_53C43FF5997344BAAADBDF967F5E5DBE as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 2

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    window show

    rs_character_2C5A1436976641208FC37F717E73B15A "森海那家伙果然和想像中一样一副累坏了的样子。\n突然就被要求加入还要出席大会，很艰巨呐。"

    rs_character_2C5A1436976641208FC37F717E73B15A "佐藤也是……今天还会不会来社团活动啊，森海那家伙。"

    rs_character_5EF3D7B611334654B9D3BDDF7B4B68DF "才认识没几天，上去搭话也不好。要是他能在自己的朋友圈里好好休息就好了。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.8

    pause 0.3

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_4BA562125E914D049B3A68EC3F0DB8A1 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 1.3

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 0.9

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6158BA9B7EE24D2EA88699A9FDB26B97 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀吼，友亲！还～好吗？"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "慎酱……"
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不好～"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_31DC2C2F7D164AA2B6F4DCFBBBFB98BB as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "也是～所以我就来了！我想给这样的你打打气。"

    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谢谢。我很高兴，不过这个……"

    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯嗯，非常烦恼以至于说不出来没关系，可不要为此紧闭自己的心灵哦！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "所以首先，是要给心灵放松！来友亲！飞扑到我的怀里来！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸、欸？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_C98211B62EA04A368AA5021885891661 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好了，来！！"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔、嗯。"

    window hide

    pause 0.9

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 3.png
    $ zorder_rs_image_4C2D5276FCBB40F0B0DEB04A3E2EC3B5 = -100
    show rs_image_4C2D5276FCBB40F0B0DEB04A3E2EC3B5 as rs_image_4C2D5276FCBB40F0B0DEB04A3E2EC3B5 zorder zorder_rs_image_4C2D5276FCBB40F0B0DEB04A3E2EC3B5 onlayer master
    hide rs_image_4C2D5276FCBB40F0B0DEB04A3E2EC3B5

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_4C2D5276FCBB40F0B0DEB04A3E2EC3B5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "（抚摸抚摸）～～～……怎样？他人的温暖很舒服对不对。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……不知为何镇定下来了。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "乖乖，就这样把绷紧过头的力量放松下来～作为交换好好感受放松的心情。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "趁现在尽可能多补充一点能量，等放学后再用在社团活动上哦。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……社团……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "怎么了？那么不喜欢社团？不开心吗？？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "弹钢琴很开心。可是……唔……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "适应不了社团，只是一味地紧张，很辛苦？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸……这都明白……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼，不要小看我的观察力！\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "太见外了～友亲！为什么不向我们抱怨呢？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "因为……\n一开始接受这一切的就是我自己，事到如今还要吐苦水，太逊了……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "NO！友亲！！你太高看自己了！本来友亲就不可能那么帅的！"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不如说总是在装帅途中出问题的那种逊！这些都是只要结果好就一切好的。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "舍弃微妙的自尊，动用全部力量，不到最后不放弃才是最帅的！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "慎酱……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呐♪给我看看友亲帅气的地方。为此！不要隐藏自己的感受哦。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔、嗯……！！"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_367D6887C01741AFA0312C70A109F138

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6158BA9B7EE24D2EA88699A9FDB26B97 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……谢谢，慎酱。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "放松了？"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！已经完全放松了。就像从肩头卸下重担的感觉～"

    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "看♪轻松一点就能更加努力一会了。所以以后要常来抱怨哦！"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谢谢……"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊～不管怎么说慎酱都好帅！！\n真心，最喜欢了！！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C98211B62EA04A368AA5021885891661 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼♪那当然，再怎么说我可都是花乃汤足以自豪的看板少年・慎酱！"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 1.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2A528A20757145A78087B876421EFAF4 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那我去开中午的会议了！"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "走好～要加油哦～"

    show rs_image_27FF4633286B4DF59BF4C1A761DDF98E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好——的。"

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君好像恢复心情了呐。发生什么好事情了吗？"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是某人做了些宠人的事对不，奥村？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_C98211B62EA04A368AA5021885891661 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈♪欸～为什么会暴露呐？果然我有这种气场嘛～☆"

    show rs_image_15F70AA27431427FADF805F167EE684B as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我就觉得是这样。慎酱总是能给大家带来笑容呐。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_40D5CD49BBBB4364929E4A0AE66AB708 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔，真、真是的！那是贬义——！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "慎太郎总是能把人卷到各种事里令他拿回笑容，这种地方非常棒。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "小、小忍～"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这种时候意外地会害羞呐。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这种谦虚之处也是奥村的魅力之一。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_C43CDCE2089F485094F071FBC81A3038 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "真、真的太不好意思了饶了我……我投降……"

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    pause 0.4

    show rs_image_8F3888CA89DF4DDEB58EC097C79B8FC0 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_63B7FCD9DF38442BA0683EF60F550969 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哈哈。"

    window hide

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 0.5

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（……太好了呐，友。）"

    window hide

    pause 1

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 3

    if sys_music2_current_file != "sound/Effect Sound/Night insect 1.ogg":
        play music2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_0D1A14CC6DD549EA877967C087A4F0E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 2

    show rs_image_D9702ABDB70E4886A88A4038D68B5421 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F7C0A55C2AAD46A09EC5C9F64521E3DB

    pause 2

    stop music2 fadeout 1.5
    $ sys_music2_current_file = ""

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_AE45B7F5C4A14CEA97060F4FC018F7F1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    pause 0.5

    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "回来了啊。"

    window hide

    pause 0.9

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_48D26C14A18B4805B108A02B239C32FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    if sys_music_current_file != "sound/BGM/The past precious.ogg":
        play music "sound/BGM/The past precious.ogg" loop
        $ sys_music_current_file = "sound/BGM/The past precious.ogg"

    pause 0.4

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，辛苦了。晚饭妈妈已经帮你准备好了……"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_217A4C9242A54EB08D3CEBF5B98B0435 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_59308A2352314B1E8ABB34860FDB9423 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 0.4

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼……呼……"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "已经睡了？……真是尽全力了呢。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "就这么睡下制服会被压皱的……\n"
    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "友——睡觉没关系先换衣服。"

    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "洗澡……可以早上再说。但就这么睡下也太不讲卫生了。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼……呼……"

    show rs_image_BEF582EB5C1541099B31FB6D3CD3509F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "睡前要先换衣服……！"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    extend "唔……只能我来了……"

    if sys_effect_current_file != "sound/Effect Sound/Search 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Search 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Search 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "内裤也换掉算了……"
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "唔，居然还穿着这条。{w}\n那～个，睡衣在……"

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2E62A030F335405E9F99D592FF0CBF10 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D3337C6701A1424493940A3CA157D89B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "奇怪，一直都是放在这里的……去什么地方了……"

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊嚏！{w}{w=0.3}{nw}"
    show rs_image_2E62A030F335405E9F99D592FF0CBF10 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "嗯……？什么时候睡……"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 200
    show rs_image_59308A2352314B1E8ABB34860FDB9423 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D5C4904EF1E743FA8C7F976069780D4D as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_top zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫！？我为什么只剩一条内裤了！？！？这是这是怎么回事！？？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    pause 0.3

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，起来了？知道睡衣放什么地方了吗？？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_D5C4904EF1E743FA8C7F976069780D4D as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "难道是忍把我脱成这个样子的！？呀禽兽——！！\n"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_27425D50829F4EFB989F8C75DFB8E220 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……先发推特。"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "给我等等，因为你穿着制服就睡下了，不得已我才给你换衣服的。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_8E2E74098B014E9D9A3DCB40290623B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这还真是抱歉抱歉～睡衣拿去洗了哦～"

    show rs_image_6CCABDB8E3334425A7B9F5DF69F1B9A6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不去把干了的衣服拿回来不行呐……\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F0E0F9F576F74526A6ADB695D46367AA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯？有股好香的味道！？是什么这个味道！"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，是我家妈妈为这么努力的友做的饭。{w}说要好好吃饭，充分回复体力。"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_598E675438F245A697168F9D5DB12B55 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇～谢谢，忍的妈妈♪\n"
    show rs_image_8E2E74098B014E9D9A3DCB40290623B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那事不宜迟……{w=0.7}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    extend "我开动了～！！"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，在那之前先把衣服换了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_48D26C14A18B4805B108A02B239C32FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_B7FD1CBC47B64425A7CCD02EFC26A9F1 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "无所谓的无所谓的！腹空无以为战～！嗯！好好～吃♪真的好棒～♪"

    window hide

    pause 0.8

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 4.png
    $ zorder_rs_image_4D24DED204CD42949FB326EEF358987F = -100
    show rs_image_4D24DED204CD42949FB326EEF358987F as rs_image_4D24DED204CD42949FB326EEF358987F zorder zorder_rs_image_4D24DED204CD42949FB326EEF358987F onlayer master
    hide rs_image_4D24DED204CD42949FB326EEF358987F

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_4D24DED204CD42949FB326EEF358987F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 1

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "最近总觉得饭越来越好吃了，为什么呐？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这就是努力的证据。正因为活动消耗了大量能量，饭才要好好吃。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "原～来如此！我最近很努力了呐～！总觉得自己在慢慢成长呐！！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友一定能找到全新的自我。{w}……接下来也会慢慢产生变化吧。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当然会变了！一直一个样子也太无聊了！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "身高会增长，体毛也会有，发现将来的梦想，走在自己独一无二的道路上！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是啊……对呢。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过这个饭真的好好吃哦～♪\n就像职场回来的工薪男大喊“酒真好喝”一样的感觉？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "也许。我们将来会不会也成为那样的大人呢。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谁知道～说不定忍会刷地长大……{w=0.6}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "啊，应该不可能。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说什么呢，也是有可能的。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "～不会的不会的！忍一直就是小忍就好～了！各种地方都小小的♪"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……友，明早不叫你起床了，好自为之。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸欸欸！？我是开玩笑的～！！不要在意嘛～！"

    window hide

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Night insect 1.ogg"

    stop music fadeout 6
    $ sys_music_current_file = ""

    show rs_image_53C43FF5997344BAAADBDF967F5E5DBE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_DCEBC7527B8F4B4EA0FF44E692174034

    pause 3

    stop effect fadeout 2
    $ sys_effect_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 3


    if judge_lm_condition([]):
        jump block_0000403D

    return

label block_0000403D:
    # Node: 0000403D (變革進行曲 2)
    $ set_window("イベントモード")
    if sys_music2_current_file != "sound/Effect Sound/Swallow 1.ogg":
        play music2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B444FDE4EF1A43E5A2345A44A71061D5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1.5

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9B8DAC89E5144010A4E0E9EF7657680E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……唔～早上了啊……"
    show rs_image_090583914F36486EA2E7A56AF765A727 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "……"
    show rs_image_FA5B703A676F4C829E63A8555EB84BD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "……{w}{w=0.3}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1985C4123DCC4DA4B4189F547147C9CC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "七点了！？？\n忍、忍真的不叫我了！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_FA5B703A676F4C829E63A8555EB84BD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "哦，今天没有晨练……呼～……太好了。"

    show rs_image_6215465F385F4702A227A74F52C707E0 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天就和过去一样优哉游哉地过……啊，也就是说，\n"
    stop music2 fadeout 2.5
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    show rs_image_6A27F1FE3930449AA4B1D1B4EC283DBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    extend "好久没做的早起{color=#FF00FF}嗡嗡{/color}也可以做了～♪呼呼♪"

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_25A2A019D65543BB904CF8D7CDC67F42

    pause 2.5

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.9

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我出门了。"

    pause 0.7

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_A1B95DB5524442E4BEBF32BAE17F8F8E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "结果直到最后忍也没来。难得睡过头了？"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Bell 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 2.ogg"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.7

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "早上好，我是友！忍君在吗——？"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_69E4C25BE6F24CC0A44F7F54179040D3 "早上好。友君来这边接忍真是很少见呐。"

    show rs_image_285E40B50F3F466F9AE41CD837D82E42 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈，也许。最近一直拜托忍。\n"
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那忍呢？"

    rs_character_69E4C25BE6F24CC0A44F7F54179040D3 "今天早上有晨练所以很早就出门了。说起来，友君也加入社团了？"

    rs_character_69E4C25BE6F24CC0A44F7F54179040D3 "社团活动很辛苦对不对？不过，要加油哦。\n作为替代，一定能收获好的回忆的。"

    show rs_image_285E40B50F3F466F9AE41CD837D82E42 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好、好的，我会加油的……"

    show rs_image_0DCD6DA8D946484F9F316BDB90DB6D40 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，昨天的便当真的非常感谢！特别好吃哦！"

    rs_character_69E4C25BE6F24CC0A44F7F54179040D3 "那就好，多吃一些，更加朝气蓬勃！阿姨很期待友君的活跃哦。"

    show rs_image_FD381C6412CC4FE7A52F90CB708C2E44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "活、活跃什么的……"
    show rs_image_285E40B50F3F466F9AE41CD837D82E42 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那我先走了。"

    rs_character_69E4C25BE6F24CC0A44F7F54179040D3 "走好，注意安全哦——"

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 2

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_42C3B526C247471AA015209476FA27F8 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "早上好，森海君。"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_5FDFEC36A7CD48EB809A2759645E1AF1 as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_81D16F74A3C44B8982DB528D7D934850 "好呀——！班长。"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "早上好～泉君，加藤君。"

    show rs_image_3DE36583042D4EF283177E16D538DDFC as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "哦？今天吹奏乐部没有晨练？"

    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天休息。加藤君这都知道？"

    show rs_image_A614FAD01A194B11AD51E6D6B5FAB95A as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯，从泉那里听说的。是那个对不对？啦啦啦～这样地吹？"

    show rs_image_47A1CF95832441F79773CE6246CC941C as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "不是哦，加藤君。森海君负责的是钢琴部分。"

    show rs_image_5FDFEC36A7CD48EB809A2759645E1AF1 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "对哦。叮叮叮地弹的那个？而且还要参加正式比赛。"

    show rs_image_285E40B50F3F466F9AE41CD837D82E42 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔、嗯。算是……"

    show rs_image_E81EA15E904A462294C3D31D7E13FC74 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "吹奏乐部那些人非常重视这次大赛，能在这种时候被请过去真是厉害。"

    show rs_image_39E6D29FE80C465594D4446F8137BE4F as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "特地从社团外寻找帮手，还这么认真，看来对森海君期待很高。"

    show rs_image_A614FAD01A194B11AD51E6D6B5FAB95A as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "加油～班长！\n可不要给一直努力到现在的吹奏乐部抹黑，不要被他们记恨哦～"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……"

    show rs_image_801DE23A647744BCBFCB3A3097F1FE5E as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "加、加藤君，说那种话会让森海君压力更大的。"

    show rs_image_5FDFEC36A7CD48EB809A2759645E1AF1 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "玩笑玩笑。嘛，就算真失误了，\n以能让自己相信那是不可抗力为势头勤加练习就没问题！"

    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w=0.7}{nw}"
    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "两位也觉得大赛很重要，所以才会那样天天练习？"

    show rs_image_39E6D29FE80C465594D4446F8137BE4F as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "嗯，就是这样的……为什么突然这么说？"

    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "越听越觉得我被委任了一个相当重要的职务。"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "一开始只是想要确认自己的实力一时脑热接下的。现在有些害怕了。"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这种半吊子觉悟真的可以吗，真的不会辜负大家的期待？越来越着急。"

    show rs_image_E81EA15E904A462294C3D31D7E13FC74 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_81D16F74A3C44B8982DB528D7D934850 "所以才要练习。为了对抗这股焦灼感，只能尽可能练习，让大赛成功了。"

    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是、是啊……确实。\n"
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "但是，如果失败的话……"

    show rs_image_6BEDE232AC5D4CA6AF91A160A7EFC9E6 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_8D9249CA1389416BAF6A122851E276D0 "当然，不管怎么练习也存在失败的可能。不过，这并不是逃避练习的理由。"

    show rs_image_26C754426240474DB9C3EDFE51B5E3DF as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "疏于练习导致失败，周围人肯定会不满。更重要的是，将会无法原谅自己。"

    show rs_image_C16547297FF840538E7675A4823EEF0A as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "为了不变成那样才要勤加练习，让周围人都看到你在努力。"
    show rs_image_42C3B526C247471AA015209476FA27F8 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    show rs_image_5FDFEC36A7CD48EB809A2759645E1AF1 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "其他部员看到这个气势也会上升。\n在这个意义上，整个社团都是作为一个团队参战的。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔——……我会考虑的。我会加油、的。唔……呜呜。"

    show rs_image_801DE23A647744BCBFCB3A3097F1FE5E as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "呃？是不是施加了不必要的压力？"

    show rs_image_A614FAD01A194B11AD51E6D6B5FAB95A as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "认真对待是好事，但也不要过头了哦。加油！"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_F7C0A55C2AAD46A09EC5C9F64521E3DB

    pause 1.5

    if sys_music2_current_file != "sound/Effect Sound/Clamorous 1.ogg":
        play music2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D138810390DC4843A14969EAD39A7E06 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.35

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（我当然明白练习要加油，可总觉得心里说不过去。）"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（或者说和想像中差距太大……或者说我根本没有重视起来）"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w=0.8}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=36}啊嚏！！！！{/size}"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_02ECE9B805B742C6B558DFD2FD5D2608 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_4D5E70DCADBB4F2CA52AB49DED72D7C5 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哇，友君，打了个好大的喷嚏。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3F5AF2DAC6F94773B04A709D2558F647 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "所有妨碍思考的事全都打出去了。"

    show rs_image_02AF4E98AE404A37BBF5189D1BD66AE6 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "思考的事……社团？"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就是啊～"

    show rs_image_CB70B28808D840B5A51436CA4E858F49 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "大赛已经很近了，不是感冒就好了。"

    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，不是感冒。头很晕不过只是因为最近要考虑的事太多了……"

    show rs_image_F40F5A6526E84289B66370816B121742 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "森海，有烦恼就要说出来。不要自己扛。"

    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谢谢～可这次完全就是我自己的事就算抱怨也不会解决的。"

    show rs_image_BDC291B5081C42168C8A1886FB5FACD3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是嘛。那还真是……考虑不过来的时候，休息是必要的。"

    show rs_image_63B7FCD9DF38442BA0683EF60F550969 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊，要不要喝点什么？我去买。"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "空真会察言观色呐……一定能嫁给好人家的。啊，一瓶浓可尔必思。"

    show rs_image_A52160C305F54813BC6542DBBC09E25D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "OK——！哥哥？"

    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "绿茶。"

    show rs_image_D6385A1D6C184F9A93FE94370445F27F as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "明白了！"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_02AF4E98AE404A37BBF5189D1BD66AE6 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "（能趁这个休息时间帮森海放松一下是最好可……）"

    window hide

    pause 0.9

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊嚏！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A51FC16534344AB291AA801BC1DAFEA2 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊，友君，又打喷嚏了。身体不舒服？又在想什么复杂的事？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不是的……这次只是、有点、冷……"

    show rs_image_CB70B28808D840B5A51436CA4E858F49 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸。那绝对是感冒了！下节体育课还是请假比较好。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦……"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "小忍，怎么了？"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "原因我明白……大概就是真的感冒。"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_B550C4E9D1DB474BBEDD133EA85FDFC5 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是吗。那么……"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "空。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D6385A1D6C184F9A93FE94370445F27F as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "了解，哥哥。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D6385A1D6C184F9A93FE94370445F27F as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哇哇？！你、你们想干什么！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这叫强制押送，森海。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "带去保健室。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_FD381C6412CC4FE7A52F90CB708C2E44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_D6385A1D6C184F9A93FE94370445F27F as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸、欸欸欸！这、这点小事没关系的。\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊嚏！！！{w=0.7}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_34E241C96D16409BBECDFE411E12F665 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "大、大总统！"

    show rs_image_2B8CA379875246C784AD29CB254874FC as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "别想着骗人了。来，走了。"

    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哦～忍～慎酱～做点什么～……"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.4

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "祝愿你哦，友亲，大家都是基于爱行动的哦……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "等下会去看你的，要好好休息。"

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……好的。"

    window hide

    pause 0.9

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_F9DBAF1EE9EF4C7F828153AA794ECB5E

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_0BAEC978FE74423CAE38311274CCA0C8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_217A4C9242A54EB08D3CEBF5B98B0435 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_EF2D3A4912BA490B9BDDB92C8700586E

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼～……呼～……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_7AE3125258BC4D33A7DBD94B1EAB358D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那就把友所有的东西都放到这边。"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_F9A39BA944784657A4798D479F6DA366 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "便当是自己准备的？饮料呐？"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_84F46056D888472D96B364CB550E92C6 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "刚才我去买来了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_35A4BD86F80A4212B18966F780E77624 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "万幸没有发烧。这几天社团活动太辛苦，应该是疲劳积累下来了。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_E038CC93A8F84492ADFD433CE6B7FE4F as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_8E38A0CD75524F369B073740B18B8B95 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "钻进被窝的瞬间就睡过去了。很壮观哦，和大雄有的比。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "是嘛。真是的，友亲真是太令人担心了～"

    show rs_image_0FBB9EFD437D46ED98CA46FE9AFB2697 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "大家一定是被友君如此努力的姿态吸引了吧。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_3FCC3369494D4504ACACF75A7FA3D37E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    window hide

    pause 0.6

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼……又是一样的练习……呼。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦呀？说梦话了呐。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼……大家……谢……\n"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 2.ogg"

    extend "谢……大家……加油的……呼。"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.3

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……响彻心扉。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "多么令人怜爱……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "友亲……！！"

    window hide

    pause 0.7

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D735A93C30724DC191EE5509F35D2AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.9

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.2

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……唔？嗯嗯……睡得好好……"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "嗯！？这里是？"

    if sys_music_current_file != "sound/BGM/Guitar 1.ogg":
        play music "sound/BGM/Guitar 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Guitar 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "保健室哦。傍晚好，友君。"

    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，空！晚上好。哦对，我就那么睡过去了……\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊！现在几点！？必须要去社团！？！"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_BDC291B5081C42168C8A1886FB5FACD3 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "吹奏乐部那边已经以身体状况不好为由替你请假了。\n不要勉强，早点休息快点治好才是贤明之策。"

    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "阿月——！{nw}"
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "你们一直在这里陪我吗？\n明明你们也有社团活动的……"

    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "毕竟有把森海安全送到家的任务。今天我们也请假了。"

    show rs_image_63B7FCD9DF38442BA0683EF60F550969 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君，走得动吗？如果很困难的话就像上次那样靠着我的肩膀好了。"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不用了，拜大家所赐基本没什么异常了，自己一个人也能走回去没关系的。"

    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "是嘛，那就好。\n"
    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_A52160C305F54813BC6542DBBC09E25D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "对了，既然要回去，不如为了转换心情散散步如何？"

    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "当然前提是吹奏乐部那群家伙不会发现呐。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_02ECE9B805B742C6B558DFD2FD5D2608 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我、我们也得小心不被剑道部部员发现……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，在校内散步？"
    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "欸？？"

    window hide

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 0.9

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_FAE04D9AEB58490C92EEB463378364AF

    pause 2


    if judge_lm_condition([]):
        jump block_0000403E

    return

label block_0000403E:
    # Node: 0000403E (CP3 Twilight 月空友)
    call block_00001E0A from _call_block_00001E0A

    if judge_lm_condition([]):
        jump block_00004249

    return

label block_00004249:
    # Node: 00004249 (變革進行曲 3)
    pause 0.8

    $ set_window("イベントモード")
    if sys_music2_current_file != "sound/Effect Sound/Swallow 1.ogg":
        play music2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8EC5717E792241CB9E9610819A6E1D46

    pause 3

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 2

    window show

    if sys_effect3_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}鼓掌鼓掌鼓掌！{/size}"

    window hide

    pause 0.5

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 6.png
    $ zorder_rs_image_44D20D14619C4C49BA2A44119906A340 = -100
    show rs_image_44D20D14619C4C49BA2A44119906A340 as rs_image_44D20D14619C4C49BA2A44119906A340 zorder zorder_rs_image_44D20D14619C4C49BA2A44119906A340 onlayer master
    hide rs_image_44D20D14619C4C49BA2A44119906A340

    show rs_image_44D20D14619C4C49BA2A44119906A340 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A17594B834D64AA8ABA217241EE9B0AA

    pause 1

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "非常好听哦！！大赛上就是要弹这首曲子呐！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "感觉很成熟、气氛很好、还有……那个那个。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "爵士乐的感觉。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，是的，爵士乐的感觉，非常棒！！\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "越来越痴迷……{w=0.4}尊敬了！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哈哈哈～♪谢谢，翼君。对～了，我很帅？我帅不帅？？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯！！坐在钢琴前就更有魅力了～！语言无法好好表达的帅！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀～会害羞的～！哈哈～♪好了～！就这样继续更帅气一些！！"

    window hide

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3C4C246AAFC1459DBB1711584019784D as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说起来，在学习中还能特地赶过来，谢了。"

    show rs_image_E3D2D87C0D4C4A54B7016B01E2AC7D10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "没什么，我也想稍微转换一下心情，能看到不断努力的友君真是太好了。"

    show rs_image_F0AF18EA5ED94E6B9426EA7B01961357 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我也有能继续努力的勇气了呐。我、我这边才要说谢谢。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是、是吗？"

    show rs_image_E8DD9768D82A468CA794353ED73907AD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯！我也不能输哦。\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_8C106322A86B43E599BD9F3A2962F305 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "啊，不，不可能敌过友君的呐……"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没有这回事哦！我也是像翼君这样从别人那里获得勇气的哦。"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "现在我也能像他们一样了还有点开心呐。\n"
    show rs_image_0DCD6DA8D946484F9F316BDB90DB6D40 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "虽然也有很辛苦的时候，{nw}"
    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "不过能接下来真是太好了。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C197AB750EF8424887D8CF5ECCE7226B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友、友君帅过头了！继续这么下去我就无法直视了！"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_34E241C96D16409BBECDFE411E12F665 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哈哈哈！超级友光线打败翼怪兽了！"

    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "唔！我会变得越来越强的，才不会被那么简单打倒呐！"

    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "被这么说的话不管怎样都要打倒了呐～！！\n"
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "我们一起加油，翼君！"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F0AF18EA5ED94E6B9426EA7B01961357 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯！"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_40BD583A95C74300ACB4618268AB48FF

    pause 0.9

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_B5EB5E7774A14E2CB2C60E113DB587A9 as tag_923338EC67B148CE944D61C9091B72C5 at center_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 0.35

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "森海，顾问老师叫你过去。"

    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，{color=#00FFFF}冈岛前辈{/color}！我明白了，现在就去。\n"
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "再见了，翼君。"

    show rs_image_9538619ECD0849688D07CEC63FB8B083 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "要是还能来听我演奏就好了呐。我好像是被表扬就会更有干劲的类型哦。"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯，请务必让我再来。要可以的话我任何时候都能来的。"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_326E3AFD35A54F98B9DA03FD6E4165E5 as tag_923338EC67B148CE944D61C9091B72C5 at center_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    rs_character_193BCCFE681D42C8993A47A884FF2200 "别废话了快走！"
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_34EA3FF6756742B9B40F0095C34BB921 as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "真是的…"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇，对不起！"

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_923338EC67B148CE944D61C9091B72C5
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.8

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_93384CF7101E46B99C76C26B616C4A01 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_186B19EF8A8141319DE9B5EB9DE2BAC0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……前辈好可怕……"

    window hide

    pause 0.9

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2.4

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.9

    window show

    rs_character_776382753FF149B49443F348F4356521 "离大赛终于只剩一个月了。{w}\n所以，为了决定究竟谁负责钢琴部分，我打算来一次试音会。"

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_326E3AFD35A54F98B9DA03FD6E4165E5 as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    show rs_image_F747693390C4400FA3B7302024E8B5EA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.35

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶，钢琴部分除了我之外还有其他人吗？？"

    show rs_image_34EA3FF6756742B9B40F0095C34BB921 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_776382753FF149B49443F348F4356521 "嗯，这次冈岛负责的是其他部分，否则他会一直负责钢琴部分的。"

    rs_character_776382753FF149B49443F348F4356521 "似乎他自己也在练习，也对我说了想要再考虑一下这个安排。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_776382753FF149B49443F348F4356521 "这次的曲子存在钢琴独奏的部分，能明白由谁负责是个很重要的问题么？"

    rs_character_776382753FF149B49443F348F4356521 "所以要听过两人的演奏后再决定，不要留下遗憾好好努力。"

    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_326E3AFD35A54F98B9DA03FD6E4165E5 as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "是。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是、是的……"

    window hide

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_923338EC67B148CE944D61C9091B72C5
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7962041686F34839A342E7B6E33F2B84 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B5EB5E7774A14E2CB2C60E113DB587A9 as tag_923338EC67B148CE944D61C9091B72C5 at left_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"
    show rs_image_285E40B50F3F466F9AE41CD837D82E42 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "啊……哈哈。前辈，请、请多多指教了～……"

    show rs_image_34EA3FF6756742B9B40F0095C34BB921 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    if sys_music2_current_file != "sound/Effect Sound/Cut the wind 1.ogg":
        play music2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_326E3AFD35A54F98B9DA03FD6E4165E5 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_193BCCFE681D42C8993A47A884FF2200 "明明是中间才来的，真敢和我平起平坐。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那、那个……对、对不起。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C70172768F92498A92988C76E79AF8AA as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_193BCCFE681D42C8993A47A884FF2200 "你这种人就该……"
    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    extend "哼。"

    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……"
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "唔……"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "就算这么说……\n拜托我来的也是吹奏乐部啊……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊～不行不行！！好不容易有了干劲的！\n"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯！加油！绝对不能输！！"

    window hide

    pause 0.7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_28CB16F81175458EA97C8F0250448304 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    stop music fadeout 4
    $ sys_music_current_file = ""

    pause 2.5

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F747693390C4400FA3B7302024E8B5EA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 1

    if sys_music_current_file != "sound/BGM/Something strange 1.ogg":
        play music "sound/BGM/Something strange 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something strange 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.2

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？我的乐谱不见了……呃？欸？？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_96013754928A470894D94BAC81A99E0D as tag_346FE7CD97BB4FB18CB50E78275F4E23 at left_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "怎么了？森海。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我的乐谱找不到了！唔～到底在什么地方。"

    show rs_image_9B6EA9CA0C0541BAAD8AE6254AB5AC9D as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "欸～拜托好好干啦～马上就要开始合奏了，这可怎么好。"

    show rs_image_A579F650612D4CA18E2B222221DBF547 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜呜～乐谱至少记住了一些，总会有方案的……"

    window hide

    pause 0.4

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_84D7210FBBF34E428243573CCC75C981

    pause 0.6

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}合奏中{/color}"

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F0DA0BADE3484D76A433C390166A2DF7

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（欸……这里有曲段来着？？……那个那个！）"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_776382753FF149B49443F348F4356521 "停！刚才谁错了？"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F747693390C4400FA3B7302024E8B5EA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对、对不起……是我……"

    rs_character_776382753FF149B49443F348F4356521 "真是的。再来一次，这次从D开始！预备，起！！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（啊哇哇！D是哪一块！？没有乐谱根本不知道章节号啊～！）"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 0.45

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_776382753FF149B49443F348F4356521 "钢琴！！怎么不弹？！"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对、对不起～！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_A86787761B4F4226AFB3C2FA698779F2 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_EA9AA88E88D84B559B925363E2931756 "……"

    window hide

    pause 0.4

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_FAE04D9AEB58490C92EEB463378364AF

    pause 0.5

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7962041686F34839A342E7B6E33F2B84 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_FAE04D9AEB58490C92EEB463378364AF

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……唔。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_633EE8E0E8604D0A9FB1BAE76DEA33AB as tag_346FE7CD97BB4FB18CB50E78275F4E23 at left_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "不、不要在意！不要这么低落嘛。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可是，合奏练习因为我变得乱七八糟了……"

    show rs_image_F640D24E91BC44AB8E0808AF82ED2885 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "嘛，也是呐。谁都会有失败的时候，不要太过在意了。"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜～……"

    show rs_image_3F84B60D1FD24C9CAD32F21E89A94324 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "……嗯？\n"
    show rs_image_96013754928A470894D94BAC81A99E0D as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那边乐器架下面有什么东西压着哦。"

    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，真的……\n"
    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.4

    extend "诶！？这是我的乐谱！！"

    show rs_image_633EE8E0E8604D0A9FB1BAE76DEA33AB as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "什么嘛～能找到真是太好了。为了不再弄掉这次一定要好好保管哦。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯、嗯～对不起……\n"
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "可我不记得有放到那边啊……"

    window hide

    pause 0.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_84D7210FBBF34E428243573CCC75C981

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}翌日{/color}"

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F0DA0BADE3484D76A433C390166A2DF7

    pause 0.4

    rs_character_2C5A1436976641208FC37F717E73B15A "森海，我们还有点事，你先去合奏场打开空调降降温。"

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_7962041686F34839A342E7B6E33F2B84 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，我明白了～！"

    rs_character_5EF3D7B611334654B9D3BDDF7B4B68DF "拜托你了哦～"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    pause 0.3

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_A58FA4D4F3DA4D62A421C5FCE76AA975

    pause 1.3

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F747693390C4400FA3B7302024E8B5EA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.9

    if sys_effect_current_file != "sound/Effect Sound/Switch 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Switch 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Switch 1.ogg"

    show rs_image_F747693390C4400FA3B7302024E8B5EA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_27FF4633286B4DF59BF4C1A761DDF98E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好，这就可以了～那我先去厕所～♪"

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1.2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F747693390C4400FA3B7302024E8B5EA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B1E776E59E0F4078A22BEFCAB3389387

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_2C5A1436976641208FC37F717E73B15A "呜哇怎么了！？合奏场怎么变成桑拿房了！？"

    rs_character_5EF3D7B611334654B9D3BDDF7B4B68DF "这不是制冷是制热！！谁干的！！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "屋里这么热可没法练习啊～"

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9538619ECD0849688D07CEC63FB8B083 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼～舒服了♪"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哇，好热！？怎么回事！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_2C5A1436976641208FC37F717E73B15A "森海～！居然连冷热都能调错！合奏只能推迟了～！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸欸～！是、是我？我明明调成制冷了啊……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_5EF3D7B611334654B9D3BDDF7B4B68DF "别瞎说了！真是的都没法进去了——"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……对不起……"

    window hide

    pause 0.6

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_038A3EB7489F4B51B2A1AD7FBC2E0808

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7962041686F34839A342E7B6E33F2B84 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.7

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "呜……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_96013754928A470894D94BAC81A99E0D as tag_346FE7CD97BB4FB18CB50E78275F4E23 at left_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.3

    rs_character_EA9AA88E88D84B559B925363E2931756 "最近一直在失败呐。\n……确实是有些慌张，但没想到会做到这种程度。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这绝对有问题……"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3F5AF2DAC6F94773B04A709D2558F647 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "呜……{w=0.499}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A86787761B4F4226AFB3C2FA698779F2 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "怒了！！！"

    rs_character_EA9AA88E88D84B559B925363E2931756 "森、森海？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_3F5AF2DAC6F94773B04A709D2558F647 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为什么总要和我过不去！！明明人家好不容易拿出赶干劲了的！"

    show rs_image_33DAA2B0F1C244C4B2C872213860A04A as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "唔……抱歉，{w=0.5}{nw}"
    show rs_image_DD649A23A0C54C3B99DE6AF655696477 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "给你留下了这种回忆。"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？"

    show rs_image_F640D24E91BC44AB8E0808AF82ED2885 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "不，只是觉得想做却做不好很气人啊～什么的。"

    show rs_image_6EB06386B3BF438184595D042608116A as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "是我拜托你来帮忙的，没想到会变成这样。"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊、不用，没有道歉的必要。我也拜此所赐成长了呐。"

    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我是真心觉得能来参加真是太好了的。\n"
    show rs_image_285E40B50F3F466F9AE41CD837D82E42 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "抱歉佐藤君，让你那么在意。"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我会更努力的。"

    show rs_image_DD649A23A0C54C3B99DE6AF655696477 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "是吗。嗯，那就好。\n"
    show rs_image_33DAA2B0F1C244C4B2C872213860A04A as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……"
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.6

    extend "……{w=0.45}试音会，我会替你加油的。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！谢谢！！"

    rs_character_EA9AA88E88D84B559B925363E2931756 "……"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_1C428704E5E24078848D388A31B861CE

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    pause 3.5

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6B0609ABE3C348F3A84F5E9250E70BE7

    pause 1.2

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_34E241C96D16409BBECDFE411E12F665 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg"

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好！今天晨练也要加油哦！！"

    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "干劲很足呐。因为有试音会？今天来得比往常都早呐。"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当然也有那个原因，不过最近干劲就像山林大海一样不断涌出来哦！！"

    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸，是嘛。那当然很好，肯定社团里其他人也这么觉得的。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_D8FBA8060A9B457F9D8A35FB71E72F10 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！正因为大家都在支持我呐！！不管什么绝境都能挺过去！"

    window hide

    stop music fadeout 4
    $ sys_music_current_file = ""

    pause 0.5

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_music2_current_file != "sound/Piano/hero.ogg":
        play music2 "sound/Piano/hero.ogg" noloop
        $ sys_music2_current_file = "sound/Piano/hero.ogg"

    pause 0.85

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w=0.7}{nw}"
    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……诶？钢琴的声音。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "真的呢。水准……很好？"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，非常棒！是谁在弹呐？啊，难道是老师！"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，不可能这么早去弹琴的，老师也不是闲人。"

    show rs_image_4ADA38AD8AC240F48211FBA4F8807972 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w}{w=0.3}{nw}"
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_4ADA38AD8AC240F48211FBA4F8807972 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EF2D3A4912BA490B9BDDB92C8700586E

    pause 0.8

    extend "真的好～棒啊……非常熟练。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……不赶快去社团没关系吗？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "反正今天来得很早，稍微听一会嘛～"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 0.5

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……到音乐室附近的话不是能听得更清楚嘛？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊！对！确实是！！"
    show rs_image_2A528A20757145A78087B876421EFAF4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "冲啊冲啊！快去，忍！"

    show rs_image_83253C644D7341D899A80F5E86570559 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……好好。"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "换上室内鞋…………"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……这是什么？"

    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怎么了？"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "有张纸。"

    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "情书？"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……不可能。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什、什么嘛——！不打开谁也不知道嘛！！\n"
    show rs_image_D8FBA8060A9B457F9D8A35FB71E72F10 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "那～么，是谁的情书呐～？"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.7

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w}嗯嗯？{w=1}{nw}"
    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    extend "{size=28}呜诶诶诶！？！？{/size}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怎么了？果然是恶作剧？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不不不不是的！！不是那种东西……这、这是……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    pause 0.5

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FF0000}『现在立刻滚出吹奏乐部，否则就不客气了。』{/color}"

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    window show

    pause 0.3

    rs_character_3A742340BEAD415FAC80AFEA0A84B586 "{size=32}威胁信！！{/size}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "到底是谁……"

    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，注意点。我会好好守护你的，不用担心。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……呵呵……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……？"

    window hide

    pause 1

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect3_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5EB601DCA8974E1A8C893840BF4F8D12

    pause 0.4

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=28}{color=#FFFF00}哈哈！！啊——哈哈哈！！！！{/color}{/size}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怎、怎么了？有什么地方不对劲！？"

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Break 1.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 10.png
    $ zorder_rs_image_61D8FFFC34E4460B9E6EAB78BB0388BC = -100
    show rs_image_61D8FFFC34E4460B9E6EAB78BB0388BC as rs_image_61D8FFFC34E4460B9E6EAB78BB0388BC zorder zorder_rs_image_61D8FFFC34E4460B9E6EAB78BB0388BC onlayer master
    hide rs_image_61D8FFFC34E4460B9E6EAB78BB0388BC

    show rs_image_61D8FFFC34E4460B9E6EAB78BB0388BC as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B19552D0E67040E083A0922154EFFFFE

    pause 0.8

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "只会用这种下三滥手段的胆小鬼根本不足为惧，滑稽！"

    if sys_effect3_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Impact 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这种家伙我怎么可能赢不了！！！我怎么可能放弃！！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我去晨练了。正合我意，就和你正面较量！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "太危险了！明明连对方是谁都不知道，还是更慎重一些……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍，离试音会没多少时间了，我可没空管这种只会干这个的家伙。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没关系，我明白大家都在支持着我。{w}\n绝对不会失败的，我不会让它失败的。"

    window hide

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 1

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……已经完全融入吹奏乐部了呢。"
    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "可是，我……"

    window hide

    pause 0.8

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AEF730D86D5343AF81880AC735BAFAC6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_3AD71FD0B91B482CBB280A8611C2741C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "绝对不会输！怎么可能输！！\n"
    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……嗯？那是冈岛前辈……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊！是我的乐谱……"

    window hide

    pause 0.5

    hide tag_ECFB5B509A334A868686B3435242BF90
    show rs_image_725B3378F65449E68B514C0E69BECE43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_4D8F1D6A70C24A34A3E6C37B69619470 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    pause 0.4

    window show

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……切！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}{color=#FF0000}（撕碎）{/color}{/size}"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F33DA7B19039419089D2B31DD1FAE879 as tag_923338EC67B148CE944D61C9091B72C5 at left_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "前、前辈！！！……？！"

    rs_character_193BCCFE681D42C8993A47A884FF2200 "！？"

    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为什么要……！难、难道在鞋箱里放威胁信的是……？"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_C70172768F92498A92988C76E79AF8AA as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "混蛋！！"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    hide tag_923338EC67B148CE944D61C9091B72C5
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜哇！？前辈！？！唔！唔——！！"

    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B20A60886DAF4ED0952F6EC66609FECA as tag_923338EC67B148CE944D61C9091B72C5 at center_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_193BCCFE681D42C8993A47A884FF2200 "别来碍事，你这……！！"

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A5017E40756A40EC8FEE981F51739B02

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔嗯——！！呜——！！"

    window hide

    pause 0.8

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_3FBF9470026545738C69B18D7D539AA9

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.8

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友！！没发生什么吧！？"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_A86787761B4F4226AFB3C2FA698779F2 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at right_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_EA9AA88E88D84B559B925363E2931756 "哇。不是，我不是森海哦～？"

    show rs_image_CA32B3074CBF4DB08BA59AE12141A4F7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊……抱歉。那个，有什么事？"

    show rs_image_89F334479C0B443DB4509C2A29D021C9 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "森海还没来学校嘛吗晨练的时候他没参加，所以我来看看。"

    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "诶？"
    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……{w=0.7}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    show rs_image_A86787761B4F4226AFB3C2FA698779F2 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    extend "（坏了）！！"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_48394E3397A94AD090308D24BFC677E3 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_4D5E70DCADBB4F2CA52AB49DED72D7C5 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_67CC8482272C470BA429E4D589C7E28E "……？"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003FCD

    return

label block_00003FCD:
    # Node: 00003FCD (CP3 Daytime 忍)
    call block_00001E62 from _call_block_00001E62

    if judge_lm_condition([]):
        jump block_00003FCC

    return

label block_00003FCC:
    # Node: 00003FCC (變革進行曲 4)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Key 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Key 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Key 1.ogg"

    show rs_image_37DD260DB3B64875AFF0FBF4F01BD3E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "吹奏乐部的仓库……有这么一个地方啊。{w}…………"

    show rs_image_CD2EEFA824144E4EA57A4C040DABF455 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.7

    stop music fadeout 3
    $ sys_music_current_file = ""

    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 4.5

    $ set_window("イベントモード")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔～！！{w}{w=0.3}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "呜……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（呜……刚和忍约好要大显身手，这下子根本没脸见人了啊～～！）"

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Hit 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "唔！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（！？）"

    window hide

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 1.5

    if sys_music_current_file != "sound/BGM/The past precious.ogg":
        play music "sound/BGM/The past precious.ogg" loop
        $ sys_music_current_file = "sound/BGM/The past precious.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 8.png
    $ zorder_rs_image_67BB6AD80CAE4374A5BE1811B7D7D1D5 = -100
    show rs_image_67BB6AD80CAE4374A5BE1811B7D7D1D5 as rs_image_67BB6AD80CAE4374A5BE1811B7D7D1D5 zorder zorder_rs_image_67BB6AD80CAE4374A5BE1811B7D7D1D5 onlayer master
    hide rs_image_67BB6AD80CAE4374A5BE1811B7D7D1D5

    show rs_image_67BB6AD80CAE4374A5BE1811B7D7D1D5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_266255D4821A4095BCA7860D44F0A511

    pause 0.8

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友！！没事吧！？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍～！！……我明明刚刚还那么装帅的，结果一下子就变成这样样子……对不起。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "果然我不能没有忍……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不要在意那种小事。就像依赖大家那样，也来依靠我。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈……忍～。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……我也有必须要向你道歉的事……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？什么？"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 9.png
    $ zorder_rs_image_9B3BE1450BA84524B154AAD914462F24 = -100
    show rs_image_9B3BE1450BA84524B154AAD914462F24 as rs_image_9B3BE1450BA84524B154AAD914462F24 zorder zorder_rs_image_9B3BE1450BA84524B154AAD914462F24 onlayer master
    hide rs_image_9B3BE1450BA84524B154AAD914462F24

    show rs_image_9B3BE1450BA84524B154AAD914462F24 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.5

    rs_character_193BCCFE681D42C8993A47A884FF2200 "唔……混……蛋……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "赏了你前辈一拳……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……不过，这本来就是我该做的，只是忍替我……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯……抱歉。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没关系。反正我也下不去手，前辈现在也不是能反抗的立场。"

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "已经明白了我身边有强大的盟友，应该不会再对我做什么了。谢谢。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯……剩下就是你们两个的问题，我就先回避了。早会不要迟到了哦。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，等下见。"

    window hide

    pause 1

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_76FE494B2D9D4C618B449EB276C14E59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    if sys_music_current_file != "sound/BGM/My precious time - slowly.ogg":
        play music "sound/BGM/My precious time - slowly.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time - slowly.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A33CBE44BBBD4405A261A6BD9FAF5CDD as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "冈岛前辈……"

    show rs_image_34EA3FF6756742B9B40F0095C34BB921 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……对不住啊，做过头了。"

    show rs_image_A33CBE44BBBD4405A261A6BD9FAF5CDD as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_193BCCFE681D42C8993A47A884FF2200 "你真的很碍眼。我负责钢琴部分不就能很自然地出席大赛了吗。"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……"

    show rs_image_B5EB5E7774A14E2CB2C60E113DB587A9 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_193BCCFE681D42C8993A47A884FF2200 "可你突然就入部，把我挤下去了。这次大赛已经是我中学最后一次了。"

    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "！！{w=0.5}{nw}"
    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "这、这个……对……不起。"

    show rs_image_34EA3FF6756742B9B40F0095C34BB921 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……说实话，也确实没好好练习，\n"
    show rs_image_A33CBE44BBBD4405A261A6BD9FAF5CDD as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "老师也可能已经放弃了。哈哈。"

    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可、可是！前辈钢琴弹得很好不是吗！！\n"
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "今天早上是前辈在弹对不对？"

    show rs_image_326E3AFD35A54F98B9DA03FD6E4165E5 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "哈！我就算再怎么练习也不如你。"

    show rs_image_B5EB5E7774A14E2CB2C60E113DB587A9 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "这种事最清楚的当然就是我自己。你反正也会弹，听也听得出来。"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没有那回事！我都听入迷了哦！只是我的演奏风格正好对了前辈的喜好而已。"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "喜欢听前辈演奏的人也一定存在的，\n"
    show rs_image_34F5B1EB5D2E4F4396E2FBC2BAFBEAA1 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "就像我一样……"

    window hide

    pause 0.6

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.6

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "只是，前辈太逊了。"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "欸……？"

    pause 0.3

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F747693390C4400FA3B7302024E8B5EA as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_74B823B258904383B62BED7A123D3E96

    pause 0.45

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我直到不久前也毫无自信，一直都很消极。"

    show rs_image_F6470A84AD8845BE97EAAA615A68C2F5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "如果弹不好，如果和吹奏乐部的其他人对不上，完全不知如何是好。"

    show rs_image_51A12E9EAB2B492E9FD30BC2C01A5C1B as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过，看到朋友们努力的样子，真的很帅。\n我也要像他们那样，我也要那样做，有了这种想法。"

    show rs_image_819903C0E7144FDDADE04672BA6B63AE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "但是，只知道给别人添乱的前辈，真的太逊了。"

    window hide

    pause 0.6

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.5

    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_B5EB5E7774A14E2CB2C60E113DB587A9 as tag_923338EC67B148CE944D61C9091B72C5 at center_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    window show

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……好学生的思维方式呢。"

    show rs_image_A33CBE44BBBD4405A261A6BD9FAF5CDD as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "你有好到能被吹奏乐部请来帮忙的余裕，才能说出这种漂亮话。"

    show rs_image_0CFCF59974504AC495C8FC45B44D0B76 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "我能做到的话当然也想堂堂正正的啊。可是，不被选上就毫无意义。"

    rs_character_193BCCFE681D42C8993A47A884FF2200 "这才不是什么陶醉于一贯的正义的擅自的想法。\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C70172768F92498A92988C76E79AF8AA as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……不久前还是归宅部的人怎么可能理解得了。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……确实我不能理解。"
    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过，正因如此才能明白。"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "正因为不知道这次大赛的重要性，才能毫无偏见地欣赏前辈的演奏。"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "然后，这样的演奏就打动了我的内心。很不甘心，但确实比我要好得多。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F33DA7B19039419089D2B31DD1FAE879 as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "都说了，这种说法就是在讽刺……"

    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "肯定也有很多人承认了前辈的能力的！否则就不会变成这种情况了。"

    show rs_image_326E3AFD35A54F98B9DA03FD6E4165E5 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……？为何？"

    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "听过我那么多遍演奏的老师不是还是考虑了前辈的请求吗？"

    show rs_image_B5EB5E7774A14E2CB2C60E113DB587A9 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "天知道……因为是我最后一次比赛起了同情心？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_4ADA38AD8AC240F48211FBA4F8807972 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "才不是！如果那样前辈早就被叫去职员室委任钢琴部分了。{w}事实不是这样。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没有确定我来担当的意思就是，年级什么的都不重要，最后要靠实力来决定。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "老师不决定是我还是前辈，而是通过比较来决定，就说明我们的实力差距并不大。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_A33CBE44BBBD4405A261A6BD9FAF5CDD as tag_923338EC67B148CE944D61C9091B72C5 at center_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_193BCCFE681D42C8993A47A884FF2200 "老师也，对我……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A33CBE44BBBD4405A261A6BD9FAF5CDD as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "所以前辈没有必要用这些手段！如果前辈本来就不情愿的话，更不该做了！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "所以请不要从一开始就逃避！请和我正面决胜。"

    show rs_image_0CFCF59974504AC495C8FC45B44D0B76 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……{w=0.5}{nw}"
    show rs_image_A33CBE44BBBD4405A261A6BD9FAF5CDD as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "有道理。对不起了。\n"
    show rs_image_A55765D64B69474CB7292398EDD238EB as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……有点自信了。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，不……谢谢。"

    show rs_image_758CA32B10AD4D749FA2D5D577EDF989 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_193BCCFE681D42C8993A47A884FF2200 "不过，不用比了。我会退出的。"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶——？！？为、为什么！？"

    show rs_image_B5EB5E7774A14E2CB2C60E113DB587A9 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "吹奏乐一定是团体赛，所以不能无视周围。{w}至少要明白老师这层含义。"

    show rs_image_34EA3FF6756742B9B40F0095C34BB921 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "然而，我却为了陷害你不断妨碍社团活动。这根本就不是团结。"

    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可、可是，都做到会把我关起来这种程度了！\n对前辈来说，这也是最后一次大赛……！"

    show rs_image_9DE3C45471674FB8B7109B7FD4C19C25 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_193BCCFE681D42C8993A47A884FF2200 "无所谓了。\n已经知道老师没有对我失望，某种意义上需要的成就感已经可以了……"

    show rs_image_A55765D64B69474CB7292398EDD238EB as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……不，用你的话来说，我这就是不战而败了。果然敌不过你呐。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "等、等等！！这样不行！前辈已经努力了两年半了……"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "练习很辛苦。我有好几次都想要放弃了。"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "一直这么努力，最后怎么可以是这样的结局！{w}\n这种事情、这种事情……"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    extend "啊！！"

    stop music fadeout 3
    $ sys_music_current_file = ""

    rs_character_193BCCFE681D42C8993A47A884FF2200 "？"

    window hide

    pause 0.7

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_76FE494B2D9D4C618B449EB276C14E59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if sys_music2_current_file != "sound/BGM/My precious time of now.ogg":
        play music2 "sound/BGM/My precious time of now.ogg" loop
        $ sys_music2_current_file = "sound/BGM/My precious time of now.ogg"

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呐，就那对我不爽的感觉作为动力怎么样！\n那样的话肯定就有竞争心了吧！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_D8FBA8060A9B457F9D8A35FB71E72F10 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对了！就送给前辈可恨的我的等身大海报如何！\n挂在房间里肯定练习会很投入的哦～！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_F33DA7B19039419089D2B31DD1FAE879 as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_193BCCFE681D42C8993A47A884FF2200 "你……脑袋到底怎么长的……"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_6636F3FA642745AE8103D258F3BF47F2 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "因为我也想要劲敌呐！！那样我为了不输也能不断进步了。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "想打倒看着不爽的我？！还是说，为了比我更强，想当我的劲敌？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "来！要选什么！？除此之外的回答不予受理哦！！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_193BCCFE681D42C8993A47A884FF2200 "真是乱来的……"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "时间到！回答是！？请在“好”和“YES”中选一个。"

    hide tag_923338EC67B148CE944D61C9091B72C5
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……{w}好。"
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_9DE3C45471674FB8B7109B7FD4C19C25 as tag_923338EC67B148CE944D61C9091B72C5 at center_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.8

    show rs_image_758CA32B10AD4D749FA2D5D577EDF989 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    extend "YES。"

    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_34E241C96D16409BBECDFE411E12F665 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "太、太好了……！"

    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_A55765D64B69474CB7292398EDD238EB as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "你可别为把我留下后悔啊。我认真起来可不止之前那种程度。"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈，我也会变得更好的哦！不要留下悔恨，大家要一起全力以赴吧。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_0C39C5160FFF4610BD5C9410681CAAFF as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "说不准呐。我某种意义上还是很不择手段的～？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——！这种事就算了～！那种只在SM里做就可以了～！！"

    show rs_image_EA97B5806E55484DBC3CBE0C26E74E99 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_193BCCFE681D42C8993A47A884FF2200 "什么啊，原来你好那一口。早知道就多给你来点疼痛体验了。"

    show rs_image_FF4A588462534B15B9D5F444704F26BB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那样的话前辈会更麻烦哦。我家的忍不会坐视不管的！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_A55765D64B69474CB7292398EDD238EB as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_193BCCFE681D42C8993A47A884FF2200 "啊～那个就算了。已经尝到那种直面逆鳞的恐怖感了……"

    window hide

    pause 0.7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 2

    stop music2 fadeout 5
    $ sys_music2_current_file = ""

    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_923338EC67B148CE944D61C9091B72C5
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B458977B6F2E4C8ABD6196FDA6E1C3C8

    pause 2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_28CB16F81175458EA97C8F0250448304 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 2

    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A58FA4D4F3DA4D62A421C5FCE76AA975

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_DA3F8B10BDD94A2EA7654CAF57BE44D6 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.7

    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔～这里要弹得更加活跃一些。{w}前辈的即兴演奏要更加帅气一些……"

    if sys_music2_current_file != "sound/Effect Sound/Open window 1.ogg":
        play music2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.7

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_3DF1699B103D4492AAD9F78AF0406858 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at right_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 0.3

    rs_character_EA9AA88E88D84B559B925363E2931756 "你好呀！森海。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "佐藤君，下午好——怎么样？萨克斯部分还好？"

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_48B621B61D744137AB3444EC6DA27FB0 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "当然♪爵士乐的主力就是我们萨克斯！\n也有一些改编，肯定能不负众望地好好表演的。"

    show rs_image_27FF4633286B4DF59BF4C1A761DDF98E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是嘛～！我也想试试萨克斯呐～看起来听起来都好帅的感觉。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_0A1BC250AF51455791A38A520909E1DC as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "呵呵。森海，作为门外汉眼光还不错嘛♪\n"
    show rs_image_633EE8E0E8604D0A9FB1BAE76DEA33AB as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "说起来，你那边怎么样？"

    show rs_image_285E40B50F3F466F9AE41CD837D82E42 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊、哈哈～这边差不多。\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "不会再像上次那样了放心！"

    show rs_image_0B4D1CA8EB3342D881C010956B338E02 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "好强的自信啊，真的没问题吗？我可是听说一班的班长又天然又冒失的。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什～么！？谁说的——！怎么可以这么说自己的班长！"

    if sys_effect3_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_96013754928A470894D94BAC81A99E0D as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "谁说的……一班所有人都这么说哦。"

    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……\n{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_FF4A588462534B15B9D5F444704F26BB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "随便，不管了。反正大家也都很喜欢我嘛。"

    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……啊，对了，之前就有想要问的事了，可以问问吗？"

    show rs_image_3DF1699B103D4492AAD9F78AF0406858 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "嗯？什么？"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "佐藤君为什么要叫我去帮忙呢？冈岛前辈明明那么厉害。"

    show rs_image_33DAA2B0F1C244C4B2C872213860A04A as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_EA9AA88E88D84B559B925363E2931756 "嗯……必须说吗？\n"
    show rs_image_F640D24E91BC44AB8E0808AF82ED2885 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "可以的话，能不能大赛结束后再说呢。"

    show rs_image_A579F650612D4CA18E2B222221DBF547 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸……我现在就要听！现在就要！呐——呐——告诉我嘛～"

    show rs_image_89F334479C0B443DB4509C2A29D021C9 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_EA9AA88E88D84B559B925363E2931756 "嗯……作为叫人去帮忙的立场我也没有拒绝的权利。"

    show rs_image_FF4A588462534B15B9D5F444704F26BB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    stop music fadeout 3
    $ sys_music_current_file = ""

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就是就是！"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 300
    show rs_image_3DF1699B103D4492AAD9F78AF0406858 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.2

    if sys_music2_current_file != "sound/BGM/Guitar 1.ogg":
        play music2 "sound/BGM/Guitar 1.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Guitar 1.ogg"

    rs_character_EA9AA88E88D84B559B925363E2931756 "冈岛前辈从很小的时候就一直在练习钢琴，才会那么优秀。"

    show rs_image_F640D24E91BC44AB8E0808AF82ED2885 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "啊，顺便一说冈岛前辈是我们班冈岛的哥哥哦，新闻部的那个。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_758CA32B10AD4D749FA2D5D577EDF989 as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    show rs_image_E283497485C94D2C96064B6CA8800E56 as tag_CC4336DE74164173AC47C2C317367F10 at left_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？是这样？！啊～说起来确实很像呐～"

    rs_character_EA9AA88E88D84B559B925363E2931756 "算了先不管这个。\n"
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    extend "前辈从一年级开始就一直在大赛里负责钢琴部分。"

    rs_character_EA9AA88E88D84B559B925363E2931756 "我刚入部时非常憧憬，当然社团之外也是。\n有时会借一间小录音室，一起二重奏。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～听起来好棒～！"

    window hide

    pause 0.5

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 7.png
    $ zorder_rs_image_4D66E39D4F0541B297D6075145C4D09A = -100
    show rs_image_4D66E39D4F0541B297D6075145C4D09A as rs_image_4D66E39D4F0541B297D6075145C4D09A zorder zorder_rs_image_4D66E39D4F0541B297D6075145C4D09A onlayer master
    hide rs_image_4D66E39D4F0541B297D6075145C4D09A

    show rs_image_4D66E39D4F0541B297D6075145C4D09A as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_2A62662A9A9C44A1A266E7BB1BDCA6A0

    pause 0.8

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "我啊，比起在社团弹钢琴的前辈，更喜欢只和我二重奏的时候的前辈。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～？独占欲～？？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_EA9AA88E88D84B559B925363E2931756 "笨蛋！！不是那样的！是两人独处的话更容易听清音色！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可是，喜欢“前辈”对不对？"

    rs_character_EA9AA88E88D84B559B925363E2931756 "啊～那么说是有确实的理由的。社团中的前辈，简直就像换了个人。"

    rs_character_EA9AA88E88D84B559B925363E2931756 "音色完全不同，有的很有活力有的却……\n毕竟是社团活动，当然不可能演奏的曲目全是喜欢的。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～根据喜好区别对待，这样做真的可以吗？"

    rs_character_EA9AA88E88D84B559B925363E2931756 "当然，不可以……{w=0.5}一般的话。{w}\n不过，前辈不同，前辈是社团里最重要的钢琴家。"

    rs_character_EA9AA88E88D84B559B925363E2931756 "二重奏本来就是玩的性质，当然只有喜欢的曲子。\n结果，我就注意到前辈在偷懒了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯～然后直接和前辈说明了？"

    rs_character_EA9AA88E88D84B559B925363E2931756 "不……就算我说了也毫无意义。无关我的想法，前辈都是唯一的钢琴家。"

    window hide

    pause 0.8

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_923338EC67B148CE944D61C9091B72C5
    hide tag_CC4336DE74164173AC47C2C317367F10
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，是这样……所以才叫我……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_633EE8E0E8604D0A9FB1BAE76DEA33AB as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_EA9AA88E88D84B559B925363E2931756 "正确！不过我也没想到森海能坚持到现在。"

    show rs_image_48B621B61D744137AB3444EC6DA27FB0 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "本来只是想靠森海燃起前辈抗争的火种的，没想到会发展到试音会这一步……"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_3F5AF2DAC6F94773B04A709D2558F647 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3DF1699B103D4492AAD9F78AF0406858 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at right_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，那我不就只是个弃子吗！？佐藤君好腹黑！"

    show rs_image_F640D24E91BC44AB8E0808AF82ED2885 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "啊～……关于这个真的很抱歉。把你卷进我个人的计划真的对不起。"

    show rs_image_3DF1699B103D4492AAD9F78AF0406858 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "不过，多亏了森海，这次将会是有史以来最好的演奏。\n关于这个，请允许我表示感谢。"

    show rs_image_3F84B60D1FD24C9CAD32F21E89A94324 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_EA9AA88E88D84B559B925363E2931756 "森海……"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    extend "谢谢你努力到现在！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我、我明白了快抬起头！我很不习惯这种礼仪的……"

    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔——嗯……也就是说，佐藤君果然是想要最喜欢的冈岛前辈参加大会的。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_8B5E09CB821B48C29590BEFB90AE0DDB as tag_346FE7CD97BB4FB18CB50E78275F4E23 at right_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "其、其实也并不怎么喜欢。那种冒……{w}而且！我认同水准好的出赛这一点。"

    show rs_image_DD649A23A0C54C3B99DE6AF655696477 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_EA9AA88E88D84B559B925363E2931756 "当然，也不可能对继续社团活动的前辈完全没有想法，\n但这本来就是那个人的错。"

    show rs_image_3F84B60D1FD24C9CAD32F21E89A94324 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "本来那么出色，最后却输给森海的话，足以说明那个人平时有多偷懒了。"

    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可、可是。"

    show rs_image_89F334479C0B443DB4509C2A29D021C9 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "不需要可是或轻视！！实力决胜的世界不需要同情！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_8B5E09CB821B48C29590BEFB90AE0DDB as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "你、你可不要考虑太多，集中于现在！再见。"

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 1

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    stop music2 fadeout 5
    $ sys_music2_current_file = ""

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "佐藤君也是正值青春！"
    show rs_image_6636F3FA642745AE8103D258F3BF47F2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "反正也看到可爱的一面了，\n放放水也是可以的哦～！"

    pause 0.3

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.4

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……那么，我也必须转换一下心情了。"

    window hide

    pause 0.8

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003FA8

    return

label block_00003FA8:
    # Node: 00003FA8 (CP3 Twilight)
    call block_00001EC4 from _call_block_00001EC4

    if judge_lm_condition([{ "scope": 0, "content": "C3F6Route == 0" }]):
        jump block_00003FA5
    if judge_lm_condition([]):
        jump block_00003FA6

    return

label block_00003FA5:
    # Node: 00003FA5 (變革進行曲 友 END 1)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/My precious time of now - piano.ogg":
        play music "sound/BGM/My precious time of now - piano.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time of now - piano.ogg"

    $ set_window("イベントモード")
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1.5

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_1084DAF07A574EC18C0EDEF9E03F423C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_93E7311915BC403AAFABACFA29A7DDB1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A46E468ABE0345679EB63CE570AD59F9

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，技安……"

    show rs_image_486F70F1E27D43BC868FA3ADA0B574BE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哦，笨蛋。有事？"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没有，没什么。"

    show rs_image_7F843C6F478A4CA391089291EB2F56A3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈？怎么了那张脸。还以为最近加入吹奏乐部后你早就成核心成员了。"

    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "只是去帮忙的，没有那种……\n"
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "说起来，篮球部有多少人？"

    show rs_image_486F70F1E27D43BC868FA3ADA0B574BE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "突然问这个干嘛……四十人左右。没那么多？嗯～反正差不多。"

    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "能出席比赛的人只有一小部分？"

    show rs_image_5B75C21196E6494E82DFA6A82B22212D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嗯，五个。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！？只有那么点！？？"

    show rs_image_D7279DBAD79D48199C2509989B89EA00 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "对。休息区会站十二个。"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就是说三年级也有不能出赛的人？"

    show rs_image_5B75C21196E6494E82DFA6A82B22212D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "当然。和年级无关，只要有比起三年级的技术更好的人，低年级就会上。"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸……{w=0.65}{nw}"
    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "不会有罪恶感？\n不会想要让给前辈？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_486F70F1E27D43BC868FA3ADA0B574BE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……所以才说归宅部真是天真。"

    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么？一般都会说想要上啊，明明只是后辈啊之类的才对？"

    show rs_image_7F843C6F478A4CA391089291EB2F56A3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_17BE89E1E45A45008C16668BC9724267 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "森海君长得这么帅，头脑也好，真的好厉害呐。\n不好不好，快要迷上了——"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么！？突然做什么！"

    show rs_image_7F843C6F478A4CA391089291EB2F56A3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你觉得我刚才说的是真心话？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3F5AF2DAC6F94773B04A709D2558F647 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么可能是！！用那种说法……只会觉得恼火。"

    pause 0.3

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "要是作为后辈的我们真的像你说的那么做，{w}\n前辈们的想法恐怕和现在的你是一样的。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸……"

    window hide

    pause 0.5

    # Gallery unlock: images/CG/Revolution-march/Revolution-march TomoEND 1.png
    $ zorder_rs_image_82C2A7F9AB474FB6AA0C71F77E91070C = -100
    show rs_image_82C2A7F9AB474FB6AA0C71F77E91070C as rs_image_82C2A7F9AB474FB6AA0C71F77E91070C zorder zorder_rs_image_82C2A7F9AB474FB6AA0C71F77E91070C onlayer master
    hide rs_image_82C2A7F9AB474FB6AA0C71F77E91070C

    show rs_image_82C2A7F9AB474FB6AA0C71F77E91070C as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.7

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不管是篮球还是吹奏乐，对方都是认真的。\n我们要是不认真对待，会非常失礼。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "是否要手下留情不是后辈该考虑的。倒不如说，会那么想才该有罪恶感。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "面对对手，全力以赴才是对前辈们起码的尊重。\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "明白了没？"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……{w}穗海有时还挺帅呐。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march TomoEND 2.png
    $ zorder_rs_image_793A50EA5F1D4DD095383254ED6D5645 = -100
    show rs_image_793A50EA5F1D4DD095383254ED6D5645 as rs_image_793A50EA5F1D4DD095383254ED6D5645 zorder zorder_rs_image_793A50EA5F1D4DD095383254ED6D5645 onlayer master
    hide rs_image_793A50EA5F1D4DD095383254ED6D5645

    show rs_image_793A50EA5F1D4DD095383254ED6D5645 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈、哈啊？突然说什么呢。{w}而且第一次直呼我的名字……"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀～对这么认真的人还要用“技安”太失礼了～这么觉得。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你啊，比起前辈那边首先还是对我言过其实了吧。{w}\n怎样？有参考价值吗？森海君。"

    window hide

    pause 0.6

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_D4AF6091BD0341CFBF561C2744F3FD83 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，当然了……谢谢！\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_A39671BE6D8246F5ACCB45CA04C8C3D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "我会把技安的魅力告诉翼君的！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E54A2DFBC85F4C20B96B216AE6D076B7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈！？别做多余的事！\n"
    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_C507E18213D34AE4A482BBE2CE5D35AD as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "还有最后还是叫回“技安”了啊！"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈♪那就这样，下次见～！"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    show rs_image_A39671BE6D8246F5ACCB45CA04C8C3D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.8

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_B276F958003A43A59D0E1DAFE5CCAA4E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"
    show rs_image_D7279DBAD79D48199C2509989B89EA00 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "简直就是给敌人送盐……"

    window hide

    pause 1

    stop music fadeout 4
    $ sys_music_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 4

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 1

    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.4

    window show

    rs_character_776382753FF149B49443F348F4356521 "试音会的结果，{w}这次负责钢琴部分的是……"

    window hide

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_F33DA7B19039419089D2B31DD1FAE879 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    hide tag_923338EC67B148CE944D61C9091B72C5
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    pause 5

    if sys_effect_current_file != "sound/Effect Sound/Clap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Clap 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_510ED9F495254C89972BC4C1C431D966 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_673B577A4E15407397C9C9B62906A309

    $ renpy.pause(2.0, hard=True)

    $ zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD = 300

    show concert_description (_("12号节目\n御咲学园初中部吹奏乐部\n指挥：平井 米")) as tag_0BDB8A4A05BB44ED81AE140BE96066BD at Transform(xpos=677,ypos=158,xanchor=1.0) zorder zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD onlayer master
    with rs_effect_AE78B5E92416464A93F1A10BE1C93CE6

    $ renpy.pause(1.0, hard=True)

    $ zorder_tag_03723FC929AD4F0BA44259F7A076ADFD = 300
    show concert_description (_("♪ 指定曲目\n三号曲\n♪ 自由演奏\nRhapsody for Concert Band and Jazz Ensemble\nComposer: Patrick Williams")) as tag_03723FC929AD4F0BA44259F7A076ADFD at Transform(xpos=674,ypos=285,xanchor=1.0) zorder zorder_tag_03723FC929AD4F0BA44259F7A076ADFD onlayer master
    with rs_effect_AE78B5E92416464A93F1A10BE1C93CE6

    $ renpy.pause(4.5, hard=True)

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_0BDB8A4A05BB44ED81AE140BE96066BD
    hide tag_03723FC929AD4F0BA44259F7A076ADFD
    with rs_effect_673B577A4E15407397C9C9B62906A309

    $ renpy.pause(1.5, hard=True)

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_418B7345B9854BA0B93A4CBBA12BAE8E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ renpy.pause(1.5, hard=True)

    show rs_image_8EF12B9EF1EB482A96213CEB566AAA47 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ renpy.pause(1.5, hard=True)

    show rs_image_CA830C5BFF094868BD5D4E1AF370A76A as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ renpy.pause(2.5, hard=True)

    if sys_effect3_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march Concert 4.png
    $ zorder_rs_image_29E9A807D6B148168EEACEB2EA7D0A5E = -100
    show rs_image_29E9A807D6B148168EEACEB2EA7D0A5E as rs_image_29E9A807D6B148168EEACEB2EA7D0A5E zorder zorder_rs_image_29E9A807D6B148168EEACEB2EA7D0A5E onlayer master
    hide rs_image_29E9A807D6B148168EEACEB2EA7D0A5E

    show rs_image_29E9A807D6B148168EEACEB2EA7D0A5E as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    $ renpy.pause(3.0, hard=True)

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_B6D2CFDC1CB5407EACD7FBC1D100D198

    $ renpy.pause(3.0, hard=True)


    if judge_lm_condition([]):
        jump block_00003FA4

    return

label block_00003FA4:
    # Node: 00003FA4 (變革進行曲 友 END 2)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_75A864E3BFC9426C817C95EDE531DCA5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EF2D3A4912BA490B9BDDB92C8700586E

    if sys_music_current_file != "sound/BGM/To the future.ogg":
        play music "sound/BGM/To the future.ogg" loop
        $ sys_music_current_file = "sound/BGM/To the future.ogg"

    pause 0.8

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.3

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，辛苦了！非常帅气哦！！"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_CDE407350E4A49AC8933C6D199FE9A13 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜——太感动了眼泪……根本停不下来。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_31DC2C2F7D164AA2B6F4DCFBBBFB98BB as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "确实，友太郎也长大成出色的孩子了啊……！\n"
    show rs_image_A2E7C1AAED834AD7861668C6EE330F80 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "妈妈很开心哦，都忍不住哭出来了哦！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_89D53127B93243A194D7108DECE8802F as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "…………"
    show rs_image_4683860EE22143EDB1980090E250F53A as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "森海，请一定要原谅不才的我，请再演奏一次！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_30CFC5FBE4104C718C904D0C834E6E9A as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不用在意哥哥的。"
    show rs_image_A52160C305F54813BC6542DBBC09E25D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "说起来，真的非常厉害呐！"

    show rs_image_1CDBF9A281F54418A7363E36408C7DD5 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "一直以来开朗阳光的友君当然很好，不过认真起来的友君更棒哦！"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A56A27CF00F74EF798B09E4211817332 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "大家谢谢……！"
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "我……我能努力到现在，\n都是多亏了大家的应援哦！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_EFDC09B34577437A8D2B581A3FFFC9E4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谢谢，大家……真的非常感谢！！呜、呜……"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D5EEA08F613D4581B90B56569FE7A25D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友真是的，别、别哭啊。\n"
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "真的很努力了，很厉害哦。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_CDE407350E4A49AC8933C6D199FE9A13 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……我、越来越、迷上友君了……{w}\n友啾绝对是世界上第一帅的人。（哭）"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_A2E7C1AAED834AD7861668C6EE330F80 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊咧啊咧，大家都是爱哭鬼呐。真是的……（抽泣）。"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_4683860EE22143EDB1980090E250F53A as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "………………"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_C8509382B1E34741B9130C4CA5DE55D6 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥，等这次大赛出CD或DVD后买回去在家里听算了。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_B4F55DFE937C4D9B8956BB29AB3AB0B3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "什么！还有那种东西！？"
    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……得救了。"

    window hide

    pause 0.6

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_28CB16F81175458EA97C8F0250448304 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 0.6

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈……说起来，仔细想想的话，真的只是一瞬呐。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "就是这样哦。刚开始的时候可能会觉得很久。{w}社团不继续参加了吗？"

    pause 0.4

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.5

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯～退……"
    if sys_music2_current_file != "sound/Effect Sound/Dorky 1.ogg":
        play music2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "啊～！唔～！！我该怎么做！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_5465258BCE404B519910FD1F4172107B as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "怎么了？有必要那么烦恼？？"

    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "确实想要退出，可一想到刚才舞台上的样子，就又想继续做下去了……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_2EDCBF8750D348A8A06B06DB4F635C1C as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那只要继续不就好了嘛。本来去帮忙也没有截止日期不是嘛？"

    show rs_image_5465258BCE404B519910FD1F4172107B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔。嗯，确实是那样不过……"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "还有其他理由吗？"

    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个啊……其实，我还从社团活动里意识到了一件事哦。{nw}"
    stop music fadeout 2
    $ sys_music_current_file = ""

    extend ""

    window hide

    pause 0.7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.7

    window show

    if sys_music2_current_file != "sound/Piano/sti_gymno_01_pi.ogg":
        play music2 "sound/Piano/sti_gymno_01_pi.ogg" loop
        $ sys_music2_current_file = "sound/Piano/sti_gymno_01_pi.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "至今为止已经偶尔意识到几次了……我真的一直都好幸福呐。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……和大家在一起的时候，还没有这么强烈。{w}\n当和大家分开后，我终于明白了。"

    pause 0.3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_48394E3397A94AD090308D24BFC677E3 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君……"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "失落的时候会来关心我，被抓走的时候会来救我……真的谢谢你们。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "所以我想和大家继续随心所欲地在一起哦。"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_4206BF0F2582432A8C2017FD937CB719 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "既、既然这样！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 400
    show rs_image_F9AEB450C2A74F568F5D4EC1B5A961F0 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯。本来决定好大赛结束后就要回来了，可刚才那样的演奏却让我……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 400
    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_F9AEB450C2A74F568F5D4EC1B5A961F0 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍……我到底该选什么。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……我……"
    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……说不出口。\n这是非常重要的选择，必须友自己来回答。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 400
    show rs_image_5465258BCE404B519910FD1F4172107B as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……我很没用，继续社团活动的话，肯定会连烦恼的机会都没有的。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "最近上课时也一直在发呆呐。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜～无法反驳……连那个也不能做了。\n"
    show rs_image_F9AEB450C2A74F568F5D4EC1B5A961F0 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过，能让我这么着迷的事……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    $ zorder_tag_016E98039DFE4B72A2BB3866B2AD7FF3 = 200
    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_016E98039DFE4B72A2BB3866B2AD7FF3 at center_top zorder zorder_tag_016E98039DFE4B72A2BB3866B2AD7FF3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "友亲，听我一言如何？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_016E98039DFE4B72A2BB3866B2AD7FF3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，什么？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不打算听听我的意见吗？说不定能成为参考哦♪"

    show rs_image_3766CD2AF98244F5AECA23E096C299D8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯、嗯……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "慎太郎，你……"

    pause 0.2

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_7F497F24D349433FB39C83C619E61AB8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.4

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if sys_music2_current_file != "sound/BGM/The end of touch.ogg":
        play music2 "sound/BGM/The end of touch.ogg" loop
        $ sys_music2_current_file = "sound/BGM/The end of touch.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "友亲能闪耀光辉的地方，也不只有社团。{w}试着开阔一下视野如何？"

    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "比如，正在和翼亲做什么对不？不是也有那种选项吗？"

    pause 0.2

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_8A9FD25CF2224DA4B5F560425D3A98A7 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F0AF18EA5ED94E6B9426EA7B01961357 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊……能、能让我也说一句吗……\n"
    show rs_image_C18E9E3152D24005B446B9C4987139A3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "要解散小钢琴部什么的……我真的很寂寞。"

    show rs_image_9071DE7B7E5343C897D93F24F8DF7BAF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "现在我因为饲育系的事情完全没有空余时间。\n能早一点适应的话，肯定能回来的。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_F59CF92171C0495BA4E334AC96BA8B63 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "和重视吹奏乐部的胜利相对的，也重视一下在小钢琴部收获的快乐比较好哦。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "既然如此，和森还更相称的，不就是后者吗？"

    pause 0.3

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.5

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "大家……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "小忍，要想收获幸福的话，不要把所有选项委任给对方，\n试着为对方提供最为幸福的选项也是一个好方法哦。"

    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w}{w=0.3}{nw}"
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_52820B68402A48B88D6C1517EC79E403 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.4

    $ zorder_tag_E68131B5463148FC8A76A11B96CD1843 = 200
    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_E68131B5463148FC8A76A11B96CD1843 at center_top zorder zorder_tag_E68131B5463148FC8A76A11B96CD1843 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    extend "……我想要友回到我身边。\n"
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_E68131B5463148FC8A76A11B96CD1843 zorder zorder_tag_E68131B5463148FC8A76A11B96CD1843 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "我想要友回到大家的生活中。"

    pause 0.3

    hide tag_E68131B5463148FC8A76A11B96CD1843
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍……\n"
    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……{nw}"
    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    extend ""

    window hide

    pause 0.5

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.9

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_07E85511B35D42B2A68B24FACDB172AB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谢谢，大家。我下定决心了。\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A56A27CF00F74EF798B09E4211817332 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    extend "我要回到大家所在的日常中！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 400
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我回来了，大家！！今后也请多多指教了哦！"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……嗯，欢迎回来！"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=370, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欢迎回来，友亲！真是的～这段时间都到什么地方去了！"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_8C106322A86B43E599BD9F3A2962F305 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=230, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "等、等你很久了哦，友君！今后也、请、请多多指教！！"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-180, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "能选择和我们在一起，我也很高兴。\n友君，再一次，请多多指教。欢迎回来。"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=500, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "你并不仅仅是回归此地，\n你在社团锻炼出来的一切将会进一步改变你的日常。重新起航，森海。"

    show rs_image_A56A27CF00F74EF798B09E4211817332 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……！大家谢谢！！感觉好幸福哦！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_0082B8EA494C49D7B202B0DC39D7AC3F as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好！！既然如此友亲的接风晚会就在我家花乃汤召开！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 400
    show rs_image_6EA040B97356486ABE5FD91F92B543D2 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "慎酱，真的嘛！？哇——！哇——！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "大家。在那之前，作为庆祝先把友抛高高怎样？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦♪来自小忍的超稀有的提案！{w}\n毕竟把友亲留在了身边，非常幸福呐～"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_41072B3B99654E4E81C3965CF973A6D4 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "慎太郎也是……倒不如说大家都是一样的。\n"
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "只靠一人是不行的，因为大家都在，友才会更加幸福。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_3C4C246AAFC1459DBB1711584019784D as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_D7BB1A8267AE4353950D17F94CE6C389 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "确实，一个人也抬不起友来呐！\n"
    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "来来，大家把友围在中间哦～！"

    show rs_image_E8DD9768D82A468CA794353ED73907AD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "马上！！我、我也、为了让友君能更加幸福，会不断努力的～！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇哇哇！？好、好可怕！！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "没关系，相信我们。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "对对，不是说“最喜欢”了嘛？"

    window hide

    pause 0.6

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_832FF861A1F843A791AAA75DA7D7D8FE

    pause 1

    show center_title (_("正如你所感受到的，我也陶醉于其中\n我也，最喜欢你了")) as center_title zorder 1000
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 4

    show center_title (_("辛苦了！！森海友！")) as center_title zorder 1000
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 4

    hide center_title
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    call scb_flag_title_end(3, _("「变革进行曲」")) from _call_scb_flag_title_end_3

    if judge_lm_condition([]):
        jump block_00003FA3

    return

label block_00003FA3:
    # Node: 00003FA3 (Phase: 0)
    $ C3S6Phase = 0
    if Chapter <> 3:
        $ del C3S6Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_00003FB6
    if judge_lm_condition([]):
        jump block_00003FA2

    return

label block_00003FB6:
    # Node: 00003FB6 (終了)
    $ del C3F6Route

    return

label block_00003FA2:
    # Node: 00003FA2 (FINISH)
    $ C3S6 = True

    if judge_lm_condition([]):
        jump block_00003FB5

    return

label block_00003FB5:
    # Node: 00003FB5 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_3

    if judge_lm_condition([]):
        jump block_000041CC

    return

label block_000041CC:
    # Node: 000041CC (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#AA0055}“变革进行曲”{/color}{color=#0080FF}成功结束。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003FB6

    return

label block_00003FA6:
    # Node: 00003FA6 (變革進行曲 岡島  END 1)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("三楼走廊"))
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    show rs_image_7962041686F34839A342E7B6E33F2B84 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    if sys_music2_current_file != "sound/Piano/hero.ogg":
        play music2 "sound/Piano/hero.ogg" noloop
        $ sys_music2_current_file = "sound/Piano/hero.ogg"

    pause 0.8

    stop music fadeout 3
    $ sys_music_current_file = ""

    pause 1.4

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这个声音，是前辈在弹……{w}……{w}果然很厉害。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（前辈的音符完美融入了大家的曲谱里。{w}很不甘心但现在的我确实做不到。）"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（果然三年一直在一起合奏的话，相对地音符就会和谐一些……）"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（嗯？谁过来了！不能被发现我在偷懒！藏、快藏起来……）"

    window hide

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    $ set_window("イベントモード")
    pause 2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7962041686F34839A342E7B6E33F2B84 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.7

    if sys_music_current_file != "sound/BGM/My precious time of now - piano.ogg":
        play music "sound/BGM/My precious time of now - piano.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time of now - piano.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_3F84B60D1FD24C9CAD32F21E89A94324 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.3

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "……"

    pause 0.3

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    show rs_image_53C99367467B48B78318249B4B9B7DA5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "佐藤君……果然很在意前辈呐。"

    window hide

    pause 0.4

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_3F84B60D1FD24C9CAD32F21E89A94324 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at center_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    show rs_image_7962041686F34839A342E7B6E33F2B84 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    show rs_image_F747693390C4400FA3B7302024E8B5EA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.8

    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_34F5B1EB5D2E4F4396E2FBC2BAFBEAA1 as tag_923338EC67B148CE944D61C9091B72C5 at left_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_193BCCFE681D42C8993A47A884FF2200 "嗯？佐藤，你怎么了？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_9B6EA9CA0C0541BAAD8AE6254AB5AC9D as tag_346FE7CD97BB4FB18CB50E78275F4E23 at right_top zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_EA9AA88E88D84B559B925363E2931756 "啊，没什么，什么都……就是来看看有没有认真练习。"

    show rs_image_A55765D64B69474CB7292398EDD238EB as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "我还真是不被信任呐……"
    show rs_image_EA97B5806E55484DBC3CBE0C26E74E99 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "我不会再偷懒了。\n多亏被你找来的那家伙，拿出气势了。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_A86787761B4F4226AFB3C2FA698779F2 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "欸。注意到是我找来的了？"

    show rs_image_34EA3FF6756742B9B40F0095C34BB921 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "社团活动里随便弹弹的时候，只有你露出了一脸不爽的表情。\n"
    show rs_image_9DE3C45471674FB8B7109B7FD4C19C25 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "我明白的。"

    show rs_image_33DAA2B0F1C244C4B2C872213860A04A as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "我、我因为兴趣一直和前辈二重奏，当然很容易听出来了……"

    show rs_image_A55765D64B69474CB7292398EDD238EB as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "能对唯一的钢琴手开刀，不错的毅力嘛～不过。"

    show rs_image_89F334479C0B443DB4509C2A29D021C9 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "正是自满导致了现状。"
    show rs_image_DD649A23A0C54C3B99DE6AF655696477 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……试音会，可以吗？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_0C39C5160FFF4610BD5C9410681CAAFF as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "完全没问题！{w=0.5}{nw}"
    show rs_image_34EA3FF6756742B9B40F0095C34BB921 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "……确实想这么说。\n但，实话说，非常不安。那家伙，太强了。"

    show rs_image_6EB06386B3BF438184595D042608116A as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "没出息。有在反省自己平时的偷懒行为吗？"

    show rs_image_B5EB5E7774A14E2CB2C60E113DB587A9 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "嗯。所以，现在要全力以赴。后悔也晚了。"

    show rs_image_DD649A23A0C54C3B99DE6AF655696477 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F640D24E91BC44AB8E0808AF82ED2885 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_EA9AA88E88D84B559B925363E2931756 "好好，尽可能努力哦。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_F33DA7B19039419089D2B31DD1FAE879 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "你啊～就算是因为兴趣，对最亲近的前辈就这种态度？"

    show rs_image_34EA3FF6756742B9B40F0095C34BB921 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "要是有我很熟悉的可爱的后辈的加油的话说不定能有点自信呐～"

    show rs_image_33DAA2B0F1C244C4B2C872213860A04A as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "别撒娇了。"

    show rs_image_9DE3C45471674FB8B7109B7FD4C19C25 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "切……明白了。我会自行处理的。再怎么说，也是我最后一次机会了。"

    show rs_image_A55765D64B69474CB7292398EDD238EB as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "啊～啊。不过，果然还是有点后悔呐。{w}你肯定没问题的，要珍惜现在。"

    show rs_image_DD649A23A0C54C3B99DE6AF655696477 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "……是。我会照做的。"

    show rs_image_758CA32B10AD4D749FA2D5D577EDF989 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "嗯。那我要继续练习了。"

    show rs_image_33DAA2B0F1C244C4B2C872213860A04A as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "……"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_34F5B1EB5D2E4F4396E2FBC2BAFBEAA1 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    show rs_image_3F84B60D1FD24C9CAD32F21E89A94324 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "……前辈！"

    rs_character_193BCCFE681D42C8993A47A884FF2200 "嗯？"

    show rs_image_DD649A23A0C54C3B99DE6AF655696477 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "……我、和所有部员，都会支援熟练的一方出席大赛。\n"
    show rs_image_3F84B60D1FD24C9CAD32F21E89A94324 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "为了胜利。"

    show rs_image_9DE3C45471674FB8B7109B7FD4C19C25 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "嗯，当然的。"

    rs_character_EA9AA88E88D84B559B925363E2931756 "但是，我……"
    show rs_image_64FE521C7CFC4339B609B88E4AE9FFFB as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "……我想和前辈一起。\n"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_8B5E09CB821B48C29590BEFB90AE0DDB as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……再见！{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    show rs_image_34F5B1EB5D2E4F4396E2FBC2BAFBEAA1 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    extend ""

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_34F5B1EB5D2E4F4396E2FBC2BAFBEAA1 as tag_923338EC67B148CE944D61C9091B72C5 at center_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_193BCCFE681D42C8993A47A884FF2200 "欸，啊，回来佐藤！！"

    show rs_image_9DE3C45471674FB8B7109B7FD4C19C25 as tag_923338EC67B148CE944D61C9091B72C5 zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_193BCCFE681D42C8993A47A884FF2200 "……{w}谢了。"

    window hide

    pause 0.8

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_923338EC67B148CE944D61C9091B72C5
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7962041686F34839A342E7B6E33F2B84 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1.4

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    stop music fadeout 4
    $ sys_music_current_file = ""

    pause 4

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 1

    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.4

    window show

    rs_character_776382753FF149B49443F348F4356521 "试音会的结果，{w}这次负责钢琴部分的是……"

    window hide

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_923338EC67B148CE944D61C9091B72C5 = 200
    show rs_image_F33DA7B19039419089D2B31DD1FAE879 as tag_923338EC67B148CE944D61C9091B72C5 at right_top zorder zorder_tag_923338EC67B148CE944D61C9091B72C5 onlayer master
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    hide tag_923338EC67B148CE944D61C9091B72C5
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    pause 5

    if sys_effect_current_file != "sound/Effect Sound/Clap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Clap 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_510ED9F495254C89972BC4C1C431D966 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_673B577A4E15407397C9C9B62906A309

    $ renpy.pause(2.0, hard=True)

    $ zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD = 300
    show concert_description (_("12号节目\n御咲学园初中部吹奏乐部\n指挥：平井 米")) as tag_0BDB8A4A05BB44ED81AE140BE96066BD at Transform(xpos=677,ypos=158,xanchor=1.0) zorder zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD onlayer master
    with rs_effect_AE78B5E92416464A93F1A10BE1C93CE6

    $ renpy.pause(1.0, hard=True)

    $ zorder_tag_03723FC929AD4F0BA44259F7A076ADFD = 300
    show concert_description (_("♪ 指定曲目\n三号曲\n♪ 自由演奏\nRhapsody for Concert Band and Jazz Ensemble\nComposer: Patrick Williams")) as tag_03723FC929AD4F0BA44259F7A076ADFD at Transform(xpos=677,ypos=285,xanchor=1.0) zorder zorder_tag_03723FC929AD4F0BA44259F7A076ADFD onlayer master
    with rs_effect_AE78B5E92416464A93F1A10BE1C93CE6

    $ renpy.pause(4.5, hard=True)

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_0BDB8A4A05BB44ED81AE140BE96066BD
    hide tag_03723FC929AD4F0BA44259F7A076ADFD
    with rs_effect_673B577A4E15407397C9C9B62906A309

    $ renpy.pause(1.5, hard=True)

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_418B7345B9854BA0B93A4CBBA12BAE8E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ renpy.pause(1.5, hard=True)

    show rs_image_8EF12B9EF1EB482A96213CEB566AAA47 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ renpy.pause(1.5, hard=True)

    show rs_image_CA830C5BFF094868BD5D4E1AF370A76A as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ renpy.pause(2.5, hard=True)

    if sys_effect3_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march Concert 5.png
    $ zorder_rs_image_41428618BA4343D9B122066AD821CA68 = -100
    show rs_image_41428618BA4343D9B122066AD821CA68 as rs_image_41428618BA4343D9B122066AD821CA68 zorder zorder_rs_image_41428618BA4343D9B122066AD821CA68 onlayer master
    hide rs_image_41428618BA4343D9B122066AD821CA68

    show rs_image_41428618BA4343D9B122066AD821CA68 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    $ renpy.pause(3.0, hard=True)

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_B6D2CFDC1CB5407EACD7FBC1D100D198

    $ renpy.pause(3.0, hard=True)


    if judge_lm_condition([]):
        jump block_00003FA7

    return

label block_00003FA7:
    # Node: 00003FA7 (變革進行曲 岡島 END 2)
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_75A864E3BFC9426C817C95EDE531DCA5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EF2D3A4912BA490B9BDDB92C8700586E

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.4

    if sys_music_current_file != "sound/Piano/sti_gymno_01_pi.ogg":
        play music "sound/Piano/sti_gymno_01_pi.ogg" loop
        $ sys_music_current_file = "sound/Piano/sti_gymno_01_pi.ogg"

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么样！？怎么样！？我们部很厉害对不对！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_0082B8EA494C49D7B202B0DC39D7AC3F as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "超级棒哦～！！大家都超帅的哦！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_4BBDCD83023642F6923D76BE102A1BB9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "演奏乐器的男孩子也好吸引人呐！\n眼睛也是，耳朵也是，心灵也是，都被灌满了～"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_AD84853E028D4D33B3C789E264354AE3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我还是第一次听音乐听到这么痛快。\n"
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过，我还是想在舞台上看到友。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_A2534044EF094540BC82F97E1E03D950 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜～我也是。为什么会是那个坏心眼的前辈负责钢琴部分……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_89D53127B93243A194D7108DECE8802F as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……吹奏乐部的大家创造的时间就在梦里过去了……"

    show rs_image_460C6B5F6FA34A3E939381F99A268C0E as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "真是的～哥哥，难得幸福的时候，太浪费了。"

    show rs_image_63B7FCD9DF38442BA0683EF60F550969 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君也辛苦了！吹奏乐部的练习真的非常辛苦呐。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈～谢谢！"
    show rs_image_350F6A2B48EE49C8B631CE0B02F5BC2C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "没能出席大赛很遗憾，\n但我也毫不后悔。"

    show rs_image_07E85511B35D42B2A68B24FACDB172AB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不管我还是前辈还是大家，\n全都拿出最高水准带来的就是这次演奏哦。这可是最棒的一次哦。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦！友亲！好帅哦！"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "很伟大呐。"

    window hide

    pause 0.6

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_28CB16F81175458EA97C8F0250448304 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 0.6

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这样社团生活也结束了呐。{w}说长不长说短不短。"

    pause 0.4

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.5

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_02AF4E98AE404A37BBF5189D1BD66AE6 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_48394E3397A94AD090308D24BFC677E3 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "诶，要退出吹奏乐部？"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "趁这个机会直接入部不是很好吗？"

    show rs_image_39EA77FDE17745CA860489ACA0F6FAFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不——要。对我来说难度太高了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_EFDC09B34577437A8D2B581A3FFFC9E4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "因为啊，每天都要忙死了，连那个的时间都没有了。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_022781101FD04002AB8C506EED9156F2 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊啦，友亲，难道最近完全没做过！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯。只能计划一下～"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_332D35DF942A4E11AF6CD9B932EC0FD0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "是、是这样……\n"
    show rs_image_3C4C246AAFC1459DBB1711584019784D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那个，可以的话，{w=0.7}{nw}"
    show rs_image_4195495DF15242A7A0EB7645DFF83377 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "{size=12}请使用我……{/size}"

    show rs_image_D5EEA08F613D4581B90B56569FE7A25D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "就算不那样你也不完全认真，这么下去记得要努力学习啊。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_022781101FD04002AB8C506EED9156F2 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_C528CA6C6F534006B6F789027BE5C781 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嘛，关于那个，两边同时都处理好不可能的！\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_35B9BEFBF42E474DB41387E9345C36B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我的情况只有学习是不行的……"

    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "最近上课也一直在发呆呐。{w}不过，这样真的可以吗？"

    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯。和学习不对口。\n下去我觉得自己总有一天会倒在什么地方的。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_3C4C246AAFC1459DBB1711584019784D as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君的话肯定能发现其他想做的事情的！"

    show rs_image_350F6A2B48EE49C8B631CE0B02F5BC2C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谢谢。我也会好好寻找的。\n"
    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不过，理由其实还有一个……"

    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我……{w}{w=0.4}{nw}"
    stop music fadeout 1
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    pause 0.5

    extend "我还想和以前一样，\n一直和大家在一起优哉游哉地过！！{nw}"
    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg"

    extend ""

    pause 0.3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_4D5E70DCADBB4F2CA52AB49DED72D7C5 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "森海……"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不是说，最重要事物只有失去时才会发觉吗。\n我已经觉得自己和大家相处的时间被夺走了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那段时光对我来说是最重要最重要的，是能让我保持自我不可或缺的部分。"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_48394E3397A94AD090308D24BFC677E3 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君……"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "所以，我，我要回到大家的身边。{w}\n{w=0.3}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 400
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.3

    extend "今后也要多多指教哦，大家！"

    pause 0.3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "没问题没问题！既然如此干脆来花乃汤来一场接风晚会如何！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_6EA040B97356486ABE5FD91F92B543D2 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真的！？哇——！太好了！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_E683F1ECE3314055A6535AFF3A0F039A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "泡一下澡好好释放疲劳感也好。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "感到疲劳时花乃汤真是乐园呐！"

    show rs_image_ECD1914DBFDB442F9D1A9232EEEC99F6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那和大家一起，友。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C98211B62EA04A368AA5021885891661 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_3C4C246AAFC1459DBB1711584019784D as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！！"

    window hide

    pause 0.8

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_28CB16F81175458EA97C8F0250448304 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 2.5

    stop music fadeout 3.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 3

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Night insect 1.ogg"

    if sys_music_current_file != "sound/BGM/The end of touch.ogg":
        play music "sound/BGM/The end of touch.ogg" loop
        $ sys_music_current_file = "sound/BGM/The end of touch.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_53C43FF5997344BAAADBDF967F5E5DBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 2

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    show rs_image_5166E18B6C574BE88E2D3502DE66EEE1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 1.4

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_0E33317BD10F4802A1BBA74E011540E0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.6

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C4369F858E3847C6B9D9C068D790A539 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_46DDAF6679B74E91A5B97B3A594DC6DC as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 1.1

    show rs_image_42421C2C4C6D412D8FF7B0868729FECE as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.5

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 1.5

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2D20A6A6A8B640AD98E331EA33CE190F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B1E776E59E0F4078A22BEFCAB3389387

    pause 1.1

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0082B8EA494C49D7B202B0DC39D7AC3F as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.7

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1CDBF9A281F54418A7363E36408C7DD5 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.7

    show rs_image_350F6A2B48EE49C8B631CE0B02F5BC2C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E3D2D87C0D4C4A54B7016B01E2AC7D10 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.7

    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6A862C1FCD4240298711F04F27EDD9E0 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.7

    show rs_image_6EA79B30E52B4FE8B90AB55D569F24D3 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F3888CA89DF4DDEB58EC097C79B8FC0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 1.1

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 400
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_24B3A49A9E5E4F6283DD3ADAF445EC35 = 200
    $ zorder_tag_AE869ABB24B64F159CF5594FFE2D849D = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at Transform(xpos=80, yalign=0.0) zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    show rs_image_8C106322A86B43E599BD9F3A2962F305 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=230, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_24B3A49A9E5E4F6283DD3ADAF445EC35 at Transform(xpos=370, yalign=0.0) zorder zorder_tag_24B3A49A9E5E4F6283DD3ADAF445EC35 onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_AE869ABB24B64F159CF5594FFE2D849D at Transform(xpos=-180, yalign=0.0) zorder zorder_tag_AE869ABB24B64F159CF5594FFE2D849D onlayer master
    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=500, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    hide tag_AE869ABB24B64F159CF5594FFE2D849D
    hide tag_24B3A49A9E5E4F6283DD3ADAF445EC35
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 1.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2D20A6A6A8B640AD98E331EA33CE190F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_6EA040B97356486ABE5FD91F92B543D2 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_top zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……（狼吞虎咽）花乃汤的关东煮真是太赞了。{w}\n不过吃不了这么多～（狼吞虎咽）……♪"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 200
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_CA176C5A71144199A2E3AE0C60846C57 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at right_top zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼，哈哈。"

    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怎么了，友。"

    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "总觉得，回到该回来的地方了呐。真的好开心。"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是吗。"
    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "又回到原来那个懒散愚笨的友了啊。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_A6E70EA9F30F4DE4AD20434ED388ACFF as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么嘛——已经成长了，不会再出现懒散的友了！"

    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那还真是值得期待。\n"
    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……欢迎回来，友。"

    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……我回来了。\n"
    show rs_image_39EA77FDE17745CA860489ACA0F6FAFC as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "今后也要在一起哦，忍。"

    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这是我的台词。"

    window hide

    pause 0.8

    # Gallery unlock: images/CG/Revolution-march/Revolution-march OkajimaEND 1.png
    $ zorder_rs_image_8FD417243BAF49B6840F3190C65AA4E5 = -100
    show rs_image_8FD417243BAF49B6840F3190C65AA4E5 as rs_image_8FD417243BAF49B6840F3190C65AA4E5 zorder zorder_rs_image_8FD417243BAF49B6840F3190C65AA4E5 onlayer master
    hide rs_image_8FD417243BAF49B6840F3190C65AA4E5

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_8FD417243BAF49B6840F3190C65AA4E5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.8

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……哈，说起来真的好好吃呐，关东煮……{w}哈……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march OkajimaEND 2.png
    $ zorder_rs_image_4C236CF15FAB471C978461AE1AFB0117 = -100
    show rs_image_4C236CF15FAB471C978461AE1AFB0117 as rs_image_4C236CF15FAB471C978461AE1AFB0117 zorder zorder_rs_image_4C236CF15FAB471C978461AE1AFB0117 onlayer master
    hide rs_image_4C236CF15FAB471C978461AE1AFB0117

    show rs_image_4C236CF15FAB471C978461AE1AFB0117 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……唔。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为、什么？会……{w}唔……{w}好奇怪……{w}呜呜呜呜～！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……？怎、怎么了？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……没……"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Revolution-march/Revolution-march OkajimaEND 3.png
    $ zorder_rs_image_C57B8F2A70644733BB36E8DA3C8F5B9A = -100
    show rs_image_C57B8F2A70644733BB36E8DA3C8F5B9A as rs_image_C57B8F2A70644733BB36E8DA3C8F5B9A zorder zorder_rs_image_C57B8F2A70644733BB36E8DA3C8F5B9A onlayer master
    hide rs_image_C57B8F2A70644733BB36E8DA3C8F5B9A

    show rs_image_C57B8F2A70644733BB36E8DA3C8F5B9A as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    pause 0.4

    extend "{size=28}呜啊啊啊啊！！\n呜哇啊啊啊啊！！！{/size}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……{w}……{w=0.6}你真的很努力了，就算很不甘心……{w}\n乖，大家都在你身边，已经不会有事了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=28}呜啊啊啊啊啊啊！！！{/size}{w}\n{size=28}呜……啊啊啊啊啊！！{/size}"

    window hide

    pause 1.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    call scb_flag_title_end(3, _("「变革进行曲」")) from _call_scb_flag_title_end_4

    if judge_lm_condition([]):
        jump block_00003FA3

    return

