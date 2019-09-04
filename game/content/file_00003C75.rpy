# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003C75 (CHAPTER 3)

label block_00003C76:
    # Node: 00003C76 ()
    $ C3ShowLastWarning = False
    $ C3S1Phase = 0
    $ C3S2Phase = 0
    $ C3S3Phase = 0
    $ C3S4Phase = 0
    $ C3S5Phase = 0
    $ C3S6Phase = 0
    $ C3QNewsclubPhase = 0
    $ C3QNakayamaPhase = 0
    $ C3QYakyukenPhase = 0
    $ C3QYakyukenCheck1 = False
    $ C3QYakyukenClearState = False
    $ C3S3BeforeResidentialStreetFirstEnter = True
    $ TalkTsukiSoraF1After = False
    $ TalkTsubasaQShiroAfter = False
    $ TalkItouKimura = False
    $ TalkShintaro = 0
    $ TalkRikuta = 0
    $ TalkOkajima = 0
    $ TalkTsubasa = 0
    $ TalkTsuki = 0
    $ TalkSora = 0
    $ StudyCount = 0
    $ TalkSaburo = False
    $ TalkShinobu = 0
    $ TalkShinobuF2After = False
    $ TalkKiyo = False
    $ TalkNakayamasenior = 0
    $ FinalStudyCount = 0

    if judge_lm_condition([]):
        jump block_00003C77

    return

label block_00003C77:
    # Node: 00003C77 (OP)
    pause 1.5

    hide tag_29984812EACB4CA3AD0E4907D975E500
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0


    if judge_lm_condition([]):
        jump block_00003C84

    return

label block_00003C84:
    # Node: 00003C84 (CP3 Start)
    pause 1.8

    $ set_window("イベントモード")
    if sys_music2_current_file != "sound/Effect Sound/Swallow 1.ogg":
        play music2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_5013EC64CA634A9E9754EF6FE927CCD2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 2

    show rs_image_52A4FB95B188448396BFCDB678787F82 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    show rs_image_52A4FB95B188448396BFCDB678787F82 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.3

    window show

    rs_character_B69F854062C6466DB78FEEAEF86A4073 "哈哈，发生过这种事情呐。{w}\n嗯？{w=0.4}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "不好，已经这个时间了。"

    pause 0.3

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B444FDE4EF1A43E5A2345A44A71061D5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_B69F854062C6466DB78FEEAEF86A4073 "友～！早上了～！早上了～！"

    rs_character_B69F854062C6466DB78FEEAEF86A4073 "再见，忍君。{w}因为要去机场我必须走了。接下来就拜托了。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，我明白。请走好，注意安全。"

    rs_character_B69F854062C6466DB78FEEAEF86A4073 "一直以来真是太感谢了。那我先走了。"

    window hide

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Switch 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Switch 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    window show

    if sys_music_current_file != "sound/BGM/The past precious.ogg":
        play music "sound/BGM/The past precious.ogg" loop
        $ sys_music_current_file = "sound/BGM/The past precious.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，起床了。\n你妈妈已经走了。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_090583914F36486EA2E7A56AF765A727 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔～哦～……{w}\n……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_FA5B703A676F4C829E63A8555EB84BD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "再睡五分钟。"

    show rs_image_D5EEA08F613D4581B90B56569FE7A25D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不——行。已经不早了，没时间给你折腾。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的～……外面太冷了不要不要～……{w=0.3}{nw}"
    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_41210EA5B30342049A9A851AEFDF7211 = 300
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D8F88F968B9E4B3CBEED302C0FA2B323 as tag_41210EA5B30342049A9A851AEFDF7211 at left_top zorder zorder_tag_41210EA5B30342049A9A851AEFDF7211 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_41210EA5B30342049A9A851AEFDF7211
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_D8F88F968B9E4B3CBEED302C0FA2B323 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "别撒娇！你都多大了！一点都不可爱！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1F7EBBD8148642B1BC2DC1A8430AE7A7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "给你半分钟！起来！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_9B8DAC89E5144010A4E0E9EF7657680E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫——！忍好暴力～"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "硬要形容这也只是“{color=#00FFFF}顾家的忍{/color}”而已。"

    window hide

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_507130D7BD574651B179D6DEF2CE814D = 400
    
    show rs_image_B444FDE4EF1A43E5A2345A44A71061D5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"
    
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F6493A7AD5749CFA41012A9D048C1F5 as tag_507130D7BD574651B179D6DEF2CE814D zorder zorder_tag_507130D7BD574651B179D6DEF2CE814D onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"


    show rs_image_3E86770DDFC949EA90C3480E2A3AC643 as tag_507130D7BD574651B179D6DEF2CE814D zorder zorder_tag_507130D7BD574651B179D6DEF2CE814D onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    pause 2

    hide tag_507130D7BD574651B179D6DEF2CE814D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.6

    if sys_music_current_file != "sound/BGM/Chapter 3.ogg":
        play music "sound/BGM/Chapter 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 3.ogg"

    pause 0.5

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 200
    show rs_image_B6AB8ED7C4FF45F685270512420E0C03 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ set_place_title(_("友的房间"))
    $ set_window("(標準)")
    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "准备好了？没落下东西吧？{w}好，那就去学校。"

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("友的房间"))

    if judge_lm_condition([]):
        jump block_00003C78

    return

