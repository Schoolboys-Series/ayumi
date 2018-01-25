# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003A0D (FLAG: 傲嬌男孩子的治療法)

label block_00003A0E:
    # Node: 00003A0E ()

    if judge_lm_condition([{ "scope": 0, "content": "VarExists(\"C2S2Phase\") == False" }]):
        jump block_00003A10
    if judge_lm_condition([]):
        jump block_0000426F

    return

label block_00003A10:
    # Node: 00003A10 (Prepare)
    if Not(VarExists("C2S2Phase")):
        $ C2S1Phase = 0
        $ C2S2Phase = 0
        $ C2S3Phase = 0
        $ C2S4Phase = 0
        $ C2S5Phase = 0
        $ C2S6Phase = 0
        $ C2QNewsclubPhase = 0
        $ TalkMatsutaF2 = 0
        $ TalkIzumiF2 = 0
        $ TalkTsukiF2 = 0
        $ TalkKatouF2 = 0
        $ TalkNamekoF2 = 0
        $ TalkShintaroF2 = 0
        $ TalkShinobuF2 = 0
        $ TalkSoraF2 = 0

    if judge_lm_condition([]):
        jump block_0000426F

    return

label block_0000426F:
    # Node: 0000426F (Navigator)

    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase == 99" }]):
        jump block_00003A13
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase == 98" }]):
        jump block_00003A14
    if judge_lm_condition([{ "scope": 0, "content": "C2S2Phase == 97" }]):
        jump block_00003A15
    if judge_lm_condition([]):
        jump block_0000426E

    return

