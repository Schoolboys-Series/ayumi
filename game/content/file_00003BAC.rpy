# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003BAC (FLAG: 歡迎來到食人狼之館)

label block_00003BAD:
    # Node: 00003BAD ()

    if judge_lm_condition([]):
        jump block_00003BB1

    return

label block_00003BB1:
    # Node: 00003BB1 (Phase: 99)
    if Not(VarExists("C2S6Phase")):
        $ C2S6Phase = 0
    $ C2S6Phase = 99

    if judge_lm_condition([]):
        jump block_00003BB2

    return

label block_00003BB2:
    # Node: 00003BB2 (F6 START)
    call scb_flag_title(2, "", "rs_image_FC29A6E108FC420AA588728CD98B7C3B") from _call_scb_flag_title_7

    if judge_lm_condition([]):
        jump block_00003BAE

    return

label block_00003BAE:
    # Node: 00003BAE (歡迎來到食人狼之館 1)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_91F4C74E7B844945A9976F914A36207F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EF2D3A4912BA490B9BDDB92C8700586E

    pause 0.5

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B5F32270AAE048CBBB7C1FB4F6FD6163 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你、你是……？！"

    pause 0.3

    window hide

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8EA9E85B46784DACB020EB442B0BD905 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_B5F32270AAE048CBBB7C1FB4F6FD6163 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-50, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.5

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_FDB36A5B31714742AD6D29EB49DC75EB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.4

    window show

    if sys_music_current_file != "sound/BGM/Stage of HERO.ogg":
        play music "sound/BGM/Stage of HERO.ogg" loop
        $ sys_music_current_file = "sound/BGM/Stage of HERO.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那两只是栖息在魔法森林的暗黑小熊猫，不知为什么到街上来了！"

    show rs_image_8324EB6AB2224B36AD6FF9F96528FCC6 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "这里就由我来处理，趁现在快逃！"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E0106261369045C782EB83331069C3DE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "到、到底怎么了？？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不过，这样一来你就……！"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_296DD986D1424E4AA97E52E2A1ECE378 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "没关系，交给我夕阳！这种程度的怪物退治轻松轻松♪"

    pause 0.3

    window hide

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_7450C580738B49679036CAD4B9A13B61 = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 400
    $ zorder_tag_359C09A6BFDC41098D3302BF3F292D65 = 300
    show rs_image_7354908CD2ED469180084AE15C3932F1 as tag_7450C580738B49679036CAD4B9A13B61 at Transform(xpos=370, yalign=0.0) zorder zorder_tag_7450C580738B49679036CAD4B9A13B61 onlayer master
    show rs_image_8EA9E85B46784DACB020EB442B0BD905 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_69ED399C69E74B6BACE72BFAE0862603 as tag_359C09A6BFDC41098D3302BF3F292D65 at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_359C09A6BFDC41098D3302BF3F292D65 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FDB36A5B31714742AD6D29EB49DC75EB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "好了，放马过来暗黑小熊猫！ "

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_359C09A6BFDC41098D3302BF3F292D65
    hide tag_7450C580738B49679036CAD4B9A13B61
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_E436CC5ED79D41EABE3ADFC40CD9F8B8 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B5F32270AAE048CBBB7C1FB4F6FD6163 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "“夕阳”是，{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "和{color=#00FFFF}那部漫画{/color}同名的……？\n呜哇——就像真的一样，比忍还中二……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不、不用你管！别废话了快给我站直小鹿{size=12}{color=#C0C0C0}（形容双腿颤抖的样子）{/color}{/size}友。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    stop music fadeout 1
    $ sys_music_current_file = ""

    window hide

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_7450C580738B49679036CAD4B9A13B61 = 300
    $ zorder_tag_359C09A6BFDC41098D3302BF3F292D65 = 300
    show rs_image_7354908CD2ED469180084AE15C3932F1 as tag_7450C580738B49679036CAD4B9A13B61 at Transform(xpos=350, yalign=0.0) zorder zorder_tag_7450C580738B49679036CAD4B9A13B61 onlayer master
    show rs_image_69ED399C69E74B6BACE72BFAE0862603 as tag_359C09A6BFDC41098D3302BF3F292D65 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_359C09A6BFDC41098D3302BF3F292D65 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.5

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_14D93B8AB16E48EC96B0BFCF32697307 as tag_7450C580738B49679036CAD4B9A13B61 zorder zorder_tag_7450C580738B49679036CAD4B9A13B61 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_94BAB10DED8E4AE2B5B532EDC28ACA68 "姆——！姆——！不是这样的不是这样的！"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_14D93B8AB16E48EC96B0BFCF32697307 as tag_359C09A6BFDC41098D3302BF3F292D65 zorder zorder_tag_359C09A6BFDC41098D3302BF3F292D65 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_65542CC27A6A4181AB83137C808B452F "这是你们的误解！"

    rs_character_94BAB10DED8E4AE2B5B532EDC28ACA68 "请好好听我们说到最后。"

    rs_character_65542CC27A6A4181AB83137C808B452F "我们只是在经商而已。"

    hide tag_7450C580738B49679036CAD4B9A13B61
    hide tag_359C09A6BFDC41098D3302BF3F292D65
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_7450C580738B49679036CAD4B9A13B61 = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_359C09A6BFDC41098D3302BF3F292D65 = 300
    show rs_image_14D93B8AB16E48EC96B0BFCF32697307 as tag_7450C580738B49679036CAD4B9A13B61 at Transform(xpos=370, yalign=0.0) zorder zorder_tag_7450C580738B49679036CAD4B9A13B61 onlayer master
    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_14D93B8AB16E48EC96B0BFCF32697307 as tag_359C09A6BFDC41098D3302BF3F292D65 at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_359C09A6BFDC41098D3302BF3F292D65 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "嗯？仔细看看确实只是布偶装……？那你们的目的是……"

    show rs_image_69ED399C69E74B6BACE72BFAE0862603 as tag_7450C580738B49679036CAD4B9A13B61 zorder zorder_tag_7450C580738B49679036CAD4B9A13B61 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "请仔细听好了。"

    show rs_image_7354908CD2ED469180084AE15C3932F1 as tag_359C09A6BFDC41098D3302BF3F292D65 zorder zorder_tag_359C09A6BFDC41098D3302BF3F292D65 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_50A3B84756FC458695CF53C0DC1DC85C "那就重整气势……"

    hide tag_7450C580738B49679036CAD4B9A13B61
    hide tag_359C09A6BFDC41098D3302BF3F292D65
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    # Gallery unlock: images/CG/Welcomt-to-wolfs-celemony/Welcomt-to-wolfs-celemony 1.png
    $ zorder_rs_image_3B43238981B5446E810F4A35352A9D94 = -100
    show rs_image_3B43238981B5446E810F4A35352A9D94 as rs_image_3B43238981B5446E810F4A35352A9D94 zorder zorder_rs_image_3B43238981B5446E810F4A35352A9D94 onlayer master
    hide rs_image_3B43238981B5446E810F4A35352A9D94

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3B43238981B5446E810F4A35352A9D94 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "走过路过都来看看！"

    rs_character_50A3B84756FC458695CF53C0DC1DC85C "大家都喜闻乐见的抽奖哦！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "好了——少年们，不来试试吗？不来看看吗？"

    rs_character_50A3B84756FC458695CF53C0DC1DC85C "过了这个村就没这个店了哦。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "就是这样。要说为什么的话，只有现在，免费抽奖！"

    rs_character_50A3B84756FC458695CF53C0DC1DC85C "一等奖是{color=#FFFF00}三天两夜{/color}的豪华旅行券哦。"

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    rs_character_F798676F0E9448499D48B0E2448BB32D "快——快——！来！试试！走过路过都来看看！"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_AB838172A2DB46ABA7F4AC2B3C09693D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "什么啊……还以为是被强行推销了，只是宣传啊。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7D82D2EF95ED49EA821B9751FF70275C as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-50, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的～基本上忍总是会大惊小怪地误会呐——\n要好好反省哦——"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_69663BD5BF254491A6E7462E56A2621F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "要再变小鹿一次？"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "这还真是对不起，虽然想谢罪这次就先允许我口头上说说。"

    show rs_image_39EA77FDE17745CA860489ACA0F6FAFC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍！我们也来试试。好不容易有免费的！"

    show rs_image_1F55CB120A6948E28641DFC1C52982EE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯、嗯。"

    window hide

    pause 0.4

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Lottery 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Lottery 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Lottery 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}嘎啦嘎啦{/size}\n{w=0.8}{nw}"
    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    if sys_effect2_current_file != "sound/Effect Sound/Lottery 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Lottery 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Lottery 1.ogg"

    extend "{size=28}嘎啦嘎啦{/size}{w=0.8}"

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    pause 0.5

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "从你们身上感觉到了无比愉悦的能量。"

    rs_character_50A3B84756FC458695CF53C0DC1DC85C "肯定，能摇出好结果的。"

    window hide

    pause 0.4

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 3.5

    if sys_effect3_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_735E3DE57F8F40979A42554EDFC9B275 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_933B4652A6BC4717B52077103CB5742A

    pause 0.8

    window show

    $ zorder_tag_359C09A6BFDC41098D3302BF3F292D65 = 300
    $ zorder_tag_7450C580738B49679036CAD4B9A13B61 = 300
    show rs_image_69ED399C69E74B6BACE72BFAE0862603 as tag_359C09A6BFDC41098D3302BF3F292D65 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_359C09A6BFDC41098D3302BF3F292D65 onlayer master
    show rs_image_69ED399C69E74B6BACE72BFAE0862603 as tag_7450C580738B49679036CAD4B9A13B61 at Transform(xpos=350, yalign=0.0) zorder zorder_tag_7450C580738B49679036CAD4B9A13B61 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "这样就好。"

    rs_character_50A3B84756FC458695CF53C0DC1DC85C "那就……"

    hide tag_7450C580738B49679036CAD4B9A13B61
    hide tag_359C09A6BFDC41098D3302BF3F292D65
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_82CC0337267A43429DF54A35A9B24DFB = 300
    show rs_image_4692ED5E5B26488589FEF7BB7C852930 as tag_82CC0337267A43429DF54A35A9B24DFB at center_top zorder zorder_tag_82CC0337267A43429DF54A35A9B24DFB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    rs_character_9EDF48057FB84D428D56198A69E2880E "哦，有抽奖啊！一等奖是什么？让我也来一次。"

    hide tag_82CC0337267A43429DF54A35A9B24DFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_359C09A6BFDC41098D3302BF3F292D65 = 300
    $ zorder_tag_7450C580738B49679036CAD4B9A13B61 = 200
    show rs_image_69ED399C69E74B6BACE72BFAE0862603 as tag_359C09A6BFDC41098D3302BF3F292D65 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_359C09A6BFDC41098D3302BF3F292D65 onlayer master
    show rs_image_7354908CD2ED469180084AE15C3932F1 as tag_7450C580738B49679036CAD4B9A13B61 at Transform(xpos=370, yalign=0.0) zorder zorder_tag_7450C580738B49679036CAD4B9A13B61 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "……"

    rs_character_50A3B84756FC458695CF53C0DC1DC85C "……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_82CC0337267A43429DF54A35A9B24DFB = 300
    show rs_image_3AD096BAE82A4EF8833A719597517605 as tag_82CC0337267A43429DF54A35A9B24DFB at center_top zorder zorder_tag_82CC0337267A43429DF54A35A9B24DFB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_BC9CC5BA3ABB4C879D557212A41DCBAC "就、就来一次嘛！让我也摇个奖。"

    show rs_image_69ED399C69E74B6BACE72BFAE0862603 as tag_7450C580738B49679036CAD4B9A13B61 zorder zorder_tag_7450C580738B49679036CAD4B9A13B61 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "你这样的大叔我们没兴趣。"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DF15114974EF49E58EECE21C61E86DE1 as tag_82CC0337267A43429DF54A35A9B24DFB zorder zorder_tag_82CC0337267A43429DF54A35A9B24DFB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EDF48057FB84D428D56198A69E2880E "大、大叔！？怎么这么失礼！！\n看起来这样我才25岁！肌肉也……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_7354908CD2ED469180084AE15C3932F1 as tag_359C09A6BFDC41098D3302BF3F292D65 zorder zorder_tag_359C09A6BFDC41098D3302BF3F292D65 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_50A3B84756FC458695CF53C0DC1DC85C "给我消失。"

    hide tag_7450C580738B49679036CAD4B9A13B61
    hide tag_359C09A6BFDC41098D3302BF3F292D65
    hide tag_82CC0337267A43429DF54A35A9B24DFB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_359C09A6BFDC41098D3302BF3F292D65 = 300
    $ zorder_tag_7450C580738B49679036CAD4B9A13B61 = 300
    show rs_image_69ED399C69E74B6BACE72BFAE0862603 as tag_359C09A6BFDC41098D3302BF3F292D65 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_359C09A6BFDC41098D3302BF3F292D65 onlayer master
    show rs_image_69ED399C69E74B6BACE72BFAE0862603 as tag_7450C580738B49679036CAD4B9A13B61 at Transform(xpos=350, yalign=0.0) zorder zorder_tag_7450C580738B49679036CAD4B9A13B61 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7103FCF0405049A2A9636492EB968B3F as tag_359C09A6BFDC41098D3302BF3F292D65 zorder zorder_tag_359C09A6BFDC41098D3302BF3F292D65 onlayer master
    show rs_image_7103FCF0405049A2A9636492EB968B3F as tag_7450C580738B49679036CAD4B9A13B61 zorder zorder_tag_7450C580738B49679036CAD4B9A13B61 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    rs_character_F798676F0E9448499D48B0E2448BB32D "{size=32}快・{/size}{w=0.3}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    extend "{size=32}滚！！{/size}"

    pause 0.3

    hide tag_7450C580738B49679036CAD4B9A13B61
    hide tag_359C09A6BFDC41098D3302BF3F292D65
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_82CC0337267A43429DF54A35A9B24DFB = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DF15114974EF49E58EECE21C61E86DE1 as tag_82CC0337267A43429DF54A35A9B24DFB at center_top zorder zorder_tag_82CC0337267A43429DF54A35A9B24DFB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "噫、噫——！对不起！！"

    window hide

    hide tag_82CC0337267A43429DF54A35A9B24DFB
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    hide tag_82CC0337267A43429DF54A35A9B24DFB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_CAE7E1A8F1B9452F9A07D2E1DAAE9E40

    pause 3.5

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀～哈哈！啊——哈哈！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这种事也是有的呐。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这就是我们两个作为青梅竹马的力量吗？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "简直就是奇迹……"

    pause 0.5

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    window hide

    show rs_image_5EDDC724AF604AB8A3EC3F0CD2F0C4D6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    pause 0.5

    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_2D2761902CAE44EC807DF631A55BE304 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说起来，大家都能按时来么？\n从学校出来的时候没什么特别的，应该没事。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_CA176C5A71144199A2E3AE0C60846C57 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "有三天两夜的旅行的话，也只能选星期五了呐～♪"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A56A27CF00F74EF798B09E4211817332 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "小的们——！都来了吗——！？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_8C8329CA4FC34C279A723168C0AA6CC0 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "来了队长——！一班队全员都到齐了——！"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_A62DFA8FA08E4BD2B83B9B282B530095 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我还是第一次和大家一起旅行，有些不安呐。而且也有种成熟的感觉。"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_32D03B1B0EA34051AEC7EDA0B618F93C as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯。这也是通向我们自立的第一步。都是至今为止没有过的体验。"

    window hide

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这、这边二班队也都没有问题……"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_C6130C45B3154506B238905AA5DAD46A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那个！这、这次小的蒙幸被大人招待到如此尊贵的地方，\n真的万分感谢……！"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "冷静点一之濑，客气得太厉害了，"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "太大惊小怪了♪"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "没意思。啊——跟这些家伙根本玩不起来——"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_A56A27CF00F74EF798B09E4211817332 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么！？面对这么愉快的我们不可能高兴不起来的！"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "烦人。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_4426ECB7E6A8443FB128590CB7FEBB64 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_58CAC53C853A4ECC97CAB3038D1CAAF0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "算了算了，作哉君。这种机会也不多见，不要那么说开心去玩就好！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……不管怎样我们都是没问题的。\n"
    show rs_image_AB838172A2DB46ABA7F4AC2B3C09693D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "你们那边怎么样？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    show rs_image_202D019D0CEB444FB06F28FE932B89CB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 0.6

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_8324EB6AB2224B36AD6FF9F96528FCC6 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哦！完全没有问题！"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_3E667A569CC54E86B612A79E21C9EC9E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_57471360F48A413AB843A4E46D8C5541 "哈哈，我们这边只有两人呢。 你们那边人数多看起来更开心的样子呐。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_7D2835EC10DE4438B9BBE9F8CE5454F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "与其说热闹不如说就是折腾人……旅行期间请多多关照了。"
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_9E7B821A26DB4648BA5980B3C4E75E0D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_34FE71D3EB71405D8A5DEB69161B5815 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哦！同时中奖绝对是有缘分。\n"
    show rs_image_5AE10526B987417DB3A2B8B5DFDA6F3A as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_1382C936693A4354B456F9C02B592547 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "大家都不用说敬语好好放松即可！"

    show rs_image_63B779B9C18C4ECDA43D5CD785679229 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "……那不是我们该说的。那边才是比我们高一级的前辈。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "诶！！？真的？！！这、这还真是失礼了……！！抱歉，前辈！！"

    show rs_image_0C866D450EF342189ED1497939E81294 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不、不用、不用在意。……经常会被认错，已经习惯了……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "啊啊啊……那个、那个……\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_CA65E37C24FB460390BADAD95767936C as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哦！说起来，说好的导游呢，好慢啊！"

    show rs_image_2D2761902CAE44EC807DF631A55BE304 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_309B0F3F61544BA188E845B4B474794B as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "确实，已经到集合时间了。一般不是该举着旗子一开始就在这里等着吗。"

    window hide

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_AB838172A2DB46ABA7F4AC2B3C09693D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯？有向这边走过来的人……"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_BEE780ABA64C4D7ABB8972D17BDCBFAB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "呃——不，那人肯定不是。你看，那么…"

    window hide

    pause 0.5

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 = 300
    show rs_image_202D019D0CEB444FB06F28FE932B89CB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_15C90FB54265499E9E746DBDA51DE57E as tag_51E1CA5715FC4887A4E4083BB8D521B0 at center_top zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.7

    window show

    if sys_music_current_file != "sound/BGM/Hotel 1.ogg":
        play music "sound/BGM/Hotel 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 1.ogg"

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "大家久等了，我是这次负责导游的人。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D3230CCCAA744196B463EF066186F3A0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——！来了来了——！请多关照！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……不觉得晚了么？各种意义上……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_40F4B3A56AFE46FCB14F4500CD625791 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我是第一次遇到这种事所以不大明白……\n那货就是导游？穿的也太奇特了？？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "有何不可呢？有种无法预测的旅行的预感！我还是挺激动的～！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 = 300
    show rs_image_15C90FB54265499E9E746DBDA51DE57E as tag_51E1CA5715FC4887A4E4083BB8D521B0 at center_top zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "波乱万丈奇奇怪怪、奇想天外吃惊仰天！\n接下来会是何种旅行……"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "大家，敬请期待。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1382C936693A4354B456F9C02B592547 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "什么……"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_2B709367A1FA4DEF815337B5B014517C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……好的。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊哈哈！气氛不错嘛——！！和慎酱说的一样很有意思呐！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    show rs_image_5EDDC724AF604AB8A3EC3F0CD2F0C4D6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_9A51889A5B884F76838CF8C5D3725812 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯？哥哥，在读什么呢？"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_77C99743D39944F9AD8542E6C1310363 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "导游给的关于要住的酒店的手册。"

    show rs_image_6EA78EC2093A46F097116A0C2CBB397C as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我也调查过了。本来是岛上很老的房屋，最近改造成了旅游设施。"

    show rs_image_D7269F0DB3AF45BD8855E0CB4A5B4F64 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯，不过这幢房子非常宏伟，原来的主人可能是很有名的权力者。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_9A51889A5B884F76838CF8C5D3725812 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_06490EED355B4895A201B8859DA0B711 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不过，岛上除了这幢房子什么都没有。为何要在那种地方……"

    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼，感觉会发生什么的样子呐～就像是暴风雨前的宁静♪"

    show rs_image_2D0EC305038C4AE5AB71CFDA0756ACD1 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "慎、慎酱！不要说那种不吉利的话。"

    show rs_image_88D1205AA473480CA2A73E26453C1F61 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……毫无人气的迷之房屋。感觉就像要发生什么的样子不太舒服。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_F738E6401CA340F19552857151823031 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥也……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_202D019D0CEB444FB06F28FE932B89CB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_296DD986D1424E4AA97E52E2A1ECE378 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_C9B3C83238F74DF0BD84400376826860 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "嘛，万一真发生什么，我们跟着也不会有事的！对不对！守。"

    show rs_image_6D5D3AE8CDB84C189402900F68982BCB as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_57471360F48A413AB843A4E46D8C5541 "没看天气预报吗？那边在下雨。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "！？"

    show rs_image_63B779B9C18C4ECDA43D5CD785679229 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_57471360F48A413AB843A4E46D8C5541 "……早知道就该学学其他属性的……"

    window hide

    pause 0.5

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "这时谁都不曾预想。{w}接下来，究竟会发生何等惨事……"

    window hide

    pause 2

    stop music fadeout 3
    $ sys_music_current_file = ""

    $ zorder_tag_99488938252D4BC2B7FA91D436D9159B = 0
    show rs_image_FC29A6E108FC420AA588728CD98B7C3B as tag_99488938252D4BC2B7FA91D436D9159B at center_bottom zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_A2063DA9B93D48538E9C5EF0D4403826 as tag_99488938252D4BC2B7FA91D436D9159B zorder zorder_tag_99488938252D4BC2B7FA91D436D9159B onlayer master
    with rs_effect_7E92C9134E124E86A660C199B445F321

    pause 3

    hide tag_99488938252D4BC2B7FA91D436D9159B
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2

    if sys_effect3_current_file != "sound/Effect Sound/Wave 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Wave 2.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Wave 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_090B423E9FDD4F1BA744187FBD7BB4A9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_266255D4821A4095BCA7860D44F0A511

    pause 2.5

    show rs_image_8409DB7FAADF495087B6E4B602F1F374 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DCEBC7527B8F4B4EA0FF44E692174034

    pause 2

    window show

    $ zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 = 300
    show rs_image_15C90FB54265499E9E746DBDA51DE57E as tag_51E1CA5715FC4887A4E4083BB8D521B0 at center_top zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "大家长途旅行都辛苦了。这边就是这次住宿的酒店。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_6EA79B30E52B4FE8B90AB55D569F24D3 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦哦——！洋风的好壮观♪"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦——！爱情酒店风的好下流♪"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_7303A840CCBB4DFCA4E6D8A50257852D as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "自重一点。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜……"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "还在晕车？……谁带药了？"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_6EA78EC2093A46F097116A0C2CBB397C as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊，我带着哦！是从商店买的，应该没有问题。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_32D03B1B0EA34051AEC7EDA0B618F93C as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_ECD1914DBFDB442F9D1A9232EEEC99F6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "健身房也有……绫濑，等下要不要去试试？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不错嘛。在大浴场可以多出出汗，要是有桑拿就更好了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_07F2639BB0524AEBB4F93F1989365243 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "……"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_BEE780ABA64C4D7ABB8972D17BDCBFAB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_2CBCC9210CD74C28AD7E00D435D40944 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_57471360F48A413AB843A4E46D8C5541 "“啊啊，要是喜欢的那个孩子能来就好了呐”\n这样的想法在夕阳君心中驰骋。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "诶！？才没有！只是在想能不下雨就好了……"

    show rs_image_3E667A569CC54E86B612A79E21C9EC9E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "说不准——♪我也这么想的。能和喜欢的人来的话，\n定能度过美妙而又激情的浪漫之夜的。"

    show rs_image_B07AFDECD18C45CCA1315EC195BD4924 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "一个人开心个什么劲呢——？不会接你话的。"

    window hide

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect4_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect4 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect4_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_20D7877A2F1F4E259A2B708FC501260A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯——？嗯？嗯？嗯嗯？？"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_12E394DC341C4685AB17E83FEED856C9 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "怎么了友亲？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我的……我的呆毛好疼……"

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_58CAC53C853A4ECC97CAB3038D1CAAF0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说起来突然就阴天了呐。{w}啊，好像开始下雨了……？"

    window hide

    stop effect4 fadeout 1
    $ sys_effect4_current_file = ""

    pause 0.5

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Rain 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Rain 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Rain 1.ogg"

    show rs_image_6D595FD5594145118D9588130020DDB7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 1.5

    window show

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_C224FD27FE6D4ECA8B284AE1B4580EE3 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哇啊啊啊撤退撤退！！快点进去！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "赞成！！要淋湿了……！！用不出力量了——！！"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.5

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F1E694F9D98E4371B8F767497249ECEE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "还在想外面那么大声音……{w}真是意外的客人呐。"

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_F1E694F9D98E4371B8F767497249ECEE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D7DFB9C596074724958BBE78FF9336D3 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1.5

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_BE7A49A1C27E4A9EAA9EEF3DB775CAA5 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "欸！？！？"

    rs_character_57471360F48A413AB843A4E46D8C5541 "……哇哦。"

    window hide

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_music_current_file != "sound/BGM/Hotel 2.ogg":
        play music "sound/BGM/Hotel 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 2.ogg"

    $ zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 = 300
    show rs_image_15C90FB54265499E9E746DBDA51DE57E as tag_51E1CA5715FC4887A4E4083BB8D521B0 at center_top zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    window show

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "抱歉忘记提醒，这家酒店除了客人们还有其他人正在留宿。"

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "虽然是不情之请，但在此之上并没有更多的住客了，还请原谅。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1382C936693A4354B456F9C02B592547 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，朔同学……？"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "这可真是这可真是，你好，忍同学。奇遇呐，没想到会在这里相见。"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，什么什么忍——！这个人是谁，认识的人？？"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "朔、朔，这是怎么回事！为什么你会在这里……？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_A477062F5CFB45259A5183ED5584C4A5 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "这句话原封不动还给你。你们这群人来这家酒店……\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "哦，难道是迷路了？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔，这个混蛋……！还是一样讨人厌！"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_2CBCC9210CD74C28AD7E00D435D40944 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_57471360F48A413AB843A4E46D8C5541 "“但就是这一点令人着迷”……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_829EA2AED9E74CD48751411FB95D579D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "没这么想！"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "等下小忍！我可是第一次听说你认识这位美少年呐！\n请务必要介绍给我哦。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_EB543C918F764BD48AF5945B5D7C3278 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，嗯。这个人是朔同学，比我们小一岁。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "之前{color=#008080}有点事{/color}认识的，意气相投，好几次一起去买衣服或者吃饭……{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_7A3C9E061A0A41F8A958F8DCCCD8E4F1 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_829EA2AED9E74CD48751411FB95D579D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    rs_character_D7D446D4EF214185919394BD0E4F7E9F "我、我为什么不知道——！！"

    window hide

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_829EA2AED9E74CD48751411FB95D579D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "等等忍——！到底是怎么回事——！"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "居然在我不知道的时候和一般人有关系什么的！"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_EDB46CC6778D4FE0858464DE11647DF8 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    show rs_image_1F55CB120A6948E28641DFC1C52982EE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "就像这样一直都不得安宁很烦人呐。\n果然和朔同学一样的人一起的话更轻松一些。"

    rs_character_62324AD297554FE987C680452CEE232E "我也是，下次两人单独去喝个茶如何，忍同学。"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_C224FD27FE6D4ECA8B284AE1B4580EE3 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D7D446D4EF214185919394BD0E4F7E9F "打击——！"

    window hide

    pause 0.5

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    if sys_music_current_file != "sound/BGM/Hotel 1.ogg":
        play music "sound/BGM/Hotel 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 1.ogg"

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_852B096D59124B62B0799807BDED56B9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "（得找朔问问他为什么在这儿。{w}是有什么企图的话……）"

    window hide

    pause 0.4


    if judge_lm_condition([]):
        jump block_00003BB0

    return

label block_00003BB0:
    # Node: 00003BB0 (CP2 Daytime Hotel 夕阳)
    call block_000016B8 from _call_block_000016B8

    if judge_lm_condition([]):
        jump block_00003C0D

    return

label block_00003C0D:
    # Node: 00003C0D (朔)
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_DF96629E3C094B5BABD9997F95BF9E05 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_bottom zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "好、好啊，朔。"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_549D7A2FAB2B42648E7732B40B528C81 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "什么事？官能师。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "是魔法师！魔・法・师！！"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2D9D55E1273147FD916194309B9601B8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "呵呵，好不容易的休息日，居然要和你们这样的人住在一起……"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "休息日？毕竟是你，这次是不是又在策划什么把大家卷入的不好的事了！？"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1F690B307ECA4450A3C108BA53BF04F7 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "你到底是怎么看待我的。{w}\n又不是机器人，不要那么每天不厌其烦地问。"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8C1D521DD2674B0DA55662B722509124 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "为了以后能更加努力，休息是必要的。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_62324AD297554FE987C680452CEE232E "好好休息才能好好工作。"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那、那，一直跟着你的蚯蚓和海星……？"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_549D7A2FAB2B42648E7732B40B528C81 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "他们和我相同正在休假。"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "……你说的是真的？"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_906E8E500D7F4E8AA9C3632B62F2E0B0 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "这点都不相信的话，\n那就请自称・正义的伙伴的这位一天二十四小时好好看住我好了？"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔……内容有些不爽，不过为了伸张正义，这个提案就采用了。"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_ABA396FD0541426CA6A38D0EE9906714 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "不爽的是我。"

    rs_character_62324AD297554FE987C680452CEE232E "被把我的笑话当真的疑神疑鬼的英雄（笑）尾行了。"

    show rs_image_2D9D55E1273147FD916194309B9601B8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "这下完全休息不成了，洗澡和睡觉时也完全没气氛了。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_8C1D521DD2674B0DA55662B722509124 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "不好不好，有企图的到底是谁呐。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "别、别说胡话！！我、我怎么可能会有那种想法！\n一丁点……完全……"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DF96629E3C094B5BABD9997F95BF9E05 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "不过，真的没关系？{w}\n克服那个下雨天不能用魔法的滑稽的弱点了？？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "啊，这、这个……"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5F20890023EB412E8D944257C7FB2984 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "真是不得不同情那些把和平托付给连这点力量都没有的你的一般人啊。"

    rs_character_62324AD297554FE987C680452CEE232E "真是可怜。（假哭）"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "这、这次肯定没事。我可是好好准备了万一出问题时的后手……！"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_92D2A7D46D3F4DAC95D04FE48731EA3C as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "哦？这可真是有意思。可以好好帮我打发休息时的无聊时间了。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_62324AD297554FE987C680452CEE232E "无能的魔法师先生。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("休息室"))
    pause 0.7

    stop music fadeout 1
    $ sys_music_current_file = ""

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003C0E

    return