label block_00003C78:
    # Node: 00003C78 (Chapter3)
    $ Chapter = 3
    $ StudyCount = C3StudyCountInitValue
    $ del C3StudyCountInitValue
    $ TalkOkajima = C3TalkOkajimaInitNumber
    $ del C3TalkOkajimaInitNumber
    $ C3QYakyukenClearState = [False] * 3

    if judge_lm_condition([]):
        jump block_00003C79

    return

label block_00003C79:
    # Node: 00003C79 (Home)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Out.png","hover": "images/MOVING/ACTIONS/Out hover.png","name": "移動"}, {"pos": (408, 192),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "写真"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_703
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003C7D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"写真\"" },{ "scope": 1, "content": "C3SPhoto == False" }]):
        jump block_00003C7B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"写真\"" }]):
        jump block_00003C7C

    return

label block_00003C7D:
    # Node: 00003C7D (CP3 Daytime Misaki 友忍)
    call block_00002629 from _call_block_00002629

    if judge_lm_condition([]):
        jump block_00003C8B

    return

label block_00003C8B:
    # Node: 00003C8B (CP3 Daytime)
    call block_00001948 from _call_block_00001948

    if judge_lm_condition([{ "scope": 0, "content": "SYSReviewMode == True" }]):
        jump block_00003FBC
    if judge_lm_condition([]):
        jump block_00003FA9

    return

label block_00003FBC:
    # Node: 00003FBC (Data passby)
    $ E_TAG_TalkOkajimaInitNumber = TalkOkajima
    $ E_TAG_StudyCount = Max(E_TAG_StudyCount, StudyCount)

    if judge_lm_condition([]):
        jump block_00003FAD

    return

label block_00003FAD:
    # Node: 00003FAD ()
    $ del C3ShowLastWarning
    $ del C3S1Phase
    $ del C3S2Phase
    $ del C3S3Phase
    $ del C3S4Phase
    $ del C3S5Phase
    $ del C3S6Phase
    $ del C3QNewsclubPhase
    $ del C3QNakayamaPhase
    $ del C3QYakyukenPhase
    $ del C3QYakyukenCheck1
    $ del C3QYakyukenClearState
    $ del C3S3BeforeResidentialStreetFirstEnter
    $ del TalkTsukiSoraF1After
    $ del TalkTsubasaQShiroAfter
    $ del TalkItouKimura
    $ del TalkShintaro
    $ del TalkRikuta
    $ del TalkOkajima
    $ del TalkTsubasa
    $ del TalkTsuki
    $ del TalkSora
    $ del StudyCount
    $ del TalkSaburo
    $ del TalkShinobu
    $ del TalkShinobuF2After
    $ del TalkKiyo
    $ del TalkNakayamasenior
    $ del FinalStudyCount

    return

