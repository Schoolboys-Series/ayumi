# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00001A69 (CP3 Twilight Misaki)

label block_00001A6A:
    # Node: 00001A6A (開始)
    $ HananoRandom = 0

    if judge_lm_condition([{ "scope": 0, "content": "TalkRikuta == 2" }]):
        jump block_00003DD7
    if judge_lm_condition([]):
        jump block_00001A6D

    return

label block_00003DD7:
    # Node: 00003DD7 (AllowSukimotoTalk)
    if VarExists("C3AllowSukimotoTalk") == False:
        $ C3AllowSukimotoTalk = True

    if judge_lm_condition([]):
        jump block_00001A6D

    return

label block_00001A6D:
    # Node: 00001A6D (Misaki)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "tomo"
    $ sys_ayumi_global_map_time = "twilight"

    if judge_lm_condition([]):
        jump block_00001A6E

    return

label block_00001A6E:
    # Node: 00001A6E (Misaki LCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", True, False, talk_label="block_00001A6B", target_label="block_00001A6C") from _call_scb_global_map_25
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" },{ "scope": 1, "content": "C3SShiroYuki == True" }]):
        jump block_00002FEE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"住宅街\"" }]):
        jump block_00001A6F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" }]):
        jump block_00001A77
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" }]):
        jump block_00002575
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲駅\"" }]):
        jump block_00001AA2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"昼休み\"" }]):
        jump block_000027A0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00001A6B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001A6C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001A6E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001F8A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲学園\"" }]):
        jump block_0000279E

    return

label block_00002FEE:
    # Node: 00002FEE (Park)
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

    $ set_place_title(_("公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "CXQKaruta == False" },{ "scope": 1, "content": "C3S1Phase + C3S2Phase + C3S3Phase + C3S4Phase + C3S5Phase  + C3S6Phase == 0" }]):
        jump block_00002FE6
    if judge_lm_condition([]):
        jump block_00002FE3

    return

label block_00002FE6:
    # Node: 00002FE6 (Park 小林 quest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (160, 184),"image": "images/Menu/Kobayashi quest.png","hover": "images/Menu/Kobayashi hover.png","name": "小林"}, {"pos": (320, 184),"image": "images/Menu/Minami.png","hover": "images/Menu/Minami hover.png","name": "南"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_202
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" }]):
        jump block_00002FE7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003D8F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" }]):
        jump block_0000425C

    return

label block_00002FE7:
    # Node: 00002FE7 (南)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_BEF9DE93926B41AEA207953580E58EC3 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_9A978AAD07624C598B6179F23F51FB2D "你好——友哥。放学回家吗？\n中学生这么晚还在上学呐。"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "CXQKaruta == False" },{ "scope": 1, "content": "C3S1Phase + C3S2Phase + C3S3Phase + C3S4Phase + C3S5Phase  + C3S6Phase == 0" }]):
        jump block_00002FE6
    if judge_lm_condition([]):
        jump block_00002FE3

    return

label block_00002FE3:
    # Node: 00002FE3 (Park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (160, 184),"image": "images/Menu/Kobayashi.png","hover": "images/Menu/Kobayashi hover.png","name": "小林"}, {"pos": (320, 184),"image": "images/Menu/Minami.png","hover": "images/Menu/Minami hover.png","name": "南"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_203
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" },{ "scope": 1, "content": "CXQKaruta == True" }]):
        jump block_00002FE4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" },{ "scope": 1, "content": "CXQKaruta == True" }]):
        jump block_00002FE0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" }]):
        jump block_00002FE7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" }]):
        jump block_00002FDF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003D8F

    return

label block_00002FE4:
    # Node: 00002FE4 (小林)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_F3C56AC05CFF4764BCEAA3638847A04F as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EA79386263E543A88D4DC03B8BD44485 "要一起来玩歌牌吗？"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00003DAF

    return

label block_00003DAF:
    # Node: 00003DAF (選擇)
    call scb_selector("", [{"name":"はい", "content":_("好呀")}, {"name":"いいえ", "content":_("以后再说")}]) from _call_scb_selector_16

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003DB1
    if judge_lm_condition([]):
        jump block_00002FE3

    return

label block_00003DB1:
    # Node: 00003DB1 (小林翻歌牌)
    call block_000020C2 from _call_block_000020C2_1

    if judge_lm_condition([{ "scope": 0, "content": "CXQKaruta == False" }]):
        jump block_00002FE8
    if judge_lm_condition([]):
        jump block_00003DB2

    return

label block_00002FE8:
    # Node: 00002FE8 (After)
    pause 0.5

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1CDB21F0CE5D4659A6BA9E03A4285F77 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EA79386263E543A88D4DC03B8BD44485 "啊——好好玩♪\n下次也要一起哦，友哥！"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_7AB112E4EED34DAFBB2FA71D1F060DBF as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "不过，每次都是一样的牌就太没意思了。"

    show rs_image_BEF9DE93926B41AEA207953580E58EC3 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "虽然不知道是什么时候，\n但下次遇到爷爷时我们会\n多要一些牌的。"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("公园"))

    if judge_lm_condition([]):
        jump block_00003DB3

    return

label block_00003DB3:
    # Node: 00003DB3 (QUEST FINISH)
    $ set_window("(標準)")
    if sys_music2_current_file != "sound/BGM/Quest Finished.ogg":
        play music2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.8


    if judge_lm_condition([]):
        jump block_00003DB4

    return

label block_00003DB4:
    # Node: 00003DB4 (CXQKaruta)
    $ CXQKaruta = True

    if judge_lm_condition([]):
        jump block_00003DB5

    return

label block_00003DB5:
    # Node: 00003DB5 (CLEAR)
    $ GKarutaViewMode = False

    if judge_lm_condition([]):
        jump block_00002FE3

    return

label block_00003DB2:
    # Node: 00003DB2 (CLEAR)
    $ GKarutaViewMode = False

    if judge_lm_condition([]):
        jump block_00002FEE

    return

label block_00002FE0:
    # Node: 00002FE0 (南)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_BEF9DE93926B41AEA207953580E58EC3 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_9A978AAD07624C598B6179F23F51FB2D "要看友哥所有拿到的牌吗？"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00003DB0

    return

label block_00003DB0:
    # Node: 00003DB0 (ViewMode)
    $ GKarutaViewMode = True

    if judge_lm_condition([]):
        jump block_00003DAF

    return

label block_00002FDF:
    # Node: 00002FDF (小林)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1CDB21F0CE5D4659A6BA9E03A4285F77 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EA79386263E543A88D4DC03B8BD44485 "啊！是友哥！\n呐——呐——！和我们玩！和我们玩！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "抱歉，现在友哥很忙，\n所以下次再说好吗。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1FF2B98C6C1E44809702A907624A30EB as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA79386263E543A88D4DC03B8BD44485 "欸——好的——下次见——"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002FE3

    return

label block_00003D8F:
    # Node: 00003D8F (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00003D8E

    return

label block_00003D8E:
    # Node: 00003D8E (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00003D8D

    return

label block_00003D8D:
    # Node: 00003D8D (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00001A6D

    return

label block_0000425C:
    # Node: 0000425C (小林)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1CDB21F0CE5D4659A6BA9E03A4285F77 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EA79386263E543A88D4DC03B8BD44485 "啊！是友哥！\n呐——呐——！和我们玩！和我们玩！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可以哦。年轻人就是好，\n我在学校都快用光HP了。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_034008D743F14BD3ADD73D120F5F6179 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "什么嘛，一股老人气——？\n"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_E714266E48C34071B1AFC8E511D39DD5 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那下次就不叫“友哥”改叫“友叔”好了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔，年轻人就是不知轻重！\n我还宝刀未……"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "不不不，\n这个梗对你们还太早了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说起来，今天想玩什么？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0DD616D8E2914FC2859CDB40FCB50F1A as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "是会让友叔大吃一惊的游戏哦！"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_3171B5940A5B4E6FAB23370F6FC4A7EC as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_9A978AAD07624C598B6179F23F51FB2D "不久前从认识爷爷那里得到的！\n最近我们一直在玩，大家一起来♪"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00003DB1

    return

label block_00001A6F:
    # Node: 00001A6F (Residential street)
    stop music2 fadeout 1
    $ sys_music2_current_file = ""

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

    $ set_place_title(_("住宅街"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_FB8046DBE16F4BA8BE96613E8F3A850C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001A73

    return

label block_00001A73:
    # Node: 00001A73 (Residential street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (552, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (696, 360),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_204
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003D8F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" },{ "scope": 1, "content": "C3S3 == True" }]):
        jump block_00001A80
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" },{ "scope": 1, "content": "C3S3BeforeResidentialStreetFirstEnter == True" }]):
        jump block_00002FD9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00002FDA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00001A86

    return

label block_00001A80:
    # Node: 00001A80 (Residential street turning)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("住宅街路口"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BAA43B4F4198492BA4DCD8836A92877B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001A81

    return

label block_00001A81:
    # Node: 00001A81 (Residential street turning)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (120, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "花乃湯"}, {"pos": (512, 320),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "神社"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_205
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"花乃湯\"" }]):
        jump block_00001A8C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"神社\"" },{ "scope": 1, "content": "C3S3 == True" }]):
        jump block_00001A8A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"神社\"" }]):
        jump block_00002FDB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001A6F

    return

