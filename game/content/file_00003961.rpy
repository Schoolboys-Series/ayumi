# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003961 (CHAPTER 2)

label block_00003962:
    # Node: 00003962 ()
    $ TalkTomoTsubasaF1 = False
    $ TalkMatsutaF2 = 0
    $ TalkIzumiF2 = 0
    $ TalkTsukiF2 = 0
    $ TalkKatouF2 = 0
    $ TalkNamekoF2 = 0
    $ TalkShintaroF2 = 0
    $ TalkShinobuF2 = 0
    $ TalkSoraF2 = 0
    $ TalkKimuraF3After = False
    $ TalkIzumiF3After = False
    $ TalkSaburoF4After = False
    $ TalkShintaroF4After = False
    $ TalkSumoRikuF4After = False
    $ TalkSumoRikuF5After = False
    $ TalkShinobuF6After = False
    $ TalkTsubasaF6After = False
    $ TalkSoraF6After = False
    $ TalkTsukiF6After = False
    $ TalkSaburoF6After = False
    $ TalkYuuhiMamoruF6After = False
    $ TalkShintaroF6After = False
    $ TalkKimuraQKimuraAfter = False
    $ TalkResidentialQYuuhi = False
    $ TalkSchoolQYuuhi = False
    $ TalkHomeQYuuhi = False
    $ TalkJinjaQYuuhi = False
    $ TalkSumoRiku = 0
    $ TalkTsukiSora = False
    $ TalkKimura = 0
    $ TalkItou = 0
    $ TalkSatou = 0
    $ TalkMatsuta = 0
    $ TalkKatou = 0
    $ TalkYuuhi = 0
    $ TalkOkajima = 0
    $ TalkTsubasa = 0
    $ TalkIzumi = 0
    $ TalkShinobu = 0
    $ F1ToiletCheck = False
    $ F2Check1 = False
    $ F6Check1 = False
    $ C2S1Phase = 0
    $ C2S2Phase = 0
    $ C2S3Phase = 0
    $ C2S4Phase = 0
    $ C2S5Phase = 0
    $ C2S6Phase = 0
    $ C2QNewsclubPhase = 0
    $ C2QYuuhiPhase = 0
    $ FEnterForest = True
    $ StudyCount = 0
    $ TalkKatouStudy = False

    if judge_lm_condition([]):
        jump block_00003C80

    return

label block_00003C80:
    # Node: 00003C80 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_9

    if judge_lm_condition([]):
        jump block_00003964

    return

label block_00003964:
    # Node: 00003964 (OP)
    pause 1.5

    hide tag_29984812EACB4CA3AD0E4907D975E500
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0


    if judge_lm_condition([]):
        jump block_00003965

    return

label block_00003965:
    # Node: 00003965 (CP2 Start)
    pause 1.8

    $ set_window("イベントモード")
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 2.5

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Daily 2.ogg":
        play music "sound/BGM/Daily 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 200
    show rs_image_952D06E912C54776B1C4F5BB577DFB95 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_87A4A951CCF94134BEC8CCB7D574B6E1 as tag_061CD0864C4E48C0B3AA935440B7C90D at right_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.9

    show rs_image_3CDBB93600FA40048DE19330047E1350 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "真是的，你怎么老这样！"

    show rs_image_E262B3AC8BDF48E4A8BEEBA281DFA194 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……对不起……"

    show rs_image_C0F02B9EC0484E97848C810E5DD5BB34 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "今天总之先把学校的库存制服给你，将就着过好了。"

    show rs_image_9BAD09B7F4DE47339C69A165D80E6844 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "还有，要是有空记得过来，我还有事找你。"

    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是……"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（呜，这次一定会被大骂一顿了。）"

    window hide

    pause 0.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_983AAB15D221450491B2AE59ADC6E0CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E171694AA5EA439D89CA41EAFBA81DEA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈哈哈，一如既往的友的作风呐。"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_A6E70EA9F30F4DE4AD20434ED388ACFF as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "太过分了忍！明明昨天在一起时根本就没提醒我！"

    show rs_image_1F55CB120A6948E28641DFC1C52982EE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊——？我说了，是你没听到。"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "才没说！绝——对没说！！"

    show rs_image_5D3A0AF418B44317B24FC87798F86D15 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……行就算没说，别老怨别人。{w}\n反正最后吃亏的也是你自己。{nw}"
    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend ""

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_2D2761902CAE44EC807DF631A55BE304 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"
    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at right_top zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "看招！！{w=0.7}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……居然闪开了！？"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_E171694AA5EA439D89CA41EAFBA81DEA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "同样的手段不会奏效两次。笨蛋笨蛋。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么！！{w}可恶！{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.1

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_2C5EC61F9FAC4FDA897D61101BDE1CB3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.6

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E7E6E31C347642E086AADC4895CE778C as tag_C3CCF1D5899F4E609345C51A82FBFFAE at right_top zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.1

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_4A9AC5BBBA6D44F5B5DCB7EEF0B9EAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "混蛋！！"

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.2

    rs_character_62D2A2AA61774A129B8EF3867F430DA8 "你们！！再说一遍这里是图书馆！！"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_5465258BCE404B519910FD1F4172107B as tag_C3CCF1D5899F4E609345C51A82FBFFAE at left_top zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    show rs_image_0C866D450EF342189ED1497939E81294 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.3

    rs_character_3A742340BEAD415FAC80AFEA0A84B586 "对、对不起……"

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
    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
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
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_EE31CA18510041B0B14F3F78B918C22F as tag_507130D7BD574651B179D6DEF2CE814D at center_bottom zorder zorder_tag_507130D7BD574651B179D6DEF2CE814D onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DFF2A9F38FC64BFD8997DE5E33FE4870 as tag_507130D7BD574651B179D6DEF2CE814D zorder zorder_tag_507130D7BD574651B179D6DEF2CE814D onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 2

    $ set_window("(標準)")
    hide tag_507130D7BD574651B179D6DEF2CE814D
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.6

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_00003967

    return

