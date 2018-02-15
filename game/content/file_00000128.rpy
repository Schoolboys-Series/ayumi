# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00000128 (CP1 Opening Celemony)

label block_00000129:
    # Node: 00000129 ()
    $ C0SShinobuState = 0
    $ IsSchoolhouseArrived = False
    $ IsAtriumArrived = False
    $ IsSchoolDoorArrived = False
    $ IsShoeCupboardArrived = False

    if judge_lm_condition([]):
        jump block_000038F5

    return

label block_000038F5:
    # Node: 000038F5 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_23

    if judge_lm_condition([]):
        jump block_00000796

    return

label block_00000796:
    # Node: 00000796 (Opening celemony)
    $ set_window("イベントモード")
    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    show center_title (_("2eme Gymnopédie\n呈  献")) as gymno_title:
        alpha 0.0
        linear 1.0 alpha 1.0
        pause 5.5
        linear 1.5 alpha 0.0

    pause 1.5

    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_7A0224DB2C384755BF67935D5C9F432F

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    pause 2

    show rs_image_5013EC64CA634A9E9754EF6FE927CCD2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    show rs_image_AC1A95BA21694004A67885C809E98CFF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    if sys_music_current_file != "sound/BGM/Chapter 3.ogg":
        play music "sound/BGM/Chapter 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 3.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Class bell 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 0.7

    window show

    pause 0.4

    window show

    hide gymno_title

    rs_character_F1F8F8B6C0BC4143AA96964050DAC24E "全校学生们，大家好。"

    window hide

    pause 0.4

    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.5

    window show

    rs_character_F1F8F8B6C0BC4143AA96964050DAC24E "炎热漫长的暑假已然结束，终于第二学期也要开始了。"

    window hide

    pause 0.5

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 100
    show rs_image_9C291073B0E14AC7BABB30C07BB5205D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at left_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 0.8

    window show

    # Gallery unlock: images/CG/Opening celemony/Opening celemony 3.png
    $ zorder_rs_image_8311E1236AED463A9358E6303D1D2F5C = -100
    show rs_image_8311E1236AED463A9358E6303D1D2F5C as rs_image_8311E1236AED463A9358E6303D1D2F5C zorder zorder_rs_image_8311E1236AED463A9358E6303D1D2F5C onlayer master
    hide rs_image_8311E1236AED463A9358E6303D1D2F5C

    $ zorder_tag_C35197E0A50A470FA7C5D15E6DAEFAA0 = 0
    show rs_image_8311E1236AED463A9358E6303D1D2F5C as tag_C35197E0A50A470FA7C5D15E6DAEFAA0 at center_bottom zorder zorder_tag_C35197E0A50A470FA7C5D15E6DAEFAA0 onlayer master
    show rs_image_246166525FD449B09D87DE661DFC870E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.4

    rs_character_F1F8F8B6C0BC4143AA96964050DAC24E "今年夏天气温又拔新高，大家过得如何？"

    rs_character_F1F8F8B6C0BC4143AA96964050DAC24E "我忠实希望大家互相都度过了一个有意义的夏天。"

    window hide

    pause 0.3

    # Gallery unlock: images/CG/Opening celemony/Opening celemony 4.png
    $ zorder_rs_image_84E3A40E55C74C5C9B705CF5E3FE58A1 = -100
    show rs_image_84E3A40E55C74C5C9B705CF5E3FE58A1 as rs_image_84E3A40E55C74C5C9B705CF5E3FE58A1 zorder zorder_rs_image_84E3A40E55C74C5C9B705CF5E3FE58A1 onlayer master
    hide rs_image_84E3A40E55C74C5C9B705CF5E3FE58A1

    show rs_image_84E3A40E55C74C5C9B705CF5E3FE58A1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.6

    window show

    show rs_image_97EBCB09C7D34DE5B0AD380270B93CEB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.4

    rs_character_F1F8F8B6C0BC4143AA96964050DAC24E "当然，我对于所有人都平平安安地于今天站在这里\n迎接新学期表示欣慰。"

    rs_character_F1F8F8B6C0BC4143AA96964050DAC24E "那么，对于三年级的学生，这个第二学期是你们\n用来决定自己未来的重要的时间…………"

    window hide

    pause 0.4

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C35197E0A50A470FA7C5D15E6DAEFAA0
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    # Gallery unlock: images/CG/Opening celemony/Opening celemony 5.png
    $ zorder_rs_image_87A38905C919455BB6D35DB596394AC9 = -100
    show rs_image_87A38905C919455BB6D35DB596394AC9 as rs_image_87A38905C919455BB6D35DB596394AC9 zorder zorder_rs_image_87A38905C919455BB6D35DB596394AC9 onlayer master
    hide rs_image_87A38905C919455BB6D35DB596394AC9

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_87A38905C919455BB6D35DB596394AC9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.8

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼——呼——"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈，猫山，快看那个。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "ZZZ……{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "嗯？怎么了怎么了？"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "不得了，站着就睡着了。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Opening celemony/Opening celemony 6.png
    $ zorder_rs_image_691F32B0298245DE8278009B3F9589BE = -100
    show rs_image_691F32B0298245DE8278009B3F9589BE as rs_image_691F32B0298245DE8278009B3F9589BE zorder zorder_rs_image_691F32B0298245DE8278009B3F9589BE onlayer master
    hide rs_image_691F32B0298245DE8278009B3F9589BE

    show rs_image_691F32B0298245DE8278009B3F9589BE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.3

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "……呃，穗海，你难道想……"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}啪嚓！！{/size}"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_24188CBA120A4166B08F8A3535548A8D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔呀！！？？"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_7C7F47B899A04C1E9877716E2B4CC7B5 "{size=32}！？！？{/size}"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_177F59374F16409DB2C167CEC51615A0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "呼——呵呵呵……！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_A48E3C15AF6146FA91F9AD97CAF30F5C as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗯？发生什么了？"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_1439FC37B6EB4D19A2C3CA56559E02E4 as tag_724406A84D7141298EFF0D864FAE1534 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "……某种意义上被救了一命啊，猫山。"

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_59759FB9DA7E42C1AE0F25BD7F9EB4B2 as tag_2C4A74BADF6540698EF3E9A300893D1A at Transform(xpos=-130, yalign=0.0) zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_FB2D1F0CA559413E9A783A63C89DF060 as tag_CC4336DE74164173AC47C2C317367F10 at Transform(xpos=90, yalign=0.0) zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    show rs_image_B5266B4702AD4685B763598227C3363A as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at Transform(xpos=300, yalign=0.0) zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    show rs_image_08917E60F7E24896AA5D34106EADD613 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=470, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    rs_character_7C7F47B899A04C1E9877716E2B4CC7B5 "发、发生什么了？{w}\n好像后面发生什么事了。{w}\n会被老师骂的哦——"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_196DD7AD90A44808BDEE6497906554C9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸……这是什么地方？我又是谁？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DDCF28CD404544018157C723EF785904 as tag_061CD0864C4E48C0B3AA935440B7C90D at right_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "森……海……！！"

    window hide

    pause 0.3

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect2_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shock 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    window show

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "{size=40}等会给我过来——！！！！{/size}"

    window hide

    pause 1.5

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 0.5

    image op_movie = Movie(channel="movie_main", play="movie/op.mpg", size=(800, 600))

    show op_movie at Transform(xalign=0.5, yalign=0.5) as op_movie

    pause 77.5

    hide op_movie

    if judge_lm_condition([]):
        jump block_000011A7

    return