label block_00001A8C:
    # Node: 00001A8C (Hanano)
    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("花乃汤"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_530777FF5DE0403C85E0F13A632298D3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C3S3 == True" }]):
        jump block_00001A8D
    if judge_lm_condition([]):
        jump block_00002FDD

    return

label block_00001A8D:
    # Node: 00001A8D (Hanano)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "ポスター"}, {"pos": (232, 272),"image": "images/Menu/Shougintoki.png","hover": "images/Menu/Shougintoki hover.png","name": "翔銀時"}, {"pos": (80, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_206
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001A80
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001A9E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"翔銀時\"" }]):
        jump block_00002FFC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ポスター\"" }]):
        jump block_00001F7B

    return

label block_00001A9E:
    # Node: 00001A9E (River)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("河边"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C3QShiro == True" }]):
        jump block_000027B5
    if judge_lm_condition([{ "scope": 0, "content": "C1S4 == True" }]):
        jump block_000027B4
    if judge_lm_condition([]):
        jump block_00001A9F

    return

label block_000027B5:
    # Node: 000027B5 (River 貝ー)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (336, 352),"image": "images/Menu/Be-- river.png","hover": "images/Menu/Be-- river hover.png","name": "ベー"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_207
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001A8C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ベー\"" }]):
        jump block_000027B7

    return

label block_000027B7:
    # Node: 000027B7 (貝ー)
    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_BC99B0ED590743F2B5BB46826572A7BB as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    window show

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "呼姆——。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『要玩“{/color}{color=#FF8000}向左向右看”{/color}{color=#0080FF}吗？』{/color}"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("河边"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"


    if judge_lm_condition([]):
        jump block_000027BD

    return

label block_000027BD:
    # Node: 000027BD (選擇)
    call scb_selector("", [{"name":"はい", "content":_("要玩要玩")}, {"name":"いいえ", "content":_("药丸药丸")}]) from _call_scb_selector_17

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_000027BC
    if judge_lm_condition([]):
        jump block_000027B5

    return

label block_000027BC:
    # Node: 000027BC (CLEAR)
    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ set_window("イベントモード")
    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_E36043F8C80E4415B6B2D5553D497F8B

    pause 0.8


    if judge_lm_condition([]):
        jump block_000027B6

    return

label block_000027B6:
    # Node: 000027B6 (向左向右看)
    call block_00002493 from _call_block_00002493_1

    if judge_lm_condition([]):
        jump block_00004255

    return

label block_00004255:
    # Node: 00004255 (RESET)
    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("河边"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001A9F

    return

label block_00001A9F:
    # Node: 00001A9F (River)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_208
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001A8C

    return

label block_000027B4:
    # Node: 000027B4 (River 四朗 quest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (320, 304),"image": "images/Chapter 3/Menu/Shiro river quest.png","hover": "images/Chapter 3/Menu/Shiro river hover.png","name": "ベー"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_209
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001A8C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ベー\"" }]):
        jump block_000027B8

    return

label block_000027B8:
    # Node: 000027B8 (四朗)
    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_CE2AA99006A14FB68F9A5BA7EB0C8B29 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_bottom zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？猫君Jr君在这里做什么呢？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_41A84CEAB4B9488D918E907B63CC8E1A as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "森海前辈好。其实直到刚才\n一直和翼前辈在一起，不过走散了……"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "原来你们会一起玩？\n关系这么好！我都不知道！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CD2255EE7C77442EA5D34AF3CB25F51A as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哈哈，毕竟发生了很多事。\n"
    show rs_image_AEEAC84D9A0D467A865EBA13D1DB3715 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过，那个人该说是好动过头了\n还是什么类似的。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "在学校是不是也是那种感觉呐。\n那样的话就是个十足的问题儿童……"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，翼君？{w}不不，那孩子\n总是战战兢兢地像刚出生的小狗。\n翼君应该是这种感觉才对。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_783A06C8ED3C44E89BF1C17E4D55DB5E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸——不对正相反！{w}\n翼前辈是那种喜欢打闹元气满满\n的小狗的感觉才对。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B8EF7BF57F6247F99CCB6B9498C36831 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DA3198F0CE840DFBC14AD2B78D1AA0D "？？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.8

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    $ set_window("イベントモード")
    pause 3.5

    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FA560BBE27804FA796D19D7894653F2D as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_7A311FCC247849CC97FD917F1150A24A as tag_BB92C9F2A35745708E1E70CBF033E3C3 at right_top zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    window show

    if sys_music_current_file != "sound/BGM/Ailurus fulgens.ogg":
        play music "sound/BGM/Ailurus fulgens.ogg" loop
        $ sys_music_current_file = "sound/BGM/Ailurus fulgens.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "你们在叫我——！？"

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆——！"

    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！翼君！？\n{w=0.4}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……和……什么东西！这个横向生长的！！？"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_76A6FDF06765424DBC1E2AE1C0D1ADA1 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "还以为去什么地方，原来是去找这孩子了。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 200
    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_059C21EE40DA45BB8CEE77053FCF922C as tag_BB92C9F2A35745708E1E70CBF033E3C3 at right_top zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "对哦——！去找{color=#FF8000}贝——{/color}来玩了哦♪"

    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 200
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CBD2AF53D136432CA26466E5BD1ED8E7 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_628CBB6D3CA24E23958195F453C57AF1 as tag_BB92C9F2A35745708E1E70CBF033E3C3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哇！你是！被作哉讨厌的叫友的家伙——！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F4302AF8D2CE4813B30E77067EFB476B as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "（观察中）——……{w=0.6}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_652D7701AFFE418E87F460AA0381F86F as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……呼！"

    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "啊！贝——也不喜欢——"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……就算是笨蛋如我也看不明白现状了……"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_7C2E9E7F5F0D47D1BF49B03E25F8C320 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哈哈哈，一开始我也是，已经习惯了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "呐——呐——！来玩那个游戏——♪\n"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "{color=#FF8000}“向左向右看♪”{/color}"

    show rs_image_1DC349F94DE94D6FACCF6AD451DDAE8E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸——我就算了。森海前辈，请。"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 200
    show rs_image_FD381C6412CC4FE7A52F90CB708C2E44 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_652D7701AFFE418E87F460AA0381F86F as tag_BB92C9F2A35745708E1E70CBF033E3C3 at right_top zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、我不要——那东西好像很讨厌我。"

    show rs_image_166E61569A9246C3AEB94A8278FC2C50 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_CBB316F2A1384D18B8532DF5B9E23C0A = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_166E61569A9246C3AEB94A8278FC2C50 as tag_CBB316F2A1384D18B8532DF5B9E23C0A at center_top zorder zorder_tag_CBB316F2A1384D18B8532DF5B9E23C0A onlayer master
    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_CBB316F2A1384D18B8532DF5B9E23C0A
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 300
    show rs_image_166E61569A9246C3AEB94A8278FC2C50 as tag_BB92C9F2A35745708E1E70CBF033E3C3 at right_top zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我、我明白了！我做还不行嘛！\n真是的，不讲道理的小熊猫……"

    window hide

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    with rs_effect_E36043F8C80E4415B6B2D5553D497F8B

    pause 0.8


    if judge_lm_condition([]):
        jump block_000027B6

    return

label block_00002FFC:
    # Node: 00002FFC (Random)
    $ HananoRandom = Random(3)

    if judge_lm_condition([{ "scope": 0, "content": "HananoRandom == 0" }]):
        jump block_00002FFA
    if judge_lm_condition([{ "scope": 0, "content": "HananoRandom == 1" },{ "scope": 1, "content": "C2S4 == False" }]):
        jump block_00002FF8
    if judge_lm_condition([{ "scope": 0, "content": "HananoRandom == 1" }]):
        jump block_00002FF9
    if judge_lm_condition([{ "scope": 0, "content": "HananoRandom == 2" }]):
        jump block_00002FFB

    return

label block_00002FFA:
    # Node: 00002FFA (翔銀時 1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_D7825E4D13D149599171D72320D84152 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "你好。你是御咲学园的学生呐。\n学校生活如何？\n我还在上学的时候也很不守规矩的。"

    show rs_image_27A65FC15594414F8E6CF36C64C026E2 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "当时学校里流传着{color=#3A00C4}禁忌之箱{/color}的传说。"

    show rs_image_D7825E4D13D149599171D72320D84152 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "于是和朋友在夜里偷偷四处寻找，\n结果反而被老师逮到，骂了个狗血淋头。"

    show rs_image_4E1328DF58984CDDB873E6CA9A162506 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "现在想来也是一段不错的回忆。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001A8D

    return

label block_00002FF8:
    # Node: 00002FF8 (翔銀時 2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_CA5DCF09EC6F43D3BF094A232BE224FB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "你好。你来过这家花乃汤吗？\n店长的儿子应该和你同年。"

    show rs_image_4E1328DF58984CDDB873E6CA9A162506 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "这家店也是很有年头了。\n以前社团活动结束时总是来这里放松。"

    show rs_image_1DB126B964544691AE7B64404BF2995F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "啊……不过，周三会有特别的客人来，那一天就算了。\n{w=0.4}{nw}"
    show rs_image_27A65FC15594414F8E6CF36C64C026E2 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……那孩子也是，这么下去真的很担心啊……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001A8D

    return

label block_00002FF9:
    # Node: 00002FF9 (翔銀時 C2F4后)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_CA5DCF09EC6F43D3BF094A232BE224FB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "你好。你来过这家花乃汤吗？\n店长的儿子应该和你同年。"

    show rs_image_4E1328DF58984CDDB873E6CA9A162506 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "最近经常见到慎太郎君的朋友来呢。\n……那孩子来的时候店里气氛真的非常愉快。"

    show rs_image_CA5DCF09EC6F43D3BF094A232BE224FB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "以后会成为每天必来的休息场所吧。\n你放学后也可以来看看。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001A8D

    return

label block_00002FFB:
    # Node: 00002FFB (翔銀時 3)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_4E1328DF58984CDDB873E6CA9A162506 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "你好。今天天气真不错。\n晴朗温暖，稍不注意就会睡过去。"

    show rs_image_1DB126B964544691AE7B64404BF2995F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "从学校来的路上，\nY字路口右转有一间神社。"

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "那里祭祀的是很灵验的梦境之神，\n似乎能让人{color=#808000}做想做的梦{/color}。"

    show rs_image_CA5DCF09EC6F43D3BF094A232BE224FB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "正好也很久没去了，\n你要不要也陪我去看看呢。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("花乃汤"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00001A8D

    return

label block_00001F7B:
    # Node: 00001F7B (Poster)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_048FEDA101B44195A010E4D967CEAF07 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    show rs_image_7448A3B2C6EF4B219EA7F33064B8CE76 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([{ "scope": 0, "content": "C3S3 == True" }]):
        jump block_00001A8D
    if judge_lm_condition([]):
        jump block_00002FDD

    return

label block_00002FDD:
    # Node: 00002FDD (Hanano empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "ポスター"}, {"pos": (80, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_210
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001A9E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ポスター\"" }]):
        jump block_00001F7B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00002FDA

    return