label block_00003FA9:
    # Node: 00003FA9 (END)
    pause 1.5

    play music "sound/BGM/Theme/Schoolboys Theme - Bet of Love.ogg" noloop

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show black
    show rs_image_2AA11555E74B47CEBCD61F4C0B239F9A as border_1 zorder 100:
        alpha 1
        pause 153.85
        linear 1 alpha 0
    show rs_image_6DAA391E5F2A40618487F4AF2067F4AC as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    show rs_image_29E65B9F2B294317A6C20C0C2C26C0DE ("{color=#42A5F5}ORIGINAL{/color}\nスクールボーイズ！\nスクールボーイズ！歩\n{size=16}© 2016 Kiriya, Kasasagi{/size}\n\n{color=#42A5F5}CASTS{/color}\nTomo Moriumi\nShinobu Ayase\nTsubasa Ichinose\nSakuya Houmi\nTsuki Akamine\nSora Akamine\nShintarou Okumura\nSaburou Nekoyama\nShirou Nekoyama\nYukio Sakaki\nTsubasa-chan\nYuuhi\nNori\nMamoru Seigi\nKei Itou\nItsuki Kimura\nHikaru Satou\nNaoya Okajima\nTadashi Kojima\nJyunta Katou\nKenji Matsuda\nKakeru Izumi\nKobayashi\nMinami\nIsao Rikuta\nKokoro Sugimoto\nTakehito Kiyoshi\nKanon Nakayama\nYuusuke Okajima\nShion Nakayama\nMr. Nameko\nSyougintoki Suwabe\nSyouhei Suwabe\nYumi Nakajima\nOwner of Ramen shop\nOwner of Sushi shop\nOwner of Madchen Cafe\nOwner of Dagashi shop\nTentacle A\nTentacle B\nDark lesser panda\nMonster A\nMonster B\nMonster C\nOther monsters\nKyubi\nSusumu Tokiwa\nKouya Sakase\nKai\nHe——\nBe——\n\n{color=#42A5F5}RESOURCES{/color}\nDOVA-SYNDROME\n音楽素材MusMus\nMusic is VFR\nポケットsound\n369\n音楽の卵\n小森平の使い方\n効果音ラボ\nGATAG (Steinway & Sons/Alan Alim)\n野田工房P\nOn-Jin ~音人~\n素材Good\nぴぽや\n\n{color=#42A5F5}OPENING THEME{/color}\n{size=30}Don't be afraid!!{/size}\n{size=16}by t.tam{/size}\n\n{color=#42A5F5}ENDING THEME{/color}\n{size=30}愛をかけて{/size}\n{size=16}by t.tam{/size}\n\n{color=#42A5F5}OPENING ANIMATION{/color}\nしょうちゃん\n\n{color=#42A5F5}PROGRAMMING{/color}\nLundarl Gholoi\n\n{color=#42A5F5}QUALITY ASSURANCES{/color}\nr98341034\n超级大白\n幽月艾\n凤箫剑\nTony Yang\n\n{color=#42A5F5}LOCALIZATION - CHINESE{/color}\nLundarl Gholoi\nr98341034\n电摩星人\n幽月艾\n") as staff_list zorder 1000:
        xanchor 0
        yanchor 0
        xpos 40
        ypos 650
        alpha 1
        parallel:
            linear 151 ypos 0
        parallel:
            linear 151 yanchor 1.0

    show rs_image_29E65B9F2B294317A6C20C0C2C26C0DE "{size=20}To Be Continue...?{/size}" as staff_1 zorder 1000:
        xanchor 0
        yanchor 0.5
        xpos 40
        ypos 300
        alpha 0
        pause 151
        linear 2 alpha 1    
    
    pause 154

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1

    hide staff_list
    hide border_1
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1

    hide staff_1
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    stop music fadeout 1

    pause 2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_32D0BBC2E623421F81987D13AFF8B019 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.5

    $ zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD = 300
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_514AB31E9F5945EEA9AD0CA77359CA06 as tag_0BDB8A4A05BB44ED81AE140BE96066BD at center_bottom zorder zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD onlayer master
    show rs_image_9C058B4785934A84B6E833C97FAFAA9B _("{font=font/zcool-happy-ayumi-extended.ttf}第三章 完成{/font}") as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_center zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 2

    $ set_window("体育祭、音楽祭")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#000000}接下来会进入“学期末”（二周目）章节。{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#000000}此章节内满足一定条件可重新进行一周目的故事。{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#000000}因此二周目也请记得随时保存。{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#000000}下面请保存你的{/color}{color=#FF0000}通关进度{/color}{color=#000000}。{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003FAA

    return

label block_00003FAA:
    # Node: 00003FAA (Set: SaveCaption)
    $ _lm_save_caption = "第三章結束后（通關進度）"

    if judge_lm_condition([]):
        jump block_00003FAB

    return

label block_00003FAB:
    # Node: 00003FAB (Save)
    call screen save

    if judge_lm_condition([]):
        jump block_00003FAC

    return

label block_00003FAC:
    # Node: 00003FAC (SaveCaption: NULL)
    $ _lm_save_caption = ""

    if judge_lm_condition([]):
        jump block_00003FAF

    return