label block_000011A7:
    # Node: 000011A7 (After celemony)

    pause 1.5

    $ set_window("イベントモード")
    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5

    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_952D06E912C54776B1C4F5BB577DFB95 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_08917E60F7E24896AA5D34106EADD613 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哦……唔哦……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "别再怪叫了。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哦……可是……"

    show rs_image_7D82F0AC87B944F387E87AC4C14DE788 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "本来错就在友，谁让你睡过去的。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "行了，快去找老师，记得被好好修理一顿哦。"

    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……忍……"

    show rs_image_7780BD482A234B81970D2A4B4EE70A97 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯？先说好，我可不会陪你去的。{w}\n自己一个人去就行了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "无情小人！什么嘛什么嘛！我们可是青梅竹马的！\n对我好一点又能怎么样嘛！"

    show rs_image_BA68039D702C4EA2A6CF95AF1F2E9D2E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是是，请走好。"

    window hide

    pause 0.6

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.9

    $ set_place_title(_("体育馆前"))
    pause 0.5

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    $ set_window("(標準)")
    if sys_effect_current_file != "sound/Effect Sound/Start 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Start 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Start 1.ogg"

    $ zorder_tag_19574BB6F1EA4B9398A6E58989D99A66 = 500
    show rs_image_BBC08FE81C4D4D4880E65137C1106107 as tag_19574BB6F1EA4B9398A6E58989D99A66 at center_bottom zorder zorder_tag_19574BB6F1EA4B9398A6E58989D99A66 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause

    show rs_image_548A86F86BBF4C03947CB8C3753B9DF8 as tag_19574BB6F1EA4B9398A6E58989D99A66 zorder zorder_tag_19574BB6F1EA4B9398A6E58989D99A66 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause

    hide tag_19574BB6F1EA4B9398A6E58989D99A66
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_0000013A

    return