label block_00003A13:
    # Node: 00003A13 (傲嬌男孩子的治療法 2-1)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_9C551C4C1CCA4C6FAF29D7A15E237645 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_E7E6E31C347642E086AADC4895CE778C as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "技安！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "怎、怎么了。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C528CA6C6F534006B6F789027BE5C781 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "和我一起吃午饭！我有很多话要告诉你！跟我来！"

    show rs_image_D3230CCCAA744196B463EF066186F3A0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈？说什么不着边际的话呢。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_253B2776672D49EA928D506D0DCEB77F as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "行了去就是了♪这也是为了你好！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "猫山也是说什……{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    extend "哇、等等！别拉我！住手森海！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_CFCEEA46658B45C38D3ED429DE9FF37D as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "白痴呆毛……真是好人啊。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_16A6E61BE73842BD96D048EA49360C1D "？？？"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    window hide


    if judge_lm_condition([{ "scope": 0, "content": "TalkMatsutaF2 + TalkNamekoF2 + TalkShintaroF2 + TalkSoraF2 > F2PreviousStep" }]):
        jump block_00003A1C
    if judge_lm_condition([]):
        jump block_00003A1B

    return

label block_00003A1C:
    # Node: 00003A1C (Win)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_window("イベントモード")
    pause 0.6

    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    pause 0.4

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 1.png
    $ zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 = -100
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as rs_image_6A16110F14C64AA89B2FAD22D32413C7 zorder zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 onlayer master
    hide rs_image_6A16110F14C64AA89B2FAD22D32413C7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_A0BF18F892C54E3D9D094E5CD477ECEE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 1.png
    $ zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 = -100
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as rs_image_6A16110F14C64AA89B2FAD22D32413C7 zorder zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 onlayer master
    hide rs_image_6A16110F14C64AA89B2FAD22D32413C7

    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_A0BF18F892C54E3D9D094E5CD477ECEE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.9

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1.3

    if sys_effect_current_file != "sound/Effect Sound/Correct 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Correct 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Correct 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_64C987B3866E43999077769BDA7EB8C7 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 1


    if judge_lm_condition([]):
        jump block_00003A1D

    return

label block_00003A1D:
    # Node: 00003A1D (Win 12)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_253B2776672D49EA928D506D0DCEB77F as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好的！技安那家伙，因为我的劝说变得有些动摇了！"

    show rs_image_07E85511B35D42B2A68B24FACDB172AB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "下次也要按这个势头继续！"

    window hide

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    pause 0.8


    if judge_lm_condition([]):
        jump block_00003A32

    return

label block_00003A32:
    # Node: 00003A32 (Phase --)
    $ C2S2Phase = C2S2Phase - 1
    $ F2PreviousStep = TalkMatsutaF2 + TalkNamekoF2 + TalkSoraF2 + TalkShintaroF2

    if judge_lm_condition([]):
        jump block_00003A28

    return

label block_00003A28:
    # Node: 00003A28 ()

    return

label block_00003A1B:
    # Node: 00003A1B (Lose)
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_window("イベントモード")
    pause 0.6

    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    pause 0.4

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 1.png
    $ zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 = -100
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as rs_image_6A16110F14C64AA89B2FAD22D32413C7 zorder zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 onlayer master
    hide rs_image_6A16110F14C64AA89B2FAD22D32413C7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_A0BF18F892C54E3D9D094E5CD477ECEE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 1.png
    $ zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 = -100
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as rs_image_6A16110F14C64AA89B2FAD22D32413C7 zorder zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 onlayer master
    hide rs_image_6A16110F14C64AA89B2FAD22D32413C7

    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_A0BF18F892C54E3D9D094E5CD477ECEE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.9

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1.3

    if sys_effect2_current_file != "sound/Effect Sound/Wrong 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 0
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 1


    if judge_lm_condition([]):
        jump block_00003A1E

    return

label block_00003A1E:
    # Node: 00003A1E (Lose 12)
    $ set_window("イベントモード")
    if sys_effect3_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……反应不太好。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "下次找其他人听听意见好了。"

    window hide

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    pause 0.8


    if judge_lm_condition([]):
        jump block_00003A32

    return

label block_00003A14:
    # Node: 00003A14 (傲嬌男孩子的治療法 2-2)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9C551C4C1CCA4C6FAF29D7A15E237645 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A56A27CF00F74EF798B09E4211817332 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "技安！今天也来嘛。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_F477EFD4F5134EA9A29DCCDC67E15837 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……不了谢谢。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A6E70EA9F30F4DE4AD20434ED388ACFF as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "猫君！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "了解！！"

    show rs_image_BE8486E53367484D8879711D82BE0D21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好了，穗海！别任性了快走！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_70576159A31C474CAECF9B7AFDBBF16F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "从昨天开始你们到底在干什么啊！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    extend "啊……等……放开我！！"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    window hide


    if judge_lm_condition([{ "scope": 0, "content": "TalkMatsutaF2 + TalkNamekoF2 + TalkShintaroF2 + TalkSoraF2 > F2PreviousStep" }]):
        jump block_00003A1C
    if judge_lm_condition([]):
        jump block_00003A1B

    return

label block_00003A15:
    # Node: 00003A15 (傲嬌男孩子的治療法 2-3)
    $ set_window("イベントモード")
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9C551C4C1CCA4C6FAF29D7A15E237645 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_6EA79B30E52B4FE8B90AB55D569F24D3 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "技安！"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.6

    window show

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_E3F6ADD43DE44A428E1224756613C694 "快被调教好了呐。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_710A38AC94C841779DB701B5AC1010FD "说话方式太下流了，变态。"

    show rs_image_F82BC248415F46ACBF47A770CDE09E67 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "嗯？伊藤酱在妄想些什么呐？？\n明明这么可爱，内心真是无比下流呢！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "可、可爱……！{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3B561EDD5FE14AB3949693F15E6C2035 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "乱说什么！扁你哦！！"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    window hide


    if judge_lm_condition([{ "scope": 0, "content": "TalkMatsutaF2 + TalkNamekoF2 + TalkShintaroF2 + TalkSoraF2 > F2PreviousStep" }]):
        jump block_00003A19
    if judge_lm_condition([]):
        jump block_00003A18

    return

label block_00003A19:
    # Node: 00003A19 (Win)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_window("イベントモード")
    pause 0.6

    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    pause 0.4

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 1.png
    $ zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 = -100
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as rs_image_6A16110F14C64AA89B2FAD22D32413C7 zorder zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 onlayer master
    hide rs_image_6A16110F14C64AA89B2FAD22D32413C7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_A0BF18F892C54E3D9D094E5CD477ECEE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 1.png
    $ zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 = -100
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as rs_image_6A16110F14C64AA89B2FAD22D32413C7 zorder zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 onlayer master
    hide rs_image_6A16110F14C64AA89B2FAD22D32413C7

    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_A0BF18F892C54E3D9D094E5CD477ECEE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.9

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1.3

    if sys_effect_current_file != "sound/Effect Sound/Correct 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Correct 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Correct 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_64C987B3866E43999077769BDA7EB8C7 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 1


    if judge_lm_condition([{ "scope": 0, "content": "TalkMatsutaF2 + TalkNamekoF2 + TalkShintaroF2 + TalkSoraF2 == 3" }]):
        jump block_00003A1F
    if judge_lm_condition([{ "scope": 0, "content": "TalkMatsutaF2 + TalkNamekoF2 + TalkShintaroF2 + TalkSoraF2 == 2" }]):
        jump block_00003A20
    if judge_lm_condition([]):
        jump block_00003A21

    return

label block_00003A1F:
    # Node: 00003A1F (3)
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 1.5

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你做的不错嘛！！能明显感觉到和之前气氛变了！{w}\n确实在向着好的方向发展啊！！"

    window hide

    pause 0.5

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 2


    if judge_lm_condition([]):
        jump block_00003A98

    return

label block_00003A98:
    # Node: 00003A98 (REMOVE)
    $ del F2PreviousStep
    $ TalkMatsutaF2 = 0
    $ TalkIzumiF2 = 0
    $ TalkTsukiF2 = 0
    $ TalkKatouF2 = 0
    $ TalkNamekoF2 = 0
    $ TalkShintaroF2 = 0
    $ TalkShinobuF2 = 0
    $ TalkSoraF2 = 0

    if judge_lm_condition([]):
        jump block_00003A16

    return

label block_00003A16:
    # Node: 00003A16 (傲嬌男孩子的治療法 3)
    $ set_window("イベントモード")
    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F7C0A55C2AAD46A09EC5C9F64521E3DB

    pause 0.8

    if sys_music_current_file != "sound/BGM/Afternoon.ogg":
        play music "sound/BGM/Afternoon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Afternoon.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "辛苦了～！！不过几天，穗海的脾气已经被磨掉很多了呐！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你那些建议挺有用的嘛。"

    show rs_image_E436CC5ED79D41EABE3ADFC40CD9F8B8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔～谈话的工作还是很辛苦的呐……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "话题很难选，实际说的时候也要注意不要弄错方向出现反效果～"

    show rs_image_13EEE138043542FB90557CFB44BADDE4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那么，你是怎么攻略那个不良少年的？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_253B2776672D49EA928D506D0DCEB77F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼呼！嘛，各种手段都有呐！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_6EA79B30E52B4FE8B90AB55D569F24D3 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "而且啊，下周，\n给了他两张去动物园一起玩的票哦。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D41A51E2B16F4674B1A8FB746C8F1328 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "能让人和好的丘比特・友的实力，看到了没！"

    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "多谢多谢～！"

    show rs_image_97AEAB5F7F86404C83B970C313450D38 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "没想到竟然连门票都准备了真是细心～\n亲戚在动物园工作？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不，在对面预约了，一定期限内给钱就行了。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_7303A840CCBB4DFCA4E6D8A50257852D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你、不会是、自己付的……"

    show rs_image_350F6A2B48EE49C8B631CE0B02F5BC2C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不要在意细节！接下来就只剩下祈祷他们约会成功了——！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_A56A27CF00F74EF798B09E4211817332 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀——做了好事心情真棒～♪"

    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不过，说不定穗海那家伙就会对一之濑移情别恋哦？"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_834C395C91BD400FAE5C9641C1D3849B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那白痴呆毛的受欢迎期也就顺利关门大吉了～"

    if sys_effect3_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇！真的呀！！翼君会抢走技安的！！"

    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……不过那也无所谓。那两个人一定能顺利发展的——"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_D41A51E2B16F4674B1A8FB746C8F1328 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我就识相地退到一边……"

    show rs_image_3C9E62B61C1744D1BDFDAD9A5EDD41C6 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你、你啊……真是条汉子！！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_6EA79B30E52B4FE8B90AB55D569F24D3 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E54B94670E804565963ECDB491A87076 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    extend "快迷上你了哦——！"

    if sys_effect3_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Drum 1.ogg"

    show rs_image_C34FAA8E3ADA4F78B2AEA97BA5E71368 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当・然・哦☆"

    window hide

    pause 0.55

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    stop music fadeout 1.4
    $ sys_music_current_file = ""

    window hide

    pause 4.5

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg"

    pause 2.5

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CF8D012E90904DCBB01FAD0593AEDF0A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 1.5

    show rs_image_113786E335B748148131070A96ED1C50 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 1.5

    show rs_image_44E4AB2358D94ED6BC1C77C63B6547A7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 1.5

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    window show

    pause 0.3

    rs_character_FF84A07B8C0D45C988EECF8CC61B3FAE "班长就决定是你了。负起责任好好加油。"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_AB40D0F221684FFA9F1FFE1528514C06 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……是。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_44E4AB2358D94ED6BC1C77C63B6547A7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.8

    show rs_image_F3D3F6687B4A4439B2B5EC69CF49B662 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_B03AE974EF09471985A2F163B9793DEF as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那个副班主任，太不讲道理了，\n只是因为学号是第一个就直接把班长的活塞过来。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_230BD7FA063A41F8BE135E566A07BE12 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_F3D3F6687B4A4439B2B5EC69CF49B662 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸，啊、那个……"

    show rs_image_CC1E83A6773C473596AE0228B0930B22 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊，抱歉这么突然，只是有些气不打一处来。"

    show rs_image_505CD7760BFD456C8B1B66ADE30FC053 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我是，“穗海作哉”。"

    show rs_image_AB40D0F221684FFA9F1FFE1528514C06 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，你好。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_CBCC9A1A52CE4DDC8A58F8F167874EBB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "岁……会……穗海君。"

    show rs_image_4E16BFB610AA4794B1562C064202F479 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "直接叫我作哉就行了。"

    show rs_image_505CD7760BFD456C8B1B66ADE30FC053 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嘛，已经当上了也就只能这样了。\n加油，真有什么事我会帮忙的。"

    show rs_image_6B6118D656CE45B58DD76B5492616A5A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，谢谢。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_CBCC9A1A52CE4DDC8A58F8F167874EBB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "作、作……作哉君。"

    show rs_image_4E16BFB610AA4794B1562C064202F479 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "叫不顺名字呐，是你的什么癖好？"

    show rs_image_989B13A334254ADEBEC1929753DF8026 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯、嗯。有些不知所措，经常没法顺利进行。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "慌、慌慌张张的……会让人觉得很不舒服呐，抱歉……"

    show rs_image_505CD7760BFD456C8B1B66ADE30FC053 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "并没有。我挺喜欢这个样子的，{w}简直和那家伙一样。"

    show rs_image_6B6118D656CE45B58DD76B5492616A5A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_CC1E83A6773C473596AE0228B0930B22 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊……没、没什么特别的意思！我没有那方面的兴趣。"

    show rs_image_336D0D4DE8904F49A10E6F396E89A9CE as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸……哈哈，是吗。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_CBCC9A1A52CE4DDC8A58F8F167874EBB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "啊！那个，抱……抱歉。"

    show rs_image_4E16BFB610AA4794B1562C064202F479 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "什么嘛转换这么频繁，哈哈。"

    show rs_image_C54F4D5E46644D54BE9C079FB8B9CFCB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸、欸……"

    window hide

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_07BACEE3C1C64F1DAD61CD240DF0C2E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    pause 0.6

    window show

    pause 0.4

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "突然被作哉君叫出来……{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_EAAB6CC3A5464202B2C5DE5D303795FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "难道说，终于要开始对付我了！？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_C6130C45B3154506B238905AA5DAD46A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊哇哇哇，果然我被讨厌了……。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……被打的话希望不会太痛……"

    window hide

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    window show

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "一之濑。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_EAAB6CC3A5464202B2C5DE5D303795FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "噫！？啊、作、作哉君！{w}\n{nw}"
    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那个，请一定要手下留情！！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_DD2B6D134E374D149ADE7F976BF51DC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可以的话请不要打露在外面的地方，请下手轻一点！！"

    show rs_image_D3230CCCAA744196B463EF066186F3A0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你是笨蛋啊。你到底是来干什么的。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_C6130C45B3154506B238905AA5DAD46A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "被、被打得……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_F477EFD4F5134EA9A29DCCDC67E15837 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊！？……那就如你所愿，\n{w=0.55}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_02CC0EBCB4BD407082D06D6C95D57796 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_2F778F94B33845D09CADF7780A31F9FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "先把那件看上去还不错的连帽衫交出来。"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_C6130C45B3154506B238905AA5DAD46A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哇、哇啊啊啊！只有这个还请放过我！！"

    show rs_image_F477EFD4F5134EA9A29DCCDC67E15837 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "说的也是啊，毕竟是最喜欢的那家伙送的重要的礼物呐～～～？"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_DD2B6D134E374D149ADE7F976BF51DC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "噫、噫！真的生气了！果然真的要打我？？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "至少请不要像{color=#008080}上次那样{/color}，饶过我……{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C9DE1C1D0E7E4BD58E316FCC6B30EEEB as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……{w=0.5}{nw}"
    show rs_image_9138D3EAFC66405AA95FD2DC03C7E56E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "真是的我是开玩笑的。别遇到什么都退缩啊笨蛋。{w}\n{nw}"
    show rs_image_B2C01DFF41914E56A428EBCACA72C51F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "今天是，我，那个……想和你一起去玩。"
    show rs_image_EAAB6CC3A5464202B2C5DE5D303795FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸？玩？作哉君和我？"

    show rs_image_9138D3EAFC66405AA95FD2DC03C7E56E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……是啊。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    extend "给，你的票。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "拿好别掉了，毕竟你挺冒失的。"

    show rs_image_1E50AF4024FA4A80BD7205FE7C7FF1DF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "非、非常感谢！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_275B22DDBE294B889403F68883C99EC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "这是动物园的……今天就是要去那里……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_1E50AF4024FA4A80BD7205FE7C7FF1DF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，票钱！多、我要付多少？"

    show rs_image_B2C01DFF41914E56A428EBCACA72C51F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……不用了，这是送给你的，虽说本来是免费的。\n走，去坐电车了。"

    show rs_image_9D0666C01E89408289145D59F704EFAB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好、好的……"

    window hide

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Train 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Train 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Train 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 2.5

    if sys_music2_current_file != "sound/Effect Sound/Train 1.ogg":
        play music2 "sound/Effect Sound/Train 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Train 1.ogg"

    pause 0.5

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_7A73A02D46B5439995C7016BA9FC1F8E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 1.5

    show rs_image_E804E40382F44A6587193E39A879A290 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 1.5

    window show

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "怎么挤成……这样……！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "运气不是很好呐………{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    extend "……哇！"

    window hide

    pause 0.5

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 2.png
    $ zorder_rs_image_821554C146A04ADF85F552B16E7C73A1 = -100
    show rs_image_821554C146A04ADF85F552B16E7C73A1 as rs_image_821554C146A04ADF85F552B16E7C73A1 zorder zorder_rs_image_821554C146A04ADF85F552B16E7C73A1 onlayer master
    hide rs_image_821554C146A04ADF85F552B16E7C73A1

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_821554C146A04ADF85F552B16E7C73A1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A2F5530406854E5098F52F72EE26DA66

    pause 0.7

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "（啊～啊，事先抓住吊环就好了呐。）"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜呜呜。"

    if sys_effect3_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "（稍微张开了一点脚。\n不知道这么贫弱的身体能支持到什么时候呢～？）"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}咚{/size}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊哇哇，抱、抱歉。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "（呵呵，结果还是撞了。）"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 2-1.png
    $ zorder_rs_image_03FE1F27E00741CCAF415509C1FF7783 = -100
    show rs_image_03FE1F27E00741CCAF415509C1FF7783 as rs_image_03FE1F27E00741CCAF415509C1FF7783 zorder zorder_rs_image_03FE1F27E00741CCAF415509C1FF7783 onlayer master
    hide rs_image_03FE1F27E00741CCAF415509C1FF7783

    show rs_image_03FE1F27E00741CCAF415509C1FF7783 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    extend "……。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "（别……别看我这边。）"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8A9FD25CF2224DA4B5F560425D3A98A7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……（呜呜）"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "（别用那种小狗一般的视线看我啊……！）"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "真是的……！……{w}……抓住我？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 2.png
    $ zorder_rs_image_821554C146A04ADF85F552B16E7C73A1 = -100
    show rs_image_821554C146A04ADF85F552B16E7C73A1 as rs_image_821554C146A04ADF85F552B16E7C73A1 zorder zorder_rs_image_821554C146A04ADF85F552B16E7C73A1 onlayer master
    hide rs_image_821554C146A04ADF85F552B16E7C73A1

    show rs_image_821554C146A04ADF85F552B16E7C73A1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可、可以吗？太、太感谢了！真的非常感谢……！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "（明明是你先朝我投来那种满怀期待的视线的……）"

    window hide

    pause 0.7

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_53B376EDDA024633A3328E405F058927

    extend "{size=32}DUANG{/size}"

    rs_character_7BB92FC0674F4F1C941FD574AF249950 "哇！"

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 3.png
    $ zorder_rs_image_ECECD9655F024DD9ABD97ABDC960DC82 = -100
    show rs_image_ECECD9655F024DD9ABD97ABDC960DC82 as rs_image_ECECD9655F024DD9ABD97ABDC960DC82 zorder zorder_rs_image_ECECD9655F024DD9ABD97ABDC960DC82 onlayer master
    hide rs_image_ECECD9655F024DD9ABD97ABDC960DC82

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_ECECD9655F024DD9ABD97ABDC960DC82 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.6

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……谢、谢谢。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我、我明白了，快起来……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "抱、抱歉～……！……可、{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "可是怎么才能恢复到原来的姿势呢……？？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "什么！我怎么可能知道啊笨蛋！\n就是因为你平时根本不锻炼才会这么站不稳的，冒失鬼！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "非常抱歉——！对不起……！"

    window hide

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    pause 0.5

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1.5

    if sys_effect2_current_file != "sound/Effect Sound/Train 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Train 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Train 2.ogg"

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_EF8094E63B394108BA21AC3F61424182 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    window show

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_CF5AA529110045B9AA052BA9023E6FA3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "结果还是引出了很大的麻烦……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……无所谓，算了。走。"

    show rs_image_328406EB66B449C99EAA3BC3E5C0EE95 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好、好。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.45

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_EAAB6CC3A5464202B2C5DE5D303795FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.8

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_43D770DA1C8F437BAB29025F2847BF0B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_DDA00DBFDDC245EC9D675EA5711B37C9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "又怎么了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_EF8094E63B394108BA21AC3F61424182 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "车、车票……"

    show rs_image_43D770DA1C8F437BAB29025F2847BF0B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……钱包？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_EF8094E63B394108BA21AC3F61424182 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "没……没有。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_43D770DA1C8F437BAB29025F2847BF0B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_DDA00DBFDDC245EC9D675EA5711B37C9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "外套。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_EF8094E63B394108BA21AC3F61424182 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_9B9F6DFAAEB44A1FB0A65329C35C3541 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "没、没有……！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_43D770DA1C8F437BAB29025F2847BF0B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D3230CCCAA744196B463EF066186F3A0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "口袋？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_EF8094E63B394108BA21AC3F61424182 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_C6130C45B3154506B238905AA5DAD46A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "找不到！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_43D770DA1C8F437BAB29025F2847BF0B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那再找一次钱包。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_EF8094E63B394108BA21AC3F61424182 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_DD2B6D134E374D149ADE7F976BF51DC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "没……{w=0.5}啊咧？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_2486E9AC1518402DA6CBAA06B85610C8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    extend "啊，找到了！！"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_43D770DA1C8F437BAB29025F2847BF0B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F477EFD4F5134EA9A29DCCDC67E15837 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不爽……！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9ACAEF851EAF4CECBC5BA7CA6AAF6C36 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_02CC0EBCB4BD407082D06D6C95D57796 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "你个不长记性的！！赶紧给我走！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_EF8094E63B394108BA21AC3F61424182 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_C6130C45B3154506B238905AA5DAD46A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "是！对不起！"

    window hide

    pause 0.4

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1.5

    if sys_music2_current_file != "sound/Effect Sound/Clamorous 1.ogg":
        play music2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_616B75EC1EAF421896D5EB4FA01F9675 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    window show

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_0BD950ADC14245578BC5105060EF0E00 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "总算到了呐。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "啊，那边能看到通地阁呢～"

    show rs_image_15A2B3B975314AA1B94A1058C95E9FB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我还是第一次到这一带来呐。{w=0.3}{nw}"
    show rs_image_B2C01DFF41914E56A428EBCACA72C51F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend ""

    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……是吗。总之，入园需要门票，先拿出来。"

    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，是的。\n那个……{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_2B709367A1FA4DEF815337B5B014517C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊咧？啊咧咧。"

    show rs_image_D3230CCCAA744196B463EF066186F3A0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "对对对对不起！我、我记得是在……"

    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_9B9F6DFAAEB44A1FB0A65329C35C3541 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个那个……！\n{w=0.5}{nw}"
    show rs_image_2B709367A1FA4DEF815337B5B014517C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊！找到了找到了！！是这个！"

    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    show rs_image_E53075204ECC459689595B5A7E7E345C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个……非、非常抱歉……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_862E41C0B01E451EB9C2E88AECBFEDBB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你这一点真的很令人火大。"

    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "！！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_9F9E3AB5982941C7A3FF42BB60F86B4D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……对不起。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_8F627C7508AF48D38DD03487599E72F7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    window show

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_20D50D7E2029427A96A2E0A6E34FC3DD as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你想去看什么？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "请、请你决定。"

    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那就去看小熊猫好了。"

    show rs_image_328406EB66B449C99EAA3BC3E5C0EE95 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "小、小熊猫？……没听说过。"

    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "真的！？那肯定要去看一看！！就像会动的玩偶一样哦！"

    show rs_image_0BD950ADC14245578BC5105060EF0E00 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君真的很喜欢动物呐。"

    show rs_image_5ECF4017CE3E48E0B749AA1981DD40C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "欸？嗯，算是。"

    show rs_image_15A2B3B975314AA1B94A1058C95E9FB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哈哈，只要涉及到动物的话题作哉君就会笑起来呢，感觉好怀念。"

    show rs_image_179BC6B4F1EE4152A4570701E0F0E41E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊……"
    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "嗯……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_2486E9AC1518402DA6CBAA06B85610C8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我想去看看！作哉君极力推荐的小熊猫！"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    stop music fadeout 2
    $ sys_music_current_file = ""

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B1E776E59E0F4078A22BEFCAB3389387

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_9F4B5E5A171D45DB9C9203215C25189E as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_401EFA0096CB44FEB03CFF085350295A

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 9-1.png
    $ zorder_rs_image_849CEB1C756A40EC9091CD060431DA06 = -100
    show rs_image_849CEB1C756A40EC9091CD060431DA06 as rs_image_849CEB1C756A40EC9091CD060431DA06 zorder zorder_rs_image_849CEB1C756A40EC9091CD060431DA06 onlayer master
    hide rs_image_849CEB1C756A40EC9091CD060431DA06

    show rs_image_849CEB1C756A40EC9091CD060431DA06 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.6

    if sys_music_current_file != "sound/BGM/Flurry 2.ogg":
        play music "sound/BGM/Flurry 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 2.ogg"

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好、好可爱——！！！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "对不！？完全忍不住，那种厚实的感觉！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "毛茸茸彭松松，动起来蠢笨的样子，\n简直就是集齐了所有可爱的要素……就是天使！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯嗯嗯！这种动物居然存在呐～！\n真好啊……好想养一只～！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "说起来，这不太可能。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小熊猫已经作为易危物种被保护起来了，\n一般家庭是不能饲养的。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，是这样，好遗憾哦……"

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Attention 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attention 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attention 1.ogg"

    pause 0.6

    window show

    rs_character_A84468996B914B0C9E7E488D91B36BE9 "仅限今天的小熊猫\n“看看，摸摸，真心感受！心跳不已说明会”马上就要开始了。"

    rs_character_A84468996B914B0C9E7E488D91B36BE9 "请有兴趣的游客务必光临我们在激动人心高山区前的会场。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "去！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好！"

    window hide

    pause 0.6

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_8F627C7508AF48D38DD03487599E72F7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_983D3ABC05A64E488B0C017601C96E4D as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    window show

    pause 0.3

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "真、真的就像玩偶一样呐……手上还留着那时的感觉～"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "闻起来也和狗狗一样，实在是太可爱了！"

    show rs_image_5ECF4017CE3E48E0B749AA1981DD40C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那个孩子因为没有母亲抚养，所以是被人工抚养长大的。"

    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "管理那么严格，是为了不让它们沾染人类的病菌。\n不愧是动物园……"

    show rs_image_2B709367A1FA4DEF815337B5B014517C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个……作哉君，刚才拍的照片，\n请、请问可以传一张到我的手机里吗？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_9B9F6DFAAEB44A1FB0A65329C35C3541 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……我、我也想给朋友看！拜、拜托了！"

    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "说的朋友，无非就是那个笨蛋？"

    show rs_image_8791FBC16EE045C8A5316E8761B3EC61 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "是、是的……不可以吗……？"

    show rs_image_B2C01DFF41914E56A428EBCACA72C51F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_054279E603CE4B2A9A7A8F8E26DF9492 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "吼……可以哦，以此自豪即可。"

    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "能和最可爱的动物接触，那家伙想必也会羡慕吧！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_2486E9AC1518402DA6CBAA06B85610C8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯！！非常感谢！嘿嘿。"

    show rs_image_3DE5824BE0644C96928A4FBCD72BE70B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "说起来，你对那家伙总是莫名其妙地在意呐，难道你们是同？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_9D0666C01E89408289145D59F704EFAB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸？同、同是……是什么意思？"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "就是说{color=#FF00FF}喜欢{/color}。"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_C6130C45B3154506B238905AA5DAD46A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_B8EFAA9CE5AC4872B1F5E3E6C65290EB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_DC107C264C484B3A8306E39B61626CF6

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "噫噫——！！？？突、突然说什么呐！！\n那、那个……可、我们都是男孩子……"

    show rs_image_3DE5824BE0644C96928A4FBCD72BE70B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "所以才说是同。同志的同。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_2F778F94B33845D09CADF7780A31F9FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不不、不是的！！我我我绝对不是！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_054279E603CE4B2A9A7A8F8E26DF9492 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "被一之濑摸过的小熊猫好可怜哦，\n说不定已经感染了一之濑的同志病毒了呐。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_9B9F6DFAAEB44A1FB0A65329C35C3541 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "真是的！不、不要捉弄我！"

    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈哈哈。"
    show rs_image_5ECF4017CE3E48E0B749AA1981DD40C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……我还真是单纯。\n只是因为附近有动物就变得这么健谈。"

    show rs_image_9D0666C01E89408289145D59F704EFAB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸……？"

    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "该吃饭了，有些话想和你说。"

    show rs_image_A20D31D533CF44CDA4A7F67CEC353CDE as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好、好的……"

    window hide

    pause 0.5

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.6

    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 2.5

    show rs_image_28CB16F81175458EA97C8F0250448304 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2.5

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 3

    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg"

    pause 1.5

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4E32A773CC3946229F89F0974C32743A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 0.8

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_14E10B79E7314B8983D11ADEDBABF615 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那个……作哉君。"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_9A154D2ECA194EFA979469EB618CF53B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    show rs_image_BF0091E3804A4BA2A59CDD5854A1D816 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我、我、我做错什么了吗？\n如果真的是这样，我会道歉的。所以，那个……"

    show rs_image_FD6A99042EC646D6BC8E5E7FEF7E4624 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "切……烦人，看见你就觉得气不打一处来。{w}\n一副忧郁的样子，别再出现在我面前了。"

    show rs_image_C41CBEB3EEB3490DAA0FDD91A803B370 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "！！"

    show rs_image_9A154D2ECA194EFA979469EB618CF53B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……{w=0.5}哼。{nw}"
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend ""

    window hide

    show rs_image_E0DC7CB514A34268BD283D9C552D720A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    stop music2 fadeout 1.2
    $ sys_music2_current_file = ""

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_44E4AB2358D94ED6BC1C77C63B6547A7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at left_top zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8C818451D3534586ADE16DBAE08932F5

    pause 0.8

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_B03AE974EF09471985A2F163B9793DEF as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_054BE1C5516844E3B1306DC2881D3BA1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嗯。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "诶……扫帚和簸箕？"

    show rs_image_9A154D2ECA194EFA979469EB618CF53B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "今天本该打扫卫生的家伙没来，那就只能让班长做了对不。"

    show rs_image_14E10B79E7314B8983D11ADEDBABF615 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好、好的。"

    show rs_image_C5D5B2DF260742E8B056632378443C20 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那就给我好好做。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.7

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_E0DC7CB514A34268BD283D9C552D720A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"

    window hide

    pause 0.7

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_ABCB76CFFBF3494495385A4159D4B0A4 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_17E38514AE2A41199D5818D2DC151809 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 0.8

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_C41CBEB3EEB3490DAA0FDD91A803B370 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.3

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F9266AE6604F436C8CB09C18A6DFC845 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8C818451D3534586ADE16DBAE08932F5

    pause 0.8

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_C5D5B2DF260742E8B056632378443C20 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_72BDD404343D4BD19917E4ACF4D1EDD1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那家伙好烦的，体育课的时候也一点不安分——"

    pause 0.4

    show rs_image_CC1E83A6773C473596AE0228B0930B22 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_67149490BFB34AC09E23A9F5D1F21D4C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "请不要说友君的坏话！！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "！？"

    show rs_image_72BDD404343D4BD19917E4ACF4D1EDD1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"

    window hide

    pause 0.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.2

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D2F7AA66B3134030823B285A797FFEBA as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_4458A1124D094371885BBD5D776780FA as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_849653D9A0F7486F9F75662EF47D4A60 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    window show

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "穗海，看看那个！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "一之濑和……{w=0.5}{nw}"
    show rs_image_245E50B1E6E340DCBF19C047062EE8BB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "一班的那个。"

    show rs_image_AD95686CD0F74B248164B29F10779041 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好少见的场景！一之濑也终于交到好朋友了啊♪太好了。"

    show rs_image_E77FE4233F12452FB03391826E6241DF as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    show rs_image_7AED4918171E48E19413364F98D13AA1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈！！刚才交换喂饭了！难道他们两个是那种情侣么！？"

    show rs_image_0CDEECFD95E44F1EB0D76A48AFDB0A1D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    show rs_image_AD95686CD0F74B248164B29F10779041 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呜哇～……男校好可怕。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"
    show rs_image_AA7360089FD745E296548670C6B6BDE9 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "那个塑胶瓶我替你处理。"

    show rs_image_287120B11A4447AC97117BB60B9E6B99 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_80D1BC1D41FE4F2194B92884E6EDDF9E as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊，多谢♪……"
    show rs_image_32DF284DC24B4F3098D45777757C47CC as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "等等你想干什么！？\n会打到他们的，那怎么说也太过分了！！"

    window hide

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_CC027157794040E7866FEC1531A05375 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.6

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_0CDEECFD95E44F1EB0D76A48AFDB0A1D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_5DE93FEED47B44FFA9E5B7724C7E2E8D as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 1.3

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 4.png
    $ zorder_rs_image_4D6DF38872224876B0346DDC8236880E = -100
    show rs_image_4D6DF38872224876B0346DDC8236880E as rs_image_4D6DF38872224876B0346DDC8236880E zorder zorder_rs_image_4D6DF38872224876B0346DDC8236880E onlayer master
    hide rs_image_4D6DF38872224876B0346DDC8236880E

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_4D6DF38872224876B0346DDC8236880E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_261D08C838924E20AF161341FB0958E9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EF2D3A4912BA490B9BDDB92C8700586E

    pause 1

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_E53075204ECC459689595B5A7E7E345C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.7

    window show

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……是这样……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "至今为止，对不起。我明白我是不会那么容易被原谅的。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "零零散散地做了这么多坏事，今天也是，没能好好……"

    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "才、才才没有……！能、能把这些事告诉我真的非常感谢。"

    show rs_image_20D50D7E2029427A96A2E0A6E34FC3DD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不过，我没有养过动物，\n更别说是生命这种……家里的所有人也很健康。"

    show rs_image_9F9E3AB5982941C7A3FF42BB60F86B4D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "要明白作哉君的心情可能会很困难……\n……对不起。"

    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    show rs_image_15A2B3B975314AA1B94A1058C95E9FB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不过，能明白个中理由也是很好的。我、我、一直在想其中的原因……"

    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "今、今后我会努力不再让作哉君感到焦躁的。"

    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "本来就是我无故发火，不用这么在意的。{w}大骂我一场说不定要更好……"

    show rs_image_20D50D7E2029427A96A2E0A6E34FC3DD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "虽、虽然我说不出像是我也明白这种话，\n不过，我明白作哉君也很苦恼。"

    show rs_image_15A2B3B975314AA1B94A1058C95E9FB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "所以，请不要如此在意了。"

    show rs_image_179BC6B4F1EE4152A4570701E0F0E41E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "一之濑……"

    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个……{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8A626993E4D845D382910F0B900F3F2B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "朋友啊就是要好好相处的！听到没！！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_CF5AA529110045B9AA052BA9023E6FA3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……{w=0.5}……那个，我、怎、怎么做才能真正发起火来呐……"

    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "呼……你这家伙真是……{w}\n{nw}"
    show rs_image_5ECF4017CE3E48E0B749AA1981DD40C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……谢了。"

    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你啊，又冒失又懦弱，不过很强呢。{w}\n我就是喜欢你这样的地方。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_DFDDF6139A514ABE9424DFC7D868DAB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸？欸！啊、那、那还真是……谢谢了……"

    show rs_image_3DE5824BE0644C96928A4FBCD72BE70B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈……脸红了？你谁都行？真轻浮～"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9B9F6DFAAEB44A1FB0A65329C35C3541 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "没、没有这回事！！我、我是很专一的！"

    show rs_image_5ECF4017CE3E48E0B749AA1981DD40C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "呼……是嘛。\n算了，我会给你加油的。"
    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "毕竟是朋友。{w=0.7}{nw}"
    show rs_image_1E50AF4024FA4A80BD7205FE7C7FF1DF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend ""

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_DD2B6D134E374D149ADE7F976BF51DC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君……"

    window hide

    pause 0.4

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 5.png
    $ zorder_rs_image_B6A08DC7BC7B43CA9586AF3377BA9930 = -100
    show rs_image_B6A08DC7BC7B43CA9586AF3377BA9930 as rs_image_B6A08DC7BC7B43CA9586AF3377BA9930 zorder zorder_rs_image_B6A08DC7BC7B43CA9586AF3377BA9930 onlayer master
    hide rs_image_B6A08DC7BC7B43CA9586AF3377BA9930

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B6A08DC7BC7B43CA9586AF3377BA9930 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.6

    window show

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……（抽泣）……谢谢……呜……谢谢……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "为什么要挑这时候哭啊……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "只……只是对我来说……太感动了……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "至今为止的各种错误，现在终于找到合适的前进道路了……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我……不会忘记的。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……是啊，我也……绝对不会忘的。{w}\n{size=14}——我的感情。{/size}"

    window hide

    pause 1.5

    stop music fadeout 4
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_EBC84B71B65143808176EA1567C48144

    pause 3.5


    if judge_lm_condition([]):
        jump block_00003A17

    return

label block_00003A17:
    # Node: 00003A17 (傲嬌男孩子的治療法 4)
    $ set_window("イベントモード")
    if sys_music2_current_file != "sound/Effect Sound/Train 1.ogg":
        play music2 "sound/Effect Sound/Train 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Train 1.ogg"

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A23899BFC22148238415EF01457A8E8A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 1.5

    show rs_image_82D23914AAB94ABCA721834E99AFCAC7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 1.2

    window show

    pause 0.3

    rs_character_63EB8D07C5894F3AA957DE8833800788 "下一站是伊丹咲，伊丹咲。"

    window hide

    pause 1

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_A20D31D533CF44CDA4A7F67CEC353CDE as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_F16151FFFEEE4959AE54C7BCBD1B7FE2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    if sys_music_current_file != "sound/BGM/Guitar 1.ogg":
        play music "sound/BGM/Guitar 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Guitar 1.ogg"

    pause 0.5

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君要在下一站下车？"

    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不，回学校还有事，会一直坐到御咲。"

    show rs_image_0BD950ADC14245578BC5105060EF0E00 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，"
    show rs_image_B2C01DFF41914E56A428EBCACA72C51F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "小……翼的照顾？"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_345AD24DAEE64B9A963489B5AD613EE7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "对，没错。……"
    show rs_image_B2C01DFF41914E56A428EBCACA72C51F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "应该没关系，\n今天比平时晚了很多，有些担心。天也冷下来了。"

    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个……我也可以去吗？"

    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "诶？啊，嗯，可以。不过只是日常照顾，不会有什么意思的。"

    show rs_image_15A2B3B975314AA1B94A1058C95E9FB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "没关系的，今天已经看过各种动物，突然也想看看狗了。"

    show rs_image_5ECF4017CE3E48E0B749AA1981DD40C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "是嘛。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3DE5824BE0644C96928A4FBCD72BE70B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嘛，要是被咬了也不要在意啊。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_EAAB6CC3A5464202B2C5DE5D303795FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸！？会、会被咬……？？"

    show rs_image_054279E603CE4B2A9A7A8F8E26DF9492 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "狗的下颚力量可是强大到只要有那个意思\n就可以轻松咬断人类的手腕哦～"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "噫————！哇哇哇，果、果然还是不要去了……"

    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "开玩笑的！小翼不会咬人，可是被好好教育过的。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_1E50AF4024FA4A80BD7205FE7C7FF1DF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸？嗯。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_EAAB6CC3A5464202B2C5DE5D303795FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊！……{w=0.3}{nw}"
    show rs_image_2B709367A1FA4DEF815337B5B014517C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    extend "好。"

    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "刚才听成自己了？"

    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可、可是这也太容易混了，名字都是一样的……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊，是嘛。是取名的我不好。好好，抱歉抱歉。"

    show rs_image_2B709367A1FA4DEF815337B5B014517C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哇啊啊，不要生气嘛——！"

    show rs_image_345AD24DAEE64B9A963489B5AD613EE7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "呼。"

    window hide

    pause 0.4

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1.5

    show rs_image_0BC8ECCA889E453086280F2D1BD1799C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    stop music2 fadeout 1.5
    $ sys_music2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2.5

    if sys_music2_current_file != "sound/Effect Sound/Night insect 1.ogg":
        play music2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5333E0D1BE9A4EB995FB5238B3E3566A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2

    show rs_image_A43B4B084B6748278EEE9217194B9925 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 0.6

    if sys_music_current_file != "sound/BGM/Night.ogg":
        play music "sound/BGM/Night.ogg" loop
        $ sys_music_current_file = "sound/BGM/Night.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_0BD950ADC14245578BC5105060EF0E00 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_5ECF4017CE3E48E0B749AA1981DD40C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.6

    window show

    stop music2 fadeout 1.5
    $ sys_music2_current_file = ""

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小翼——小翼——！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "小翼酱……"

    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "很奇怪啊……一直以来都是一叫就出来的。"

    show rs_image_9D0666C01E89408289145D59F704EFAB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "说不定已经休息了……"

    show rs_image_9138D3EAFC66405AA95FD2DC03C7E56E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不，还没到时间。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "小翼——！{w}{w=0.7}{nw}"
    stop music fadeout 0.4
    $ sys_music_current_file = ""

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    extend "小翼……？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "果然休息了……？"

    window hide

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 6.png
    $ zorder_rs_image_3D4DEC86BCC44FEC9C0353067818153E = -100
    show rs_image_3D4DEC86BCC44FEC9C0353067818153E as rs_image_3D4DEC86BCC44FEC9C0353067818153E zorder zorder_rs_image_3D4DEC86BCC44FEC9C0353067818153E onlayer master
    hide rs_image_3D4DEC86BCC44FEC9C0353067818153E

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_3D4DEC86BCC44FEC9C0353067818153E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_195F518B89564C98A557F130D2E603F0

    pause 0.7

    window show

    if sys_music_current_file != "sound/BGM/My precious time.ogg":
        play music "sound/BGM/My precious time.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time.ogg"

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小翼！怎么了小翼！？振作点！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "小翼酱，怎么了……？"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "样子很奇怪，呼吸节奏也很诡异！{w}\n怎么了？不舒服！？小翼！小翼！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作、作哉君！我、我、有我能做的没有？"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "水、拿水！总之弄水来！自来水就行了！拜托了！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "马上！"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_A2F5530406854E5098F52F72EE26DA66

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_A43B4B084B6748278EEE9217194B9925 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_B3143F82636A4131AB87119A7919051D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A2F5530406854E5098F52F72EE26DA66

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小翼……到底怎么了小翼……！！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_87329FCC9A2B4CA490D6646C6014EF88 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君，水来了！！"

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 7.png
    $ zorder_rs_image_10467CBD22854ED498CC690F9E3ABF68 = -100
    show rs_image_10467CBD22854ED498CC690F9E3ABF68 as rs_image_10467CBD22854ED498CC690F9E3ABF68 zorder zorder_rs_image_10467CBD22854ED498CC690F9E3ABF68 onlayer master
    hide rs_image_10467CBD22854ED498CC690F9E3ABF68

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_10467CBD22854ED498CC690F9E3ABF68 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D6BC962AE17948D893E50BE9B4670973

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "谢了！小翼，快喝。来，张开嘴。\n到底怎么了，今天早上还那么健康的。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……好，喝下去了。总之必须带它去医院！！{w}\n一之濑，坐公交去医院！"

    window hide

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_195F518B89564C98A557F130D2E603F0

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_8A626993E4D845D382910F0B900F3F2B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "等、等等作哉君！动物要上公交必须有专门认证的！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "而且，看病的花销也……现在带了多少？"

    show rs_image_87329FCC9A2B4CA490D6646C6014EF88 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我、我不是很清楚不过，没有保险的话，费用是非常高的……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_B3143F82636A4131AB87119A7919051D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "！！那、那个时候是、开车……钱是妈妈付的……"

    window hide

    pause 0.4

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_0D1A14CC6DD549EA877967C087A4F0E5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.4

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "完了……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "明明为了不再发生那样的事，\n准备了这么多，注意了这么多，做了这么多……！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "得病该怎么做，没钱该怎么做，完全，没注意……\n这不就和过去……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "振作点作哉君！现在说这些没用！\n赶快想解决方法才是最要紧的！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……去动物园后，我明白了。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "为了让那些孩子能幸福快乐地生活，饲养员的经验和知识，\n以及到位的管理都是不可或缺的。"

    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "像我这样半知半解，只会让他们受苦……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不要……已经……为什么……\n我讨厌这样……！小翼，小翼……！！"

    window hide

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.7

    window show

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_8A626993E4D845D382910F0B900F3F2B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君！不要只靠自己，现在我也在……！！"

    show rs_image_87329FCC9A2B4CA490D6646C6014EF88 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……好。请先照看一下小翼酱。"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 2


    if judge_lm_condition([]):
        jump block_00003A1A

    return

label block_00003A1A:
    # Node: 00003A1A (CP2 Night 翼)
    call block_00000FD5 from _call_block_00000FD5

    if judge_lm_condition([]):
        jump block_00003AEC

    return

label block_00003AEC:
    # Node: 00003AEC (傲嬌男孩子的治療法 5)
    if sys_music_current_file != "sound/BGM/My precious time.ogg":
        play music "sound/BGM/My precious time.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ set_window("イベントモード")
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    show rs_image_8D7AA2A7FEF641B4BDEEE8BE2E6483BA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.8

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_8A626993E4D845D382910F0B900F3F2B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_354DFEA941CB402F9AA73F6072D895B3

    pause 0.4

    window show

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "老师！！老师！！！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_3CDBB93600FA40048DE19330047E1350 as tag_061CD0864C4E48C0B3AA935440B7C90D at left_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    show rs_image_8A626993E4D845D382910F0B900F3F2B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "一之濑！？怎么了这么晚，发生什么了！？"

    show rs_image_DD2B6D134E374D149ADE7F976BF51DC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "老师！！！太好了……我、我……！！"

    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "发生什么了！告诉老师！"

    show rs_image_8A626993E4D845D382910F0B900F3F2B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "滑子老师！！请马上跟我来！！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "请一定救救小翼酱！！"

    window hide

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2

    if sys_music2_current_file != "sound/Effect Sound/Night insect 1.ogg":
        play music2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_A43B4B084B6748278EEE9217194B9925 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222BBB56F7BA4025B3E942F40786CBC9

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_87329FCC9A2B4CA490D6646C6014EF88 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_3CDBB93600FA40048DE19330047E1350 as tag_061CD0864C4E48C0B3AA935440B7C90D at left_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.5

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "穂海！情况如何！？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "老……老师……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_8A626993E4D845D382910F0B900F3F2B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君！老师已经知道原委了！！马上去医院！！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "一之濑……滑子老师……小翼它……小翼它……"

    show rs_image_9BAD09B7F4DE47339C69A165D80E6844 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "坐我的车去医院，过来。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "可是、老师！钱……保险……"

    show rs_image_87A4A951CCF94134BEC8CCB7D574B6E1 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "我来解决！你们只要想着怎么救它就行了。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "身体还没冷马上把它抱起来。"

    show rs_image_179BC6B4F1EE4152A4570701E0F0E41E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "是、是！"

    show rs_image_87329FCC9A2B4CA490D6646C6014EF88 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君，快点！"

    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "谢谢，一之濑，老师……"

    window hide

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_75628AB8DD2D4F06B3308EDBD92F74C3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_E53075204ECC459689595B5A7E7E345C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_1E50AF4024FA4A80BD7205FE7C7FF1DF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.7

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_87A4A951CCF94134BEC8CCB7D574B6E1 as tag_061CD0864C4E48C0B3AA935440B7C90D at right_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_FFC620A1302E417EBD9CB71C6CDE9274

    pause 1.5

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_87329FCC9A2B4CA490D6646C6014EF88 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.4

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "老、老师……小翼酱的身体……？"

    show rs_image_B08F170752C74A09BC000D1CF77FA609 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "没什么，只是普通的肠胃炎症而已。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "住院挂几天点滴就可以恢复了，放心。没有性命之忧。"

    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这样！作、作哉君，太好了呐。"

    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……嗯。"

    show rs_image_C0F02B9EC0484E97848C810E5DD5BB34 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "最近气温变化幅度很大，因此生病的动物也不在少数。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "不管再怎么加强负责照顾的人手，\n要保证绝对不会生病也是很难的。"

    show rs_image_9BAD09B7F4DE47339C69A165D80E6844 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "所以，穗海，不要太过责备自己了。"

    show rs_image_179BC6B4F1EE4152A4570701E0F0E41E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……嗯……"

    show rs_image_C0F02B9EC0484E97848C810E5DD5BB34 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "那么，小翼……{w=0.45}{nw}"
    show rs_image_B08F170752C74A09BC000D1CF77FA609 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "酱今天就住在这里了。\n你们先回车上，我还要弄些手续。"

    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "可、可是！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_8791FBC16EE045C8A5316E8761B3EC61 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "作哉君……我们什么都做不了的。这里就听老师的话。"

    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……好。"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.3

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_87A4A951CCF94134BEC8CCB7D574B6E1 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    window show

    pause 0.3

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "……那么，现在才是问题的麻烦之处啊……"

    window hide

    pause 0.6

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_BCA8F5EC0F79434A8A764DA02F81DBC4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 1.5

    stop effect fadeout 1.5
    $ sys_effect_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_0BD950ADC14245578BC5105060EF0E00 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_179BC6B4F1EE4152A4570701E0F0E41E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    window show

    pause 0.3

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "一之濑……真的太感谢了。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哈哈，不、不客气。"

    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我完全陷入了混乱，什么都做不到。"

    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "就算能想起之前的事……就算告诉自己要做些什么，\n脑袋里也只剩下“无可奈何”这四个字……"

    show rs_image_20D50D7E2029427A96A2E0A6E34FC3DD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这、这毕竟、也是不可抗力……"

    show rs_image_9F9E3AB5982941C7A3FF42BB60F86B4D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我也是，当我去找人的时候，心理害怕得要死。\n或许我稍微有点，明白作哉君的心情了。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "和作哉君玩到这么晚，导致现在才发现病情的我也有责任。\n也、也许因为我……心中非常恐慌，非常痛苦。"

    show rs_image_E53075204ECC459689595B5A7E7E345C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "想到是平常一直受到关照的作哉君，就更加……"

    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    show rs_image_9F9E3AB5982941C7A3FF42BB60F86B4D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……这次虽然没事……可、可如果真的没能救到，\n一定会更加责备自己，越来越想不开……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……正因为是能勾起回忆的人，{w}\n{nw}"
    show rs_image_E53075204ECC459689595B5A7E7E345C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_179BC6B4F1EE4152A4570701E0F0E41E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "才不得不想方设法让他远离自己……这种无可奈何的感觉"

    pause 0.4

    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……你，很强。能理解这种欺负你的人的心情……"

    show rs_image_15A2B3B975314AA1B94A1058C95E9FB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "因为作哉君不是会随便伤害别人的人哦。"

    show rs_image_9D4ED68CEC2D4E5BA0296B4CA2A90847 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "而、而且，我们还只是孩子。要养育什么，就算是大人也很困难。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "对未成熟的我们来说，找不到合适的处理方法也是当然的。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.25

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 0.25

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "正是如此。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_1E50AF4024FA4A80BD7205FE7C7FF1DF as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "老、老师！已经可以了？"

    show rs_image_B08F170752C74A09BC000D1CF77FA609 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "嗯，不用担心。"

    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "老师，这次真的非常感谢！！"

    show rs_image_9B9F6DFAAEB44A1FB0A65329C35C3541 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "非常感谢！"

    show rs_image_9BAD09B7F4DE47339C69A165D80E6844 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "你们还是孩子，经验不充足，\n以后再出现这样的事故，会更加感觉到自己的无力。"

    show rs_image_B08F170752C74A09BC000D1CF77FA609 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "但是，这种沮丧和受挫，正是成长的证明。\n就像现在的你们一样。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "不断如此，就能不断前进。永远不要忘记失败的感觉。"

    show rs_image_87A4A951CCF94134BEC8CCB7D574B6E1 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "可是，对于一个鲜活的生命，即便是孩子，失败也是不被允许的。{w}\n{nw}"
    show rs_image_9F9E3AB5982941C7A3FF42BB60F86B4D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "我们必须考虑一下今后如何照顾小翼酱。"

    window hide

    pause 0.7

    if sys_music2_current_file != "sound/Effect Sound/Night insect 1.ogg":
        play music2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_0D1A14CC6DD549EA877967C087A4F0E5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.6

    window show

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……靠我们能做到的太有限了，\n只能借助老师的力量，由学校来管理了……？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "比如学校的兔子，鸟那样的。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "可是，那样的话，其他学生就都知道了。\n然后，就会出现欺负小翼的家伙。"

    window hide

    pause 0.6

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.7

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_87A4A951CCF94134BEC8CCB7D574B6E1 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "要由学校饲养小翼酱，同时还要防止被欺负。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_328406EB66B449C99EAA3BC3E5C0EE95 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "能做到的话自然最好可……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这、这有些太不可能了吧？应该不会下达许可……"

    window hide

    pause 0.4

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1.2

    if sys_music_current_file != "sound/BGM/The end of touch.ogg":
        play music "sound/BGM/The end of touch.ogg" loop
        $ sys_music_current_file = "sound/BGM/The end of touch.ogg"

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_9379B2194CA6444BB5C1B77F9AAD8328 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    window show

    pause 0.3

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "不，学园长每天都在不吝口舌地到处说，\n接触生命，养育生命。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "因为这对培养“丰富有涵养的人性”有益。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "而且，作为教育者，\n我们有义务为所有正在成长的学生提供任何必要的环境。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "关于这件事，我会负起责任向学校提议的。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_1E50AF4024FA4A80BD7205FE7C7FF1DF as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_ADC3F2CD374D4306B3D8E35BAC012A8F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "老师……！！"

    show rs_image_15A2B3B975314AA1B94A1058C95E9FB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "太好了呐，作哉君！这样小翼酱就可以安心了。"

    show rs_image_179BC6B4F1EE4152A4570701E0F0E41E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……老师，帮我们解决这么多事，真的太感谢了……！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不过！虽然有些狂妄，但有件事我必须确认。"

    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小翼不是教育的道具，它和我们一样，是正在成长的孩子，\n能做到在这一基础上守护它吗？"

    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我并不成熟，也不是小翼的双亲。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "老师能代替双亲，弥补我的无力，守护好小翼吗？"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "穂海……"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_9D0666C01E89408289145D59F704EFAB as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_08A0C47197394B09A28BDCD79F13CF3D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……"

    window hide

    pause 0.4

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.4

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "我……当然，这是毋庸置疑的。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "如果连这点觉悟都没有就去照看也是很困扰的。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "你们力所不及的部分，学校和我，都会好好补足的。"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "所以，你们只要做好你们自己，{w}\n{nw}"
    show rs_image_9379B2194CA6444BB5C1B77F9AAD8328 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "继续如往常一般照看小翼酱就好了。"

    window hide

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "老师……！！"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_5ECF4017CE3E48E0B749AA1981DD40C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "滑子老师！！！"

    window hide

    pause 0.45

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}非常感谢！！！！！！{/size}"

    window hide

    pause 0.5

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_2486E9AC1518402DA6CBAA06B85610C8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_9379B2194CA6444BB5C1B77F9AAD8328 as tag_061CD0864C4E48C0B3AA935440B7C90D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 2

    stop music fadeout 3.5
    $ sys_music_current_file = ""

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 4

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "看，小翼，飞到那边了哦！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "小翼酱！把球拿到我这边来哦！"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_A469B787E7E7466FA1613F380A4CBF41 at right_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_CFFDD56807F84AE49F0D2F3347F610FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.8

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊——果然还是没到这边来啊……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "当然♪这就是构筑信赖关系的时间的差距！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_9D4ED68CEC2D4E5BA0296B4CA2A90847 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "总有一天一定要做到也拿到我这边来！！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Vibration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Vibration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Vibration 1.ogg"

    extend "嗡嗡"

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_DFDDF6139A514ABE9424DFC7D868DAB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，友、友君的电话！！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_8A9FD25CF2224DA4B5F560425D3A98A7 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    extend "是、是的！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯，现在和作、作哉君在一起玩……\n不对，还有小翼酱在一起玩。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，嗯，我、我明白了。那、那么稍后见！"

    window hide

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_0BD950ADC14245578BC5105060EF0E00 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    pause 0.4

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "怎么了？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "一起吃午饭的事。哈，哈哈……"

    show rs_image_345AD24DAEE64B9A963489B5AD613EE7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嗯……{w}……"

    window hide

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_F9DB849493A74F9BAC27649C80F4251D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.4

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "果然……"
    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 8.png
    $ zorder_rs_image_772ED68CBCDA4539B968C3D37984A791 = -100
    show rs_image_772ED68CBCDA4539B968C3D37984A791 as rs_image_772ED68CBCDA4539B968C3D37984A791 zorder zorder_rs_image_772ED68CBCDA4539B968C3D37984A791 onlayer master
    hide rs_image_772ED68CBCDA4539B968C3D37984A791

    show rs_image_772ED68CBCDA4539B968C3D37984A791 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.4

    extend "还是不能给你加油。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸、欸欸！！为、为什么……"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "啊，不。\n再说了我和友君也不是那种关系！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……我也，会让你注意到我的……{w}\n{nw}"
    extend "{size=14}……{/size}{size=12}总有一天一定会的。{/size}"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "好了，小翼！再来一次！！看好了！！！"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_B6D2CFDC1CB5407EACD7FBC1D100D198

    call scb_flag_title_end(2, _("「傲娇男孩子的治疗法」")) from _call_scb_flag_title_end_17

    if judge_lm_condition([]):
        jump block_00003AEB

    return

label block_00003AEB:
    # Node: 00003AEB (Phase: 0)
    $ C2S2Phase = 0
    if Chapter <> 2:
        $ del C2S1Phase
        $ del C2S2Phase
        $ del C2S3Phase
        $ del C2S4Phase
        $ del C2S5Phase
        $ del C2S6Phase
        $ del TalkMatsutaF2
        $ del TalkIzumiF2
        $ del TalkTsukiF2
        $ del TalkKatouF2
        $ del TalkNamekoF2
        $ del TalkShintaroF2
        $ del TalkShinobuF2
        $ del TalkSoraF2
        $ del C2QNewsclubPhase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_00003A29
    if judge_lm_condition([]):
        jump block_00003AEE

    return

label block_00003A29:
    # Node: 00003A29 ()

    return

label block_00003AEE:
    # Node: 00003AEE (FINISH)
    $ C2S2 = True
    $ F2Check1 = False

    if judge_lm_condition([]):
        jump block_00003AF1

    return

label block_00003AF1:
    # Node: 00003AF1 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_21

    if judge_lm_condition([]):
        jump block_00003AF0

    return

label block_00003AF0:
    # Node: 00003AF0 (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#3A00C4}“傲娇男孩子的治疗法”{/color}{color=#0080FF}成功结束。』{/color}"

    window hide

    pause 4

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003A29

    return

label block_00003A20:
    # Node: 00003A20 (2)
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 1.5

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 2.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_AB6075791E544455A4C21B3DCBA52E1C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_97AEAB5F7F86404C83B970C313450D38 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "感觉越来越好了呐！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "虽说还不是最好，但就这样努力下去没错。"

    window hide

    pause 0.5

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003A98

    return

label block_00003A21:
    # Node: 00003A21 (1)
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 1.5

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你到底都说了些什么啊？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "别说改善，我只觉得更糟了。算我求你了……"

    window hide

    pause 0.45

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.8

    $ set_window("(標準)")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『友和三朗的作战最终失败，没能改善两人的关系。』{/color}"

    stop music fadeout 1
    $ sys_music_current_file = ""

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Notice 1.ogg"

    if judge_lm_condition([]):
        jump block_00003A22

    return

label block_00003A22:
    # Node: 00003A22 (選擇)
    call scb_selector(_("要重试吗？"), [{"name":"はい", "content":_("再试一次")}, {"name":"いいえ", "content":_("等以后有办法再说吧")}]) from _call_scb_selector_73

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003A23
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" },{ "scope": 1, "content": "SYSTheaterState == 22" }]):
        jump block_00003A24
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00003A26

    return

label block_00003A23:
    # Node: 00003A23 (RETRY)
    $ C2S2Phase = 99
    $ F2PreviousStep = 0
    $ TalkMatsutaF2 = 0
    $ TalkIzumiF2 = 0
    $ TalkTsukiF2 = 0
    $ TalkKatouF2 = 0
    $ TalkNamekoF2 = 0
    $ TalkShintaroF2 = 0
    $ TalkShinobuF2 = 0
    $ TalkSoraF2 = 0

    if judge_lm_condition([]):
        jump block_00003A27

    return

label block_00003A27:
    # Node: 00003A27 ()

    return

label block_00003A24:
    # Node: 00003A24 (RESET)
    $ TalkMatsutaF2 = 0
    $ TalkIzumiF2 = 0
    $ TalkTsukiF2 = 0
    $ TalkKatouF2 = 0
    $ TalkNamekoF2 = 0
    $ TalkShintaroF2 = 0
    $ TalkShinobuF2 = 0
    $ TalkSoraF2 = 0
    $ C2S1Phase = 0
    $ C2S2Phase = 0
    $ C2S3Phase = 0
    $ C2S4Phase = 0
    $ C2S5Phase = 0
    $ C2S6Phase = 0
    $ del F2PreviousStep
    if Chapter <> 2:
        $ del TalkMatsutaF2
        $ del TalkIzumiF2
        $ del TalkTsukiF2
        $ del TalkKatouF2
        $ del TalkNamekoF2
        $ del TalkShintaroF2
        $ del TalkShinobuF2
        $ del TalkSoraF2
        $ del C2S1Phase
        $ del C2S2Phase
        $ del C2S3Phase
        $ del C2S4Phase
        $ del C2S5Phase
        $ del C2S6Phase

    if judge_lm_condition([]):
        jump block_00003A27

    return

label block_00003A26:
    # Node: 00003A26 (No)
    pause 1

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_00003A24

    return

label block_00003A18:
    # Node: 00003A18 (Lose)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_window("イベントモード")
    pause 0.6

    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    pause 0.4

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 1.png
    $ zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 = -100
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as rs_image_6A16110F14C64AA89B2FAD22D32413C7 zorder zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 onlayer master
    hide rs_image_6A16110F14C64AA89B2FAD22D32413C7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_A0BF18F892C54E3D9D094E5CD477ECEE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    # Gallery unlock: images/CG/Drug-for-tsundere/Drug-for-tsundere 1.png
    $ zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 = -100
    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as rs_image_6A16110F14C64AA89B2FAD22D32413C7 zorder zorder_rs_image_6A16110F14C64AA89B2FAD22D32413C7 onlayer master
    hide rs_image_6A16110F14C64AA89B2FAD22D32413C7

    show rs_image_6A16110F14C64AA89B2FAD22D32413C7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_A0BF18F892C54E3D9D094E5CD477ECEE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.9

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1.3

    if sys_effect2_current_file != "sound/Effect Sound/Wrong 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 0
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 1


    if judge_lm_condition([{ "scope": 0, "content": "TalkMatsutaF2 + TalkNamekoF2 + TalkShintaroF2 + TalkSoraF2 == 2" }]):
        jump block_00003A20
    if judge_lm_condition([]):
        jump block_00003A21

    return

label block_0000426E:
    # Node: 0000426E (Phase: 99)
    $ C2S2Phase = 99
    $ TalkMatsutaF2 = 0
    $ TalkIzumiF2 = 0
    $ TalkTsukiF2 = 0
    $ TalkKatouF2 = 0
    $ TalkNamekoF2 = 0
    $ TalkShintaroF2 = 0
    $ TalkShinobuF2 = 0
    $ TalkSoraF2 = 0
    $ F2PreviousStep = 0

    if judge_lm_condition([]):
        jump block_00003A11

    return

label block_00003A11:
    # Node: 00003A11 (F2 START)
    call scb_flag_title(2, _("「傲娇男孩子的治疗法」")) from _call_scb_flag_title_15

    if judge_lm_condition([]):
        jump block_00003A0F

    return

label block_00003A0F:
    # Node: 00003A0F (傲嬌男孩子的治療法 1)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    if sys_music_current_file != "sound/BGM/Daily 2.ogg":
        play music "sound/BGM/Daily 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 2.ogg"

    pause 1

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_8DC6F44BF4644738BCD14828D87C2679 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 0.5

    window show

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦？那家伙在那儿干什么。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好呀～呆毛少年♪"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    # Gallery unlock: images/CG/Pluck hair/Pluck hair 3.png
    $ zorder_rs_image_B370E5346ABB47548DAE9D421086387D = -100
    show rs_image_B370E5346ABB47548DAE9D421086387D as rs_image_B370E5346ABB47548DAE9D421086387D zorder zorder_rs_image_B370E5346ABB47548DAE9D421086387D onlayer master
    hide rs_image_B370E5346ABB47548DAE9D421086387D

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B370E5346ABB47548DAE9D421086387D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊嗯！！这、这个就算……！{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_A6E70EA9F30F4DE4AD20434ED388ACFF as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5FBD78374DA74E3DAE8DB6DA14DD5616 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "做什么啊猫君！不要每次都这样！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈哈，本能的驱使～"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那，咋了？好像有什么烦恼的样子。"

    show rs_image_E436CC5ED79D41EABE3ADFC40CD9F8B8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就是看他们两个不合拍的样子，\n觉得需要做些什么的感觉。"

    window hide

    pause 0.5

    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_862E41C0B01E451EB9C2E88AECBFEDBB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    if sys_effect_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    pause 0.5

    show rs_image_2B709367A1FA4DEF815337B5B014517C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    show rs_image_F477EFD4F5134EA9A29DCCDC67E15837 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    show rs_image_C6130C45B3154506B238905AA5DAD46A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.8

    stop effect fadeout 0.6
    $ sys_effect_current_file = ""

    show rs_image_E436CC5ED79D41EABE3ADFC40CD9F8B8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.4

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊——那个啊。不过，也没辙对不？\n穗海也确实是十几岁感情不稳定的年纪。"

    show rs_image_8DC6F44BF4644738BCD14828D87C2679 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个，和忍说的有些不太一样～"

    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "说什么了？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……嗯……"
    if sys_effect3_current_file != "sound/Effect Sound/Correct 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Correct 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Correct 1.ogg"

    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "对了！反动形成！！{size=12}{color=#C0C0C0}*心理学术语，俗称傲娇{/color}{/size}"

    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "反、反动？意义不明的成语，什么意思？"

    show rs_image_D41A51E2B16F4674B1A8FB746C8F1328 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "明明喜欢得要命却因为不好意思不得不隐藏起来，\n而为了隐藏会故意用不善的态度对待。"

    show rs_image_7D82D2EF95ED49EA821B9751FF70275C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就像技安对我的态度一样……{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯？难道说{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_E1E1F08446C54DCAAC86BEA1B671549E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "技安对我……"

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "（惊！！）"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "瞎、瞎说什么！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "至少这个所谓的反动形成的对象是一之濑才对吧！"

    show rs_image_3766CD2AF98244F5AECA23E096C299D8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "所以说和对翼君的情况有点不一样！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7303A840CCBB4DFCA4E6D8A50257852D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "再、再说了！{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "你、凭什么！{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_871E0CFED93745B19E9B12161459C49C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "知道这个～？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这都不过是你的推测而已吧～！？"

    show rs_image_C528CA6C6F534006B6F789027BE5C781 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我过去曾经{color=#008080}直接找他问过{/color}。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_166EF55B360E499C9F44815A403A153D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦，这么回事……"

    show rs_image_AAC229C565304B76BADD3819ED261CD1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那家伙完全不肯对我开口呐。\n这就是友情和爱情的区别么……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……啊。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_E777A5278A874BAB891650C04B85E3D7 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你看……这果然……"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不对不对不对不对！！\n你太自恋了——！！"

    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "其实啊那家伙最讨厌你了………\n{w=0.5}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不行不能这么明白地说啊！！"
    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不对，不是啊啊啊啊——！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_C34FAA8E3ADA4F78B2AEA97BA5E71368 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……???♪"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "原来如——此。哈哈～。技安对我……\n受、受欢迎的人真辛苦呐♪♪"

    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "诶，就这点儿反应……完全不意外？"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_6EA79B30E52B4FE8B90AB55D569F24D3 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我、我也终于有了受欢迎期？！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "虽说对方是那个技安有些不爽……\n算了，毕竟也没有恶意嘛～♪"

    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好像一切OK的样子呐……别指着鼻子上天了哦～？"

    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，啊……{w=0.45}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_35B9BEFBF42E474DB41387E9345C36B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "先不讨论这个了！\n……那个，我们刚才在说什么来着？"

    show rs_image_5FBD78374DA74E3DAE8DB6DA14DD5616 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "让穗海和一之濑和好的话题？\n如果你是真心的，我也会帮忙的。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "毕竟我和他在同一个班，多少有点儿用。"

    show rs_image_39EA77FDE17745CA860489ACA0F6FAFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真的？帮大忙了～\n能更多了解技安的想法的话事情也会好做不少。"

    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不是很明白你想干嘛，不过先从这个大方向开始好了。"

    show rs_image_97AEAB5F7F86404C83B970C313450D38 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那你去找穗海说几句，知道他到底是在烦恼什么也是不错的。"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_07E85511B35D42B2A68B24FACDB172AB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！就这么干！"

    if sys_music2_current_file != "sound/Effect Sound/Kirakira 1.ogg":
        play music2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_CFCEEA46658B45C38D3ED429DE9FF37D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好人啊……可以被托付呐。穗海，你的眼光真是不错。"

    show rs_image_6EA79B30E52B4FE8B90AB55D569F24D3 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼♪"

    show rs_image_13EEE138043542FB90557CFB44BADDE4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那我会在远方看着，要是两人的气氛有什么变化再来报告。"

    show rs_image_A56A27CF00F74EF798B09E4211817332 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "拜托你了！！{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    extend "加油让两人和好哦——！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦！！"

    window hide

    pause 0.4

    stop music fadeout 1.4
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A5B05E7D36FC49258CAE9B6EEA5B58E4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.8

    window show

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_E436CC5ED79D41EABE3ADFC40CD9F8B8 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说是那么说，我也没经验，\n也不知道说什么话比较好。"

    show rs_image_7A5E7A2647AF4CDB9D44AF0B2AE80DFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "总之先和尽可能多的人谈谈获得一些建议，\n然后再去试试！"

    window hide

    pause 0.4

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54


    if judge_lm_condition([{ "scope": 0, "content": "Chapter <> 2" }]):
        jump block_00003C81
    if judge_lm_condition([]):
        jump block_00003A12

    return

label block_00003C81:
    # Node: 00003C81 (CP2 Daytime)
    call block_000008C9 from _call_block_000008C9_1

    if judge_lm_condition([]):
        jump block_00003A12

    return

label block_00003A12:
    # Node: 00003A12 ()

    return