label block_00003C0E:
    # Node: 00003C0E (歡迎來到食人狼之館 2)
    $ set_window("イベントモード")
    if sys_effect2_current_file != "sound/Effect Sound/Wind 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_FAA9D8A675FC415AB14CBE14F1E2FACC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 2

    show rs_image_8E4DA8AB5E3E4DE48FD5D779B0D4B69D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 2

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_0FFAFB81CEF94E09AE209050BCCD9627 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 1.3

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_03464FF4C9E0402D927F78F065C5045C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不愧是最高级酒店，晚饭也这么棒！肚子都快吃爆了！"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "确实好吃但刀叉也太多了，全部用一个不就完了，麻烦。"

    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "确实，叉子吃沙拉太难了，要是能用平常的餐具就好了呐，洗起来也好洗。"

    show rs_image_DC032925F8E44CCD8BEB9B1A25FD6E70 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "简直就是The・平民的做派～这种感觉。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈哈，真的真的！"

    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "说起来，其他人呢？{w}赤峰兄弟之前好像拿着扫帚，是想扫除么？"

    show rs_image_9138D3EAFC66405AA95FD2DC03C7E56E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "谁知道？{w}奥村和……世依木君？\n那两个人在那边好像有什么话单独去说了。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_D21B7923E9E24A7C92B7226F129DCD18 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_9387C2EF08BB4EFABA360A19A1E02C8B as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "阿夕和朔朔已经回房间了？\n也就是说，现在已经突入超级腻腻歪歪时间了？？"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_63B779B9C18C4ECDA43D5CD785679229 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_57471360F48A413AB843A4E46D8C5541 "不觉得那还太早了吗……？"

    show rs_image_F4C733D956094DDB90D3AE4E82A63BAA as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "不过话说回来，夕阳那家伙真是容易明白。\n见到朔同学后马上就黏上去了。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "要是老天爷能看明白气氛，适当弄点飓风来的话，也能期待一下吊桥效果呐。"

    show rs_image_3E667A569CC54E86B612A79E21C9EC9E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "就算那样也不会吧……\n"
    show rs_image_34FE71D3EB71405D8A5DEB69161B5815 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……不过，有些羡慕呐，能和喜欢的人一起度过这段时间。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_40F4B3A56AFE46FCB14F4500CD625791 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦呀～？难道守守也有这样的对象？单相思？还是说互相喜欢？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_15CB7C3DA9944B5EB971E19E67C5985F as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "啊……这个，勉、勉强算后者……"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3B13044431874BE09020F9368D6A8C29 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦～！什么嘛——！我想听听你那方面的事～！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_5AE10526B987417DB3A2B8B5DFDA6F3A as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "不，这就有点……话、话题到此为止。结束了，下面的都是秘密了！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈哈！害羞的守守好赞！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "原来如此！所以看到阿夕朔朔夫妇会寂寞呐！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8C8329CA4FC34C279A723168C0AA6CC0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这下子只能回房间如字面所述好好安慰自己了呐！\n多么美妙，多么官能！快忍不住了！"

    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BE7A49A1C27E4A9EAA9EEF3DB775CAA5 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_FCA6F7B3890945579DF74C8C87790626 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我也去帮忙——！守守只要闭上眼睛，想着对方……"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F0C1E10C15B741529B76E18168EFAE45 = 100
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 100
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_F0C1E10C15B741529B76E18168EFAE45 at right_top zorder zorder_tag_F0C1E10C15B741529B76E18168EFAE45 onlayer master
    show rs_image_D88BEA8DA4D145D5B87F3A179B88BE87 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_0FFAFB81CEF94E09AE209050BCCD9627 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_AB6075791E544455A4C21B3DCBA52E1C as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "咳咳！"

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "（强势围观中——）"

    pause 0.3

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_F0C1E10C15B741529B76E18168EFAE45
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_D21B7923E9E24A7C92B7226F129DCD18 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_6D5D3AE8CDB84C189402900F68982BCB as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "刚、刚才的是玩笑……"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊！对了！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "有个叫森海友的黄头发顶着呆毛的笨孩子认识吗？"

    show rs_image_A15B5B9C211846009204F1689FC8781E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那个孩子带着这种时候绝对派的上用场的好道具哦，\n借来试试怎么样？那可是非常不错的东西哦！"

    show rs_image_309B0F3F61544BA188E845B4B474794B as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "是、是这样吗。……有点兴趣呢。"

    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "快去快去！\n"
    show rs_image_A6E2B83133264FE2AC7ED2F9767DAB76 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊～～～不过关键的友亲现在在？"

    window hide

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    show rs_image_0FFAFB81CEF94E09AE209050BCCD9627 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_2D2761902CAE44EC807DF631A55BE304 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    pause 0.3

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我回来了。"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "小忍，好时机！呐——知道友亲在什么地方吗？"

    show rs_image_AB838172A2DB46ABA7F4AC2B3C09693D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友的话，和翼君一起在与导游谈话。我刚才也在，不过途中离席了。"

    show rs_image_DDBC1C0B84A24BB28416DD609F9E0B29 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸～对导游好热心呐。"

    show rs_image_2C5EC61F9FAC4FDA897D61101BDE1CB3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "成年男性不是么？友对大多数成年男性都很软弱。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好、好深刻的描述～！不愧是碧池太郎！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_D21B7923E9E24A7C92B7226F129DCD18 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_C9B3C83238F74DF0BD84400376826860 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "所以，守守！刚才说的事等有机会时拜托一下比较好哦。"

    show rs_image_F4C733D956094DDB90D3AE4E82A63BAA as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "好的，我明白了。这么麻烦你抱歉了。"

    show rs_image_40F4B3A56AFE46FCB14F4500CD625791 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼呼。男孩子就该那么正直嘛。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_C9B3C83238F74DF0BD84400376826860 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at center_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_12E394DC341C4685AB17E83FEED856C9 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_57981D44BEC64E6E999A769D75A0EC1A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……啊，说起来，雨下得非常大，明天一天可能都出不去了。"

    window hide

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_03464FF4C9E0402D927F78F065C5045C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "听到了吗？明天也下雨。"

    show rs_image_5FBD78374DA74E3DAE8DB6DA14DD5616 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸——真假的。以防万一还是看看天气应用……\n"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "这儿不在服务区！"

    show rs_image_9138D3EAFC66405AA95FD2DC03C7E56E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "迟钝，现在才知道。天气这么糟，也太过分了……"

    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "要是海面不平静开不出船去，然后再发生什么的话该如何是好……"
    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……。"

    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "咋了？突然。"

    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……我去把一之濑带过来。"

    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸？到底咋了？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "突然就想了。"

    pause 0.3

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 2

    $ set_window("イベントモード")
    window show

    if sys_music_current_file != "sound/BGM/Hotel 2.ogg":
        play music "sound/BGM/Hotel 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 2.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Search 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Search 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Search 1.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哈、嗯……怎么样朔，舒服不？我稍微拿手一些了？"

    rs_character_62324AD297554FE987C680452CEE232E "唔，这、这种事，看对方的反应自己、想。"

    if sys_effect_current_file != "sound/Effect Sound/Search 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Search 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Search 1.ogg"

    rs_character_62324AD297554FE987C680452CEE232E "啊……用力太大了。那么用力会痛的。"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "欸，抱、抱歉！这、这里呢、行吗？可以吗？"

    if sys_effect_current_file != "sound/Effect Sound/Search 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Search 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Search 1.ogg"

    rs_character_62324AD297554FE987C680452CEE232E "啊……唔，真是的，迟钝。\n要不是我很温柔，这、这种事、绝对不可原谅……"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔、唔……"

    window hide

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Thunder 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Thunder 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_70D38AAE17944382A2D42CC2C92CAB31 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_65412F8CC840413CAE303C4848D4DEA6

    pause 0.8

    window show

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C224FD27FE6D4ECA8B284AE1B4580EE3 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "就算这么说，连{color=#FF00FF}整体的心得体会{/color}都没有，\n根本不清楚穴位的位置啊！！"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_B7004DEEA80C41CC8F336C87E7A09F2E as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_62324AD297554FE987C680452CEE232E "真是的，那你到底能做什么。接下来选什么好呢，嗯……"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "等、等等，还想让我干什么？至少让我休息一下。"

    show rs_image_C276775808CC478299E73F38A0ED0B5B as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "我好不容易的休息日被破坏了，你有什么立场说这个。\n作为被尾行的补偿，这没什么问题。"

    show rs_image_6D71784C723F4F21A0E2717D3503E19E as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "而且，难道是我感觉错了？\n按摩时当手接近下半身的时候，明显有什么企图的样子。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_7D2BA1257986495BA7EE1CE21AF449F6 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔……没、没有那回事！被这么对待可是很困扰的！"

    show rs_image_A477062F5CFB45259A5183ED5584C4A5 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "是嘛，真是遗憾。那么按摩就算了。"

    show rs_image_1D53D375130B48DEA5EC714EDF7E13DD as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "本来还想在最后允许你接触你最喜欢的、最想触摸的地方的。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "诶……难道是……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_6D71784C723F4F21A0E2717D3503E19E as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "当然是脚了，很合适对不对？相对于平伏在地专职侍奉的你。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_829EA2AED9E74CD48751411FB95D579D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "火大——！！！"

    show rs_image_A477062F5CFB45259A5183ED5584C4A5 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "哦呀，这个提案似乎也不受欢迎呐。真是的，难伺候的正义的伙伴（笑）。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_C276775808CC478299E73F38A0ED0B5B as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "那就说些什么有意思的事情。\n就用你那智商有问题的话语给我找点乐子也好。"

    window hide

    pause 0.4

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_66C008E6F84D47619B0EC9EF0F554951 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.6

    # Gallery unlock: images/CG/Welcomt-to-wolfs-celemony/Welcomt-to-wolfs-celemony 2.png
    $ zorder_rs_image_E99D8EE889324E538179D61E6C5B1FC7 = -100
    show rs_image_E99D8EE889324E538179D61E6C5B1FC7 as rs_image_E99D8EE889324E538179D61E6C5B1FC7 zorder zorder_rs_image_E99D8EE889324E538179D61E6C5B1FC7 onlayer master
    hide rs_image_E99D8EE889324E538179D61E6C5B1FC7

    show rs_image_E99D8EE889324E538179D61E6C5B1FC7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_29E124AB0A66462CAB189A9D99CCF83F

    pause 0.5

    window show

    pause 0.3

    rs_character_62324AD297554FE987C680452CEE232E "哦，也就是，你被提拔成见习魔法师全都是因为大腿长得好看？"

    rs_character_62324AD297554FE987C680452CEE232E "你的师父不是因为魔法才能认同的你，而是因为紧致的大腿……呵。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_62324AD297554FE987C680452CEE232E "呀，这可真是杰作，听到了比预想中脑袋还有问题的事情呐，\n满足了，想做还是能做到的嘛。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "切，随便笑随便骂，我也是从心底里嫌弃那个变态师父的。"

    rs_character_62324AD297554FE987C680452CEE232E "哦呀哦呀，对嗯师说什么呐，他可是能发掘出你为数不多的优点的伟人哦。"

    rs_character_62324AD297554FE987C680452CEE232E "本来就很期待夕阳成为魔法师的最核心的秘密……这可真是预想以上的收获。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "我低俗的话能入得了朔大人的尊耳真是万分荣幸！呵呵！"

    window hide

    $ set_window("イベントモード")
    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_70D38AAE17944382A2D42CC2C92CAB31 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.5

    window show

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_B07AFDECD18C45CCA1315EC195BD4924 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_62324AD297554FE987C680452CEE232E "不要闹脾气了，来，下个笑料也要这么有意思。下一个是……"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_829EA2AED9E74CD48751411FB95D579D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "从刚才开始就一直在说我的事太狡猾了！这次我要听朔的事！"

    show rs_image_C276775808CC478299E73F38A0ED0B5B as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "就算这么说，但很遗憾，我并没有像夕阳那样愉快的体验。"

    show rs_image_499DC587BC1840DAABE3AD255A394093 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不是那个！肯定有什么能说的！！以前的事，家族的事……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_FDB36A5B31714742AD6D29EB49DC75EB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "对了！顺便还有Wolfs的！把邪恶组织Wolfs的事全都吐出来！"

    show rs_image_6D71784C723F4F21A0E2717D3503E19E as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "那种给敌人甜头的事你觉得我可能照做么。"

    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "这次仅仅是因为休息日停战。不要忘了我们的敌对关系。"

    show rs_image_15C5A93E72CC49F7B52D2031A6D69DEE as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哈！那就由我来提问！\n"
    show rs_image_07F2639BB0524AEBB4F93F1989365243 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那——个，Wolfs是……“狼”？"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    extend "啊！"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    # Gallery unlock: images/CG/Welcomt-to-wolfs-celemony/Welcomt-to-wolfs-celemony 9.png
    $ zorder_rs_image_7069267F64E54B868A5050EEF9D93A3B = -100
    show rs_image_7069267F64E54B868A5050EEF9D93A3B as rs_image_7069267F64E54B868A5050EEF9D93A3B zorder zorder_rs_image_7069267F64E54B868A5050EEF9D93A3B onlayer master
    hide rs_image_7069267F64E54B868A5050EEF9D93A3B

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_7069267F64E54B868A5050EEF9D93A3B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_top zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.9

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_62324AD297554FE987C680452CEE232E "等等，你到底想做什么。脸太近了，离远点。"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "嗯——怎么看都是人类呐。\n我还想会不会本体是狼，然后幻化成人类的样子什么的。"

    rs_character_62324AD297554FE987C680452CEE232E "……瞎说什么呢。{nw}"
    stop music fadeout 5
    $ sys_music_current_file = ""

    extend ""

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "从师父那里听来的，"
    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_038A3EB7489F4B51B2A1AD7FBC2E0808

    pause 0.4

    extend "过去存在幻化成人形吃掉村里人的狼，\n魔法师的任务就是要看破他们的真面目。"

    show rs_image_D6ADB3B2DBE647DC91A820FFA6D351E3 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6283E57F3B554331AD05CAFEEF576AEC

    pause 0.4

    if sys_music_current_file != "sound/BGM/Hotel 3.ogg":
        play music "sound/BGM/Hotel 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 3.ogg"

    rs_character_62324AD297554FE987C680452CEE232E "……那只是打比方。{w}话里的“狼”指的就是坏事，要做的不就是维持治安吗？"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔～是吗。是不是太过理想了呢。{w}\n和魔法师敌对的组织正好就叫Wolfs什么的……"

    rs_character_62324AD297554FE987C680452CEE232E "那你是想说我们会趁你们不注意吃人？就算是妄想也不会这么野蛮。"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "啊！我明白了！！“吃”指的肯定是朔被触手袭击的那种“吃”！"

    rs_character_62324AD297554FE987C680452CEE232E "刚才还是那么残暴的话，一下子就变成下流梗了。{w}\n不会是官能魔法师，不得不甘拜下风。"

    window hide

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_195F518B89564C98A557F130D2E603F0

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔……我还以为是个好点子的。"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_1D53D375130B48DEA5EC714EDF7E13DD as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_62324AD297554FE987C680452CEE232E "谁知道呢。说不定猜中了。"

    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "好，看在夕阳真的想出了“名”推理的情况上，我会回答你任何一个问题。"

    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "嗯，那就……"

    show rs_image_BEE780ABA64C4D7ABB8972D17BDCBFAB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "Wolfs的家伙们不会集团行动吗？就像现实中的狼群那样。"

    show rs_image_A477062F5CFB45259A5183ED5584C4A5 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "不错啊。和之前不一样，第一次从你口中听到这么深刻的问题。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_B7004DEEA80C41CC8F336C87E7A09F2E as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "闭、闭嘴！赶紧回答。"

    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "好，根据约定我会回答的。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "其实，Wolfs确实会像现实中的狼那样，基本都是集团行动的。"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    rs_character_62324AD297554FE987C680452CEE232E "不过，我和哥哥则不算在此列。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_70D38AAE17944382A2D42CC2C92CAB31 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_D7DFB9C596074724958BBE78FF9336D3 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "欸！？哥、哥哥！？你、你这家伙原来有哥哥！！"

    if sys_effect3_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_15C5A93E72CC49F7B52D2031A6D69DEE as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "真想看看！！很在意呢！！有照片吗！？"

    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "废话太多了，音量也别那么大，会打扰到别人的。"

    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "真是令人无语的魔法师。一般来说，目标身边的一切不是早就该调查到了吗。"

    show rs_image_C276775808CC478299E73F38A0ED0B5B as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "我可是知道你的哥哥的。和你不同，很成熟很可靠。"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "等、等等！？什么！？到底怎么回事！？\n详细点！！说详细点！！"

    window hide

    pause 0.3

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    if sys_effect4_current_file != "sound/Effect Sound/Rain 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect4 "sound/Effect Sound/Rain 1.ogg" loop
        $ sys_effect4_current_file = "sound/Effect Sound/Rain 1.ogg"

    pause 1.5

    if sys_music2_current_file != "sound/Effect Sound/Vibration 2.ogg":
        play music2 "sound/Effect Sound/Vibration 2.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Vibration 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_70D38AAE17944382A2D42CC2C92CAB31 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 3

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_BEE780ABA64C4D7ABB8972D17BDCBFAB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "嗯？什么声音？"

    stop music2 fadeout 5
    $ sys_music2_current_file = ""

    rs_character_62324AD297554FE987C680452CEE232E "不是雨声……好像是从隔壁传来的。"

    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "也就是说是守？这个时候到底在干什么。"

    show rs_image_3149C4BF55744A498D9A6BE1CAAF3483 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "啊，已经这个时间了。说了不少有意思的东西呢。"

    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "我差不多要去洗澡了。夕阳也准备一下。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "欸！？"

    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "不是说过吗？二十四小时片刻不离？"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_6445A86DD28745F0AD0938A8193610F2 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哦、哦……！"

    show rs_image_A477062F5CFB45259A5183ED5584C4A5 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……看在我都移驾到单人间的份上，洗澡时可要好好侍奉我身体的每个角落哦。"

    show rs_image_7D2BA1257986495BA7EE1CE21AF449F6 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "！？"

    stop effect4 fadeout 0.6
    $ sys_effect4_current_file = ""

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_00D7D13F7EE6402ABA1D776DE0C003ED

    pause 3.5

    $ set_window("イベントモード")
    if sys_effect2_current_file != "sound/Effect Sound/Wind 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6D595FD5594145118D9588130020DDB7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    $ renpy.pause(3, hard=True)

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Hotel 1.ogg":
        play music "sound/BGM/Hotel 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_350F6A2B48EE49C8B631CE0B02F5BC2C as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_58CAC53C853A4ECC97CAB3038D1CAAF0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_BD4796B7B22F4DCE84A89D7BF86E89A0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A46E468ABE0345679EB63CE570AD59F9

    $ renpy.pause(1, hard=True)

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    $ renpy.pause(0.6, hard=True)

    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E683F1ECE3314055A6535AFF3A0F039A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    $ renpy.pause(1, hard=True)

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_796B712D10B4444B8FFCDA0CB17322CC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A46E468ABE0345679EB63CE570AD59F9

    $ renpy.pause(0.8, hard=True)

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FF35A84302AE4B48ACC0F1A61B29D997 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ renpy.pause(0.6, hard=True)

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_7E08F07FB7E44A4682D1CA8B31E70D52 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_E0457AAB77814676BA08C45308E56A09 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    $ renpy.pause(0.8, hard=True)

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    show rs_image_14F00D9CB0D84CF98963CC0BD2BF80D9 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    $ renpy.pause(1, hard=True)

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_8C8329CA4FC34C279A723168C0AA6CC0 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-85, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_F1E694F9D98E4371B8F767497249ECEE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A46E468ABE0345679EB63CE570AD59F9

    $ renpy.pause(0.7, hard=True)

    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    $ renpy.pause(0.7, hard=True)

    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    $ renpy.pause(1.2, hard=True)

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ renpy.pause(0.7, hard=True)

    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(1.5, hard=True)

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    $ renpy.pause(0.4, hard=True)

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_0FFAFB81CEF94E09AE209050BCCD9627 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    $ renpy.pause(0.5, hard=True)

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(0.3, hard=True)

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(0.6, hard=True)

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(0.3, hard=True)

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_275B22DDBE294B889403F68883C99EC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(0.3, hard=True)

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_4A9AC5BBBA6D44F5B5DCB7EEF0B9EAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(0.6, hard=True)

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_4A2DF19F343B45378225DB529BF9F33C as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(0.3, hard=True)

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 400
    show rs_image_C0725D9DCFAF4402882B4880A327CD79 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(0.3, hard=True)

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(0.6, hard=True)

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ renpy.pause(0.6, hard=True)

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_296DD986D1424E4AA97E52E2A1ECE378 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ renpy.pause(1.2, hard=True)

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ renpy.pause(0.6, hard=True)

    $ zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 = 300
    show rs_image_15C90FB54265499E9E746DBDA51DE57E as tag_51E1CA5715FC4887A4E4083BB8D521B0 at center_top zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    $ renpy.pause(1.5, hard=True)

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    with rs_effect_673B577A4E15407397C9C9B62906A309

    $ renpy.pause(1, hard=True)

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D21B7923E9E24A7C92B7226F129DCD18 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    $ renpy.pause(0.6, hard=True)

    window show

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_00EDE24382514EE4A0ABD3DF8E01C76D as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "世依木君直到最后也没有来吃早饭呢。到底怎么了？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_9387C2EF08BB4EFABA360A19A1E02C8B as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼呼，肯定是昨晚从友亲那里借到秘密武器后玩过头了……"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_EFDC09B34577437A8D2B581A3FFFC9E4 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "拜此所赐我昨天的计划也都乱了……早点还给我就好了。"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "明、明明我都没用过……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_13EEE138043542FB90557CFB44BADDE4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好不容易能随便放开吃，都浪费了！！\n"
    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "对不起，请问看到世依木君了吗？"

    $ zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 = 300
    show rs_image_15C90FB54265499E9E746DBDA51DE57E as tag_51E1CA5715FC4887A4E4083BB8D521B0 at center_top zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "……不，我并不清楚。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "感觉有问题……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B0873EFC1DD2407F862D1D97E2A4B64D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_03464FF4C9E0402D927F78F065C5045C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "夕阳君，要不要去看看情况？也许生病了也说不定。"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_8E45409FAB964B1D95BC762DA3DD5DD7 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "大浴场正在清扫，不管怎么说也应该是在房间里。"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_296DD986D1424E4AA97E52E2A1ECE378 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "说的是，那我去看看。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_0FFAFB81CEF94E09AE209050BCCD9627 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "还有，朔也跟我走。"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "好好。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_03464FF4C9E0402D927F78F065C5045C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊，我也要去～♪"

    window hide

    pause 0.5

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    pause 2

    if sys_effect2_current_file != "sound/Effect Sound/Rain 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Rain 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Rain 1.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Knock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Knock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Knock 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_BD4796B7B22F4DCE84A89D7BF86E89A0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    pause 0.6

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "守——早上了——起床了——"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_12E394DC341C4685AB17E83FEED856C9 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊咧？阿夕，门没锁哦。"

    show rs_image_B07AFDECD18C45CCA1315EC195BD4924 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "真的，太不上心了。{w}守，我进来了——"

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_3B13044431874BE09020F9368D6A8C29 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "早上好呀，守亲！要睡到什么时候呐！！\n就让我来献上早起的吻……"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_73B848C8959C43B58DEDBCE04C060A28 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A6E2B83133264FE2AC7ED2F9767DAB76 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "咦？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_62324AD297554FE987C680452CEE232E "……不在。"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "呃，呃——那家伙到底去什么地方了……"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window hide

    pause 1


    if judge_lm_condition([]):
        jump block_00003C13

    return