label block_00002FDA:
    # Node: 00002FDA (Residential street turning F3前)
    if sys_music2_current_file != "sound/BGM/Drum.ogg":
        play music2 "sound/BGM/Drum.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Drum.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("住宅街路口"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BAA43B4F4198492BA4DCD8836A92877B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001A81

    return

label block_00001A8A:
    # Node: 00001A8A (Jinja)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("神社"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E231059B50CB41C989713074B50A8CA5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001A8B

    return

label block_00001A8B:
    # Node: 00001A8B (Jinja)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_211
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001A80

    return

label block_00002FDB:
    # Node: 00002FDB (Jinja F3前)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("神社"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E231059B50CB41C989713074B50A8CA5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002FDC

    return

label block_00002FDC:
    # Node: 00002FDC (Jinja 翔銀時 flag)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (357, 271),"image": "images/Chapter 3/Menu/Shougintoki flag.png","hover": "images/Chapter 3/Menu/Shougintoki hover.png","name": "翔銀時"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_212
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"翔銀時\"" }]):
        jump block_00002FDE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00002FDA

    return

label block_00002FDE:
    # Node: 00002FDE (翔銀時)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！这个太鼓的声音，难道是那个祭典？"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4E1328DF58984CDDB873E6CA9A162506 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "就是明天。今天是排练。"

    show rs_image_CA5DCF09EC6F43D3BF094A232BE224FB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "记得你是慎太郎君的朋友，\n去年也参加过吧。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是的！很开心的祭典，\n收获了非常棒的回忆哦——！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4E1328DF58984CDDB873E6CA9A162506 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "那就好。最近的孩子们基本都不参加了，\n还能有像你这样的孩子真是太好了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没什么没什么～"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（能穿那种衣服的机会可是很少的……♪）"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我很期待明天哦！\n请告诉慎酱……\n不，慎太郎君他们要加油哦。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("神社"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    pause 1

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    stop music fadeout 2
    $ sys_music_current_file = ""

    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA


    if judge_lm_condition([]):
        jump block_00003D97

    return

label block_00003D97:
    # Node: 00003D97 (FLAG CP3F3)
    call block_00003D92 from _call_block_00003D92

    if judge_lm_condition([]):
        jump block_00004251

    return

label block_00004251:
    # Node: 00004251 ()
    $ del HananoRandom

    return

label block_00002FD9:
    # Node: 00002FD9 (Residential street turning F3前 Event)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("住宅街路口"))
    if sys_music2_current_file != "sound/BGM/Drum.ogg":
        play music2 "sound/BGM/Drum.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Drum.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BAA43B4F4198492BA4DCD8836A92877B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯？是太鼓的声音……{w}\n是什么地方有祭典吗？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过现在不是那个季节呀……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("广场"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002FF0

    return

label block_00002FF0:
    # Node: 00002FF0 (Cancel: First)
    $ C3S3BeforeResidentialStreetFirstEnter = False

    if judge_lm_condition([]):
        jump block_00001A81

    return

label block_00001A86:
    # Node: 00001A86 (Square)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ reverse_volume("music", 1)

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("广场"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EA055EB7B6EB43248D57A79268B22FB3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001A87

    return

label block_00001A87:
    # Node: 00001A87 (Square)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (624, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "泉の公園"}, {"pos": (120, 328),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "？？？"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_213
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉の公園\"" }]):
        jump block_00001A99
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001A6F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"？？？\"" }]):
        jump block_0000311C

    return

label block_00001A99:
    # Node: 00001A99 (Spring water park)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("泉水公园"))
    if sys_effect2_current_file != "sound/Effect Sound/Wave 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wave 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_FD502E28BA104DF786C3A82D5A7B82B8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002C1B

    return

label block_00002C1B:
    # Node: 00002C1B (Spring water park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_214
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([]):
        jump block_00001A86

    return

label block_0000311C:
    # Node: 0000311C (Forest)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("迷之地点"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_775562F285044F0882847ACB344F1A6E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C3QNewsclubPhase > 0" }]):
        jump block_0000312F
    if judge_lm_condition([]):
        jump block_00003120

    return