label block_0000013A:
    # Node: 0000013A (Gym outside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (384, 208),"image": "images/Prologue/Menu/Shinobu.png","hover": "images/Prologue/Menu/Shinobu hover.png","name": "しのぶ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_704
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" },{ "scope": 1, "content": "C0SShinobuState == 0" }]):
        jump block_0000079D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000007AE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000012A

    return

label block_0000079D:
    # Node: 0000079D (忍1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_5028F6B94B4B4BC883B88492AB07115E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "快点去老师那里吧。{w}应该就和往常一样，\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "正在{color=#008CFF}鞋箱{/color}那里等你。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002AE5

    return

label block_00002AE5:
    # Node: 00002AE5 (C0S忍)
    $ C0SShinobuState = C0SShinobuState + 1
    if C0SShinobuState == 2:
        $ C0SShinobu = True

    if judge_lm_condition([{ "scope": 0, "content": "C0SShinobu == False" }]):
        jump block_0000013A
    if judge_lm_condition([]):
        jump block_00000851

    return

label block_00000851:
    # Node: 00000851 (Gym outside empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_705
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000012A

    return

label block_0000012A:
    # Node: 0000012A (School outside)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([{ "scope": 0, "content": "C0SShinobu == True" }]):
        jump block_000007A9
    if judge_lm_condition([]):
        jump block_000018B3

    return

label block_000007A9:
    # Node: 000007A9 (With 忍)
    $ sys_ayumi_global_map_character = "tomo_shinobu"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_000007A8

    return

label block_000007A8:
    # Node: 000007A8 (School outside XCTX)
    if judge_lm_condition([{ "scope": 1, "content": "C0SShinobu == True" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_0000239C", target_label="block_000007AA") from _call_scb_global_map_168
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_000007AC", target_label="block_000007AA") from _call_scb_global_map_169
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00000138
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_0000013C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" },{ "scope": 1, "content": "C0SShinobu == True" },{ "scope": 2, "content": "IsAtriumArrived == False" }]):
        jump block_000007A5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" }]):
        jump block_0000013E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" },{ "scope": 1, "content": "C0SShinobu == True" },{ "scope": 2, "content": "IsSchoolhouseArrived == False" }]):
        jump block_00002399
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_00000140
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" },{ "scope": 1, "content": "C0SShinobu == True" },{ "scope": 2, "content": "IsSchoolDoorArrived == False" }]):
        jump block_000007A6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_00000142
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_000007A8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_000007AA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_000007A8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C0SShinobu == True" }]):
        jump block_0000239C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000007AC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" },{ "scope": 1, "content": "C0SShinobu == True" }]):
        jump block_00001FE5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FE4

    return

label block_00000138:
    # Node: 00000138 (Gym outside)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C0SShinobu == True" }]):
        jump block_00000851
    if judge_lm_condition([]):
        jump block_0000013A

    return

label block_0000013C:
    # Node: 0000013C (Shoe cupboard)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("鞋箱"))
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "IsShoeCupboardArrived == False" }]):
        jump block_00002ADF
    if judge_lm_condition([]):
        jump block_0000013D

    return