label block_00003C13:
    # Node: 00003C13 (Room 守)
    $ set_window("(標準)")
    if sys_music_current_file != "sound/BGM/Solve the case.ogg":
        play music "sound/BGM/Solve the case.ogg" loop
        $ sys_music_current_file = "sound/BGM/Solve the case.ogg"

    pause 1

    $ set_place_title(_("208房"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_73B848C8959C43B58DEDBCE04C060A28 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003C12

    return

label block_00003C12:
    # Node: 00003C12 (Room 守)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (464, 184),"image": "images/Chapter 2/Menu/F6/Shintaro 2.png","hover": "images/Chapter 2/Menu/F6/Shintaro 2 hover.png","name": "慎太郎"}, {"pos": (290, 146),"image": "images/Chapter 2/Menu/F6/Nori 2.png","hover": "images/Chapter 2/Menu/F6/Nori 2 hover.png","name": "朔"}, {"pos": (136, 208),"image": "images/Chapter 2/Menu/F6/Item 1.png","hover": "images/Chapter 2/Menu/F6/Item 1 hover.png","name": "眼鏡"}, {"pos": (696, 280),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "ベッド"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_343
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00003C0F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"朔\"" }]):
        jump block_00003C10
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"眼鏡\"" }]):
        jump block_00003C11
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ベッド\"" }]):
        jump block_00003C16
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003C14

    return