label block_0000312F:
    # Node: 0000312F (新聞部 QUEST)
    pause 0.4

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "吼吼！从那边听到声音了……"

    window hide

    pause 0.6

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ set_window("イベントモード")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 1.7

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C84270558B44454A2A6E8B66021E559 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.9

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 200
    show rs_image_4F5C0A33D5614FA5BA5F63955E1180D4 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_A8B433B09ECE4B709853D2F65E6D9BE6 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    pause 0.5

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    window show

    rs_character_57471360F48A413AB843A4E46D8C5541 "最近棘手的敌人越来越多了。"

    show rs_image_8B52E61324A44797A9932F829455E996 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "嗯，看来我们的弱点已经暴露了……"

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EEF9B0C2698746079132D4430E2BD88F "{size=28}全都是强化过{/size}{size=28}{color=#FF00FF}快感攻击{/color}{/size}{size=28}的敌人……！{/size}"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    show rs_image_BCFB20456B6D43D6BC37C1D09AC7CB23 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_BDA0ABE94FC84F31824EC1BA83CD0C63 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_284AA099EFB44CE985BBC6A39E64434A

    pause 0.3

    rs_character_57471360F48A413AB843A4E46D8C5541 "那个，都快要肾虚了。"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "我也差不多，快干了。"

    show rs_image_6F0A3C8995204898B822C201B9B7138E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "实话说，战斗前还是会期待……想象一下的。\n那种凹凸不平的类型会不会舒服之类的。"

    show rs_image_04C70534E307410697BF4A8D2E04DCC6 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不行……不好……现在还能保持理性，\n继续下去就无法处理了。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_DFE7656E88C947F3914B1BDB28FDCEBD as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "不过我们对战斗（意味深长）的耐受度也上升了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_DEB5EEF4CD324735BF30394DA3D424A8 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "确实！那种水平低的敌人完全没问题。\n这也是我们变强了的证据呐！"

    show rs_image_E8F84349B64C4AE4A712B8B3F1D3A38E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "正是如此！我们才不会因此满足，\n当然，轻敌是大忌。"

    show rs_image_829D40A27305424197B2D502DDEB3406 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不过也是想遇到能让轻敌时的我们大吃一惊的呐！\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_3CE7632E90714ECD96EE9ACC8BD5CEDC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "好！就这么不断变强！"

    show rs_image_2A2BEF79FCD844B490D59AD7A154C949 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "……{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1626534B504446319B30BAF22C4EC025 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "不过，这样下去，会越来越不知满足的。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_CE3228D786DA4C31B3CCBF5B68FF886C as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "说、说得对……{w=0.5}{nw}"
    show rs_image_04C70534E307410697BF4A8D2E04DCC6 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "荆棘之路啊……"

    window hide

    pause 0.7

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    show rs_image_775562F285044F0882847ACB344F1A6E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好奇怪的家伙——！真是小孩子，还在玩英雄游戏。\n{w=0.55}{nw}"
    show rs_image_27FF4633286B4DF59BF4C1A761DDF98E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "呼呼呼——☆"

    window hide

    pause 0.7

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    $ set_window("(標準)")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 1.7

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_928702F45F5E4011BDA3855AB8593F59 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    window show

    if sys_music_current_file != "sound/BGM/Chapter 3.ogg":
        play music "sound/BGM/Chapter 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 3.ogg"

    $ renpy.music.set_volume(0.5, 1, "music")

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我来汇报调查结果了～"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4BF60E1CD8994FA8B74D36E307E8C354 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "哦哦，久等多时了！\n快，说出你看到的一切。"

    window hide

    pause 0.5

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 1

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 0.55

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_6BEAA3D38A204EAE8EFEE059FD541711 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    window show

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "唔……还以为会是更热门的话题，真遗憾。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_1654C244584349A6B0811665076020BD as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "嘛，{color=#FF00FF}原作{/color}差不多也是这个样子。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_07383DF7F5A94166BAD98FE0E71F4768 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "原作？"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_A3D0E6087D6B4C4DA8B5F544E1F3B782 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "……{w=0.4}{nw}"
    show rs_image_1654C244584349A6B0811665076020BD as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "部长不需要知道。\n"
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "森海君，这次也麻烦你了。\n请收下报酬。"

    window hide

    pause 0.2

    if sys_effect2_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Decision 1.ogg"

    # Gallery unlock: images/CG/Newsclub/Newsclub 3.png
    $ zorder_rs_image_692431208FC84C2BBC4BFB384C5535E2 = -100
    show rs_image_692431208FC84C2BBC4BFB384C5535E2 as rs_image_692431208FC84C2BBC4BFB384C5535E2 zorder zorder_rs_image_692431208FC84C2BBC4BFB384C5535E2 onlayer master
    hide rs_image_692431208FC84C2BBC4BFB384C5535E2

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_CC4336DE74164173AC47C2C317367F10
    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_692431208FC84C2BBC4BFB384C5535E2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.4

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『收到了“大家来打排球——！”时的照片』{/color}"

    window hide

    pause 0.3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_window("(標準)")
    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_BB675405870B497F958414550471B4BF as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "先不管结果，做的非常棒，森海君！\n这样你也是新闻部的一员了！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（一、一员！？怎、怎么会这样……\n感觉以后又会被派出去取材的样子……）"

    window hide

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_40BD583A95C74300ACB4618268AB48FF

    pause 0.8

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_93C0B7E63B614E9386D2D63EAAD23E8F as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.45

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那个……对不起……\n我找友君有点事。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君！什么什么，有什么事？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9B9B54741504444CB4B791D4CC402B1D as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、那个、这个……\n就是想问今天小钢琴部有没有活动。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "小钢琴部！\n对、就是这个！我是小钢琴部的部长！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君，去音乐室就好！我马上就去！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E5980AB1AA3E484A93A2EBD2139A77FE as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我、我明白了。我会等着的。"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_FAE04D9AEB58490C92EEB463378364AF

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对不起哦～新闻部的两位，\n我差不多该去做本职工作了！"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6BEAA3D38A204EAE8EFEE059FD541711 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "这样，原来你已经有社团了。\n那还真是对不起。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没、没什么，本来你们两人的新闻部\n我横插一脚也不好。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过，以后再有什么有趣的新闻\n我会来报告的，会替你们加油的！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我觉得你们能把我那不明所以的汇报\n写成有趣的新闻的才能很厉害哦。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "因为你们的新闻，我觉得我对学校和城镇\n更有兴趣更喜欢了哦！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_07383DF7F5A94166BAD98FE0E71F4768 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "森海君……\n"
    show rs_image_5C9006A0C6DD479B8EFFFE3A14CE4056 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "谢谢。这已经足以使我们全力以赴，\n以后我们会继续努力的。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4BF60E1CD8994FA8B74D36E307E8C354 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "我们会记住你的话，继续撰写有趣的文章。\n新闻部之后也请你多关照了。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_9511CC62DD3C41CB9B75011464423CB6 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "我会和部长一起努力。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对了，你们为什么要成立新闻部呢？"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DF83E8681DAD43B1BF6C0CF0E3555C11 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "关于这个。{w}\n……{w=0.4}{nw}"
    show rs_image_5C9006A0C6DD479B8EFFFE3A14CE4056 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "是我最尊敬的人的影响……吧。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 200
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "其实和森海君开始弹钢琴的理由差不多。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶！你们知道我弹钢琴的理由！？"

    show rs_image_9511CC62DD3C41CB9B75011464423CB6 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "哈哈，毕竟也是新闻之一♪"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("新闻部活动室"))

    if judge_lm_condition([]):
        jump block_00003131

    return

label block_00003131:
    # Node: 00003131 (QUEST FINISH)
    if sys_music2_current_file != "sound/BGM/Quest Finished.ogg":
        play music2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.8

    $ reverse_volume("music")

    if judge_lm_condition([]):
        jump block_00003130

    return

label block_00003130:
    # Node: 00003130 (C3Q新聞部)
    $ C3QNewsclub = True
    $ C3QNewsclubRedirect = True
    $ C3QNewsclubPhase = 0

    if judge_lm_condition([]):
        jump block_00003D99

    return

label block_00003D99:
    # Node: 00003D99 ()
    $ del HananoRandom

    return

label block_00003120:
    # Node: 00003120 (Forest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_215
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([]):
        jump block_00001A86

    return

label block_00001A77:
    # Node: 00001A77 (Shopping street)
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

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_97F953D82737458C83905085327ADE8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001A79

    return