label block_00002ADF:
    # Node: 00002ADF (Tutorial)
    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Start 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Start 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Start 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 500
    show rs_image_B7FEABA6D36143BC937D839859DE1FF9 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B


    if judge_lm_condition([]):
        jump block_00002AE9

    return

label block_00002AE9:
    # Node: 00002AE9 (Set: Arrived)
    $ IsShoeCupboardArrived = True

    if judge_lm_condition([]):
        jump block_0000013D

    return

label block_0000013D:
    # Node: 0000013D (Shoe cupboard)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (160, 96),"image": "images/MENU/Nameko point.png","hover": "images/MENU/Nameko hover.png","name": "滑子"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_706
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003647
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" }]):
        jump block_00001F22

    return

label block_00003647:
    # Node: 00003647 (TO: School outside)

    if judge_lm_condition([]):
        jump block_00003646

    return

label block_00003646:
    # Node: 00003646 (TO: School outside)

    if judge_lm_condition([]):
        jump block_0000012A

    return

label block_00001F22:
    # Node: 00001F22 (Next: 滑子)
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 200
    show rs_image_D7F70E4230154502BB28D6BA8AC09D91 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_1557B4E76EEC4D0E8F827C8C42924E5F as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "哦，来了啊，森海。\n真是的，你怎么老是这么能作！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜、唔。非、非常抱歉……"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 500
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 2

    if sys_effect3_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Stupid 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4E68A2DC06DC4980B15518EDB26D1FCD as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.5

    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "……要说的就这些。以后给我好好注意！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D7F70E4230154502BB28D6BA8AC09D91 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "你可以回去了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……我回去了。"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1557B4E76EEC4D0E8F827C8C42924E5F as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "先别，先等等。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "等下有时间再来我这。有话和你说。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸欸！？"

    if sys_effect_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（我难道又做错什么了？暑假作业记得好好做了啊……）"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（读后感确实抄了网上一点……）"

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9C78AB751CDB49FDA83251FA5B4A3825 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "明白了没？记得过来。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫、噫！我明白了……"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("鞋箱"))
    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ set_place_title("")
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    $ set_window("イベントモード")
    pause 2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EF2D3A4912BA490B9BDDB92C8700586E

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_952D06E912C54776B1C4F5BB577DFB95 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_04B589B0BDD948F4BB727589A05C0593 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "新学期刚开始就这么累，真辛苦你了呐。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜——已经受不了了——"

    show rs_image_3938BA4DFD63427F90A7EFC10C734A7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "肯定现在其他年级的人也在互相传。\n比如“那个二年级的逊毙了”。"

    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜。"

    show rs_image_04B589B0BDD948F4BB727589A05C0593 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这也是个好机会，学着正经些。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_3CC2CAAD5140495DAF5927162F832557 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "在这个九月到十二月的第二学期里，\n友的脚{color=#00FFFF}『步』{/color}到底能收获多少{color=#00FFFF}『成果』{/color}……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3938BA4DFD63427F90A7EFC10C734A7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "真令人期待呐。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_CC45620E61634BCBAE100C11F0CF029B as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w}{w=0.6}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    # Gallery unlock: images/CG/Tomo+Shinobu.png
    $ zorder_rs_image_03C9EB10B8D14965A3E4A9225ACC9C39 = -100
    show rs_image_03C9EB10B8D14965A3E4A9225ACC9C39 as rs_image_03C9EB10B8D14965A3E4A9225ACC9C39 zorder zorder_rs_image_03C9EB10B8D14965A3E4A9225ACC9C39 onlayer master
    hide rs_image_03C9EB10B8D14965A3E4A9225ACC9C39

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_03C9EB10B8D14965A3E4A9225ACC9C39 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.4

    extend "DUANG！！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "好痛！突然做什么呐！？"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_26ACCF5B48104DD4A398798576538F0E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……没什么。"

    window hide

    pause 0.8

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ set_place_title(_("图书馆"))
    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_507130D7BD574651B179D6DEF2CE814D = 400
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_A0865A4919654F2FA70BEFCC3EE452F9 as tag_507130D7BD574651B179D6DEF2CE814D at center_bottom zorder zorder_tag_507130D7BD574651B179D6DEF2CE814D onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_ADE5E94328D840D6AA5ABB480FF9F454 as tag_507130D7BD574651B179D6DEF2CE814D zorder zorder_tag_507130D7BD574651B179D6DEF2CE814D onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 2

    $ set_window("(標準)")
    hide tag_507130D7BD574651B179D6DEF2CE814D
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.6

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    pause 0.6

    $ set_window("(標準)")
    if sys_effect_current_file != "sound/Effect Sound/Start 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Start 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Start 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 500
    show rs_image_39791F37FDC447AABBB79924E859FEC6 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause

    show rs_image_AABABF0A10564F908EBE34524FE0C279 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B


    if judge_lm_condition([]):
        jump block_0000239E

    return