label block_00003C0F:
    # Node: 00003C0F (慎太郎)
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_D46D696B97D843B986F2242E874326F8 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_D46D696B97D843B986F2242E874326F8 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊咧咧～？好奇怪啊～？没有任何用过的纸巾呐。"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "？？奇怪？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F1B9EC1687544CF6AC26A45D3E5F4674 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "青春期少年度过一晚的房间里必定有纸巾，这可是金科玉律。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "真是的，奥村前辈这种时候就不要……"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8B48851BB9F649D9A15EC7718BAB73D5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不是～说认真的，守守可是被朋友一直放在一边，非常欲求不满呐～"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "所以刚才说的肯定是没问题的才对～"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那……去厕所冲掉了？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_400D502433E44E52A9FFEAD65F622427 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "诶，你是这么做的？"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不是！"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8B48851BB9F649D9A15EC7718BAB73D5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "可是，这边的纸巾还完全没有用过，{w}守守是会自己带纸巾的类型 吗？"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不——应该不是……{w}洗澡也是在大浴场……"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("208房"))

    if judge_lm_condition([]):
        jump block_00003C12

    return

label block_00003C10:
    # Node: 00003C10 (朔)
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_60B9FE45942F49EC96FD1964FAB1BB1B as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_bottom zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_1F690B307ECA4450A3C108BA53BF04F7 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "昨晚听到的“嗡嗡”的机械音究竟是什么呢。"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "是在很晚听到的，{w}要说是手机的振动声音也太大了，时间也太长了……"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_511A1885AB154028AF647FB028BA2458 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_bottom zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那是昨天找友亲借的电摩的声音！\n"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_CB49ABE40CB34BD7AA2C8B4E5739D95A as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯嗯！终于守守也打开了新世界的大门了……！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_60B9FE45942F49EC96FD1964FAB1BB1B as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_bottom zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "可是，那种东西现在并不在这里。{w}\n世依木君是趁夜或者一大早还回去了吗？"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那最后见到守的人最可能就是森海前辈了。{w}等下问问看。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("休息室"))

    if judge_lm_condition([]):
        jump block_00003C12

    return

label block_00003C11:
    # Node: 00003C11 (眼鏡)
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "这是什么？"
    if sys_effect3_current_file != "sound/Effect Sound/Key 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Key 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Key 1.ogg"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "啊，眼镜盒。"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "欸？眼镜还在。{w}那家伙视力很差，可没戴眼镜就出去了？"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("休息室"))

    if judge_lm_condition([]):
        jump block_00003C12

    return

label block_00003C16:
    # Node: 00003C16 (Bed)
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "……嗯？湿了好多。{w}昨天有这么热来着？"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("休息室"))

    if judge_lm_condition([]):
        jump block_00003C12

    return

label block_00003C14:
    # Node: 00003C14 (Finish)

    if judge_lm_condition([]):
        jump block_00003C15

    return

label block_00003C15:
    # Node: 00003C15 (選擇)
    call scb_selector(_("调查到此为止？"), [{"name":"はい", "content":_("调查完毕")}, {"name":"いいえ", "content":_("稍等，还有……")}]) from _call_scb_selector_33

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00003C12
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003C17

    return

label block_00003C17:
    # Node: 00003C17 (Finish)
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "先回大家那里好了。{w}到底去什么地方了……"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_2D9D55E1273147FD916194309B9601B8 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_bottom zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "外面在下暴风雨，所以肯定在馆内，说不定过一会就出现了。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("休息室"))
    pause 0.7

    stop music fadeout 1
    $ sys_music_current_file = ""

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003C18

    return