label block_00001A79:
    # Node: 00001A79 (Shopping street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (104, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_216
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003D8F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" },{ "scope": 1, "content": "C3SSabuShin == False" },{ "scope": 2, "content": "C2S4 == True" },{ "scope": 3, "content": "C3SG1 == True" }]):
        jump block_000030FE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001A82

    return

label block_000030FE:
    # Node: 000030FE (三慎 event)
    $ set_window("イベントモード")
    stop music fadeout 1.5
    $ sys_music_current_file = ""

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_91F4C74E7B844945A9976F914A36207F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_DEC2F822DD03433CB37D42439376833B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    window show

    show rs_image_282C9F7BE25049678AA10F7136B6FC9E as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呐——奥村，今天总觉得你有些低落，\n咋了？"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸！完全没有这回事哦！好不容易和三酱去电影院约会～"

    show rs_image_78AAFDF80423489CB9D3E414C6D0A594 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗯，可是……\n{w=0.5}{nw}"
    show rs_image_B7338300611E44679D3661334AC876A9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "哦，是不是电影不好看？"

    show rs_image_78AAFDF80423489CB9D3E414C6D0A594 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "都是差不多的{color=#FF00FF}恋爱故事{/color}，\n应该没什么不对劲才是。"

    show rs_image_D7BB1A8267AE4353950D17F94CE6C389 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯！没有“不对劲”！很不错的！很激动人心的♪"

    show rs_image_F1BC27BCAA724436A6E40C4DD41F6CDD as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……哦。"

    show rs_image_E17E2BD5659143D79B19D748BC854C0D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈哈。"

    show rs_image_23970544C9224BB4B785B8FB367471BC as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……"

    show rs_image_F1BC27BCAA724436A6E40C4DD41F6CDD as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "真心话？"

    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔……说实话，有些微妙。\n对不起，三酱，总觉得有些不方便说。"

    show rs_image_50D82C35F258450C9BFE07520E310720 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那种事无所谓，每个人的想法都不同。\n不然干嘛只有我们两个去看。"

    show rs_image_0600CCA9D8E5458687C3A5F9EE6CB6C5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "比起那个，我更关心你心情不好的问题。我才没那么不通人情。"

    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不愧是三酱♪\n"
    show rs_image_AD906DE4351649D4A088A775E16D4592 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那……{w=0.5}{nw}"
    show rs_image_A2E7C1AAED834AD7861668C6EE330F80 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "我就实话实说了。"

    pause 0.35

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_7F497F24D349433FB39C83C619E61AB8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.3

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "其实，我不太喜欢那种男女恋爱电影，看后总会觉得有些失落。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我们现在这么幸福，学校生活也很好……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "但说不定在别人看来过于特立独行，我们只是井底之蛙。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "再怎么说世间标准还是男女恋爱，\n自己是怎么也无法融入其中的～"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_DEC2F822DD03433CB37D42439376833B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_A2E7C1AAED834AD7861668C6EE330F80 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.3

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……类似的无聊想法。\n刚才也说过，但我现在已经非常幸福了。"

    show rs_image_14A685B89E294E398F790648705A6A46 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔……原来如此……\n"
    show rs_image_50D82C35F258450C9BFE07520E310720 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "奥村，别在意……也不能这么说……那个……"

    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "可以了，三酱。我只是有些想的太复杂罢了！"

    show rs_image_075F12352E04495CB718DBEB1B7D807C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不是……那个……唔……\n"
    show rs_image_53FEBB64B5034493AD43F17831AA22EB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……{w=0.5}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_609B18A24DC64637943B3F2C0430365E as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯！对了！"

    show rs_image_17BD4756EE4547C7999FB0FE558D991B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我也是！我讨厌水所以不喜欢游泳！"

    show rs_image_022781101FD04002AB8C506EED9156F2 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "诶？"

    show rs_image_B7338300611E44679D3661334AC876A9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不过，大多数人都喜欢游泳对不对？\n差不多就这个意思！"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……？"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_53FEBB64B5034493AD43F17831AA22EB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "大家是大家，不是说要跟他们一样感到高兴或幸福，\n反正也做不到！"

    show rs_image_609B18A24DC64637943B3F2C0430365E as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "所以奥村就那样一点儿问题都没有！"

    show rs_image_282C9F7BE25049678AA10F7136B6FC9E as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "所以……别介意……{w}……{w=0.45}{nw}"
    show rs_image_17BD4756EE4547C7999FB0FE558D991B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "抱歉……\n说的乱七八糟，大概没什么用。"

    show rs_image_7B9421782EFE49138E5AADFCD59A037D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……哈哈♪嗯，我很高兴。三酱的话语，真的有鼓励到我。"

    show rs_image_39829274F0594DCC89A2EF09B108ED2E as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "真的？没事了？"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_0082B8EA494C49D7B202B0DC39D7AC3F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "没事没事！我以后不会在三酱面前说这种奇怪的东西了！"

    show rs_image_05869A4FEB35497BB941E279D075CC45 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那就行。{w=0.45}{nw}"
    if sys_music2_current_file != "sound/Effect Sound/Strike 1.ogg":
        play music2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_0600CCA9D8E5458687C3A5F9EE6CB6C5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……不过，奥村，不许用关西腔。\n根本不合适，听着很难受。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_4BBDCD83023642F6923D76BE102A1BB9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这又咋了！\n干嘛说那么伤人的话呀——！？"

    show rs_image_2B24914707CC4FF38461FD9B7BB09975 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哇哈哈！行了停下！太好笑了～"

    window hide

    pause 0.75

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_E6A0D20A1A914A0CBCF8DCED075CD75A

    pause 1.5

    $ set_window("(標準)")
    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_97F953D82737458C83905085327ADE8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003128

    return

label block_00003128:
    # Node: 00003128 (C3S三慎)
    $ C3SSabuShin = True

    if judge_lm_condition([]):
        jump block_00001A79

    return

label block_00001A82:
    # Node: 00001A82 (Shopping street inside)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("商店街内"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_91F4C74E7B844945A9976F914A36207F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001A83

    return

label block_00001A83:
    # Node: 00001A83 (Shopping street inside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (128, 304),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "本屋"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_217
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001A77
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"本屋\"" }]):
        jump block_00001A97

    return

label block_00001A97:
    # Node: 00001A97 (Bookstore)
    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("书店"))
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4647E66D4861417FB077A035A142C3DA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003DB6

    return

label block_00003DB6:
    # Node: 00003DB6 (選擇)
    call scb_selector(_("接下来怎么做？"), [{"name":"時間を潰す", "content":_("在这里打发时间")}, {"name":"やめておく", "content":_("去别处看看")}]) from _call_scb_selector_18

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"時間を潰す\"" }]):
        jump block_00003DB7
    if judge_lm_condition([]):
        jump block_00001A82

    return