label block_0000239E:
    # Node: 0000239E (Library 忍 flag)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 1/Menu/Shinobu flag.png","hover": "images/Chapter 1/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_707
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003990
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000023A2

    return

label block_00003990:
    # Node: 00003990 ()
    $ del C0SShinobuState
    $ del IsSchoolhouseArrived
    $ del IsAtriumArrived
    $ del IsSchoolDoorArrived
    $ del IsShoeCupboardArrived

    return

label block_000023A2:
    # Node: 000023A2 (F1: 忍)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1BB16A3232D24A24A336EB3F36D6DBE2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_53AE820BA9E64560B2C6D962DEE9DD33 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说起来\n"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#0080FF}加藤君{/color}……同班的加藤君\n好像在{color=#008080}校庭{/color}里烦恼什么的样子。"

    show rs_image_A68F7C05F10E4C54B48181328DBE7E00 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "和他谈过一次，但听不明白他想表达什么意思……"

    show rs_image_8468BF81A4B147BCB4EA3E30BCD79AD5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "稍后友也去和他谈谈。拜托了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([]):
        jump block_00002AEA

    return

label block_00002AEA:
    # Node: 00002AEA (Phase ++)
    $ C1S1Phase = C1S1Phase + 1

    if judge_lm_condition([]):
        jump block_000023A3

    return

label block_000023A3:
    # Node: 000023A3 (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#008000}事件{/color}{color=#0080FF}。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_000023A5

    return

label block_000023A5:
    # Node: 000023A5 (Library 忍 waiting)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 1/Menu/Shinobu waiting.png","hover": "","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_708
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_000023A6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003990

    return

label block_000023A6:
    # Node: 000023A6 (Waiting: 忍)
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#008000}事件{/color}{color=#0080FF}。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_000023A5

    return

label block_000007A5:
    # Node: 000007A5 (Atrium +忍)
    $ set_window("イベントモード")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_1C428704E5E24078848D388A31B861CE
    $ set_place_title("")

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_324C77394BC349DB995FB24E2E90630F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.4

    window show

    show rs_image_04B589B0BDD948F4BB727589A05C0593 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "大家——胆小鬼友君大驾光临了哦——"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "等等——！不要告诉大家——！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_267C8602F530483FA102DC018C0FEB3C as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_7F82DC1BF57341ADA2F9927A97B25BDF as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_3D6A04F77BD14290ACB4CB84A6D7781B as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯？怎么回事？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_2304A61C05D54DD6B9E15DDB5A3D3949 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "恐怕是{w=0.45}\n『马上就要去老师那里挨训了可一个人好可怕，忍君也要陪我啦——』"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "就是这么回事？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_04B589B0BDD948F4BB727589A05C0593 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "完全正确。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜呜……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_267C8602F530483FA102DC018C0FEB3C as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_7F82DC1BF57341ADA2F9927A97B25BDF as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_73F69A7FB68D4D8684029D4486A79854 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "慎酱好厉害。"

    show rs_image_04CE6801CFBD460096381A21558DE1D7 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "森海真是会撒娇呐。\n说起撒娇，过去空晚上一个人去厕所的时候……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F0389DE75D7842F8AF7B3DE016346359 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哇——！！不要听——！！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_FD97A7AC280A4AA68D0BEDD058C5C756 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "恐怕是{w=0.45}\n『哥哥，一个人上厕所好可怕，陪我一起来——』这样的。"

    if sys_effect2_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9B9DCA74086B43A197B7D71BB87CC11D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_D68D83BA2D294524B36FBE62C1A85888 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "最后就在厕所里{color=#FF00FF}哈哈吼吼嘿嘿嘿☆{/color}"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D678A1AE01F94A01BD65060A58998D58 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "怎么可能！！"

    window hide

    pause 0.8

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00002AE7

    return