label block_00003C18:
    # Node: 00003C18 (歡迎來到食人狼之館 3)
    $ set_window("イベントモード")
    if sys_effect2_current_file != "sound/Effect Sound/Wind 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2BD0E40E817E44B28F8F0279FD7035C3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2.5

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_F1E694F9D98E4371B8F767497249ECEE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    window show

    if sys_music_current_file != "sound/BGM/Hotel 3.ogg":
        play music "sound/BGM/Hotel 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 3.ogg"

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶！守君不在房间里？而且我的电摩君也不在！？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_2A76FDEE70B042698EC0F747D2740BFA as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at Transform(xpos=420, yalign=0.0) zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "咦，没有还回来？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没有——！守君到底把我的电摩带去什么地方了——！"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "这到底是怎么回事。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_40F4B3A56AFE46FCB14F4500CD625791 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "难道说，守守觉得在屋里声音太大怕被发现，\n就换到别的地方去继续“自力更生”了？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "震、震惊——不过，那确实是最可能的……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_E436CC5ED79D41EABE3ADFC40CD9F8B8 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——要用电摩的话必须要有插座才可以。那种理想的地方真的有吗？"

    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "同感。还是想想其他的……{w}比如，有没有被卷入什么事件的可能性？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_9E7B821A26DB4648BA5980B3C4E75E0D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不！那绝对不可能。"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……为何？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_CA65E37C24FB460390BADAD95767936C as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那个……"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不，那家伙，看上去那样运动神经还是很好的，\n"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_B07AFDECD18C45CCA1315EC195BD4924 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "真有什么万一，力量就会觉醒什么的……"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_E436CC5ED79D41EABE3ADFC40CD9F8B8 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶——？说什么呢～？？不明白～"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_62324AD297554FE987C680452CEE232E "……原来如此，是那么回事。既然如此就不需要担心了。"

    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……夕阳。"

    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "嗯？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_1D53D375130B48DEA5EC714EDF7E13DD as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "雨天之时的后手，我很期待哦。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_B7004DEEA80C41CC8F336C87E7A09F2E as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哦、哦，好好等着吧～哈哈……"

    window hide

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_0E66EED4593D45DE99868C4E6769E92E as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "总之就算是以防万一，把所有带插座的房间都找一遍如何？"
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_CA65E37C24FB460390BADAD95767936C as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不用了，这就好！剩下的我会和朔处理的。\n奥村前辈，森海前辈，非常感谢！"

    show rs_image_08C43A31F7C049DDB885DFB2FB7A471D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不要那么说，我们也会帮忙搜索的。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_BEE780ABA64C4D7ABB8972D17BDCBFAB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "要是闹得太大了会害其他前辈也担心的。"

    show rs_image_CA65E37C24FB460390BADAD95767936C as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "而且如果真的像前辈说的那样是那种无聊的理由的话，\n等下被找出来的守的立场也很……"

    show rs_image_296DD986D1424E4AA97E52E2A1ECE378 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "可以的话请先回去，就告诉大家守正在屋里休息如何？"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔～也对。明白了，我会这么说的。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "能快点找到就好了呐～"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_9E7B821A26DB4648BA5980B3C4E75E0D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "是！非常感谢！"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_296DD986D1424E4AA97E52E2A1ECE378 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "好了，那么，开始搜索守！"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_62324AD297554FE987C680452CEE232E "是呢。"

    pause 0.3

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window hide

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_85B3D08EC940443EA7124D6973822305 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_0FFAFB81CEF94E09AE209050BCCD9627 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_05D215DF5A514599A219DAB98A1E5B7C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_503677B77FAD421497F2DB30F3240E8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Rain 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Rain 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Rain 1.ogg"

    show rs_image_BD4796B7B22F4DCE84A89D7BF86E89A0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 0.6

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "到底去什么地方了，那家伙……"

    rs_character_62324AD297554FE987C680452CEE232E "地毯式搜索也没有找到。\n"
    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "此外，还有一件需要在意的事。"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E0C9131CA0E2485C9F7FBB4809296E2F as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "导游之外一个工作人员都没有的事，对不？"

    window hide

    pause 0.3

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.3

    window show

    rs_character_62324AD297554FE987C680452CEE232E "正是如此。看来这并不只是件小事，还是召集大家说明事态为好。"

    show rs_image_B7004DEEA80C41CC8F336C87E7A09F2E as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "……好，就这么办。"

    window hide

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.3

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，尤、夕阳君和朔君，太好了。"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_2A76FDEE70B042698EC0F747D2740BFA as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "一之濑前辈，我有想对大家说的话……"

    show rs_image_0BD950ADC14245578BC5105060EF0E00 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那样的话，大家都在早饭时的餐厅里集合着呢，\n我觉得直接过去比较好。"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D7DFB9C596074724958BBE78FF9336D3 as tag_E99970E1386B453DAF81C3AE2C72BE8E at Transform(xpos=430, yalign=0.0) zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "非常感谢。{w}说起来，一之濑同学和森海同学关系很好呐。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_EAAB6CC3A5464202B2C5DE5D303795FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸，突、突然说什么呢。怎、怎么会，那个，很普通的……"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_9D0666C01E89408289145D59F704EFAB as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_D7DFB9C596074724958BBE78FF9336D3 as tag_E99970E1386B453DAF81C3AE2C72BE8E at right_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "今天早上，在听到森海同学的东西被借出去后，\n露出了无比悔恨的表情呢，我很在意这个。"

    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个是、这个……没想到真的被借出去了什么的……\n"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "呜呜，我要是那时候在场就好了。"

    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "那时候？"

    show rs_image_CF5AA529110045B9AA052BA9023E6FA3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "昨天，我和友君和导游一起谈话的时候被作哉君带出来了。"

    show rs_image_9F9E3AB5982941C7A3FF42BB60F86B4D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "和、那个时候和守君分开了，我想应该就是那个时候借出去的……"

    show rs_image_3149C4BF55744A498D9A6BE1CAAF3483 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……那还真是遗憾。"

    show rs_image_CF5AA529110045B9AA052BA9023E6FA3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯…………{size=12}我下次借借试试……{/size}\n"
    show rs_image_A20D31D533CF44CDA4A7F67CEC353CDE as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "说起来，有个问题想要问一下两位……"

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_296DD986D1424E4AA97E52E2A1ECE378 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at Transform(xpos=430, yalign=0.0) zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    show rs_image_A20D31D533CF44CDA4A7F67CEC353CDE as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "嗯，是什么？"

    pause 0.3

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_BD4796B7B22F4DCE84A89D7BF86E89A0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_2B709367A1FA4DEF815337B5B014517C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    pause 0.3

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Nori.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Nori.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Nori.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "看到月君和空君了吗？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "外面天气这个样子，\n所以我们想在餐厅集合一下商量该怎么度过这段时间，可是。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那两个人完全没有出现过……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at right_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_62324AD297554FE987C680452CEE232E "……房间里？"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_A20D31D533CF44CDA4A7F67CEC353CDE as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "当然已经确认过了，锁开着，可是很遗憾，好像出门了……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_E0C9131CA0E2485C9F7FBB4809296E2F as tag_E99970E1386B453DAF81C3AE2C72BE8E at right_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "这可能……会很麻烦。"

    rs_character_62324AD297554FE987C680452CEE232E "同感。赤峰同学他们的事或许和我们正在调查的事也有关。"

    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "一之濑同学也请和我们一起回去。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_9D0666C01E89408289145D59F704EFAB as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "诶？嗯、嗯。\n"
    show rs_image_275B22DDBE294B889403F68883C99EC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……说起来，好多灰尘呐。"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window hide

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Thunder 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Thunder 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_0FFAFB81CEF94E09AE209050BCCD9627 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈！？守君和赤峰兄弟下落不明——！？"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_2A76FDEE70B042698EC0F747D2740BFA as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at Transform(xpos=420, yalign=0.0) zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不止这样，酒店的工作人员也是。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_57981D44BEC64E6E999A769D75A0EC1A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "确实从早上就没出现过……"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "只是，那个可疑的导游还在。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "外面天气这个样子，三人应该还都在馆内。\n接下来我和朔会继续搜索。"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "前辈们就请在这里休息，保护好自己。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_3766CD2AF98244F5AECA23E096C299D8 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_07EEAD26B9C44798806C86D199A70194 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不行的哦阿夕——！！这种时候才必须依靠前辈们的力量！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说、说的没错。只有你们两个太危险了……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    rs_character_62324AD297554FE987C680452CEE232E "同意。夕阳，要认清自己的能力。"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    show rs_image_B7004DEEA80C41CC8F336C87E7A09F2E as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "什么！？我可是炎之……"

    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "这种湿度下你能做什么？还是说，用你之前说的后手？"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "这、这个……"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我觉得应该分成两队，派不上用场的人就别去碍手碍脚。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_69663BD5BF254491A6E7462E56A2621F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……归宅部，举手！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_59AAF132B57B402BB1B9171904F5D5B2

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "友 呃！\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_59AAF132B57B402BB1B9171904F5D5B2

    extend "慎太郎 哦！\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_59AAF132B57B402BB1B9171904F5D5B2

    extend "翼 唔！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_58CAC53C853A4ECC97CAB3038D1CAAF0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你们三个就留在这里，我也会留下来护卫。"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D7DFB9C596074724958BBE78FF9336D3 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "这个想法很好。只要忍同学能留在这里我就安心了。"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那么，我们四个去搜索。\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3DE5824BE0644C96928A4FBCD72BE70B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "猫山，还好不？抖得挺厉害啊——"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "别、别瞎说！这是武者按捺不住的激动！\n……唔，静不下来……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嘴上别说静不下来。嘛，真发生什么的话反正你逃得快没事。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "对——对——！逃到我的怀里来～♪"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3B13044431874BE09020F9368D6A8C29 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.6

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_275B22DDBE294B889403F68883C99EC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "现充……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我也想当现充……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_62324AD297554FE987C680452CEE232E "这种情况下也这么镇定，真是佩服大家的胆力呢。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔、唔……这样真的好嘛。"

    show rs_image_D7DFB9C596074724958BBE78FF9336D3 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "和他们比起来……优柔寡断而且没出息，就这么不敢去搜索？"

    show rs_image_6D71784C723F4F21A0E2717D3503E19E as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "万一之时就由我来保护你。请安心，正义的英雄君（笑）。"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_829EA2AED9E74CD48751411FB95D579D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不、不用你关心！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A477062F5CFB45259A5183ED5584C4A5 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    show rs_image_B07AFDECD18C45CCA1315EC195BD4924 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.6

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_7D82D2EF95ED49EA821B9751FF70275C as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "现充……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "真好……"

    window hide

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Rain 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Rain 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Rain 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_6D595FD5594145118D9588130020DDB7 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 3

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_BD4796B7B22F4DCE84A89D7BF86E89A0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_music_current_file != "sound/BGM/Solve the case.ogg":
        play music "sound/BGM/Solve the case.ogg" loop
        $ sys_music_current_file = "sound/BGM/Solve the case.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "又找了一遍，还是没发现……"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at right_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "没有任何有问题的地方。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是不是已经回去了？除此之外没别的解释了。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "唔……要是这种时候小翼在的话就好了。"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_2A76FDEE70B042698EC0F747D2740BFA as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "诶？带过来会好吗？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊，说的不是一之濑，是穗海在学校养的狗的名字。"

    show rs_image_B2C01DFF41914E56A428EBCACA72C51F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_296DD986D1424E4AA97E52E2A1ECE378 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "欸……"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_DDA00DBFDDC245EC9D675EA5711B37C9 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "和、和狗比起来这种时候猫真是一点用都没有——！\n那边那只猫！给点什么有用的特技！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "出现了！穗海的不讲道理！\n两位这么下去可不行，这个家伙真……"
    if sys_effect3_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Stupid 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊、"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊嚏！！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_9ACAEF851EAF4CECBC5BA7CA6AAF6C36 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那个喷嚏难道就有什么用？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这不是特技！真是的～扫都没扫干净～\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "啊，酒店的人也不在……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "咳咳。{w}确实，有些灰尘积下来了。"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_BEE780ABA64C4D7ABB8972D17BDCBFAB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "是吗～？完全没注意到。"

    show rs_image_3149C4BF55744A498D9A6BE1CAAF3483 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……不愧是你。不过为什么只在这一带……"

    window hide

    pause 0.4

    if sys_effect3_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1.5

    if sys_effect2_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C373DF2B48346D18DBBF3E85BAC79F8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_FDBAA7230FE34F05BBA471102428050A as tag_E99970E1386B453DAF81C3AE2C72BE8E at right_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哇！？原来灰尘来源是赤峰兄弟的房间！"

    rs_character_62324AD297554FE987C680452CEE232E "这可真是……太过分了。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不行不行我进不去！这里就拜托粗神经的各位……"

    show rs_image_7591B090AFF548F4B3459E7CA9BD2848 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……我也不进去了。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    pause 0.6


    if judge_lm_condition([]):
        jump block_00003C1A

    return

label block_00003C1A:
    # Node: 00003C1A (Room twins)
    $ set_window("(標準)")
    if sys_music_current_file != "sound/BGM/Solve the case.ogg":
        play music "sound/BGM/Solve the case.ogg" loop
        $ sys_music_current_file = "sound/BGM/Solve the case.ogg"

    $ set_place_title(_("211房"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4C373DF2B48346D18DBBF3E85BAC79F8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003C1B

    return

label block_00003C1B:
    # Node: 00003C1B (Room twins)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (639, 221),"image": "images/Chapter 2/Menu/F6/Sakuya 2.png","hover": "images/Chapter 2/Menu/F6/Sakuya 2 hover.png","name": "作哉"}, {"pos": (248, 352),"image": "images/Chapter 2/Menu/F6/Item 2.png","hover": "images/Chapter 2/Menu/F6/Item 2 hover.png","name": "ホウキ割れ"}, {"pos": (464, 264),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "ホウキロッカー"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_344
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_00003C1C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ホウキ割れ\"" }]):
        jump block_00003C1E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ホウキロッカー\"" }]):
        jump block_00003C1D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003C1F

    return

label block_00003C1C:
    # Node: 00003C1C (作哉)
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_117EA2E8EB024A4C8F46B6B5E8B1989C as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_EB9D3849888641E78C28DA84B16F2AC8 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那只猫简直一点用都没有。灰尘又怎么了。"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不过说起来，到底要怎么折腾才能弄得这么乱呐。{w}\n前辈听到过类似打架的声音吗？"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_454A1F98F91D4549A6F352AD11E26948 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不，并没什么特别的。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("211房"))

    if judge_lm_condition([]):
        jump block_00003C1B

    return

label block_00003C1E:
    # Node: 00003C1E (Broom)
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "嗯？这是什么。"

    pause 0.3

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DFF6C096971C4020B3AD59E666124B0B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "像是被折断的什么东西。"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "……说起来碎得很厉害呢。"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1A5E3A7F00B546FE8A7423BB9C2B93DB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "虽然不同班我也不清楚，但他们是这种会破坏东西的类型吗？"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "……{w}果然有问题。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("211房"))

    if judge_lm_condition([]):
        jump block_00003C1B

    return

label block_00003C1D:
    # Node: 00003C1D (wardrobe)
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Key 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Key 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Key 1.ogg"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_D88C36596D5640CBBEA1F126790B6B7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    window show

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "我的房间里并没有扫帚。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("211房"))

    if judge_lm_condition([]):
        jump block_00003C1B

    return

label block_00003C1F:
    # Node: 00003C1F (Finish)

    if judge_lm_condition([]):
        jump block_00003C20

    return

label block_00003C20:
    # Node: 00003C20 (選擇)
    call scb_selector(_("调查到此为止？"), [{"name":"はい", "content":_("调查完毕")}, {"name":"いいえ", "content":_("稍等，还有……")}]) from _call_scb_selector_34

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003C21
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00003C1B

    return

label block_00003C21:
    # Node: 00003C21 (Finish)
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_757DAFA361824FA590E148B0796C4A27 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "差不多该走了。"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "好的。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("休息室"))
    pause 0.7

    stop music fadeout 1
    $ sys_music_current_file = ""

    $ set_place_title("") 
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003C22

    return