label block_00003DB7:
    # Node: 00003DB7 (Night)
    stop music fadeout 1
    $ sys_music_current_file = ""

    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_0D1A14CC6DD549EA877967C087A4F0E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    if sys_music_current_file != "sound/BGM/Night.ogg":
        play music "sound/BGM/Night.ogg" loop
        $ sys_music_current_file = "sound/BGM/Night.ogg"

    $ set_place_title(_("商店街"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A06541B8404D4065AD2E26F7B0FBD5B4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F


    if judge_lm_condition([]):
        jump block_00003DB8

    return

label block_00003DB8:
    # Node: 00003DB8 (Shopping street empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_218
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([]):
        jump block_00003DB9

    return

label block_00003DB9:
    # Node: 00003DB9 (CP3 Night Misaki)
    call block_00001B1D from _call_block_00001B1D

    if judge_lm_condition([]):
        jump block_00003DBA

    return

label block_00003DBA:
    # Node: 00003DBA (終了)
    $ del HananoRandom

    return

label block_00002575:
    # Node: 00002575 (四朗雪緒 event)
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
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.5

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=430, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_3DE6DC5E51F14E4F86F96E18DE4838E6 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！你们在这里做什么呢？"

    show rs_image_25B4CA5E7DB54A70B991383AB9E2522F as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "和学校的大家打了一会篮球，现在正准备回家。"

    show rs_image_2D9DBFACED644B2882B38D7E4606CBF6 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "呜……明天绝对会腰酸背痛。"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦——你们已经不玩公园里的东西了？"

    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我还是小学生的时候经常爬到那些棒子上面去玩呐——"

    show rs_image_7C2E9E7F5F0D47D1BF49B03E25F8C320 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我已经算是小学高年级了，才没有那么幼稚。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_0077897C874A47EDBC6EC1288FD65064 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈哈，太天真了少年。所谓的玩具，\n根据使用方法不同可是能体验到大人的乐趣的。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D8FBA8060A9B457F9D8A35FB71E72F10 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好，今天就让大哥哥我来教你们！{w=0.3}{nw}"
    show rs_image_1DC349F94DE94D6FACCF6AD451DDAE8E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_C040277FC7FE48E19FB154ABD798FD6D as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F03237FB10EB44FDB0C2E3F6C4B4F5D2 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "拜托了——"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_76A6FDF06765424DBC1E2AE1C0D1ADA1 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我就免了……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C040277FC7FE48E19FB154ABD798FD6D as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_6636F3FA642745AE8103D258F3BF47F2 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好的！那么先从雪绪君开始实践！{w}\n比如，那边的{color=#00FFFF}滑梯{/color}。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_7726A1CB72AE4E94BF0300DE62D83E8F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "小孩子肯定就那么滑下去，但是{w}\n成为大人的雪绪君可以{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "把{color=#FF00FF}那里{/color}朝下……"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Warning 1.ogg":
        play music2 "sound/Effect Sound/Warning 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Warning 1.ogg"

    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_DEF4707300154D00B22225E4F8282BA7

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫！？{color=#FF0000}防狼警笛！？{/color}谁打开的！？快住手我会被抓进去的——！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_49886B5191F044E1BF6A40972149F4D8 = 200
    $ zorder_tag_338A54F5CAAF4B198570C829F4262A61 = 200
    show rs_image_C040277FC7FE48E19FB154ABD798FD6D as tag_49886B5191F044E1BF6A40972149F4D8 at right_top zorder zorder_tag_49886B5191F044E1BF6A40972149F4D8 onlayer master
    show rs_image_1DC349F94DE94D6FACCF6AD451DDAE8E as tag_338A54F5CAAF4B198570C829F4262A61 at left_top zorder zorder_tag_338A54F5CAAF4B198570C829F4262A61 onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "雪绪，走了。"

    show rs_image_8AD2DDD7544B43C4A6A69B2DAC1465E5 as tag_49886B5191F044E1BF6A40972149F4D8 zorder zorder_tag_49886B5191F044E1BF6A40972149F4D8 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "欸——明明接下来才更有趣的说——"

    window hide

    pause 0.8

    stop music2 fadeout 1.5
    $ sys_music2_current_file = ""

    hide tag_49886B5191F044E1BF6A40972149F4D8
    hide tag_338A54F5CAAF4B198570C829F4262A61
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 0.7

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002FEF

    return

label block_00002FEF:
    # Node: 00002FEF (C3S四朗雪緒)
    $ C3SShiroYuki = True

    if judge_lm_condition([]):
        jump block_00003D90

    return

label block_00003D90:
    # Node: 00003D90 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00003D8F

    return

label block_00001AA2:
    # Node: 00001AA2 (御咲站)
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

    $ set_place_title(_("御咲站"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7B49313C1C0A4D8E8C250CC79F444E2D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001AA6

    return

label block_00001AA6:
    # Node: 00001AA6 (御咲站)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (336, 352),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (200, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "路線図"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_219
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003D8F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003DBB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"路線図\"" }]):
        jump block_00001F67

    return

label block_00003DBB:
    # Node: 00003DBB (Station)
    $ zorder_tag_D71B998959E446A69B3BAF1EFCCB35F6 = 400

    if judge_lm_condition([]):
        jump block_00003DBC

    return

label block_00003DBC:
    # Node: 00003DBC (選擇)
    call scb_bus_selector(show_misaki=False, show_takarasaki=True, show_umesaki=True) from _call_scb_bus_selector_6

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"宝咲\"" }]):
        jump block_00001A84
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"梅咲\"" }]):
        jump block_00001A8E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"乗らない\"" }]):
        jump block_00003DBD

    return

label block_00001A84:
    # Node: 00001A84 (宝咲)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Train 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Train 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Train 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.4


    if judge_lm_condition([]):
        jump block_00001A8F

    return

label block_00001A8F:
    # Node: 00001A8F (宝咲)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("宝咲"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C778499DFA0644D284B0DEC93882F736 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C3SG1 == True" }]):
        jump block_000027A6
    if judge_lm_condition([]):
        jump block_000034BE

    return

label block_000027A6:
    # Node: 000027A6 (宝咲 夕阳 守)
    $ sys_lm_menu_item = [{"pos": (616, 240),"image": "images/Menu/Mamoru.png","hover": "images/Menu/Mamoru hover.png","name": "マモル"}, {"pos": (464, 240),"image": "images/Menu/Yuuhi.png","hover": "images/Menu/Yuuhi hover.png","name": "ユウヒ"}, {"pos": (312, 264),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_220
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001A91
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ユウヒ\"" }]):
        jump block_000027A9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"マモル\"" }]):
        jump block_000027A7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003DBE

    return

label block_00001A91:
    # Node: 00001A91 (宝咲 inside)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ reverse_volume("music", 1)

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("宝咲上学路"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2ECE68226C004D8AB64C8E0BB09BCDE9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001A92

    return

label block_00001A92:
    # Node: 00001A92 (宝咲 inside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (384, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_221
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001A8F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003DC4

    return

label block_00003DC4:
    # Node: 00003DC4 (Home)

    if judge_lm_condition([]):
        jump block_00003DC5

    return

label block_00003DC5:
    # Node: 00003DC5 (選擇)
    call scb_selector(_("回家？"), [{"name":"はい", "content":_("没问题")}, {"name":"いいえ", "content":_("还有其他事情没做完")}]) from _call_scb_selector_19

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00001B61
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00001A92

    return

label block_00001B61:
    # Node: 00001B61 (Home)
    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    $ set_place_title(_("友的房间"))
    pause 0.6

    if sys_music2_current_file != "sound/BGM/Tomo's room.ogg":
        play music2 "sound/BGM/Tomo's room.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Tomo's room.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DB5AB8A1EA534F3F81A68748DB089DF3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C3SG1 and C2SG2 and C1SG2 == True" },{ "scope": 1, "content": "C3S5 == False" }]):
        jump block_00001B5E
    if judge_lm_condition([]):
        jump block_00001B62

    return

label block_00001B5E:
    # Node: 00001B5E (C3S5 Flag)
    pause 0.4

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Type 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Type 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Type 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 1.35

    window show

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦♪这个网站的四格终于更新了——！\n赶快看赶快看～！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……不过，今天作业很多呐。\n"
    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "嘛，就半个小时无所谓的。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.3

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DB5AB8A1EA534F3F81A68748DB089DF3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈哈♪这个动画超赞的～！！\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "……哦，不知不觉都一个小时了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……没事没事，再半个小时！\n半小时后我就写作业～……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.3

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Vibration 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Vibration 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Vibration 2.ogg"

    pause 4

    stop effect2 fadeout 0.8
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_59308A2352314B1E8ABB34860FDB9423 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "完了！已经这个点了！！\n再不赶快做……\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "唔……？呃！？？"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "卷子没拿！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……真的假的。{w}\n肯定是落在学校了……\n唔～真糟，好麻烦～……。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.8

    stop music fadeout 1
    $ sys_music_current_file = ""

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.5


    if judge_lm_condition([]):
        jump block_0000300F

    return

label block_0000300F:
    # Node: 0000300F (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#8000FF}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003010

    return

label block_00003010:
    # Node: 00003010 (Phase ++)
    $ C3S5Phase = C3S5Phase + 1

    if judge_lm_condition([]):
        jump block_00001B66

    return

label block_00001B66:
    # Node: 00001B66 (CP3 Night Misaki)
    call block_00001B1D from _call_block_00001B1D_1

    if judge_lm_condition([]):
        jump block_00003DD6

    return

label block_00003DD6:
    # Node: 00003DD6 ()
    $ del HananoRandom

    return