label block_00002AE7:
    # Node: 00002AE7 (Set: Arrived)
    $ IsAtriumArrived = True

    if judge_lm_condition([]):
        jump block_0000013F

    return

label block_0000013F:
    # Node: 0000013F (Atrium)
    $ sys_lm_menu_item = [{"pos": (136, 144),"image": "images/Prologue/Menu/Shintaro.png","hover": "images/Prologue/Menu/Shintaro hover.png","name": "慎太郎"}, {"pos": (344, 146),"image": "images/Prologue/Menu/Tsuki.png","hover": "images/Prologue/Menu/Tsuki hover.png","name": "月"}, {"pos": (534, 144),"image": "images/Prologue/Menu/Sora.png","hover": "images/Prologue/Menu/Sora hover.png","name": "空"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_709
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003647
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_0000079C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_0000079A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_0000079B

    return

label block_0000079C:
    # Node: 0000079C (慎太郎)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_02FE846751D84256A0FD1890407B87EA as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_20039C19E7B74F99B8FB8542570BB3BE as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "新学期刚一开始就制造笑料了呐，友同学。{w}\n作为横扫无聊假期的新的开始再好不过了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对我来说反而是最糟的开始……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_0000013F

    return

label block_0000079A:
    # Node: 0000079A (月)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_0EBE1029E4FF475191BFB073B7BE4EA5 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_69517DBA32BF4469B148E88230A45AA5 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "森海！新学期刚开始，太不上进了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……对不起。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8FA8A472B85C4BFF9AAF2B9D00DA1DF1 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "算了，拜此所赐，\n{w=0.4}{nw}"
    if sys_effect3_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F55083532FBB4E6FA28BA128771AB1CF as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "至少我睡觉没被发现呐。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……。{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "欸。{w=0.4}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "诶诶——！？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0C73761CD21648FCB039C9F07947C6DA as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "因为森海的英勇就义被拯救到的苍生也是有的。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_0000013F

    return

label block_0000079B:
    # Node: 0000079B (空)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_0C5FFEB2760549C9B7A6F47F83C0B99B as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_4FD63F45394B43A8A80C940FC5FBAAA3 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君，刚才完全被大家注意到了呐。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "吼吼——我的粉丝也会渐渐多起来了呐。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_839C02FE2B4D43A4904A035429979493 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "真、真是杀敌一百自损八千的求关注方法啊……"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_0000013F

    return

label block_0000013E:
    # Node: 0000013E (Atrium)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("中庭"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_0000013F

    return

label block_00002399:
    # Node: 00002399 (Schoolhouse +忍)
    $ set_window("イベントモード")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1.5

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6AB5AA5EB92C42B0B217FDBBA0887900 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_EB5D0582654644B7A76BB509C31DD31E = 200
    $ zorder_tag_E68131B5463148FC8A76A11B96CD1843 = 200
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_EB5D0582654644B7A76BB509C31DD31E at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_EB5D0582654644B7A76BB509C31DD31E onlayer master
    show rs_image_BA68039D702C4EA2A6CF95AF1F2E9D2E as tag_E68131B5463148FC8A76A11B96CD1843 at Transform(xpos=60, yalign=0.0) zorder zorder_tag_E68131B5463148FC8A76A11B96CD1843 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，汪汪。"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_E68131B5463148FC8A76A11B96CD1843
    hide tag_EB5D0582654644B7A76BB509C31DD31E
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=60, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_324C77394BC349DB995FB24E2E90630F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.4

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……？{w=0.4}怎么了？为什么要站在我前面？"

    show rs_image_943958ACE1594083BA9B66D14E70D431 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？可是，忍不是很怕狗吗？"

    show rs_image_5E7D24311EEA4507B1FE775C8265EADA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是么？其实没什么。{w}……以前可能是？"

    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对——对！小时候我不是经常这么做嘛。"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "已经完全习惯了，刚才就像条件反射一样。{w}\n呀～♪真是美妙的友情呐！"

    show rs_image_08917E60F7E24896AA5D34106EADD613 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "好的好的，谢谢。"

    window hide

    pause 0.4

    show rs_image_4CBCF132AF8F49E38C726D5800545B50 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.8

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    $ set_place_title(_("校舍内"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00002AE8

    return

label block_00002AE8:
    # Node: 00002AE8 (Set: Arrived)
    $ IsSchoolhouseArrived = True

    if judge_lm_condition([]):
        jump block_0000239B

    return

label block_0000239B:
    # Node: 0000239B (Schoolhouse +小翼)
    $ sys_lm_menu_item = [{"pos": (384, 168),"image": "images/Menu/Tsubasa-chan CP12.png","hover": "images/Menu/Tsubasa-chan CP12 hover.png","name": "ツバサ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_710
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ツバサ\"" }]):
        jump block_0000239A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003646

    return

label block_0000239A:
    # Node: 0000239A (小翼)
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    show rs_image_83E2064E232640149A12D7598C5FE5C3 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_bottom zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "汪汪♪"

    show rs_image_37DD260DB3B64875AFF0FBF4F01BD3E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（友也真是的，那么久的事情都记得。{w}\n狗什么的现在已经完全不可怕了。）"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（……我还真是，过去原来那么胆小呐。）"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校舍内"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_0000239B

    return

label block_00000140:
    # Node: 00000140 (Schoolhouse)
    if sys_effect_current_file != "sound/Effect Sound/Walk.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("校舍内"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C0SShinobu == True" }]):
        jump block_0000239B
    if judge_lm_condition([]):
        jump block_00000141

    return