label block_00003C22:
    # Node: 00003C22 (歡迎來到食人狼之館 4)
    if sys_effect2_current_file != "sound/Effect Sound/Rain 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Rain 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Rain 1.ogg"

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_BD4796B7B22F4DCE84A89D7BF86E89A0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    window show

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_2B49DF326D8641F283BDF0EC54525573 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这就搜索结束了啊～完全没有成果，只能回餐厅了。"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at right_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "同意。也很担心绫濑同学他们……"

    window hide

    pause 0.4

    stop effect2 fadeout 0.4
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if sys_effect_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    window show

    pause 0.5

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=40}唔哇啊啊啊啊！！！？{/size}"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_BD4796B7B22F4DCE84A89D7BF86E89A0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.4

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "森海前辈的声音！？"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    if sys_music_current_file != "sound/BGM/Battle.ogg":
        play music "sound/BGM/Battle.ogg" loop
        $ sys_music_current_file = "sound/BGM/Battle.ogg"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F1E694F9D98E4371B8F767497249ECEE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=410, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "大、大家！！"

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_BFD82456D5174411821E86BA423170EE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "前辈！怎么了！？"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "这个笨蛋！没事干什么到处乱窜！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_E1E1F08446C54DCAAC86BEA1B671549E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那是……那个！这是……啊……！"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_E0C9131CA0E2485C9F7FBB4809296E2F as tag_E99970E1386B453DAF81C3AE2C72BE8E at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "冷静！先深呼吸！吸吸呼！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_5465258BCE404B519910FD1F4172107B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "吸吸呼……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_E0C9131CA0E2485C9F7FBB4809296E2F as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    show rs_image_B7004DEEA80C41CC8F336C87E7A09F2E as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……发生什么了？"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "难、难道说！又有谁被……！！"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊嚏！！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_70576159A31C474CAECF9B7AFDBBF16F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_E0C9131CA0E2485C9F7FBB4809296E2F as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哇！？你为什么要挑这个时候！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_62324AD297554FE987C680452CEE232E "！"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_E1E1F08446C54DCAAC86BEA1B671549E as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫！？呜哇啊啊啊！又、又出现了！！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "！？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_B7004DEEA80C41CC8F336C87E7A09F2E as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_62324AD297554FE987C680452CEE232E "夕阳！背后！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_FA71A79D75754B70A790643847D4F2C5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 = 300
    show rs_image_F1E694F9D98E4371B8F767497249ECEE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_F3E1A3402583414C9A2FC65A2F12BD81 as tag_51E1CA5715FC4887A4E4083BB8D521B0 at center_top zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_57C6381FCB1D4622A17BD77B896E5504

    pause 1

    show rs_image_15C90FB54265499E9E746DBDA51DE57E as tag_51E1CA5715FC4887A4E4083BB8D521B0 zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.4

    window show

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "不错不错，很棒的反应。"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_BFD82456D5174411821E86BA423170EE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "你、你是……！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这、这家伙，刚才是想袭击夕阳！？"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "果然全都是你干的好事！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 = 300
    show rs_image_15C90FB54265499E9E746DBDA51DE57E as tag_51E1CA5715FC4887A4E4083BB8D521B0 at center_top zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "不管是刚才的矮个子，还是再之前的双胞胎，\n最近的小孩子还挺强呐……"

    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_E1E1F08446C54DCAAC86BEA1B671549E as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B7004DEEA80C41CC8F336C87E7A09F2E as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_E0C9131CA0E2485C9F7FBB4809296E2F as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "小、一定小心！！这家伙什么攻击都没用！所以刚才忍才会被抓走的！"

    rs_character_62324AD297554FE987C680452CEE232E "那个忍会被……！看来必须要小心为上了。"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不只是绫濑前辈，能抓走那个守说明肯定不是等闲之辈……这家伙。"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_BFD82456D5174411821E86BA423170EE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "赤峰兄弟也是很强的！竟然只靠一人就……！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "切！就算这样，我们也没有坐以待毙的理由！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 = 300
    show rs_image_15C90FB54265499E9E746DBDA51DE57E as tag_51E1CA5715FC4887A4E4083BB8D521B0 at center_top zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_F3E1A3402583414C9A2FC65A2F12BD81 as tag_51E1CA5715FC4887A4E4083BB8D521B0 zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.4

    window show

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "不管你们再怎么强，也不过是小孩子。来，好好听大人的话。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_FA728451C1834C1EB48DD13001D53294 as tag_51E1CA5715FC4887A4E4083BB8D521B0 zorder zorder_tag_51E1CA5715FC4887A4E4083BB8D521B0 onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "要来了！大家后退！！你的对手是……"

    if sys_effect_current_file != "sound/Effect Sound/Knife 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Knife 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Knife 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_DC107C264C484B3A8306E39B61626CF6

    rs_character_62324AD297554FE987C680452CEE232E "我接受了。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "诶！？"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Battle 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 1.ogg"

    # Gallery unlock: images/CG/Welcomt-to-wolfs-celemony/Welcomt-to-wolfs-celemony 3.png
    $ zorder_rs_image_D5131E3A10814E4FB5007D75587FC94C = -100
    show rs_image_D5131E3A10814E4FB5007D75587FC94C as rs_image_D5131E3A10814E4FB5007D75587FC94C zorder zorder_rs_image_D5131E3A10814E4FB5007D75587FC94C onlayer master
    hide rs_image_D5131E3A10814E4FB5007D75587FC94C

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_D5131E3A10814E4FB5007D75587FC94C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.5

    if sys_effect3_current_file != "sound/Effect Sound/Knife 3.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Knife 3.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Knife 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_4D8F1D6A70C24A34A3E6C37B69619470 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Knife 4.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Knife 4.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Knife 4.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_51451FBF94C8444AA5696178E72CE210 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if sys_effect3_current_file != "sound/Effect Sound/Knife 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Knife 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Knife 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_E04DFA4059EE40D18051F1CAA5223C75 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Battle 4.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 4.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 4.ogg"

    # Gallery unlock: images/CG/Welcomt-to-wolfs-celemony/Welcomt-to-wolfs-celemony 3.png
    $ zorder_rs_image_D5131E3A10814E4FB5007D75587FC94C = -100
    show rs_image_D5131E3A10814E4FB5007D75587FC94C as rs_image_D5131E3A10814E4FB5007D75587FC94C zorder zorder_rs_image_D5131E3A10814E4FB5007D75587FC94C onlayer master
    hide rs_image_D5131E3A10814E4FB5007D75587FC94C

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_D5131E3A10814E4FB5007D75587FC94C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 1.2

    if sys_effect2_current_file != "sound/Effect Sound/Fight 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fight 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fight 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_A354D565142F4203AABA29F37DA989A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 1

    show rs_image_E012DA552AAF4732B56A50F034C2EF8E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 1.4

    if sys_effect_current_file != "sound/Effect Sound/Battle 6.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 6.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_913A439CB7C24FD4B8994A270816E4F2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 1

    window show

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "外套被……！可恶，没教养的！！"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    # Gallery unlock: images/CG/Welcomt-to-wolfs-celemony/Welcomt-to-wolfs-celemony 5.png
    $ zorder_rs_image_AB1B0D4593B3493595C05D2634542B0F = -100
    show rs_image_AB1B0D4593B3493595C05D2634542B0F as rs_image_AB1B0D4593B3493595C05D2634542B0F zorder zorder_rs_image_AB1B0D4593B3493595C05D2634542B0F onlayer master
    hide rs_image_AB1B0D4593B3493595C05D2634542B0F

    show rs_image_AB1B0D4593B3493595C05D2634542B0F as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.3

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "怎、怎么了！？发生什么了？！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "大家还好吗！？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "一之濑！你咋拿绳子了？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，至、至少能防身用……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "正好！现在马上把这家伙收拾起来！！"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_F1E694F9D98E4371B8F767497249ECEE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_72C7208BCF0A400195B83FAF43272EFD as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "什么什么，到底怎么了？为什么导游会被这样？？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "之后再解释！！\n抓紧用你那个绝对无法逃脱的那啥技术把这家伙绑起来！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_002A89DFBF4D4BD99E942D6EA4C98777 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "明、明白——！完全不明白现状不过，导游，做好觉悟——！！"

    pause 0.3

    window hide

    pause 0.4

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_51E1CA5715FC4887A4E4083BB8D521B0
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 3

    if sys_music_current_file != "sound/BGM/Solve the case.ogg":
        play music "sound/BGM/Solve the case.ogg" loop
        $ sys_music_current_file = "sound/BGM/Solve the case.ogg"

    pause 0.7

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_47456310D2C044289ADB15696A271647 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    # Gallery unlock: images/CG/Welcomt-to-wolfs-celemony/Welcomt-to-wolfs-celemony 8.png
    $ zorder_rs_image_95153E5DF032453584ADEE5B712511FC = -100
    show rs_image_95153E5DF032453584ADEE5B712511FC as rs_image_95153E5DF032453584ADEE5B712511FC zorder zorder_rs_image_95153E5DF032453584ADEE5B712511FC onlayer master
    hide rs_image_95153E5DF032453584ADEE5B712511FC

    show rs_image_95153E5DF032453584ADEE5B712511FC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A2F5530406854E5098F52F72EE26DA66

    window show

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "…………你想抵抗到什么时候。差不多，也该说点什么了。"

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "这是最后忠告了。你的目的是什么？消失的家伙们呢？"

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊——是嘛。那差不多该问问你的身体了。"

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "想活命就趁现在了。\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "……你所说的孩子，意外地还是很残酷的哦？"

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "…………。{w}…………有……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "终于愿意说了。再给你一次机会，好好说清楚。"

    pause 0.3

    window hide

    stop music fadeout 3
    $ sys_music_current_file = ""

    pause 0.3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.8

    window show

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "……{w}你们…………"

    window hide

    stop effect2 fadeout 1.5
    $ sys_effect2_current_file = ""

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_0FFAFB81CEF94E09AE209050BCCD9627 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.7

    if sys_music_current_file != "sound/BGM/Hotel 3.ogg":
        play music "sound/BGM/Hotel 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 3.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……回来了。"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_13EEE138043542FB90557CFB44BADDE4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦——辛苦了～咋样？犯人招供了么？"

    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "没，强硬到完全不肯开口。喊了这么半天都快累死了……"

    show rs_image_5FBD78374DA74E3DAE8DB6DA14DD5616 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "连穗海都没辙……真强。{w}反正逃不掉，慢慢来。"

    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……是啊。"

    window hide

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_D21B7923E9E24A7C92B7226F129DCD18 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    show rs_image_BEE780ABA64C4D7ABB8972D17BDCBFAB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "我们回来了。{w}和朔一起又搜索了一遍，没有找到任何人。"

    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "那个人显出身姿是在抓获绫濑同学几分钟后。\n所以不可能藏到很远的地方去。"

    window hide

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_03464FF4C9E0402D927F78F065C5045C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_2B709367A1FA4DEF815337B5B014517C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我、我们回来了。{w}果然，不仅是手机，酒店的电话也不能用……"

    show rs_image_E435B1F7BF9B4AB280BA8F0C6B392FB1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "用望远镜看向港口那边，也没有船只停靠。\n看来除了等待接应的船没有其他出岛的方法了。"

    show rs_image_A6E2B83133264FE2AC7ED2F9767DAB76 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三天两夜的话，明天早上就该来了。本来回程也应该是那个导游开船的……"

    show rs_image_CF5AA529110045B9AA052BA9023E6FA3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "或许也并不能期待回程的船能按时到达……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_0FFAFB81CEF94E09AE209050BCCD9627 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    show rs_image_07F2639BB0524AEBB4F93F1989365243 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "这样……\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "诶，森海前辈呢？"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，友君的话没关系的，只是去厕所了。"

    show rs_image_20D50D7E2029427A96A2E0A6E34FC3DD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "绫濑君被袭击的时候，正好是去厕所的途中……"

    show rs_image_D7DFB9C596074724958BBE78FF9336D3 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "如此这般，所以那时才会出现在走廊呐。"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_D21B7923E9E24A7C92B7226F129DCD18 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_F9AEB450C2A74F568F5D4EC1B5A961F0 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……我回来了。"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_0BD950ADC14245578BC5105060EF0E00 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君，欢迎回来。"
    show rs_image_E53075204ECC459689595B5A7E7E345C as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……没、关系吗？"

    show rs_image_5465258BCE404B519910FD1F4172107B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……还好……"

    show rs_image_8791FBC16EE045C8A5316E8761B3EC61 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君……"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_8A626993E4D845D382910F0B900F3F2B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "肯、肯定会没事的！\n绫濑君也是，大家都会没事的！！"

    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……！"

    pause 0.3

    window hide

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_03464FF4C9E0402D927F78F065C5045C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.2

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2


    if judge_lm_condition([]):
        jump block_00003C23

    return

label block_00003C23:
    # Node: 00003C23 (歡迎來到食人狼之館 5)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_47456310D2C044289ADB15696A271647 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Switch 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Switch 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Switch 1.ogg"

    show rs_image_85B3D08EC940443EA7124D6973822305 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_70576159A31C474CAECF9B7AFDBBF16F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Nori.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Nori.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Nori.ogg"

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "那个导游……不见了！！"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F5B3A302BF394B7D97ED83BF270F3B88 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "真、真的假的！？可、可是，那么紧怎么可能会自己逃得掉！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是、是啊，我之前也有过一次，\n那种就算是再怎么柔软的人都不可能……"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "是、是不是绳子上有什么地方不结实，后来断了……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_62324AD297554FE987C680452CEE232E "不，绳子上没有明显的痕迹。"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_B7004DEEA80C41CC8F336C87E7A09F2E as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "……"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "共犯……？"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2F778F94B33845D09CADF7780A31F9FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_E435B1F7BF9B4AB280BA8F0C6B392FB1 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "怎、怎么会！？\n那岂不是我们中有人故意让别人陷入危险境地吗！？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、不一定是我们，那些突然不见的酒店里的人也很有可能的！？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔……如果是那样，今天搜索这么多次一个人都没见到岂不是很奇怪？"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "正是如此。我们中存在叛徒。"
    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "这是肯定的。"

    pause 0.6

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_85B3D08EC940443EA7124D6973822305 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_7C7F47B899A04C1E9877716E2B4CC7B5 "{size=36}！？{/size}"

    pause 0.4

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "为、为什么能那么确定？"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_EB303C47CCBE4F71ADE893A14B858F6E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……其实，之前从那个导游口中问出过一个情报，\n一直没告诉大家抱歉了。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_862E41C0B01E451EB9C2E88AECBFEDBB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不过，那家伙很明确地说了，\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "『你们之中存在叛徒』！！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_EAAB6CC3A5464202B2C5DE5D303795FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "怎、怎么会……！"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_3766CD2AF98244F5AECA23E096C299D8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "背、背叛我们的人现在站出来还来得及！\n现在不会发火的！出来就原谅你！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "到底把忍和大家带到什么地方了！？快点还回来！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_2F778F94B33845D09CADF7780A31F9FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我、我不是！！对，对了，我有不在场证明！！\n晚饭后一直在和穗海聊天，然后又和奥村……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我、我也不是！可以对绳子做指纹检查的！\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，不过那就是我的绳子，肯定有指纹……"

    show rs_image_B07AFDECD18C45CCA1315EC195BD4924 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "冷、冷静下来，前辈们！这也可能是挑拨离间！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_62324AD297554FE987C680452CEE232E "但是，这也是一种可能性，考虑一下也不坏。{w}\n结合至今为止我们做过的事……"

    pause 0.3

    window hide

    pause 0.3

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 1.4

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.3

    window show

    pause 0.3

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那个啊～不一定非得找出是谁哦？\n只是我们中存在叛徒这一个情报就已经很有用了。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "慎酱，那是什么意思！？"

    show rs_image_40F4B3A56AFE46FCB14F4500CD625791 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_music_current_file != "sound/BGM/Hotel 2.ogg":
        play music "sound/BGM/Hotel 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 2.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "试着反过来想想，不要试着找叛徒，而要想想为什么会有叛徒。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_9D0666C01E89408289145D59F704EFAB as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "？？？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_A15B5B9C211846009204F1689FC8781E as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "也就是说，如果真的想置我们于危险境地的话，\n我们中的任何人都不可能会帮忙的对不对？"

    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "而且，现在也没有被罪恶感压倒仍然保持匿名的话，\n就是说这可能只是玩乐的程度。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "所以，被抓的人应该全都没事，至于这个情况，冷静看待就好♪"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_1E50AF4024FA4A80BD7205FE7C7FF1DF as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_3C9E62B61C1744D1BDFDAD9A5EDD41C6 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哦、哦哦……哦哦哦！！确、确实可能是这样呐！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不愧是奥村！说不定这只是旅行中的一个特别事件，这么想就好了！"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_1FA6F2C9243447E081F983AD4BC2B829 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……有那么乐观么……？"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B7160626341D450BA6B06268F29E3AEA as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_97AEAB5F7F86404C83B970C313450D38 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "更加轻松一点用游玩的感觉对待就好！{w}\n这样会很没意思哦，对这种现实版解谜游戏。"

    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好好释放压力也就不会有更年期了呐，\n不能太过在意，尤其是对于青春期的我们！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3B13044431874BE09020F9368D6A8C29 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好——！先是准备战斗，肚子饿了——！腹空无以为战！"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9387C2EF08BB4EFABA360A19A1E02C8B as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱！去厨房拿点好吃的♪这种紧急情况也只能这样了！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_E54B94670E804565963ECDB491A87076 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好主意！和导游捉迷藏，越来越有意思了！"

    pause 0.3

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 1

    window show

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……我不会像他们那样天真。{w}\n叛徒仍然是有的，我要先回去了。"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我、我该怎么办……\n"
    show rs_image_328406EB66B449C99EAA3BC3E5C0EE95 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "友君接下来要怎么做？"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶？我……"

    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_9ACAEF851EAF4CECBC5BA7CA6AAF6C36 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_EAAB6CC3A5464202B2C5DE5D303795FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.4

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸？作、作哉君？不是回房间了吗？"

    show rs_image_B2C01DFF41914E56A428EBCACA72C51F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……你也过来。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_B2C01DFF41914E56A428EBCACA72C51F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_EAAB6CC3A5464202B2C5DE5D303795FC as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好、好疼疼！不、不要那么强硬地拉我也可以的～！"

    pause 0.3

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 1.5

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    window show

    pause 0.3

    rs_character_62324AD297554FE987C680452CEE232E "大家都走了呐。我们该如何是好？"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔、嗯……"

    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……总之先整理一下现今的情报为好。"

    show rs_image_CA65E37C24FB460390BADAD95767936C as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "是啊，守的房间的样子也有些记不清了。"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_35B9BEFBF42E474DB41387E9345C36B4 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_296DD986D1424E4AA97E52E2A1ECE378 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_D7DFB9C596074724958BBE78FF9336D3 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那、那个——我也加入你们可以吗？\n怎么说我似乎无处可去了呐。啊哈哈。"

    show rs_image_37D78F77FCE84A4C91C869D15099E48F as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "当然可以。森海同学一直是和我们分头行动的，\n将情报集中到一起会很有用的。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_8324EB6AB2224B36AD6FF9F96528FCC6 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那我们赶快开始！"

    pause 0.3

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    window hide

    pause 1.5

    image illation_count = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#FFFFFF",
        size=52,
        text_align=0.0)

    image illation_title = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#FFFFFF",
        size=76,
        text_align=0.5)

    image illation_title_small = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#FFFFFF",
        size=46,
        text_align=0.5)

    image illation_choice1 = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#FFFFFF",
        size=46,
        text_align=0.5)

    image illation_choice2 = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#FFFFFF",
        size=46,
        text_align=0.5)

    if judge_lm_condition([]):
        jump block_00003C24

    return

label block_00003C24:
    # Node: 00003C24 (Q1)
    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.4

    show illation_count (_("问题一")) as illation_count at Transform(xpos=75, ypos=55) zorder 200
    show illation_title (_("叛徒是否存在？")) as illation_title at Transform(xalign=0.5, ypos=150) zorder 200
    show illation_choice1 (_("应该存在")) as illation_choice1 at Transform(xalign=0.5, ypos=290) zorder 200
    show illation_choice2 (_("不存在")) as illation_choice2 at Transform(xalign=0.5, ypos=408) zorder 200
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if judge_lm_condition([]):
        jump block_00003C25

    return

label block_00003C25:
    # Node: 00003C25 (Q1)
    $ sys_lm_menu_item = [{"pos": (48, 280),"image": "images/Selection/CP2F6Illation/Selector.png","hover": "images/Selection/CP2F6Illation/Selector hover.png","name": "１"}, {"pos": (48, 396),"image": "images/Selection/CP2F6Illation/Selector.png","hover": "images/Selection/CP2F6Illation/Selector hover.png","name": "２"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - popup.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_345
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    hide illation_count
    hide illation_title
    hide illation_choice1
    hide illation_choice2
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"１\"" }]):
        jump block_00003C26
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"２\"" }]):
        jump block_00003C27

    return

label block_00003C26:
    # Node: 00003C26 (1)
    $ set_window("イベントモード")
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_C528CA6C6F534006B6F789027BE5C781 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是啊，导游都直接那么说了，要从绳子里脱出一人也不可能。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide


    if judge_lm_condition([]):
        jump block_00003C28

    return

label block_00003C28:
    # Node: 00003C28 (Q2)
    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show illation_count (_("问题二")) as illation_count at Transform(xpos=75, ypos=55) zorder 200
    show illation_title_small (_("世依木守是在哪里被袭击的？")) as illation_title at Transform(xalign=0.5, ypos=150) zorder 200
    show illation_choice1 (_("房间内")) as illation_choice1 at Transform(xalign=0.5, ypos=290) zorder 200
    show illation_choice2 (_("房间外")) as illation_choice2 at Transform(xalign=0.5, ypos=408) zorder 200
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if judge_lm_condition([]):
        jump block_00003C29

    return

label block_00003C29:
    # Node: 00003C29 (Q2)
    $ sys_lm_menu_item = [{"pos": (48, 280),"image": "images/Selection/CP2F6Illation/Selector.png","hover": "images/Selection/CP2F6Illation/Selector hover.png","name": "１"}, {"pos": (48, 396),"image": "images/Selection/CP2F6Illation/Selector.png","hover": "images/Selection/CP2F6Illation/Selector hover.png","name": "２"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - popup.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_346
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    hide illation_count
    hide illation_title
    hide illation_choice1
    hide illation_choice2
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"１\"" }]):
        jump block_00003C2A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"２\"" }]):
        jump block_00003C3D

    return