label block_00001B62:
    # Node: 00001B62 (Home)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Out.png","hover": "images/MOVING/ACTIONS/Out hover.png","name": "移動"}, {"pos": (408, 192),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "写真"}, {"pos": (176, 312),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "休む"}, {"pos": (528, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "勉強する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_222
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001B65
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"休む\"" }]):
        jump block_00003DCA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"写真\"" }]):
        jump block_00001F72
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"勉強する\"" }]):
        jump block_00003DC8

    return

label block_00001B65:
    # Node: 00001B65 (Out)
    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51


    if judge_lm_condition([]):
        jump block_00001A91

    return

label block_00003DCA:
    # Node: 00003DCA (Rest)

    if judge_lm_condition([]):
        jump block_00003DCB

    return

label block_00003DCB:
    # Node: 00003DCB (選擇)
    call scb_selector(_("今天没有其他安排了？"), [{"name":"はい", "content":_("休息")}, {"name":"いいえ", "content":_("时间还早")}]) from _call_scb_selector_20

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003DD1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00001B62

    return

label block_00003DD1:
    # Node: 00003DD1 (Next day)
    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect2_current_file != "sound/BGM/Finally.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/BGM/Finally.ogg" noloop
        $ sys_effect2_current_file = "sound/BGM/Finally.ogg"

    $ set_place_title(False)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_070289614C9E4592B7E9A0F0E985B92A

    pause 3.5

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003DD2

    return

label block_00003DD2:
    # Node: 00003DD2 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_8

    if judge_lm_condition([]):
        jump block_00003DD4

    return

label block_00003DD4:
    # Node: 00003DD4 (終了)
    $ del HananoRandom

    $ reverse_volume("music", 1)

    return

label block_00001F72:
    # Node: 00001F72 (Photo)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_9C7CF5F1B0FA4AD9B3C445C4FFD0CE32 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00001B62

    return

label block_00003DC8:
    # Node: 00003DC8 (StudyCount)

    if judge_lm_condition([]):
        jump block_00003DC9

    return

label block_00003DC9:
    # Node: 00003DC9 (選擇)
    call scb_selector(_("试着学习一下？"), [{"name":"はい", "content":_("学习")}, {"name":"いいえ", "content":_("学个毛习")}]) from _call_scb_selector_21

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003DCC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00001B62

    return

label block_00003DCC:
    # Node: 00003DCC (StudyCount)
    if FinalStudyCount <> 3:
        $ FinalStudyCount = FinalStudyCount + 1

    if judge_lm_condition([]):
        jump block_00003DCD

    return

label block_00003DCD:
    # Node: 00003DCD (Night)
    if sys_effect3_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B4756ADDE8D94414B9AE6B60019B56CD

    pause 1

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_59308A2352314B1E8ABB34860FDB9423 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B4756ADDE8D94414B9AE6B60019B56CD


    if judge_lm_condition([]):
        jump block_00003DCE

    return

label block_00003DCE:
    # Node: 00003DCE (Redirect)
    $ C3StudyRedirect = True

    if judge_lm_condition([]):
        jump block_00003DCF

    return

label block_00003DCF:
    # Node: 00003DCF (CP3 Night Misaki)
    call block_00001B1D from _call_block_00001B1D_2

    if judge_lm_condition([]):
        jump block_00003DD0

    return

label block_00003DD0:
    # Node: 00003DD0 (終了)
    $ del HananoRandom

    return

label block_000027A9:
    # Node: 000027A9 (夕阳)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_3DD7D9D931A84116A4B51038A067F814 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000027A8

    return

label block_000027A8:
    # Node: 000027A8 (夕阳+守)
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_6E5666B6FFA14A90B735045E7DE61D9A as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哈～每天都是任务任务……\n真想休假几天。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_9060496A498A44A9A87B73DE0A9196C6 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "只有我们两个太辛苦了。\n说是这么说，也没法从其他地区叫支援。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_0310ED729B07455DA8B46628FE3224B3 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_57471360F48A413AB843A4E46D8C5541 "哦，对了！\n下次周边地区的英雄们\n会开个交流会来着。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_3560561C561C431BB42E1F37DFC75491 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那就好好听听找到方法，\n毕竟也是收集情报！"
    show rs_image_00E77EB1C46049238914EC204FF1AD3F as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "应该是很有意义的活动，\n肯定会听到有趣的事情的！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（那两个人的对话还是一如既往听不明白！）"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("宝咲"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000027A6

    return

label block_000027A7:
    # Node: 000027A7 (守)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_AD6987B2589A420C8E39B0044CFF9E0B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000027A8

    return

label block_00003DBE:
    # Node: 00003DBE (Station)
    $ zorder_tag_D71B998959E446A69B3BAF1EFCCB35F6 = 400

    if judge_lm_condition([]):
        jump block_00003DBF

    return

label block_00003DBF:
    # Node: 00003DBF (選擇)
    call scb_bus_selector(show_misaki=True, show_takarasaki=False, show_umesaki=True) from _call_scb_bus_selector_7

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"乗らない\"" }]):
        jump block_00003DC0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲\"" }]):
        jump block_00001A85
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"梅咲\"" }]):
        jump block_00001A8E

    return

label block_00003DC0:
    # Node: 00003DC0 (Return)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([{ "scope": 0, "content": "C3SG1 == True" }]):
        jump block_000027A6
    if judge_lm_condition([]):
        jump block_000034BE

    return

label block_000034BE:
    # Node: 000034BE (宝咲 夕阳)
    $ sys_lm_menu_item = [{"pos": (495, 232),"image": "images/Menu/Yuuhi.png","hover": "images/Menu/Yuuhi hover.png","name": "ユウヒ"}, {"pos": (312, 264),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_223
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ユウヒ\"" }]):
        jump block_000034BD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001A91
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003DBE

    return

label block_000034BD:
    # Node: 000034BD (夕阳)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_92B28690BF524F6E84FED8251700E47B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "多亏和那家伙组队，\n空余时间慢慢有了一些。"

    show rs_image_3DD7D9D931A84116A4B51038A067F814 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "今天夜里的巡视是我来，\n在那之前可以好好休息了。"

    show rs_image_6E5666B6FFA14A90B735045E7DE61D9A as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "啊——不过，今天有社团活动……\n果然还是得去露个脸。\n结果，还是忙个不停。"

    show rs_image_7CED1BC765EE4A5B93B9DC7719B0D0AB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "我和大家不同可是有各种原因的，\n至少优待我一下啊——"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（好长的独白！）"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("宝咲"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000034BE

    return

label block_00001A85:
    # Node: 00001A85 (御咲)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Train 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Train 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Train 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.4


    if judge_lm_condition([]):
        jump block_00001AA2

    return

label block_00001A8E:
    # Node: 00001A8E (梅咲)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Train 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Train 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Train 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.4


    if judge_lm_condition([]):
        jump block_00001AA1

    return

label block_00001AA1:
    # Node: 00001AA1 (梅咲)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("梅咲"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6E6622EB7E1F41F7B7D7A2E05B103428 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001AA5

    return

label block_00001AA5:
    # Node: 00001AA5 (梅咲)
    $ sys_lm_menu_item = [{"pos": (144, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}, {"pos": (536, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "バス停"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_224
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003DC1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001AAA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"バス停\"" }]):
        jump block_00001AAC

    return

label block_00003DC1:
    # Node: 00003DC1 (Station)
    $ zorder_tag_D71B998959E446A69B3BAF1EFCCB35F6 = 400

    if judge_lm_condition([]):
        jump block_00003DC2

    return

label block_00003DC2:
    # Node: 00003DC2 (選擇)
    call scb_bus_selector(show_misaki=True, show_takarasaki=True, show_umesaki=False) from _call_scb_bus_selector_8

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"乗らない\"" }]):
        jump block_00003DC3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲\"" }]):
        jump block_00001A85
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"宝咲\"" }]):
        jump block_00001A84

    return

label block_00003DC3:
    # Node: 00003DC3 (Return)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00001AA5

    return

label block_00001AAA:
    # Node: 00001AAA (梅咲 inside)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("梅咲直通路"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F626D796C06498799817646B2CE72A3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001AAD

    return

label block_00001AAD:
    # Node: 00001AAD (梅咲 inside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (120, 336),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_225
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00001AA9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001AA1

    return

label block_00001AA9:
    # Node: 00001AA9 (Alley)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("小巷"))
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B077A5B521D34F718C471A608BE99607 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkRikuta == 1" }]):
        jump block_000027C4
    if judge_lm_condition([]):
        jump block_00001AAB

    return