label block_00000141:
    # Node: 00000141 (Schoolhouse)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_711
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003646

    return

label block_000007A6:
    # Node: 000007A6 (School door +忍)
    $ set_window("イベントモード")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_177F59374F16409DB2C167CEC51615A0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哟，挺羞耻的呐～"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_376CA53D8BF64CE497CF774B53A38857 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_324C77394BC349DB995FB24E2E90630F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔唔唔～！可恶的技安～！！！{w}都怪他我才会～！！！"

    show rs_image_BA68039D702C4EA2A6CF95AF1F2E9D2E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是什么事？"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "都怪技安把我纤细脆弱的鼻泡戳破才会被这么过分对待的——！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍A梦！！干掉那种坏家伙！！"

    show rs_image_5E7D24311EEA4507B1FE775C8265EADA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯——原来是这么回事啊。{w}{nw}"
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_BA68039D702C4EA2A6CF95AF1F2E9D2E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_6D7AB645F07943258CA77C243D43A748 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……。"

    show rs_image_CAE9E92D7F644421A40585EE4A43F483 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "怎、怎么了啊。有意见么。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if sys_effect3_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_7780BD482A234B81970D2A4B4EE70A97 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，非常感谢。这对友来说会是很好的教训。{w}\n偶尔长长记性也不错。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_952D06E912C54776B1C4F5BB577DFB95 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎、怎么这样～……"

    window hide

    pause 0.8

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    $ set_place_title(_("校门"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00002AE6

    return

label block_00002AE6:
    # Node: 00002AE6 (Set: Arrived)
    $ IsSchoolDoorArrived = True

    if judge_lm_condition([]):
        jump block_00000143

    return

label block_00000143:
    # Node: 00000143 (School door)
    $ sys_lm_menu_item = [{"pos": (128, 248),"image": "images/Prologue/Menu/Tsubasa.png","hover": "images/Prologue/Menu/Tsubasa hover.png","name": "つばさ"}, {"pos": (272, 256),"image": "images/Prologue/Menu/Sakuya.png","hover": "images/Prologue/Menu/Sakuya hover.png","name": "作哉"}, {"pos": (464, 256),"image": "images/Prologue/Menu/Saburo.png","hover": "images/Prologue/Menu/Saburo hover.png","name": "三朗"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_712
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003647
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_00000797
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_00000798
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_00000799

    return

label block_00000797:
    # Node: 00000797 (翼)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_28D96DBE93084DC9AD60894E8FC483ED as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_8093AAE5FCA745689AF6ACB12D446D8D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君……开学典礼上是不能睡觉的……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可是非常想睡嘛。{w}\n啊，说起来，梦里翼君好像也出现了哦……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_FC1EB697877A47FE9D35ED5FD247302D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸、欸！是、是这样吗？\n"
    show rs_image_F5C2E50E1E4840E8BC325EAA4E4AEC7A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那个那个，梦中的我是什么样子的呢？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯——这个——那个——好像……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_2A874B8169574EC78181A7EC6887E271 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "（心跳不止）"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忘记了！"

    if sys_effect2_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_38AA851595944792BBBFDDE6AAD59E92 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "打击……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校门"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000143

    return

label block_00000798:
    # Node: 00000798 (作哉)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_8F8B36DC5AD7424388BA16D0BF2B3B15 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_677582B7E6DD4FF587A19923FF4BF803 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哦，笨蛋来了，笨蛋来了。"

    if sys_effect3_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "技安！！居然敢把我～！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E836DDCE48E14FB9AE7542E0A740122B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "都怪睡觉的那位不好。\n"
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_F15C5D2B15AC488E8A01D7050C63EB5E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "笨蛋、白痴、呆子——♪"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校门"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000143

    return

label block_00000799:
    # Node: 00000799 (三朗)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_66CC7FF4E6344DE0A8CBE2F3E7675375 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好呀——白痴呆毛！"

    window hide

    pause 0.4

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_91A1C69307F54C4B9424B1859222EE6F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊呜。\n好、好了啦猫君！不要每次都拔那里！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "有何不好嘛！不要在意细节。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我还是多亏你得救了呢。\n就当是表示感谢。谢谢你了啊。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "？？"

    window hide

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_place_title(_("校门"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00000143

    return

label block_00000142:
    # Node: 00000142 (School door)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("校门"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000143

    return

label block_000007AA:
    # Node: 000007AA (Target)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『去找滑子老师。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_0000239C:
    # Node: 0000239C (Conversation 忍)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "来，伸直脊背，精神一点。要去老师那里了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好～的……"

    window hide

    $ set_window("(標準)")

    return

label block_000007AC:
    # Node: 000007AC (Conversation)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "新学期才刚刚开始，好麻烦～\n去老师那里之前，\n先到处散散步放松一下心情好了～"

    window hide

    $ set_window("(標準)")

    return

label block_00001FE5:
    # Node: 00001FE5 (Character 友+忍)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_ED234D4517E14A4EB0C635E1C4B85E12
    hide tag_E12C07C263114A53A918CA2B2E9A063D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    return

label block_00001FE4:
    # Node: 00001FE4 (Character 友)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_ED234D4517E14A4EB0C635E1C4B85E12
    hide tag_E12C07C263114A53A918CA2B2E9A063D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    return

label block_000018B3:
    # Node: 000018B3 (Only 友)
    $ sys_ayumi_global_map_character = "tomo"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_000007A8

    return

label block_000007AE:
    # Node: 000007AE (忍2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_1BB16A3232D24A24A336EB3F36D6DBE2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_8468BF81A4B147BCB4EA3E30BCD79AD5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{size=16}（{/size}呜{size=16}——）{/size}"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1BB16A3232D24A24A336EB3F36D6DBE2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w=0.5}{nw}"
    show rs_image_1CCEFF8A5CDB48D1B28051BE030C1663 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……{w=0.5}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F20A8DE0A8E34433BF2171B22A761ADC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    extend "唉……我跟你去。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真的吗？太好了——！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_718B13A73C1D499B8D43BB96215026E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不过，只是到那里之前。{w}不会陪你进去听说教的。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我明白的我明白的！\n那么——Let's Go——！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002AE5

    return