label block_00003C2A:
    # Node: 00003C2A (1)
    $ set_window("イベントモード")
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "眼镜还在盒子里，{w}那家伙视力很差，不会没戴眼镜就到外面去的。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide


    if judge_lm_condition([]):
        jump block_00003C2C

    return

label block_00003C2C:
    # Node: 00003C2C (Q3)
    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show illation_count (_("问题三")) as illation_count at Transform(xpos=75, ypos=55) zorder 200
    show illation_title_small (_("世依木守是被谁如何袭击的？")) as illation_title at Transform(xalign=0.5, ypos=150) zorder 200
    show illation_choice1 (_("被面熟的叛徒趁机袭击")) as illation_choice1 at Transform(xalign=0.5, ypos=290) zorder 200
    show illation_choice2 (_("被变态那啥了")) as illation_choice2 at Transform(xalign=0.5, ypos=408) zorder 200
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0


    if judge_lm_condition([]):
        jump block_00003C2B

    return

label block_00003C2B:
    # Node: 00003C2B (Q３)
    $ sys_lm_menu_item = [{"pos": (48, 280),"image": "images/Selection/CP2F6Illation/Selector.png","hover": "images/Selection/CP2F6Illation/Selector hover.png","name": "１"}, {"pos": (48, 396),"image": "images/Selection/CP2F6Illation/Selector.png","hover": "images/Selection/CP2F6Illation/Selector hover.png","name": "２"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - popup.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_347
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    hide illation_count
    hide illation_title
    hide illation_choice1
    hide illation_choice2
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"１\"" }]):
        jump block_00003C2D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"２\"" }]):
        jump block_00003C3C

    return

label block_00003C2D:
    # Node: 00003C2D (1)
    $ set_window("イベントモード")
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_8DC6F44BF4644738BCD14828D87C2679 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "如果是被那个导游强行袭击的，隔壁的夕阳君肯定是能听到的。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide


    if judge_lm_condition([]):
        jump block_00003C30

    return

label block_00003C30:
    # Node: 00003C30 (Q4)
    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show illation_count (_("问题四")) as illation_count at Transform(xpos=75, ypos=55) zorder 200
    show illation_title_small (_("赤峰兄弟是被谁如何袭击的？")) as illation_title at Transform(xalign=0.5, ypos=150) zorder 200
    show illation_choice1 (_("被导游奇袭")) as illation_choice1 at Transform(xalign=0.5, ypos=290) zorder 200
    show illation_choice2 (_("被叛徒趁乱袭击")) as illation_choice2 at Transform(xalign=0.5, ypos=408) zorder 200
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0


    if judge_lm_condition([]):
        jump block_00003C2F

    return

label block_00003C2F:
    # Node: 00003C2F (Q4)
    $ sys_lm_menu_item = [{"pos": (48, 280),"image": "images/Selection/CP2F6Illation/Selector.png","hover": "images/Selection/CP2F6Illation/Selector hover.png","name": "１"}, {"pos": (48, 396),"image": "images/Selection/CP2F6Illation/Selector.png","hover": "images/Selection/CP2F6Illation/Selector hover.png","name": "２"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - popup.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_348
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    hide illation_count
    hide illation_title
    hide illation_choice1
    hide illation_choice2
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"１\"" }]):
        jump block_00003C2E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"２\"" }]):
        jump block_00003C3B

    return

label block_00003C2E:
    # Node: 00003C2E (1)
    $ set_window("イベントモード")
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_F9AEB450C2A74F568F5D4EC1B5A961F0 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那两人的房间充满灰尘，那肯定是和犯人争斗时留下的。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "和忍的时候一样，攻击完全无效。要是有竹刀的话或许还……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide


    if judge_lm_condition([]):
        jump block_00003C32

    return

label block_00003C32:
    # Node: 00003C32 (Q5)
    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show illation_count (_("问题五")) as illation_count at Transform(xpos=75, ypos=55) zorder 200
    show illation_title (_("导游是如何逃脱的？")) as illation_title at Transform(xalign=0.5, ypos=150) zorder 200
    show illation_choice1 (_("自力逃脱")) as illation_choice1 at Transform(xalign=0.5, ypos=290) zorder 200
    show illation_choice2 (_("被叛徒解救")) as illation_choice2 at Transform(xalign=0.5, ypos=408) zorder 200
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0


    if judge_lm_condition([]):
        jump block_00003C31

    return

label block_00003C31:
    # Node: 00003C31 (Q5)
    $ sys_lm_menu_item = [{"pos": (48, 280),"image": "images/Selection/CP2F6Illation/Selector.png","hover": "images/Selection/CP2F6Illation/Selector hover.png","name": "１"}, {"pos": (48, 396),"image": "images/Selection/CP2F6Illation/Selector.png","hover": "images/Selection/CP2F6Illation/Selector hover.png","name": "２"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - popup.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_349
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    hide illation_count
    hide illation_title
    hide illation_choice1
    hide illation_choice2
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"１\"" }]):
        jump block_00003C33
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"２\"" }]):
        jump block_00003C3E

    return

label block_00003C33:
    # Node: 00003C33 (1)
    $ set_window("イベントモード")
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "难道犯人有非常柔软的身体？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide


    if judge_lm_condition([]):
        jump block_00003C34

    return

label block_00003C34:
    # Node: 00003C34 (Q6)
    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show illation_count (_("问题六")) as illation_count at Transform(xpos=75, ypos=55) zorder 200
    show illation_title_small (_("世依木守失踪前最后见到的是？")) as illation_title at Transform(xalign=0.5, ypos=150) zorder 200
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4


    if judge_lm_condition([]):
        jump block_00003C35

    return