label block_00003967:
    # Node: 00003967 (Chapter: 2)
    $ Chapter = 2
    if SYSReviewMode == False:
        $ GKarutaStage = [0] * 44
        $ FillMem(GKarutaStage, False)
    $ TalkOkajima = C2TalkOkajimaInitNumber
    $ del C2TalkOkajimaInitNumber

    if judge_lm_condition([]):
        jump block_00003969

    return

label block_00003969:
    # Node: 00003969 (Library)
    $ sys_lm_menu_item = [{"pos": (250, 179),"image": "images/Chapter 2/Menu/Shinobu.png","hover": "images/Chapter 2/Menu/Shinobu hover.png","name": "しのぶ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_280
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00003968
    if judge_lm_condition([]):
        jump block_00003B8C

    return

label block_00003968:
    # Node: 00003968 (忍)
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_8FD0C8C99F91493DB85D4EB39544B538 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说起来，友，\n期中考试你真的不复习？"

    show rs_image_12E3E3C881C34AC09EF31505C89F7982 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "至少试着学点东西啊。这次再不及格就要惩罚。\n好了就这样。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——不要嘛——！{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "啊，这样说是不是考得好就有奖励呐！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6D5C4FC6CA71418A8875E35D505835E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你又……"
    show rs_image_12E3E3C881C34AC09EF31505C89F7982 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "到时候就“乖乖好孩子，下次继续努力”这样好了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不要不要——！不讲理——！"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8FD0C8C99F91493DB85D4EB39544B538 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……不想管你了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("图书馆"))

    if judge_lm_condition([{ "scope": 0, "content": "TalkShinobu == 1" }]):
        jump block_00003969
    if judge_lm_condition([]):
        jump block_0000396B

    return

label block_0000396B:
    # Node: 0000396B (T++)
    $ TalkShinobu = TalkShinobu + 1

    if judge_lm_condition([]):
        jump block_00003969

    return

label block_00003B8C:
    # Node: 00003B8C (CP2 Daytime)
    call block_000008C9 from _call_block_000008C9

    if judge_lm_condition([]):
        jump block_0000405A

    return

label block_0000405A:
    # Node: 0000405A (Check)

    if judge_lm_condition([{ "scope": 0, "content": "SYSReviewMode == True" }]):
        jump block_00003FBA
    if judge_lm_condition([]):
        jump block_00003C5F

    return

label block_00003FBA:
    # Node: 00003FBA (Data passby)
    if (TalkSumoRiku >= 3) or (E_TAG_C3AllowTriggleSukimotoTalk == True):
        $ E_TAG_C3AllowTriggleSukimotoTalk = True
    else:
        $ E_TAG_C3AllowTriggleSukimotoTalk = False
    $ E_TAG_TalkOkajimaInitNumber = TalkOkajima
    $ E_TAG_StudyCount = Max(E_TAG_StudyCount, StudyCount)

    if judge_lm_condition([]):
        jump block_00003CB8

    return

label block_00003CB8:
    # Node: 00003CB8 ()
    $ del TalkTomoTsubasaF1
    $ del TalkMatsutaF2
    $ del TalkIzumiF2
    $ del TalkTsukiF2
    $ del TalkKatouF2
    $ del TalkNamekoF2
    $ del TalkShintaroF2
    $ del TalkShinobuF2
    $ del TalkSoraF2
    $ del TalkKimuraF3After
    $ del TalkIzumiF3After
    $ del TalkSaburoF4After
    $ del TalkShintaroF4After
    $ del TalkSumoRikuF4After
    $ del TalkSumoRikuF5After
    $ del TalkShinobuF6After
    $ del TalkTsubasaF6After
    $ del TalkSoraF6After
    $ del TalkTsukiF6After
    $ del TalkSaburoF6After
    $ del TalkYuuhiMamoruF6After
    $ del TalkShintaroF6After
    $ del TalkKimuraQKimuraAfter
    $ del TalkResidentialQYuuhi
    $ del TalkSchoolQYuuhi
    $ del TalkHomeQYuuhi
    $ del TalkJinjaQYuuhi
    $ del TalkSumoRiku
    $ del TalkTsukiSora
    $ del TalkKimura
    $ del TalkItou
    $ del TalkSatou
    $ del TalkMatsuta
    $ del TalkKatou
    $ del TalkYuuhi
    $ del TalkOkajima
    $ del TalkTsubasa
    $ del TalkIzumi
    $ del TalkShinobu
    $ del F1ToiletCheck
    $ del F2Check1
    $ del F6Check1
    $ del C2S1Phase
    $ del C2S2Phase
    $ del C2S3Phase
    $ del C2S4Phase
    $ del C2S5Phase
    $ del C2S6Phase
    $ del C2QNewsclubPhase
    $ del C2QYuuhiPhase
    $ del FEnterForest
    $ del StudyCount
    $ del TalkKatouStudy

    return

label block_00003C5F:
    # Node: 00003C5F (音楽祭)
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 200
    show rs_image_D7F70E4230154502BB28D6BA8AC09D91 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "老师，我来了。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（紧张不安……）"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F48584787114538888D5C0B826EDE5F as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "辛苦了。\n这次我想和你商量{color=#0080FF}音乐祭{/color}的事。"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊！是这个！马上就是音乐祭了！\n去年唱的是什么来着？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对了，现在就准备是不是太早了？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "不，音乐祭的第二天就是{color=#FF00FF}御咲祭{/color}，\n尽早准备以防意外。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是这样啊。\n到处都是祭典，第二学期真好！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9C78AB751CDB49FDA83251FA5B4A3825 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "接下来就会很忙了。\n要是不早点开始准备音乐祭，御咲祭就没时间准备了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "原来如此。这次是不是也要抽签？{w}\n我记得合唱是{color=#0080FF}两个班{/color}一起的。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "嗯，{color=#0080FF}和隔壁班一起{/color}。{w}\n抽签倒是没有，希望你和大家\n一起决定曲目和声部。"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那谁来弹钢琴！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D7F70E4230154502BB28D6BA8AC09D91 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "音乐老师。"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么嘛……好失望。{w}\n总之就是尽快分好声部，\n赶快练习尽可能取得优胜对不对。"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F48584787114538888D5C0B826EDE5F as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "正是。交给你了。"

    window hide

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ set_place_title(_("鞋箱"))
    pause 0.9

    $ set_place_title("")
    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2.3

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Class bell 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Class bell 1.ogg"

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 2.5

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "如上所述！！{w=0.6}现在！！{w=0.6}曲子！{w=0.6}还有声部！\n{w=0.6}就必须决定下来！{w=0.6}我是这么觉得的！！！"

    window hide

    pause 0.5

    if sys_music2_current_file != "sound/Effect Sound/Clamorous 1.ogg":
        play music2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}人声噪杂{/size}{size=28}{i}{b}！{/b}{/i}{/size}{w=0.45}{size=28}&*￥#￥*#@##@{/size}{size=28}{i}{b}！{/b}{/i}{/size}"

    window hide

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2B709367A1FA4DEF815337B5B014517C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_E7E6E31C347642E086AADC4895CE778C as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F070BDCB04D4336AC7465096F0E3084 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{b}{/b}你们——！给我听话——！{b}！！{/b}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哈哈……"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "混蛋——！！别小看我们——！"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好好——！大家看这边——！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "既视感……"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "别起哄——！奥村慎太郎——！！"

    window hide

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    # Gallery unlock: images/CG/Music festival.png
    $ zorder_rs_image_9188A4E4C6424BCEA833D3C87DC25D19 = -100
    show rs_image_9188A4E4C6424BCEA833D3C87DC25D19 as rs_image_9188A4E4C6424BCEA833D3C87DC25D19 zorder zorder_rs_image_9188A4E4C6424BCEA833D3C87DC25D19 onlayer master
    hide rs_image_9188A4E4C6424BCEA833D3C87DC25D19

    show rs_image_9188A4E4C6424BCEA833D3C87DC25D19 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我们，一班和二班，\n当天打算穿这身衣服出场～！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "欸！？\这、这种衣服是怎么弄到的！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{color=#FF0080}某咖啡店{/color}的老板友情赞助♪"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "不，我不穿，这种小孩子似的衣服。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空也就罢了，我肯定穿不来。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "有点意见也无所谓♪"

    rs_character_53FF68C192E3494AB005C1909579AFFB "部长，如何？合适吗？"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "那、那个……很合适……哦。"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "伊藤酱应该也很合适哦♪"

    rs_character_710A38AC94C841779DB701B5AC1010FD "是、是么。"

    window hide

    pause 1

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_CF5AA529110045B9AA052BA9023E6FA3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F070BDCB04D4336AC7465096F0E3084 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.3

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔…………"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那就和体育祭时一样问大家意向声部好了。{w}\n{nw}"
    show rs_image_275B22DDBE294B889403F68883C99EC9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过，选曲该怎样才好呐。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_633EE8E0E8604D0A9FB1BAE76DEA33AB as tag_346FE7CD97BB4FB18CB50E78275F4E23 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    show rs_image_A20D31D533CF44CDA4A7F67CEC353CDE as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_3A156F2DA1B1456B8040379E7303C090 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.2

    rs_character_EA9AA88E88D84B559B925363E2931756 "那样的话{color=#00FFFF}《The Moldau》{/color}如何？\n古典音乐里很有名的那个。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，我知道那首！！很好！就这个！"

    show rs_image_F640D24E91BC44AB8E0808AF82ED2885 as tag_346FE7CD97BB4FB18CB50E78275F4E23 zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "嗯，那接下来请加油了——"

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    show rs_image_514BF37F25964D04836F39E1B71FFD28 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    pause 0.6

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_CF5AA529110045B9AA052BA9023E6FA3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_68F8746793BD4E3EA7E2DA518DD13B54 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "回来————！帮忙就帮到最后啊！"

    window hide

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8


    if judge_lm_condition([]):
        jump block_00003C61

    return

label block_00003C61:
    # Node: 00003C61 (音樂祭)
    call block_00000563 from _call_block_00000563

    if judge_lm_condition([]):
        jump block_00003C70

    return

label block_00003C70:
    # Node: 00003C70 (After event)
    $ set_window("イベントモード")
    pause 0.8

    if sys_music2_current_file != "sound/Effect Sound/Clamorous 1.ogg":
        play music2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_418B2D7888D74C87A5171CEFE82AA355 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 2.5

    show rs_image_F67525886A8D46E18BC4D8326357E6FC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 2

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    show rs_image_0B3E62D93B474CFA80C2DE4B381FEC4B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    if sys_music2_current_file != "sound/Effect Sound/Fire 1.ogg":
        play music2 "sound/Effect Sound/Fire 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Fire 1.ogg"

    if sys_music_current_file != "sound/BGM/My precious time of now - piano.ogg":
        play music "sound/BGM/My precious time of now - piano.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time of now - piano.ogg"

    show rs_image_C712A610882D45D1A4B445693F2246E0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_09527D61D3AC4B06AC9CB5A39F0A0855

    pause 1.5

    window show

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀～{color=#FF0000}御咲营火{/color}，真漂亮～！\n今年作为班长干了这么多，越发觉得好了。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "说的是呢，比去年看起来更好。疲劳都一瞬间消失了。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "一之濑君们这次真的是做了很多，辛苦你们了。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "谢谢。拜你们所赐现在才能这么愉快。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈！不客气！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "没、没那么夸张的。这都是大家各司其职的必然结果。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "绫濑君也是，作为御咲祭的\n{color=#008080}手工班{/color}负责人真是受到太多照顾了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍！再多夸夸我！然后就这么把我带去吃豪华大餐也可以哦！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "并没有想对友说的话。"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "讨厌——不公平——！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "表面上这么说，背地里忍君可是一直在夸友君做得很好哦。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "空、空！不许告诉友这些。"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么嘛——！原来这样——！怎么就不能坦率呐——！你呀——！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "闭嘴——！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "怎么了？和平常的奥村不同不太活跃呢。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯——总觉得少了什么人——"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "总觉的应该——{w=0.5}{color=#00FFFF}还有一人{/color}……。{w}\n……{w=0.5}没什么，什么都没有！忘掉就好忘掉就好！"

    window hide

    pause 2

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_7926C3EA1AF24681BEBB1CF4D788BFF6

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 4

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_32D0BBC2E623421F81987D13AFF8B019 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.5

    $ zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD = 300
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_514AB31E9F5945EEA9AD0CA77359CA06 as tag_0BDB8A4A05BB44ED81AE140BE96066BD at center_bottom zorder zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD onlayer master
    show rs_image_53F792C20E22409FAC4D02C606C2D225 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 2

    $ set_window("体育祭、音楽祭")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#000000}请保存至今为止的进度。{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003C71

    return

label block_00003C71:
    # Node: 00003C71 (Set: SaveCaption)
    $ _lm_save_caption = "第二章結束后"

    if judge_lm_condition([]):
        jump block_00003C72

    return

label block_00003C72:
    # Node: 00003C72 (Save)
    call screen save

    if judge_lm_condition([]):
        jump block_00003C73

    return

label block_00003C73:
    # Node: 00003C73 (SaveCaption: NULL)
    $ _lm_save_caption = ""

    if judge_lm_condition([]):
        jump block_00003DD8

    return

label block_00003DD8:
    # Node: 00003DD8 (Generate parameter)
    if TalkSumoRiku >= 3:
        $ C3AllowTriggleSukimotoTalk = True
    $ C3StudyCountInitValue = 0
    $ C3StudyCountInitValue = StudyCount
    $ C3TalkOkajimaInitNumber = 0
    if VarExists("TalkOkajima") == True:
        $ C3TalkOkajimaInitNumber = TalkOkajima
    else:
        $ C3TalkOkajimaInitNumber = TalkOkajima
        $ del TalkOkajima

    if judge_lm_condition([]):
        jump block_00003C74

    return

label block_00003C74:
    # Node: 00003C74 (CLEAR)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_0BDB8A4A05BB44ED81AE140BE96066BD
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 1


    if judge_lm_condition([]):
        jump block_00003C7E

    return

label block_00003C7E:
    # Node: 00003C7E (CHAPTER 3)
    $ del TalkTomoTsubasaF1
    $ del TalkMatsutaF2
    $ del TalkIzumiF2
    $ del TalkTsukiF2
    $ del TalkKatouF2
    $ del TalkNamekoF2
    $ del TalkShintaroF2
    $ del TalkShinobuF2
    $ del TalkSoraF2
    $ del TalkKimuraF3After
    $ del TalkIzumiF3After
    $ del TalkSaburoF4After
    $ del TalkShintaroF4After
    $ del TalkSumoRikuF4After
    $ del TalkSumoRikuF5After
    $ del TalkShinobuF6After
    $ del TalkTsubasaF6After
    $ del TalkSoraF6After
    $ del TalkTsukiF6After
    $ del TalkSaburoF6After
    $ del TalkYuuhiMamoruF6After
    $ del TalkShintaroF6After
    $ del TalkKimuraQKimuraAfter
    $ del TalkResidentialQYuuhi
    $ del TalkSchoolQYuuhi
    $ del TalkHomeQYuuhi
    $ del TalkJinjaQYuuhi
    $ del TalkSumoRiku
    $ del TalkTsukiSora
    $ del TalkKimura
    $ del TalkItou
    $ del TalkSatou
    $ del TalkMatsuta
    $ del TalkKatou
    $ del TalkYuuhi
    $ del TalkOkajima
    $ del TalkTsubasa
    $ del TalkIzumi
    $ del TalkShinobu
    $ del F1ToiletCheck
    $ del F2Check1
    $ del F6Check1
    $ del C2S1Phase
    $ del C2S2Phase
    $ del C2S3Phase
    $ del C2S4Phase
    $ del C2S5Phase
    $ del C2S6Phase
    $ del C2QNewsclubPhase
    $ del C2QYuuhiPhase
    $ del FEnterForest
    $ del StudyCount
    $ del TalkKatouStudy
    jump block_00003C76

    return