label block_00003FAF:
    # Node: 00003FAF (CLEAR)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_0BDB8A4A05BB44ED81AE140BE96066BD
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 1


    if judge_lm_condition([]):
        jump block_00003FB0

    return

label block_00003FB0:
    # Node: 00003FB0 (Final score)
    call block_00003F3E from _call_block_00003F3E

    if judge_lm_condition([]):
        jump block_00003FBD

    return

label block_00003FBD:
    # Node: 00003FBD (Generate parameter)
    $ EOSStudyCount = 0
    $ EOSStudyCount = StudyCount
    $ EOSTalkOkajimaInitNumber = 0
    $ EOSTalkOkajimaInitNumber = TalkOkajima
    $ EOSAllowTriggleSukimotoTalk = False
    if (TalkRikuta > 0) or (VarExists("C3AllowTriggleSukimotoTalk")):
        $ EOSAllowTriggleSukimotoTalk = True

    if judge_lm_condition([]):
        jump block_00003FB2

    return

label block_00003FB2:
    # Node: 00003FB2 (END OF SEMESTER)
    $ del C3ShowLastWarning
    $ del C3S1Phase
    $ del C3S2Phase
    $ del C3S3Phase
    $ del C3S4Phase
    $ del C3S5Phase
    $ del C3S6Phase
    $ del C3QNewsclubPhase
    $ del C3QNakayamaPhase
    $ del C3QYakyukenPhase
    $ del C3QYakyukenCheck1
    $ del C3QYakyukenClearState
    $ del C3S3BeforeResidentialStreetFirstEnter
    $ del TalkTsukiSoraF1After
    $ del TalkTsubasaQShiroAfter
    $ del TalkItouKimura
    $ del TalkShintaro
    $ del TalkRikuta
    $ del TalkOkajima
    $ del TalkTsubasa
    $ del TalkTsuki
    $ del TalkSora
    $ del StudyCount
    $ del TalkSaburo
    $ del TalkShinobu
    $ del TalkShinobuF2After
    $ del TalkKiyo
    $ del TalkNakayamasenior
    $ del FinalStudyCount
    jump block_00003CBD

    return

label block_00003C7B:
    # Node: 00003C7B (Photo event)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_9C7CF5F1B0FA4AD9B3C445C4FFD0CE32 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.5

    # Gallery unlock: images/CG/Photo 2.png
    $ zorder_rs_image_3B270FDC9BBD4F209FD7C52684B74402 = -100
    show rs_image_3B270FDC9BBD4F209FD7C52684B74402 as rs_image_3B270FDC9BBD4F209FD7C52684B74402 zorder zorder_rs_image_3B270FDC9BBD4F209FD7C52684B74402 onlayer master
    hide rs_image_3B270FDC9BBD4F209FD7C52684B74402

    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    show rs_image_3B270FDC9BBD4F209FD7C52684B74402 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈哈，不管什么时候看，这张照片的友都好有趣……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——为什么——"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "自己猜……{size=16}♪{/size}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那样的话我有更有趣的照片哦。"

    window hide

    pause 0.5

    # Gallery unlock: images/CG/Photo 3.png
    $ zorder_rs_image_C95DA2C7DAF24261815104970FA26629 = -100
    show rs_image_C95DA2C7DAF24261815104970FA26629 as rs_image_C95DA2C7DAF24261815104970FA26629 zorder zorder_rs_image_C95DA2C7DAF24261815104970FA26629 onlayer master
    hide rs_image_C95DA2C7DAF24261815104970FA26629

    show rs_image_C95DA2C7DAF24261815104970FA26629 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.8

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呵呵！『忍{color=#FF8040}なめ太郎{/color}』 {size=12}{color=#C0C0C0}*日本一种吉祥物，样子请看忍的表情{/color}{/size}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这不是友擅自设成我的LINE的头像的么。{w}就这么有意思？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈！当然了。{w}哈哈！当然了真的和忍很像哦♪"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……呵呵～"

    window hide

    pause 0.8

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    $ set_place_title(_("友的房间"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003C7A

    return

label block_00003C7A:
    # Node: 00003C7A (C3S照片)
    $ C3SPhoto = True

    if judge_lm_condition([]):
        jump block_00003C79

    return

label block_00003C7C:
    # Node: 00003C7C (Photo)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_9C7CF5F1B0FA4AD9B3C445C4FFD0CE32 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003C79

    return