label block_00003C35:
    # Node: 00003C35 (Q6)
    $ sys_lm_menu_item = [{"pos": (156, 250),"image": "images/Selection/CP2F6Illation/Tomo.png","hover": "images/Selection/CP2F6Illation/Tomo hover.png","name": "友"}, {"pos": (281, 250),"image": "images/Selection/CP2F6Illation/Shinobu.png","hover": "images/Selection/CP2F6Illation/Shinobu hover.png","name": "しのぶ"}, {"pos": (406, 250),"image": "images/Selection/CP2F6Illation/Tsuki.png","hover": "images/Selection/CP2F6Illation/Tsuki hover.png","name": "月"}, {"pos": (531, 250),"image": "images/Selection/CP2F6Illation/Sora.png","hover": "images/Selection/CP2F6Illation/Sora hover.png","name": "空"}, {"pos": (86, 416),"image": "images/Selection/CP2F6Illation/Tsubasa.png","hover": "images/Selection/CP2F6Illation/Tsubasa hover.png","name": "つばさ"}, {"pos": (212, 416),"image": "images/Selection/CP2F6Illation/Sakuya.png","hover": "images/Selection/CP2F6Illation/Sakuya hover.png","name": "作哉"}, {"pos": (337, 416),"image": "images/Selection/CP2F6Illation/Shintaro.png","hover": "images/Selection/CP2F6Illation/Shintaro hover.png","name": "慎太郎"}, {"pos": (462, 416),"image": "images/Selection/CP2F6Illation/Saburo.png","hover": "images/Selection/CP2F6Illation/Saburo hover.png","name": "三朗"}, {"pos": (588, 416),"image": "images/Selection/CP2F6Illation/Mamoru.png","hover": "images/Selection/CP2F6Illation/Mamoru hover.png","name": "マモル"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - popup.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_350
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    hide illation_count
    hide illation_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if judge_lm_condition([]):
        jump block_00003C36

    return

label block_00003C36:
    # Node: 00003C36 (Q7)
    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show illation_count (_("问题七")) as illation_count at Transform(xpos=75, ypos=55) zorder 200
    show illation_title_small (_("导游逃脱时没有不在场证明的是？")) as illation_title at Transform(xalign=0.5, ypos=150) zorder 200
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4


    if judge_lm_condition([]):
        jump block_00003C37

    return

label block_00003C37:
    # Node: 00003C37 (Q7)
    $ sys_lm_menu_item = [{"pos": (156, 250),"image": "images/Selection/CP2F6Illation/Tomo.png","hover": "images/Selection/CP2F6Illation/Tomo hover.png","name": "友"}, {"pos": (281, 250),"image": "images/Selection/CP2F6Illation/Shinobu.png","hover": "images/Selection/CP2F6Illation/Shinobu hover.png","name": "しのぶ"}, {"pos": (406, 250),"image": "images/Selection/CP2F6Illation/Tsuki.png","hover": "images/Selection/CP2F6Illation/Tsuki hover.png","name": "月"}, {"pos": (531, 250),"image": "images/Selection/CP2F6Illation/Sora.png","hover": "images/Selection/CP2F6Illation/Sora hover.png","name": "空"}, {"pos": (86, 416),"image": "images/Selection/CP2F6Illation/Tsubasa.png","hover": "images/Selection/CP2F6Illation/Tsubasa hover.png","name": "つばさ"}, {"pos": (212, 416),"image": "images/Selection/CP2F6Illation/Sakuya.png","hover": "images/Selection/CP2F6Illation/Sakuya hover.png","name": "作哉"}, {"pos": (337, 416),"image": "images/Selection/CP2F6Illation/Shintaro.png","hover": "images/Selection/CP2F6Illation/Shintaro hover.png","name": "慎太郎"}, {"pos": (462, 416),"image": "images/Selection/CP2F6Illation/Saburo.png","hover": "images/Selection/CP2F6Illation/Saburo hover.png","name": "三朗"}, {"pos": (588, 416),"image": "images/Selection/CP2F6Illation/Mamoru.png","hover": "images/Selection/CP2F6Illation/Mamoru hover.png","name": "マモル"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - popup.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_351
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    hide illation_count
    hide illation_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if judge_lm_condition([]):
        jump block_00003C38

    return

label block_00003C38:
    # Node: 00003C38 (Q8)
    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show illation_count (_("问题八")) as illation_count at Transform(xpos=75, ypos=55) zorder 200
    show illation_title (_("叛徒是？")) as illation_title at Transform(xalign=0.5, ypos=150) zorder 200
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6


    if judge_lm_condition([]):
        jump block_00003C39

    return

label block_00003C39:
    # Node: 00003C39 (Q8)
    $ sys_lm_menu_item = [{"pos": (156, 250),"image": "images/Selection/CP2F6Illation/Tomo.png","hover": "images/Selection/CP2F6Illation/Tomo hover.png","name": "友"}, {"pos": (281, 250),"image": "images/Selection/CP2F6Illation/Shinobu.png","hover": "images/Selection/CP2F6Illation/Shinobu hover.png","name": "しのぶ"}, {"pos": (406, 250),"image": "images/Selection/CP2F6Illation/Tsuki.png","hover": "images/Selection/CP2F6Illation/Tsuki hover.png","name": "月"}, {"pos": (531, 250),"image": "images/Selection/CP2F6Illation/Sora.png","hover": "images/Selection/CP2F6Illation/Sora hover.png","name": "空"}, {"pos": (86, 416),"image": "images/Selection/CP2F6Illation/Tsubasa.png","hover": "images/Selection/CP2F6Illation/Tsubasa hover.png","name": "つばさ"}, {"pos": (212, 416),"image": "images/Selection/CP2F6Illation/Sakuya.png","hover": "images/Selection/CP2F6Illation/Sakuya hover.png","name": "作哉"}, {"pos": (337, 416),"image": "images/Selection/CP2F6Illation/Shintaro.png","hover": "images/Selection/CP2F6Illation/Shintaro hover.png","name": "慎太郎"}, {"pos": (462, 416),"image": "images/Selection/CP2F6Illation/Saburo.png","hover": "images/Selection/CP2F6Illation/Saburo hover.png","name": "三朗"}, {"pos": (588, 416),"image": "images/Selection/CP2F6Illation/Mamoru.png","hover": "images/Selection/CP2F6Illation/Mamoru hover.png","name": "マモル"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - popup.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 1) from _call_lm_menu_352
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    hide illation_count
    hide illation_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if judge_lm_condition([]):
        jump block_00003C3A

    return

label block_00003C3A:
    # Node: 00003C3A (歡迎來到食人狼之館 6)
    $ set_window("イベントモード")
    stop music fadeout 3
    $ sys_music_current_file = ""

    if sys_effect3_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 5

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_A477062F5CFB45259A5183ED5584C4A5 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    window show

    rs_character_62324AD297554FE987C680452CEE232E "可惜，错了。"

    pause 0.4

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_47456310D2C044289ADB15696A271647 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_D244929D2FE04BEBB96CD94BCD6EB0BA as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_EAB6125F00314E55BA76194FA758EFA9

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Battle 5.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_51451FBF94C8444AA5696178E72CE210 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Battle 5.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_4D8F1D6A70C24A34A3E6C37B69619470 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 3

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    # Gallery unlock: images/CG/Welcomt-to-wolfs-celemony/Welcomt-to-wolfs-celemony 6.png
    $ zorder_rs_image_99E537CF1D264E8A9DC364659ADA92B3 = -100
    show rs_image_99E537CF1D264E8A9DC364659ADA92B3 as rs_image_99E537CF1D264E8A9DC364659ADA92B3 zorder zorder_rs_image_99E537CF1D264E8A9DC364659ADA92B3 onlayer master
    hide rs_image_99E537CF1D264E8A9DC364659ADA92B3

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_99E537CF1D264E8A9DC364659ADA92B3 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    pause 0.5

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Nori.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Nori.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Nori.ogg"

    window show

    rs_character_62324AD297554FE987C680452CEE232E "好了，闹剧结束，真是辛苦你们了。那边的处理也已经结束了呐。"

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "是的，朔大人。\n在尽快消除记忆后已经直接送到{color=#FF0000}那位大人{/color}那里了。"

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "这个黄头发的就是最后一个了？\n呼～这次的工作比平时的要辛苦太多了。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "朔、朔……是……共犯……？不……可能……\n你可……一直都和我……在一起……的……"

    rs_character_3AD49134E90444729FD2EFC8D1296F7D "哦呀，意识还残留着……朔大人，夕阳大人也要由我们来处理吗？"

    pause 0.4

    rs_character_62324AD297554FE987C680452CEE232E "……{w}……不，他的话…………"

    window hide

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_20A8817D51644BE6A7913BD30673F110

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 4

    $ set_window("イベントモード")
    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 2.5

    stop effect3 fadeout 2
    $ sys_effect3_current_file = ""

    show rs_image_202D019D0CEB444FB06F28FE932B89CB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.5

    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_CA176C5A71144199A2E3AE0C60846C57 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    pause 0.4

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀～真是快乐的旅行呐！"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_E683F1ECE3314055A6535AFF3A0F039A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，第一天天气很糟，不过第二天开始就是晴天了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_9387C2EF08BB4EFABA360A19A1E02C8B as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱面对泳池时那股紧张感，想想就觉得……！哈哈哈！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊——好烦——！为什么雨说停就停了！？\n拜此所赐被看到了好羞耻的一面……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_D3A7495152E44A10B9BD045BA5CCCDE8 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_5ECF4017CE3E48E0B749AA1981DD40C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "作哉君也很坏心眼呐，没必要逼到那种程度的。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_054279E603CE4B2A9A7A8F8E26DF9492 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我只是在活用猫山作为角色的特长。\n说是这么说，空也很喜欢这种对不对？"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_4A2DF19F343B45378225DB529BF9F33C as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "打西瓜也很有意思，能在那种地方感觉到平日练习的成果……不错。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_0BD950ADC14245578BC5105060EF0E00 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "果然月君很厉害呐！我只是在原地转圈，一步也走不动……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_296DD986D1424E4AA97E52E2A1ECE378 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "终于是回到有信号的地方了。啊——到底来了多少邮件了呐。"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_3E667A569CC54E86B612A79E21C9EC9E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "作为交换，完全不被打扰地好好玩了一场不是很好嘛♪\n那个，确认邮件，确认邮件……"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2D2761902CAE44EC807DF631A55BE304 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇！一口气来了好多！震动停不下来。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我这边也是。加藤君，松田君，泉君也……？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "伊藤和木村也发了。真是的，耐不住气的家伙们。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我这边也来了，真是一群闲人。\n这是一会儿也等不了非要听我们好好聊聊的节奏了啊！！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_1E50AF4024FA4A80BD7205FE7C7FF1DF as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "诶……?……？那个……空君，有件事情我想确认一下……"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_9A51889A5B884F76838CF8C5D3725812 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯？什么事？……"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_F738E6401CA340F19552857151823031 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "诶！为何！？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_33C65BBD622D4D51B8D81050A5F71B11 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-90, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "究竟是怎么会是……我们应该是周五出发，\n经过三天两夜的旅行后回来……"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_BE7A49A1C27E4A9EAA9EEF3DB775CAA5 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    rs_character_57471360F48A413AB843A4E46D8C5541 "可是……今天不是周日……是{w=0.6}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    extend "{size=28}周一！？{/size}"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "……也就是说……？"

    pause 0.5

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    window hide

    stop music fadeout 1
    $ sys_music_current_file = ""

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_7C7F47B899A04C1E9877716E2B4CC7B5 "{size=32}学校！！！？？{/size}"

    window hide

    pause 0.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 2.5

    if sys_effect3_current_file != "sound/Effect Sound/Wave 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Wave 2.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Wave 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_090B423E9FDD4F1BA744187FBD7BB4A9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_266255D4821A4095BCA7860D44F0A511

    if sys_music_current_file != "sound/BGM/Hotel 1.ogg":
        play music "sound/BGM/Hotel 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 1.ogg"

    pause 2.5

    show rs_image_8409DB7FAADF495087B6E4B602F1F374 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DCEBC7527B8F4B4EA0FF44E692174034

    pause 3

    stop effect3 fadeout 1.5
    $ sys_effect3_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91


    if judge_lm_condition([]):
        jump block_00003C5C

    return

label block_00003C5C:
    # Node: 00003C5C (CP2 Daytime Hotel 朔)
    call block_00003C40 from _call_block_00003C40

    if judge_lm_condition([]):
        jump block_00003BBB

    return

label block_00003BBB:
    # Node: 00003BBB (歡迎來到食人狼之館 7)
    $ set_window("イベントモード")
    stop music fadeout 1
    $ sys_music_current_file = ""

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_1FA0293EBE6E473086100ED3BC00B11F

    pause 2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_596F4961E48C4D78A7EDBC2BDA784CAA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.8

    window show

    pause 0.3

    rs_character_62324AD297554FE987C680452CEE232E "这次的活动满意吗？{w}{color=#FF00FF}晦哥{/color}。"

    window hide

    pause 0.3

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1.5

    if sys_effect2_current_file != "sound/Effect Sound/Thunder 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Thunder 1.ogg"

    if sys_music_current_file != "sound/BGM/Monster 1.ogg":
        play music "sound/BGM/Monster 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Monster 1.ogg"

    $ zorder_tag_A45595F91B474CC9A0810932B96DD8EC = 300
    show rs_image_5EB13F937774441CAAE6E8F5717F6920 as tag_A45595F91B474CC9A0810932B96DD8EC at center_top zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.7

    window show

    pause 0.3

    rs_character_EE1903694D624E399209772C95A20AAA "啊，那可自然。直到最后都，很好，呢。"

    hide tag_A45595F91B474CC9A0810932B96DD8EC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_A45595F91B474CC9A0810932B96DD8EC = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_2F430E02CF774048BDB58B5FE52C418B as tag_A45595F91B474CC9A0810932B96DD8EC at right_top zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    show rs_image_E0C9131CA0E2485C9F7FBB4809296E2F as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.3

    rs_character_EE1903694D624E399209772C95A20AAA "你很清楚令哥哥高兴的方法嘛。真是贤慧的弟弟。"

    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "毕竟是最重要的哥哥的生日，早就决定好要送上最好的礼物了。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_C925EF76DB674B98A239202896D4806D as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "嗯，味道凝重的主菜呐，确实有神秘故事的味道。"

    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "那只是偶然罢了。\n脱下狸猫布偶装后那些家伙也很聒噪，然后稍微玩了一下。"

    show rs_image_67A5BF46DA6A49B7A37971AD05A21477 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "朔，你还没弄对。那个布偶不是狸猫。"

    show rs_image_3149C4BF55744A498D9A6BE1CAAF3483 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "我对这个并不关心。\n"
    show rs_image_D41773CA35204737A4DF7ACE459D6756 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "倒是……明明有合适的人，坏心眼。"

    show rs_image_10EDC597730C48C187CE16D28C4DEB17 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "他因为要考试也很忙的。因为我是大人，不会提任性的要求，会好好忍耐的。。"

    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "都那么发散压力了，耐性才这么点。"

    show rs_image_2F430E02CF774048BDB58B5FE52C418B as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "啊，对了对了，也要向酒店那些人道谢呐。\n没想到真会从梅咲一路赶来，吓了我一跳。"

    show rs_image_67A5BF46DA6A49B7A37971AD05A21477 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "他们平时店里随便向老头子们抛几个眉眼就能大把捞钱，\n这次真是委屈了。"

    show rs_image_D7DFB9C596074724958BBE78FF9336D3 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "好像很忙的样子，大家第一天就都回店里去了。"

    show rs_image_EDB46CC6778D4FE0858464DE11647DF8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "即便如此听闻事件后，二话不说就答应下来。{w}\n足以一窥和哥哥的关系。还是一如既往的会使唤人。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_149C51C26D3D4ED4920A747F413CE022 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "莫语他人恶评，此谓人望。平时我们都是在一起工作的。"

    show rs_image_3149C4BF55744A498D9A6BE1CAAF3483 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "谁知道。"
    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……我这边的触手们也干了很多，\n大家都叫着说肌肉痛。"

    show rs_image_67A5BF46DA6A49B7A37971AD05A21477 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "是哦，等会要送点膏药过去。不知道对触手酱们管不管用？呼呼。"

    window hide

    hide tag_A45595F91B474CC9A0810932B96DD8EC
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    window show

    pause 0.3

    rs_character_62324AD297554FE987C680452CEE232E "先不说这个，这次到底是吹的什么风？"

    rs_character_62324AD297554FE987C680452CEE232E "哥哥的话，不是喜欢更加成熟的类型嘛。"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_A45595F91B474CC9A0810932B96DD8EC = 300
    show rs_image_C925EF76DB674B98A239202896D4806D as tag_A45595F91B474CC9A0810932B96DD8EC at center_top zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "嗯，不过，一直都品尝着美味的东西的话，\n有时也会腻的，就想试一些一般的东西。"

    hide tag_A45595F91B474CC9A0810932B96DD8EC
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A45595F91B474CC9A0810932B96DD8EC = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_EBB886D8C67B4B0F935343DC8454B874 as tag_A45595F91B474CC9A0810932B96DD8EC at right_top zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    show rs_image_D7237C565A3B4E798F5B4E551B4FE0A8 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "这一点和哥哥的趣味完全不相称。那么，你的恋人又怎么说？"

    show rs_image_5EB13F937774441CAAE6E8F5717F6920 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "他是特别的。朔虽然长大了点，内心还是小孩子呐。\n恋人并不是只令自己满足的人哦。"

    show rs_image_3149C4BF55744A498D9A6BE1CAAF3483 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "嗯——……"

    show rs_image_67A5BF46DA6A49B7A37971AD05A21477 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "并不需要奢求什么，只要能在一起就很满足了。\n只要能增加两人间的回忆就很幸福了。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_C925EF76DB674B98A239202896D4806D as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EE1903694D624E399209772C95A20AAA "不觉得很美妙么？保持着理性，成为像人类一样的自己。"

    show rs_image_E0C9131CA0E2485C9F7FBB4809296E2F as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "……无趣。所有恋爱并不是都像哥哥说的那样的。"

    show rs_image_2F430E02CF774048BDB58B5FE52C418B as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EE1903694D624E399209772C95A20AAA "还是那么不坦率呐。\n"
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_10EDC597730C48C187CE16D28C4DEB17 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "……可，朔，哥哥全都看到了。"

    show rs_image_3149C4BF55744A498D9A6BE1CAAF3483 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_62324AD297554FE987C680452CEE232E "……什么事？"

    window hide

    pause 0.3

    hide tag_A45595F91B474CC9A0810932B96DD8EC
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    show rs_image_4C7B0452B51546E8A6B501F94A0F93E9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 1.5

    $ zorder_tag_A45595F91B474CC9A0810932B96DD8EC = 300
    show rs_image_10EDC597730C48C187CE16D28C4DEB17 as tag_A45595F91B474CC9A0810932B96DD8EC at center_top zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.6

    window show

    pause 0.3

    rs_character_EE1903694D624E399209772C95A20AAA "我只收到了九个礼物。朔真是坏孩子，其中一个被抢走了吧？"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_A45595F91B474CC9A0810932B96DD8EC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_3149C4BF55744A498D9A6BE1CAAF3483 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_62324AD297554FE987C680452CEE232E "……"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_A45595F91B474CC9A0810932B96DD8EC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A45595F91B474CC9A0810932B96DD8EC = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_CED2471FD5264B5B82273369AE30FA2B as tag_A45595F91B474CC9A0810932B96DD8EC at right_top zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    show rs_image_E0C9131CA0E2485C9F7FBB4809296E2F as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_EE1903694D624E399209772C95A20AAA "为何要做那种事。告诉哥哥你的理由。"

    show rs_image_3149C4BF55744A498D9A6BE1CAAF3483 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_62324AD297554FE987C680452CEE232E "……他……应该不合哥哥的口味。{w}太过野蛮……我个人认为。"

    show rs_image_10EDC597730C48C187CE16D28C4DEB17 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    rs_character_EE1903694D624E399209772C95A20AAA "嗯……"

    window hide

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Thunder 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Thunder 1.ogg"

    # Gallery unlock: images/CG/Welcomt-to-wolfs-celemony/Welcomt-to-wolfs-celemony 7.png
    $ zorder_rs_image_6416585972644DE1BFEFE64812811D22 = -100
    show rs_image_6416585972644DE1BFEFE64812811D22 as rs_image_6416585972644DE1BFEFE64812811D22 zorder zorder_rs_image_6416585972644DE1BFEFE64812811D22 onlayer master
    hide rs_image_6416585972644DE1BFEFE64812811D22

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_6416585972644DE1BFEFE64812811D22 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 1

    window show

    rs_character_EE1903694D624E399209772C95A20AAA "不可能不合我的口味的，再怎么说，他可是……"

    rs_character_62324AD297554FE987C680452CEE232E "……"

    rs_character_EE1903694D624E399209772C95A20AAA "啊——我指名的十个人里他可是最受期待的呐。\n做好受处罚的觉悟了？"

    rs_character_EE1903694D624E399209772C95A20AAA "{nw}"
    window hide

    extend "{color=#800080}还是说，{/color}{w}{color=#800080}那个孩子是朔看上的？{/color}{w}{color=#800080}那样的话就饶了你。{/color}{w}\n{w=0.3}{color=#800080}不过，如果不是的话……{/color}"

    window hide

    rs_character_62324AD297554FE987C680452CEE232E "……"

    rs_character_EE1903694D624E399209772C95A20AAA "嗯～？"

    rs_character_62324AD297554FE987C680452CEE232E "……{w}……"
    stop music fadeout 0.5
    $ sys_music_current_file = ""

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "……一股酒臭味，哥哥，你喝多了。\n马上给我去洗脸，然后，多喝水。"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_A45595F91B474CC9A0810932B96DD8EC = 300
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 300
    show rs_image_596F4961E48C4D78A7EDBC2BDA784CAA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D64F60163C0440CDA776A48688E14063 as tag_A45595F91B474CC9A0810932B96DD8EC at right_top zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    show rs_image_7591B090AFF548F4B3459E7CA9BD2848 as tag_E99970E1386B453DAF81C3AE2C72BE8E at left_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 0.3

    if sys_music_current_file != "sound/BGM/Hotel 1.ogg":
        play music "sound/BGM/Hotel 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Hotel 1.ogg"

    rs_character_EE1903694D624E399209772C95A20AAA "欸——！！接下来才是有趣的地方的说！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_62324AD297554FE987C680452CEE232E "真是的……喝酒喝到语气都变了真是没出息。\n醉酒的哥哥太傲慢了，我讨厌这样。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "今天不许继续喝了。知道自己开瓶会有什么下场么。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_EBB886D8C67B4B0F935343DC8454B874 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EE1903694D624E399209772C95A20AAA "朔，最后那个问题，好好回答一下嘛～"

    show rs_image_C276775808CC478299E73F38A0ED0B5B as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "对了对了，回床上去也很容易出问题，今天就请你睡浴室了。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_D64F60163C0440CDA776A48688E14063 as tag_A45595F91B474CC9A0810932B96DD8EC zorder zorder_tag_A45595F91B474CC9A0810932B96DD8EC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EE1903694D624E399209772C95A20AAA "只、只有这个还请饶了我！我可是很柔软的，不在床上就睡不着的……！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_351932D89641414887A798BAE92493AB as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_62324AD297554FE987C680452CEE232E "不许抱怨。要恨的话只有一次也好还请恨你自己。"

    window hide

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_A45595F91B474CC9A0810932B96DD8EC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_8409DB7FAADF495087B6E4B602F1F374 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.3

    window show

    pause 0.3

    rs_character_62324AD297554FE987C680452CEE232E "唔……{w}俗话说的，难照顾的哥哥……"

    window hide

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A45595F91B474CC9A0810932B96DD8EC
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_B6D2CFDC1CB5407EACD7FBC1D100D198

    call scb_flag_title_end(2, _("「欢迎来到食人狼之馆」")) from _call_scb_flag_title_end_9

    if judge_lm_condition([]):
        jump block_00003BB9

    return

label block_00003BB9:
    # Node: 00003BB9 (Phase: 0)
    $ C2S6Phase = 0
    if Chapter <> 2:
        $ del C2S6Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_00003BBD
    if judge_lm_condition([]):
        jump block_00003BB8

    return

label block_00003BBD:
    # Node: 00003BBD (終了)

    return

label block_00003BB8:
    # Node: 00003BB8 (FINISH)
    $ C2S6 = True
    $ TalkSoraF6After = True
    $ TalkTsukiF6After = True
    $ TalkSaburoF6After = True
    $ TalkShintaroF6After = True
    $ TalkShinobuF6After = True
    $ TalkYuuhiMamoruF6After = True
    $ TalkTsubasaF6After = True
    $ F6Check1 = False

    if judge_lm_condition([]):
        jump block_00003BBE

    return

label block_00003BBE:
    # Node: 00003BBE (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_10

    if judge_lm_condition([]):
        jump block_00003BBD

    return

label block_00003C3E:
    # Node: 00003C3E (2)
    $ set_window("イベントモード")
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "在穗海前辈的询问后，我们就放置导游一个人在那里了。\n叛徒趁那个机会解开绳子……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide


    if judge_lm_condition([]):
        jump block_00003C34

    return

label block_00003C3B:
    # Node: 00003C3B (2)
    $ set_window("イベントモード")
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_8DC6F44BF4644738BCD14828D87C2679 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "阿月和小空如果抵抗的话肯定会有很大的声响，可是并没有人听到过。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide


    if judge_lm_condition([]):
        jump block_00003C32

    return

label block_00003C3C:
    # Node: 00003C3C (2)
    $ set_window("イベントモード")
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_69E4B1516C13405D8DC9ADE4070255DB as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说、说什么呢？夕阳君好下流！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide


    if judge_lm_condition([]):
        jump block_00003C30

    return

label block_00003C3D:
    # Node: 00003C3D (2)
    $ set_window("イベントモード")
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_3766CD2AF98244F5AECA23E096C299D8 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "夕阳君去房间看情况的时候确实存在争斗的痕迹，肯定是在室外遇袭的。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide


    if judge_lm_condition([]):
        jump block_00003C2C

    return

label block_00003C27:
    # Node: 00003C27 (2)
    $ set_window("イベントモード")
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AC27A45CC157410884B3090FD8432964 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_D9B482934C42403EA8360ECACCBDBC67 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at left_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_A6E70EA9F30F4DE4AD20434ED388ACFF as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我们之中才不会有叛徒！\n"
    show rs_image_8DC6F44BF4644738BCD14828D87C2679 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "可是，这样的话导游是怎么从绳子里逃脱的呢？"

    show rs_image_07F2639BB0524AEBB4F93F1989365243 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔、唔……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide


    if judge_lm_condition([]):
        jump block_00003C28

    return