label block_000027C4:
    # Node: 000027C4 (杉本 event)
    pause 0.5

    pause 0.7

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（哦？{color=#0080FF}杉本先生{/color}居然在那里。{w}\n还有一个大叔……）"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（……难道……{w}\n不不不，怎么可能。\n肯定是经理或者什么人。）"

    window hide

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    window show

    rs_character_7774C43AB3D24D60ACC24B764E0E67B4 "杉本君，这次做得很好。\n那么，我们继续之前的话题。"

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_A5C7E9EBD8B1421D895E2CB250E2023A as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_7C178421D3DA4E2CB70D4336919888FB "……哈哈哈，我才是该说多谢。{w}\n真的非常感谢，以后也请多多关照。"

    window hide

    pause 0.35

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_FFC620A1302E417EBD9CB71C6CDE9274

    pause 1.3

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（明明比我小还这么厉害，\n不过艺能界也确实很辛苦。）"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（肯定就算是在那个年龄也不得不站在最前线吧。）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("小巷"))

    if judge_lm_condition([]):
        jump block_00003007

    return

label block_00003007:
    # Node: 00003007 (T ++)
    $ TalkRikuta = TalkRikuta + 1

    if judge_lm_condition([]):
        jump block_00001AAB

    return

label block_00001AAB:
    # Node: 00001AAB (Alley)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_226
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001AAA

    return

label block_00001AAC:
    # Node: 00001AAC (梅咲 square)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("梅咲广场"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_75A864E3BFC9426C817C95EDE531DCA5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkRikuta == 2" },{ "scope": 1, "content": "VarExists(\"C3AllowSukimotoTalk\") == True" }]):
        jump block_000027C5
    if judge_lm_condition([{ "scope": 0, "content": "TalkRikuta < 2" },{ "scope": 1, "content": "VarExists(\"C3AllowTriggleSukimotoTalk\") == True" }]):
        jump block_000027C3
    if judge_lm_condition([]):
        jump block_00001AAE

    return

label block_000027C5:
    # Node: 000027C5 (梅咲 square 陸田 杉本)
    $ sys_lm_menu_item = [{"pos": (200, 208),"image": "images/Menu/Rikuta umesaki.png","hover": "images/Menu/Rikuta umesaki hover.png","name": "陸田"}, {"pos": (368, 208),"image": "images/Menu/Sumoto umesaki.png","hover": "images/Menu/Sumoto umesaki hover.png","name": "杉本"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_227
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"杉本\"" }]):
        jump block_000027C6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"陸田\"" }]):
        jump block_000027C8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001AA1

    return

label block_000027C6:
    # Node: 000027C6 (杉本)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_7753ED91AD104B6C8767AA10B5191840 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000027C7

    return

label block_000027C7:
    # Node: 000027C7 (杉本陸田 event)
    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天好耶——♪你们二位！{w}\n哦？带着{color=#0080FF}行李箱{/color}呐，\n接下来要出门吗？"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2FB61747AED54E08ACC1F998C30D040F as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "说得对——听我说哦～友同学♪"

    if sys_effect2_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5A33491B84034DD2AB1830E78EB16F23 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "竟然！我们“陆田&杉本”有新节目……\n而且是在全国播放的常规节目！"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_71CB04B02B4B48DFAA5213665555BCB0 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7C178421D3DA4E2CB70D4336919888FB "憧憬许久的全国范围！至今为止\n不断磨练出的技巧终于能让大家都看到了"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "接下来会变得很忙的哦～♪"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦哦～（鼓掌鼓掌）！好厉害！也就是说\n以后会更经常出现在电视上了呐！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说不定年底还会出现在\n{color=#FF0000}《绝对不准笑》{/color}和\n{color=#808000}《艺人等级鉴定》{/color}上呐！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2FB61747AED54E08ACC1F998C30D040F as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7C178421D3DA4E2CB70D4336919888FB "就是说呀！也许能一炮走红呢♪"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_9E0771C128CD4195A4659B2B4FBF28F2 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "接下来就要坐新干线去东京。而且是一等车厢！\n{size=12}{color=#808080}*从大阪到东京约合人民币322元{/color}{/size}\n"
    show rs_image_BF5966E1F19E4459A8639805C22B453E as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我们会尽力做到越来越出名的。"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_767DA33F80F84FEA9AAF27A753D98CC9 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "请记得看广播的节目表哦♪{w}我们走了——！"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_E0B8A219896B49168D47409135D3624F
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A46E468ABE0345679EB63CE570AD59F9

    pause 1.5

    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ set_place_title(_("梅咲广场"))
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026


    if judge_lm_condition([]):
        jump block_0000300D

    return

label block_0000300D:
    # Node: 0000300D (T ++)
    $ TalkRikuta = TalkRikuta + 1
    $ del C3AllowSukimotoTalk

    if judge_lm_condition([]):
        jump block_00001AAE

    return

label block_00001AAE:
    # Node: 00001AAE (梅咲 square)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_228
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001AA1

    return

label block_000027C8:
    # Node: 000027C8 (陸田)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_9E0771C128CD4195A4659B2B4FBF28F2 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_000027C7

    return

label block_000027C3:
    # Node: 000027C3 (梅咲 square 陸田)
    $ sys_lm_menu_item = [{"pos": (200, 208),"image": "images/Menu/Rikuta umesaki 2.png","hover": "images/Menu/Rikuta umesaki 2 hover.png","name": "陸田"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_229
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"陸田\"" }]):
        jump block_000027C2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001AA1

    return

label block_000027C2:
    # Node: 000027C2 (陸田 event)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_0CE956266D364F74B154FDDE322EEDEE as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_4B9533E6E39449D886CFE2CAC3DC64DA as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "啊，友同学。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么了？很没精神的样子。\n你的伙伴杉本君呢？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0CE956266D364F74B154FDDE322EEDEE as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "这个……早上还联络过的。{w}\n毕竟是他，也许只是去其他地方闲晃了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "应该就是那样？\n现在梅咲路边确实有很多好吃的。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BF5966E1F19E4459A8639805C22B453E as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "……我想也是。"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("梅咲广场"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "TalkRikuta == 0" }]):
        jump block_00003006
    if judge_lm_condition([]):
        jump block_000027C3

    return

label block_00003006:
    # Node: 00003006 (T ++)
    $ TalkRikuta = TalkRikuta + 1
    $ del C3AllowTriggleSukimotoTalk

    if judge_lm_condition([]):
        jump block_000027C3

    return

label block_00003DBD:
    # Node: 00003DBD (Return)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00001AA6

    return

label block_00001F67:
    # Node: 00001F67 (Map)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_507B7F77C4F74464A02D5387DFA7FE2C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    show rs_image_64016442C6754AFBA84D936DA56D33FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00001AA6

    return

label block_000027A0:
    # Node: 000027A0 (Daytime)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    stop music fadeout 1
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 0.8

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003D9E

    return

label block_00003D9E:
    # Node: 00003D9E ()
    $ del HananoRandom

    return

label block_00001A6B:
    # Node: 00001A6B (Conversation)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天一天也辛苦了呐！\n{w}祝贺我自己♪"

    window hide

    $ set_window("(標準)")

    return

label block_00001A6C:
    # Node: 00001A6C (Target)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『放学后自由放松就好。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001F8A:
    # Node: 00001F8A (Character)
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

label block_0000279E:
    # Node: 0000279E (Misaki school)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ reverse_volume("music", 1)

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
    show rs_image_F95856ACBC5A49B2B61D4DBB1E7B4294 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_0000279F

    return

label block_0000279F:
    # Node: 0000279F (Misaki school)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (96, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "屋外トイレへ"}, {"pos": (456, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "学校看板"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_230
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学校看板\"" }]):
        jump block_0000279D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外トイレへ\"" }]):
        jump block_0000279B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003D8E

    return

label block_0000279D:
    # Node: 0000279D (Board)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_3BE9AC227F0142FBAABEEB7605D6A3F9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_0000279F

    return

label block_0000279B:
    # Node: 0000279B (Outside toilet)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("室外厕所"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AC86D4E564124F9A8DE5EF0A5293F191 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_0000279C

    return

label block_0000279C:
    # Node: 0000279C (Outside toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_231
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000279E

    return

